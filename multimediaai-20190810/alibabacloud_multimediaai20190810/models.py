# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


class CreateCoverTaskRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        video_name: str = None,
        video_url: str = None,
        template_id: int = None,
        callback_url: str = None,
        scales: str = None,
    ):
        self.application_id = application_id
        self.video_name = video_name
        self.video_url = video_url
        self.template_id = template_id
        self.callback_url = callback_url
        self.scales = scales

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.scales is not None:
            result['Scales'] = self.scales
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Scales') is not None:
            self.scales = m.get('Scales')
        return self


class CreateCoverTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateCoverTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateCoverTaskResponseBody = None,
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
            temp_model = CreateCoverTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFaceGroupRequest(TeaModel):
    def __init__(
        self,
        face_group_name: str = None,
        description: str = None,
    ):
        self.face_group_name = face_group_name
        self.description = description

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_group_name is not None:
            result['FaceGroupName'] = self.face_group_name
        if self.description is not None:
            result['Description'] = self.description
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGroupName') is not None:
            self.face_group_name = m.get('FaceGroupName')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        return self


class CreateFaceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        face_group_id: int = None,
    ):
        self.request_id = request_id
        self.face_group_id = face_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.face_group_id is not None:
            result['FaceGroupId'] = self.face_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FaceGroupId') is not None:
            self.face_group_id = m.get('FaceGroupId')
        return self


class CreateFaceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFaceGroupResponseBody = None,
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
            temp_model = CreateFaceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFacePersonRequest(TeaModel):
    def __init__(
        self,
        face_group_id: int = None,
        face_person_name: str = None,
        image_urls: str = None,
    ):
        self.face_group_id = face_group_id
        self.face_person_name = face_person_name
        self.image_urls = image_urls

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_group_id is not None:
            result['FaceGroupId'] = self.face_group_id
        if self.face_person_name is not None:
            result['FacePersonName'] = self.face_person_name
        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGroupId') is not None:
            self.face_group_id = m.get('FaceGroupId')
        if m.get('FacePersonName') is not None:
            self.face_person_name = m.get('FacePersonName')
        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')
        return self


class CreateFacePersonResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        face_person_id: int = None,
    ):
        self.request_id = request_id
        self.face_person_id = face_person_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.face_person_id is not None:
            result['FacePersonId'] = self.face_person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('FacePersonId') is not None:
            self.face_person_id = m.get('FacePersonId')
        return self


class CreateFacePersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateFacePersonResponseBody = None,
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
            temp_model = CreateFacePersonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGifTaskRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        video_name: str = None,
        video_url: str = None,
        template_id: int = None,
        callback_url: str = None,
        scales: str = None,
    ):
        self.application_id = application_id
        self.video_name = video_name
        self.video_url = video_url
        self.template_id = template_id
        self.callback_url = callback_url
        self.scales = scales

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.scales is not None:
            result['Scales'] = self.scales
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Scales') is not None:
            self.scales = m.get('Scales')
        return self


class CreateGifTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateGifTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGifTaskResponseBody = None,
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
            temp_model = CreateGifTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLabelTaskRequest(TeaModel):
    def __init__(
        self,
        application_id: str = None,
        video_name: str = None,
        video_url: str = None,
        template_id: int = None,
        callback_url: str = None,
    ):
        self.application_id = application_id
        self.video_name = video_name
        self.video_url = video_url
        self.template_id = template_id
        self.callback_url = callback_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        return self


class CreateLabelTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: int = None,
        request_id: str = None,
    ):
        self.task_id = task_id
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateLabelTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLabelTaskResponseBody = None,
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
            temp_model = CreateLabelTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTemplateRequest(TeaModel):
    def __init__(
        self,
        template_name: str = None,
        content: str = None,
        is_default: bool = None,
        type: int = None,
    ):
        self.template_name = template_name
        self.content = content
        self.is_default = is_default
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.content is not None:
            result['Content'] = self.content
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class CreateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        template_id: str = None,
    ):
        self.request_id = request_id
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class CreateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateTemplateResponseBody = None,
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
            temp_model = CreateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceGroupRequest(TeaModel):
    def __init__(
        self,
        face_group_id: int = None,
    ):
        self.face_group_id = face_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_group_id is not None:
            result['FaceGroupId'] = self.face_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGroupId') is not None:
            self.face_group_id = m.get('FaceGroupId')
        return self


class DeleteFaceGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFaceGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFaceGroupResponseBody = None,
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
            temp_model = DeleteFaceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFaceImageRequest(TeaModel):
    def __init__(
        self,
        face_group_id: int = None,
        face_person_id: int = None,
        face_image_id: int = None,
    ):
        self.face_group_id = face_group_id
        self.face_person_id = face_person_id
        self.face_image_id = face_image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_group_id is not None:
            result['FaceGroupId'] = self.face_group_id
        if self.face_person_id is not None:
            result['FacePersonId'] = self.face_person_id
        if self.face_image_id is not None:
            result['FaceImageId'] = self.face_image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGroupId') is not None:
            self.face_group_id = m.get('FaceGroupId')
        if m.get('FacePersonId') is not None:
            self.face_person_id = m.get('FacePersonId')
        if m.get('FaceImageId') is not None:
            self.face_image_id = m.get('FaceImageId')
        return self


class DeleteFaceImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFaceImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFaceImageResponseBody = None,
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
            temp_model = DeleteFaceImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFacePersonRequest(TeaModel):
    def __init__(
        self,
        face_group_id: int = None,
        face_person_id: int = None,
    ):
        self.face_group_id = face_group_id
        self.face_person_id = face_person_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_group_id is not None:
            result['FaceGroupId'] = self.face_group_id
        if self.face_person_id is not None:
            result['FacePersonId'] = self.face_person_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGroupId') is not None:
            self.face_group_id = m.get('FaceGroupId')
        if m.get('FacePersonId') is not None:
            self.face_person_id = m.get('FacePersonId')
        return self


class DeleteFacePersonResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteFacePersonResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFacePersonResponseBody = None,
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
            temp_model = DeleteFacePersonResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskResultRequest(TeaModel):
    def __init__(
        self,
        task_id: int = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskResultResponseBodyResult(TeaModel):
    def __init__(
        self,
        error_name: str = None,
        error_message: str = None,
        error_code: str = None,
        video_name: str = None,
        analysis_use_time: int = None,
        process_result_url: str = None,
        application_id: str = None,
        error_reason: str = None,
        video_url: str = None,
    ):
        self.error_name = error_name
        self.error_message = error_message
        self.error_code = error_code
        self.video_name = video_name
        self.analysis_use_time = analysis_use_time
        self.process_result_url = process_result_url
        self.application_id = application_id
        self.error_reason = error_reason
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.error_name is not None:
            result['ErrorName'] = self.error_name
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.video_name is not None:
            result['VideoName'] = self.video_name
        if self.analysis_use_time is not None:
            result['AnalysisUseTime'] = self.analysis_use_time
        if self.process_result_url is not None:
            result['ProcessResultUrl'] = self.process_result_url
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id
        if self.error_reason is not None:
            result['ErrorReason'] = self.error_reason
        if self.video_url is not None:
            result['VideoUrl'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorName') is not None:
            self.error_name = m.get('ErrorName')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('VideoName') is not None:
            self.video_name = m.get('VideoName')
        if m.get('AnalysisUseTime') is not None:
            self.analysis_use_time = m.get('AnalysisUseTime')
        if m.get('ProcessResultUrl') is not None:
            self.process_result_url = m.get('ProcessResultUrl')
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')
        if m.get('ErrorReason') is not None:
            self.error_reason = m.get('ErrorReason')
        if m.get('VideoUrl') is not None:
            self.video_url = m.get('VideoUrl')
        return self


class GetTaskResultResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        request_id: str = None,
        result: GetTaskResultResponseBodyResult = None,
    ):
        self.status = status
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetTaskResultResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetTaskResultResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTaskResultResponseBody = None,
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
            temp_model = GetTaskResultResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatusRequest(TeaModel):
    def __init__(
        self,
        task_id: int = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class GetTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: int = None,
        request_id: str = None,
    ):
        self.status = status
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.status is not None:
            result['Status'] = self.status
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTaskStatusResponseBody = None,
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
            temp_model = GetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: int = None,
    ):
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetTemplateResponseBody(TeaModel):
    def __init__(
        self,
        is_default: bool = None,
        category: int = None,
        request_id: str = None,
        content: Dict[str, Any] = None,
        create_time: str = None,
        update_time: str = None,
        template_name: str = None,
        template_id: str = None,
    ):
        self.is_default = is_default
        self.category = category
        self.request_id = request_id
        self.content = content
        self.create_time = create_time
        self.update_time = update_time
        self.template_name = template_name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.category is not None:
            result['Category'] = self.category
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class GetTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetTemplateResponseBody = None,
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
            temp_model = GetTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFaceGroupsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFaceGroupsResponseBodyFaceGroupsTemplates(TeaModel):
    def __init__(
        self,
        name: str = None,
        id: str = None,
    ):
        self.name = name
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class ListFaceGroupsResponseBodyFaceGroups(TeaModel):
    def __init__(
        self,
        description: str = None,
        face_group_name: str = None,
        person_count: int = None,
        image_count: int = None,
        face_group_id: int = None,
        templates: List[ListFaceGroupsResponseBodyFaceGroupsTemplates] = None,
    ):
        self.description = description
        self.face_group_name = face_group_name
        self.person_count = person_count
        self.image_count = image_count
        self.face_group_id = face_group_id
        self.templates = templates

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.face_group_name is not None:
            result['FaceGroupName'] = self.face_group_name
        if self.person_count is not None:
            result['PersonCount'] = self.person_count
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.face_group_id is not None:
            result['FaceGroupId'] = self.face_group_id
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('FaceGroupName') is not None:
            self.face_group_name = m.get('FaceGroupName')
        if m.get('PersonCount') is not None:
            self.person_count = m.get('PersonCount')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('FaceGroupId') is not None:
            self.face_group_id = m.get('FaceGroupId')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListFaceGroupsResponseBodyFaceGroupsTemplates()
                self.templates.append(temp_model.from_map(k))
        return self


class ListFaceGroupsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        face_groups: List[ListFaceGroupsResponseBodyFaceGroups] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.face_groups = face_groups

    def validate(self):
        if self.face_groups:
            for k in self.face_groups:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['FaceGroups'] = []
        if self.face_groups is not None:
            for k in self.face_groups:
                result['FaceGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.face_groups = []
        if m.get('FaceGroups') is not None:
            for k in m.get('FaceGroups'):
                temp_model = ListFaceGroupsResponseBodyFaceGroups()
                self.face_groups.append(temp_model.from_map(k))
        return self


class ListFaceGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFaceGroupsResponseBody = None,
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
            temp_model = ListFaceGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFaceImagesRequest(TeaModel):
    def __init__(
        self,
        face_group_id: int = None,
        face_person_id: int = None,
        page_number: int = None,
        page_size: int = None,
    ):
        self.face_group_id = face_group_id
        self.face_person_id = face_person_id
        self.page_number = page_number
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_group_id is not None:
            result['FaceGroupId'] = self.face_group_id
        if self.face_person_id is not None:
            result['FacePersonId'] = self.face_person_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGroupId') is not None:
            self.face_group_id = m.get('FaceGroupId')
        if m.get('FacePersonId') is not None:
            self.face_person_id = m.get('FacePersonId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListFaceImagesResponseBodyFaceImages(TeaModel):
    def __init__(
        self,
        face_rectangle: List[float] = None,
        image_url: str = None,
        face_image_id: int = None,
    ):
        self.face_rectangle = face_rectangle
        self.image_url = image_url
        self.face_image_id = face_image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_rectangle is not None:
            result['FaceRectangle'] = self.face_rectangle
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.face_image_id is not None:
            result['FaceImageId'] = self.face_image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceRectangle') is not None:
            self.face_rectangle = m.get('FaceRectangle')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('FaceImageId') is not None:
            self.face_image_id = m.get('FaceImageId')
        return self


class ListFaceImagesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
        face_images: List[ListFaceImagesResponseBodyFaceImages] = None,
    ):
        self.total_count = total_count
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number
        self.face_images = face_images

    def validate(self):
        if self.face_images:
            for k in self.face_images:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['FaceImages'] = []
        if self.face_images is not None:
            for k in self.face_images:
                result['FaceImages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.face_images = []
        if m.get('FaceImages') is not None:
            for k in m.get('FaceImages'):
                temp_model = ListFaceImagesResponseBodyFaceImages()
                self.face_images.append(temp_model.from_map(k))
        return self


class ListFaceImagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFaceImagesResponseBody = None,
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
            temp_model = ListFaceImagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFacePersonsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        face_group_id: int = None,
        face_person_name: str = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.face_group_id = face_group_id
        self.face_person_name = face_person_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.face_group_id is not None:
            result['FaceGroupId'] = self.face_group_id
        if self.face_person_name is not None:
            result['FacePersonName'] = self.face_person_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('FaceGroupId') is not None:
            self.face_group_id = m.get('FaceGroupId')
        if m.get('FacePersonName') is not None:
            self.face_person_name = m.get('FacePersonName')
        return self


class ListFacePersonsResponseBodyFacePersons(TeaModel):
    def __init__(
        self,
        image_url: str = None,
        image_count: int = None,
        face_person_id: int = None,
        face_person_name: str = None,
    ):
        self.image_url = image_url
        self.image_count = image_count
        self.face_person_id = face_person_id
        self.face_person_name = face_person_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        if self.image_count is not None:
            result['ImageCount'] = self.image_count
        if self.face_person_id is not None:
            result['FacePersonId'] = self.face_person_id
        if self.face_person_name is not None:
            result['FacePersonName'] = self.face_person_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        if m.get('ImageCount') is not None:
            self.image_count = m.get('ImageCount')
        if m.get('FacePersonId') is not None:
            self.face_person_id = m.get('FacePersonId')
        if m.get('FacePersonName') is not None:
            self.face_person_name = m.get('FacePersonName')
        return self


class ListFacePersonsResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        face_persons: List[ListFacePersonsResponseBodyFacePersons] = None,
        request_id: str = None,
        page_size: int = None,
        page_number: int = None,
    ):
        self.total_count = total_count
        self.face_persons = face_persons
        self.request_id = request_id
        self.page_size = page_size
        self.page_number = page_number

    def validate(self):
        if self.face_persons:
            for k in self.face_persons:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['FacePersons'] = []
        if self.face_persons is not None:
            for k in self.face_persons:
                result['FacePersons'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.face_persons = []
        if m.get('FacePersons') is not None:
            for k in m.get('FacePersons'):
                temp_model = ListFacePersonsResponseBodyFacePersons()
                self.face_persons.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        return self


class ListFacePersonsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListFacePersonsResponseBody = None,
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
            temp_model = ListFacePersonsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplatesRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        template_id: int = None,
        template_name: str = None,
        type: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.template_id = template_id
        self.template_name = template_name
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListTemplatesResponseBodyTemplates(TeaModel):
    def __init__(
        self,
        type: int = None,
        is_default: bool = None,
        update_time: str = None,
        create_time: str = None,
        template_name: str = None,
        template_id: str = None,
    ):
        self.type = type
        self.is_default = is_default
        self.update_time = update_time
        self.create_time = create_time
        self.template_name = template_name
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        return self


class ListTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_size: int = None,
        request_id: str = None,
        page_number: int = None,
        templates: List[ListTemplatesResponseBodyTemplates] = None,
        total_amount: int = None,
    ):
        self.total_count = total_count
        self.page_size = page_size
        self.request_id = request_id
        self.page_number = page_number
        self.templates = templates
        self.total_amount = total_amount

    def validate(self):
        if self.templates:
            for k in self.templates:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        result['Templates'] = []
        if self.templates is not None:
            for k in self.templates:
                result['Templates'].append(k.to_map() if k else None)
        if self.total_amount is not None:
            result['TotalAmount'] = self.total_amount
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        self.templates = []
        if m.get('Templates') is not None:
            for k in m.get('Templates'):
                temp_model = ListTemplatesResponseBodyTemplates()
                self.templates.append(temp_model.from_map(k))
        if m.get('TotalAmount') is not None:
            self.total_amount = m.get('TotalAmount')
        return self


class ListTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListTemplatesResponseBody = None,
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
            temp_model = ListTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProcessFaceAlgorithmRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        app_key: str = None,
    ):
        self.data = data
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ProcessFaceAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ProcessFaceAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ProcessFaceAlgorithmResponseBody = None,
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
            temp_model = ProcessFaceAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProcessImageTagAlgorithmRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        app_key: str = None,
    ):
        self.data = data
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ProcessImageTagAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ProcessImageTagAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ProcessImageTagAlgorithmResponseBody = None,
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
            temp_model = ProcessImageTagAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProcessLandmarkAlgorithmRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        app_key: str = None,
    ):
        self.data = data
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ProcessLandmarkAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ProcessLandmarkAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ProcessLandmarkAlgorithmResponseBody = None,
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
            temp_model = ProcessLandmarkAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProcessLogoAlgorithmRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        app_key: str = None,
    ):
        self.data = data
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ProcessLogoAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ProcessLogoAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ProcessLogoAlgorithmResponseBody = None,
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
            temp_model = ProcessLogoAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProcessNewsAlgorithmRequest(TeaModel):
    def __init__(
        self,
        data: str = None,
        app_key: str = None,
    ):
        self.data = data
        self.app_key = app_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        return self


class ProcessNewsAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ProcessNewsAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ProcessNewsAlgorithmResponseBody = None,
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
            temp_model = ProcessNewsAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProcessNlpAlgorithmRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        data: str = None,
    ):
        self.app_key = app_key
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ProcessNlpAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ProcessNlpAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ProcessNlpAlgorithmResponseBody = None,
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
            temp_model = ProcessNlpAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProcessOcrAlgorithmRequest(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        data: str = None,
    ):
        self.app_key = app_key
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ProcessOcrAlgorithmResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        data: str = None,
        code: int = None,
    ):
        self.message = message
        self.request_id = request_id
        self.data = data
        self.code = code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.data is not None:
            result['Data'] = self.data
        if self.code is not None:
            result['Code'] = self.code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        return self


class ProcessOcrAlgorithmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ProcessOcrAlgorithmResponseBody = None,
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
            temp_model = ProcessOcrAlgorithmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RegisterFaceImageRequest(TeaModel):
    def __init__(
        self,
        face_group_id: int = None,
        face_person_id: int = None,
        image_url: str = None,
    ):
        self.face_group_id = face_group_id
        self.face_person_id = face_person_id
        self.image_url = image_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_group_id is not None:
            result['FaceGroupId'] = self.face_group_id
        if self.face_person_id is not None:
            result['FacePersonId'] = self.face_person_id
        if self.image_url is not None:
            result['ImageUrl'] = self.image_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceGroupId') is not None:
            self.face_group_id = m.get('FaceGroupId')
        if m.get('FacePersonId') is not None:
            self.face_person_id = m.get('FacePersonId')
        if m.get('ImageUrl') is not None:
            self.image_url = m.get('ImageUrl')
        return self


class RegisterFaceImageResponseBodyFaceImages(TeaModel):
    def __init__(
        self,
        face_image_id: int = None,
    ):
        self.face_image_id = face_image_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.face_image_id is not None:
            result['FaceImageId'] = self.face_image_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FaceImageId') is not None:
            self.face_image_id = m.get('FaceImageId')
        return self


class RegisterFaceImageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        face_images: List[RegisterFaceImageResponseBodyFaceImages] = None,
    ):
        self.request_id = request_id
        self.face_images = face_images

    def validate(self):
        if self.face_images:
            for k in self.face_images:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['FaceImages'] = []
        if self.face_images is not None:
            for k in self.face_images:
                result['FaceImages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.face_images = []
        if m.get('FaceImages') is not None:
            for k in m.get('FaceImages'):
                temp_model = RegisterFaceImageResponseBodyFaceImages()
                self.face_images.append(temp_model.from_map(k))
        return self


class RegisterFaceImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RegisterFaceImageResponseBody = None,
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
            temp_model = RegisterFaceImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
        template_name: str = None,
        content: str = None,
        is_default: bool = None,
        type: int = None,
    ):
        self.template_id = template_id
        self.template_name = template_name
        self.content = content
        self.is_default = is_default
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.template_name is not None:
            result['TemplateName'] = self.template_name
        if self.content is not None:
            result['Content'] = self.content
        if self.is_default is not None:
            result['IsDefault'] = self.is_default
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class UpdateTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTemplateResponseBody = None,
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
            temp_model = UpdateTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



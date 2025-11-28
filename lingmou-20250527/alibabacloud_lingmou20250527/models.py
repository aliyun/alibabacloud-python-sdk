# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Any, List, Dict


class TemplateVariable(TeaModel):
    def __init__(
        self,
        name: str = None,
        properties: Any = None,
        type: str = None,
    ):
        self.name = name
        self.properties = properties
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.properties is not None:
            result['properties'] = self.properties
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('properties') is not None:
            self.properties = m.get('properties')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class BroadcastTemplate(TeaModel):
    def __init__(
        self,
        create_time: str = None,
        id: str = None,
        modified_time: str = None,
        name: str = None,
        variables: List[TemplateVariable] = None,
    ):
        self.create_time = create_time
        self.id = id
        self.modified_time = modified_time
        self.name = name
        self.variables = variables

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time
        if self.name is not None:
            result['name'] = self.name
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = TemplateVariable()
                self.variables.append(temp_model.from_map(k))
        return self


class BroadcastVideo(TeaModel):
    def __init__(
        self,
        alignment_file_url: str = None,
        caption_url: str = None,
        cover_url: str = None,
        create_time: str = None,
        id: str = None,
        modified_time: str = None,
        name: str = None,
        status: str = None,
        video_url: str = None,
    ):
        self.alignment_file_url = alignment_file_url
        self.caption_url = caption_url
        self.cover_url = cover_url
        self.create_time = create_time
        self.id = id
        self.modified_time = modified_time
        self.name = name
        self.status = status
        self.video_url = video_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alignment_file_url is not None:
            result['alignmentFileURL'] = self.alignment_file_url
        if self.caption_url is not None:
            result['captionURL'] = self.caption_url
        if self.cover_url is not None:
            result['coverURL'] = self.cover_url
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.id is not None:
            result['id'] = self.id
        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time
        if self.name is not None:
            result['name'] = self.name
        if self.status is not None:
            result['status'] = self.status
        if self.video_url is not None:
            result['videoURL'] = self.video_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alignmentFileURL') is not None:
            self.alignment_file_url = m.get('alignmentFileURL')
        if m.get('captionURL') is not None:
            self.caption_url = m.get('captionURL')
        if m.get('coverURL') is not None:
            self.cover_url = m.get('coverURL')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('videoURL') is not None:
            self.video_url = m.get('videoURL')
        return self


class ChatSessionInfo(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        main_account_id: int = None,
        session_id: str = None,
    ):
        self.created_at = created_at
        self.main_account_id = main_account_id
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['createdAt'] = self.created_at
        if self.main_account_id is not None:
            result['mainAccountId'] = self.main_account_id
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')
        if m.get('mainAccountId') is not None:
            self.main_account_id = m.get('mainAccountId')
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class CloseChatInstanceSessionsRequest(TeaModel):
    def __init__(
        self,
        session_ids: List[str] = None,
    ):
        self.session_ids = session_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_ids is not None:
            result['sessionIds'] = self.session_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionIds') is not None:
            self.session_ids = m.get('sessionIds')
        return self


class CloseChatInstanceSessionsShrinkRequest(TeaModel):
    def __init__(
        self,
        session_ids_shrink: str = None,
    ):
        self.session_ids_shrink = session_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_ids_shrink is not None:
            result['sessionIds'] = self.session_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionIds') is not None:
            self.session_ids_shrink = m.get('sessionIds')
        return self


class CloseChatInstanceSessionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ChatSessionInfo] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ChatSessionInfo()
                self.data.append(temp_model.from_map(k))
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CloseChatInstanceSessionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloseChatInstanceSessionsResponseBody = None,
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
            temp_model = CloseChatInstanceSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfirmTrainPicAvatarRequest(TeaModel):
    def __init__(
        self,
        avatar_id: str = None,
        status: str = None,
    ):
        # This parameter is required.
        self.avatar_id = avatar_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_id is not None:
            result['avatarId'] = self.avatar_id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarId') is not None:
            self.avatar_id = m.get('avatarId')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class ConfirmTrainPicAvatarResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ConfirmTrainPicAvatarResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ConfirmTrainPicAvatarResponseBody = None,
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
            temp_model = ConfirmTrainPicAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBackgroundPicRequest(TeaModel):
    def __init__(
        self,
        filename: str = None,
        oss_key: str = None,
    ):
        self.filename = filename
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.filename is not None:
            result['filename'] = self.filename
        if self.oss_key is not None:
            result['ossKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('filename') is not None:
            self.filename = m.get('filename')
        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')
        return self


class CreateBackgroundPicResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class CreateBackgroundPicResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateBackgroundPicResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateBackgroundPicResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateBackgroundPicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBackgroundPicResponseBody = None,
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
            temp_model = CreateBackgroundPicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBroadcastStickerRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        oss_key: str = None,
    ):
        self.file_name = file_name
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.oss_key is not None:
            result['ossKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')
        return self


class CreateBroadcastStickerResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class CreateBroadcastStickerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateBroadcastStickerResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateBroadcastStickerResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateBroadcastStickerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBroadcastStickerResponseBody = None,
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
            temp_model = CreateBroadcastStickerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateBroadcastVideoFromTemplateRequestVideoOptions(TeaModel):
    def __init__(
        self,
        fps: int = None,
        resolution: str = None,
        watermark: bool = None,
    ):
        self.fps = fps
        self.resolution = resolution
        self.watermark = watermark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fps is not None:
            result['fps'] = self.fps
        if self.resolution is not None:
            result['resolution'] = self.resolution
        if self.watermark is not None:
            result['watermark'] = self.watermark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fps') is not None:
            self.fps = m.get('fps')
        if m.get('resolution') is not None:
            self.resolution = m.get('resolution')
        if m.get('watermark') is not None:
            self.watermark = m.get('watermark')
        return self


class CreateBroadcastVideoFromTemplateRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        template_id: str = None,
        variables: List[TemplateVariable] = None,
        video_options: CreateBroadcastVideoFromTemplateRequestVideoOptions = None,
    ):
        self.name = name
        self.template_id = template_id
        self.variables = variables
        self.video_options = video_options

    def validate(self):
        if self.variables:
            for k in self.variables:
                if k:
                    k.validate()
        if self.video_options:
            self.video_options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.template_id is not None:
            result['templateId'] = self.template_id
        result['variables'] = []
        if self.variables is not None:
            for k in self.variables:
                result['variables'].append(k.to_map() if k else None)
        if self.video_options is not None:
            result['videoOptions'] = self.video_options.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        self.variables = []
        if m.get('variables') is not None:
            for k in m.get('variables'):
                temp_model = TemplateVariable()
                self.variables.append(temp_model.from_map(k))
        if m.get('videoOptions') is not None:
            temp_model = CreateBroadcastVideoFromTemplateRequestVideoOptions()
            self.video_options = temp_model.from_map(m['videoOptions'])
        return self


class CreateBroadcastVideoFromTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BroadcastVideo = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = BroadcastVideo()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateBroadcastVideoFromTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateBroadcastVideoFromTemplateResponseBody = None,
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
            temp_model = CreateBroadcastVideoFromTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatConfigRequest(TeaModel):
    def __init__(
        self,
        avatar_id: str = None,
        background_id: str = None,
    ):
        self.avatar_id = avatar_id
        self.background_id = background_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_id is not None:
            result['avatarId'] = self.avatar_id
        if self.background_id is not None:
            result['backgroundId'] = self.background_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarId') is not None:
            self.avatar_id = m.get('avatarId')
        if m.get('backgroundId') is not None:
            self.background_id = m.get('backgroundId')
        return self


class CreateChatConfigResponseBodyData(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class CreateChatConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateChatConfigResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateChatConfigResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateChatConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChatConfigResponseBody = None,
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
            temp_model = CreateChatConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateChatSessionRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        license: str = None,
        platform: str = None,
    ):
        # This parameter is required.
        self.instance_id = instance_id
        self.license = license
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.license is not None:
            result['license'] = self.license
        if self.platform is not None:
            result['platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('license') is not None:
            self.license = m.get('license')
        if m.get('platform') is not None:
            self.platform = m.get('platform')
        return self


class CreateChatSessionResponseBodyDataAvatarAssets(TeaModel):
    def __init__(
        self,
        md_5: str = None,
        min_required_version: str = None,
        secret: str = None,
        type: str = None,
        url: str = None,
    ):
        self.md_5 = md_5
        self.min_required_version = min_required_version
        self.secret = secret
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.md_5 is not None:
            result['md5'] = self.md_5
        if self.min_required_version is not None:
            result['minRequiredVersion'] = self.min_required_version
        if self.secret is not None:
            result['secret'] = self.secret
        if self.type is not None:
            result['type'] = self.type
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('md5') is not None:
            self.md_5 = m.get('md5')
        if m.get('minRequiredVersion') is not None:
            self.min_required_version = m.get('minRequiredVersion')
        if m.get('secret') is not None:
            self.secret = m.get('secret')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class CreateChatSessionResponseBodyDataRtcParams(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        avatar_user_id: str = None,
        channel: str = None,
        client_user_id: str = None,
        gslb: str = None,
        nonce: str = None,
        server_user_id: str = None,
        timestamp: int = None,
        token: str = None,
    ):
        self.app_id = app_id
        self.avatar_user_id = avatar_user_id
        self.channel = channel
        self.client_user_id = client_user_id
        self.gslb = gslb
        self.nonce = nonce
        self.server_user_id = server_user_id
        self.timestamp = timestamp
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['appId'] = self.app_id
        if self.avatar_user_id is not None:
            result['avatarUserId'] = self.avatar_user_id
        if self.channel is not None:
            result['channel'] = self.channel
        if self.client_user_id is not None:
            result['clientUserId'] = self.client_user_id
        if self.gslb is not None:
            result['gslb'] = self.gslb
        if self.nonce is not None:
            result['nonce'] = self.nonce
        if self.server_user_id is not None:
            result['serverUserId'] = self.server_user_id
        if self.timestamp is not None:
            result['timestamp'] = self.timestamp
        if self.token is not None:
            result['token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appId') is not None:
            self.app_id = m.get('appId')
        if m.get('avatarUserId') is not None:
            self.avatar_user_id = m.get('avatarUserId')
        if m.get('channel') is not None:
            self.channel = m.get('channel')
        if m.get('clientUserId') is not None:
            self.client_user_id = m.get('clientUserId')
        if m.get('gslb') is not None:
            self.gslb = m.get('gslb')
        if m.get('nonce') is not None:
            self.nonce = m.get('nonce')
        if m.get('serverUserId') is not None:
            self.server_user_id = m.get('serverUserId')
        if m.get('timestamp') is not None:
            self.timestamp = m.get('timestamp')
        if m.get('token') is not None:
            self.token = m.get('token')
        return self


class CreateChatSessionResponseBodyData(TeaModel):
    def __init__(
        self,
        avatar_assets: CreateChatSessionResponseBodyDataAvatarAssets = None,
        rtc_params: CreateChatSessionResponseBodyDataRtcParams = None,
        session_id: str = None,
    ):
        self.avatar_assets = avatar_assets
        self.rtc_params = rtc_params
        self.session_id = session_id

    def validate(self):
        if self.avatar_assets:
            self.avatar_assets.validate()
        if self.rtc_params:
            self.rtc_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_assets is not None:
            result['avatarAssets'] = self.avatar_assets.to_map()
        if self.rtc_params is not None:
            result['rtcParams'] = self.rtc_params.to_map()
        if self.session_id is not None:
            result['sessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarAssets') is not None:
            temp_model = CreateChatSessionResponseBodyDataAvatarAssets()
            self.avatar_assets = temp_model.from_map(m['avatarAssets'])
        if m.get('rtcParams') is not None:
            temp_model = CreateChatSessionResponseBodyDataRtcParams()
            self.rtc_params = temp_model.from_map(m['rtcParams'])
        if m.get('sessionId') is not None:
            self.session_id = m.get('sessionId')
        return self


class CreateChatSessionResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateChatSessionResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateChatSessionResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateChatSessionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateChatSessionResponseBody = None,
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
            temp_model = CreateChatSessionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateNoTrainPicAvatarRequest(TeaModel):
    def __init__(
        self,
        expressiveness: str = None,
        gender: str = None,
        generate_assets: bool = None,
        image_oss_path: str = None,
        jwt_token: str = None,
        name: str = None,
        transparent: bool = None,
    ):
        self.expressiveness = expressiveness
        self.gender = gender
        self.generate_assets = generate_assets
        self.image_oss_path = image_oss_path
        self.jwt_token = jwt_token
        self.name = name
        self.transparent = transparent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expressiveness is not None:
            result['expressiveness'] = self.expressiveness
        if self.gender is not None:
            result['gender'] = self.gender
        if self.generate_assets is not None:
            result['generateAssets'] = self.generate_assets
        if self.image_oss_path is not None:
            result['imageOssPath'] = self.image_oss_path
        if self.jwt_token is not None:
            result['jwtToken'] = self.jwt_token
        if self.name is not None:
            result['name'] = self.name
        if self.transparent is not None:
            result['transparent'] = self.transparent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expressiveness') is not None:
            self.expressiveness = m.get('expressiveness')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('generateAssets') is not None:
            self.generate_assets = m.get('generateAssets')
        if m.get('imageOssPath') is not None:
            self.image_oss_path = m.get('imageOssPath')
        if m.get('jwtToken') is not None:
            self.jwt_token = m.get('jwtToken')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('transparent') is not None:
            self.transparent = m.get('transparent')
        return self


class CreateNoTrainPicAvatarResponseBodyData(TeaModel):
    def __init__(
        self,
        avatar_id: str = None,
        pass_: bool = None,
    ):
        self.avatar_id = avatar_id
        self.pass_ = pass_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_id is not None:
            result['avatarId'] = self.avatar_id
        if self.pass_ is not None:
            result['pass'] = self.pass_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarId') is not None:
            self.avatar_id = m.get('avatarId')
        if m.get('pass') is not None:
            self.pass_ = m.get('pass')
        return self


class CreateNoTrainPicAvatarResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateNoTrainPicAvatarResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateNoTrainPicAvatarResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateNoTrainPicAvatarResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateNoTrainPicAvatarResponseBody = None,
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
            temp_model = CreateNoTrainPicAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTTSVoiceCustomRequest(TeaModel):
    def __init__(
        self,
        file_name: str = None,
        gender: str = None,
        name: str = None,
        oss_key: str = None,
    ):
        # This parameter is required.
        self.file_name = file_name
        self.gender = gender
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.oss_key = oss_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_name is not None:
            result['fileName'] = self.file_name
        if self.gender is not None:
            result['gender'] = self.gender
        if self.name is not None:
            result['name'] = self.name
        if self.oss_key is not None:
            result['ossKey'] = self.oss_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fileName') is not None:
            self.file_name = m.get('fileName')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')
        return self


class CreateTTSVoiceCustomResponseBodyData(TeaModel):
    def __init__(
        self,
        audio_url: str = None,
        censor_status: str = None,
        common: bool = None,
        create_time: str = None,
        description: str = None,
        error_detail: str = None,
        gender: str = None,
        id: str = None,
        language: str = None,
        modified_time: str = None,
        name: str = None,
        pitch_rate: float = None,
        remain_seconds: int = None,
        speech_rate: float = None,
        status: str = None,
        text: str = None,
        voice_key: str = None,
    ):
        self.audio_url = audio_url
        self.censor_status = censor_status
        self.common = common
        self.create_time = create_time
        self.description = description
        self.error_detail = error_detail
        self.gender = gender
        self.id = id
        self.language = language
        self.modified_time = modified_time
        self.name = name
        self.pitch_rate = pitch_rate
        self.remain_seconds = remain_seconds
        self.speech_rate = speech_rate
        self.status = status
        self.text = text
        self.voice_key = voice_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_url is not None:
            result['audioURL'] = self.audio_url
        if self.censor_status is not None:
            result['censorStatus'] = self.censor_status
        if self.common is not None:
            result['common'] = self.common
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.error_detail is not None:
            result['errorDetail'] = self.error_detail
        if self.gender is not None:
            result['gender'] = self.gender
        if self.id is not None:
            result['id'] = self.id
        if self.language is not None:
            result['language'] = self.language
        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time
        if self.name is not None:
            result['name'] = self.name
        if self.pitch_rate is not None:
            result['pitchRate'] = self.pitch_rate
        if self.remain_seconds is not None:
            result['remainSeconds'] = self.remain_seconds
        if self.speech_rate is not None:
            result['speechRate'] = self.speech_rate
        if self.status is not None:
            result['status'] = self.status
        if self.text is not None:
            result['text'] = self.text
        if self.voice_key is not None:
            result['voiceKey'] = self.voice_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioURL') is not None:
            self.audio_url = m.get('audioURL')
        if m.get('censorStatus') is not None:
            self.censor_status = m.get('censorStatus')
        if m.get('common') is not None:
            self.common = m.get('common')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('errorDetail') is not None:
            self.error_detail = m.get('errorDetail')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('pitchRate') is not None:
            self.pitch_rate = m.get('pitchRate')
        if m.get('remainSeconds') is not None:
            self.remain_seconds = m.get('remainSeconds')
        if m.get('speechRate') is not None:
            self.speech_rate = m.get('speechRate')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('voiceKey') is not None:
            self.voice_key = m.get('voiceKey')
        return self


class CreateTTSVoiceCustomResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateTTSVoiceCustomResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateTTSVoiceCustomResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateTTSVoiceCustomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTTSVoiceCustomResponseBody = None,
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
            temp_model = CreateTTSVoiceCustomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateTrainPicAvatarRequest(TeaModel):
    def __init__(
        self,
        gender: str = None,
        generate_assets: bool = None,
        image_oss_path: str = None,
        name: str = None,
        template_id: str = None,
        transparent: bool = None,
    ):
        # This parameter is required.
        self.gender = gender
        self.generate_assets = generate_assets
        # This parameter is required.
        self.image_oss_path = image_oss_path
        # This parameter is required.
        self.name = name
        # This parameter is required.
        self.template_id = template_id
        self.transparent = transparent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.gender is not None:
            result['gender'] = self.gender
        if self.generate_assets is not None:
            result['generateAssets'] = self.generate_assets
        if self.image_oss_path is not None:
            result['imageOssPath'] = self.image_oss_path
        if self.name is not None:
            result['name'] = self.name
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.transparent is not None:
            result['transparent'] = self.transparent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('generateAssets') is not None:
            self.generate_assets = m.get('generateAssets')
        if m.get('imageOssPath') is not None:
            self.image_oss_path = m.get('imageOssPath')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('transparent') is not None:
            self.transparent = m.get('transparent')
        return self


class CreateTrainPicAvatarResponseBodyData(TeaModel):
    def __init__(
        self,
        avatar_id: str = None,
        expected_completion_time: int = None,
        pass_: bool = None,
    ):
        self.avatar_id = avatar_id
        self.expected_completion_time = expected_completion_time
        self.pass_ = pass_

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_id is not None:
            result['avatarId'] = self.avatar_id
        if self.expected_completion_time is not None:
            result['expectedCompletionTime'] = self.expected_completion_time
        if self.pass_ is not None:
            result['pass'] = self.pass_
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarId') is not None:
            self.avatar_id = m.get('avatarId')
        if m.get('expectedCompletionTime') is not None:
            self.expected_completion_time = m.get('expectedCompletionTime')
        if m.get('pass') is not None:
            self.pass_ = m.get('pass')
        return self


class CreateTrainPicAvatarResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: CreateTrainPicAvatarResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = CreateTrainPicAvatarResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class CreateTrainPicAvatarResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateTrainPicAvatarResponseBody = None,
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
            temp_model = CreateTrainPicAvatarResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetBroadcastTemplateRequest(TeaModel):
    def __init__(
        self,
        template_id: str = None,
    ):
        # This parameter is required.
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.template_id is not None:
            result['templateId'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        return self


class GetBroadcastTemplateResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: BroadcastTemplate = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = BroadcastTemplate()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetBroadcastTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetBroadcastTemplateResponseBody = None,
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
            temp_model = GetBroadcastTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTrainPicAvatarStatusRequest(TeaModel):
    def __init__(
        self,
        avatar_id: str = None,
    ):
        # This parameter is required.
        self.avatar_id = avatar_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_id is not None:
            result['avatarId'] = self.avatar_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarId') is not None:
            self.avatar_id = m.get('avatarId')
        return self


class GetTrainPicAvatarStatusResponseBodyData(TeaModel):
    def __init__(
        self,
        avatar_id: str = None,
        preview_url: str = None,
        status: str = None,
    ):
        self.avatar_id = avatar_id
        self.preview_url = preview_url
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_id is not None:
            result['avatarId'] = self.avatar_id
        if self.preview_url is not None:
            result['previewURL'] = self.preview_url
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatarId') is not None:
            self.avatar_id = m.get('avatarId')
        if m.get('previewURL') is not None:
            self.preview_url = m.get('previewURL')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetTrainPicAvatarStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetTrainPicAvatarStatusResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetTrainPicAvatarStatusResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetTrainPicAvatarStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTrainPicAvatarStatusResponseBody = None,
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
            temp_model = GetTrainPicAvatarStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadPolicyRequest(TeaModel):
    def __init__(
        self,
        jwt_token: str = None,
        type: str = None,
    ):
        self.jwt_token = jwt_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.jwt_token is not None:
            result['jwtToken'] = self.jwt_token
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('jwtToken') is not None:
            self.jwt_token = m.get('jwtToken')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetUploadPolicyResponseBodyDataOssPolicy(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        policy: str = None,
        signature: str = None,
    ):
        # accessId。
        self.access_id = access_id
        self.dir = dir
        self.expire = expire
        self.host = host
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_id is not None:
            result['accessId'] = self.access_id
        if self.dir is not None:
            result['dir'] = self.dir
        if self.expire is not None:
            result['expire'] = self.expire
        if self.host is not None:
            result['host'] = self.host
        if self.policy is not None:
            result['policy'] = self.policy
        if self.signature is not None:
            result['signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('accessId') is not None:
            self.access_id = m.get('accessId')
        if m.get('dir') is not None:
            self.dir = m.get('dir')
        if m.get('expire') is not None:
            self.expire = m.get('expire')
        if m.get('host') is not None:
            self.host = m.get('host')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        return self


class GetUploadPolicyResponseBodyData(TeaModel):
    def __init__(
        self,
        oss_key: str = None,
        oss_policy: GetUploadPolicyResponseBodyDataOssPolicy = None,
    ):
        self.oss_key = oss_key
        self.oss_policy = oss_policy

    def validate(self):
        if self.oss_policy:
            self.oss_policy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_key is not None:
            result['ossKey'] = self.oss_key
        if self.oss_policy is not None:
            result['ossPolicy'] = self.oss_policy.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ossKey') is not None:
            self.oss_key = m.get('ossKey')
        if m.get('ossPolicy') is not None:
            temp_model = GetUploadPolicyResponseBodyDataOssPolicy()
            self.oss_policy = temp_model.from_map(m['ossPolicy'])
        return self


class GetUploadPolicyResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: GetUploadPolicyResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = GetUploadPolicyResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class GetUploadPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUploadPolicyResponseBody = None,
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
            temp_model = GetUploadPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBroadcastTemplatesRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        size: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.page = page
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class ListBroadcastTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[BroadcastTemplate] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page: int = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.page = page
        self.request_id = request_id
        self.size = size
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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.message is not None:
            result['message'] = self.message
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page is not None:
            result['page'] = self.page
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.size is not None:
            result['size'] = self.size
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = BroadcastTemplate()
                self.data.append(temp_model.from_map(k))
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListBroadcastTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBroadcastTemplatesResponseBody = None,
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
            temp_model = ListBroadcastTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListBroadcastVideosByIdRequest(TeaModel):
    def __init__(
        self,
        video_ids: List[str] = None,
    ):
        self.video_ids = video_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_ids is not None:
            result['videoIds'] = self.video_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoIds') is not None:
            self.video_ids = m.get('videoIds')
        return self


class ListBroadcastVideosByIdShrinkRequest(TeaModel):
    def __init__(
        self,
        video_ids_shrink: str = None,
    ):
        self.video_ids_shrink = video_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.video_ids_shrink is not None:
            result['videoIds'] = self.video_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('videoIds') is not None:
            self.video_ids_shrink = m.get('videoIds')
        return self


class ListBroadcastVideosByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[BroadcastVideo] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = BroadcastVideo()
                self.data.append(temp_model.from_map(k))
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListBroadcastVideosByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListBroadcastVideosByIdResponseBody = None,
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
            temp_model = ListBroadcastVideosByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPrivateTTSVoicesCustomRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        name: str = None,
        next_token: str = None,
        page_index: int = None,
        page_size: int = None,
    ):
        self.max_results = max_results
        self.name = name
        self.next_token = next_token
        # This parameter is required.
        self.page_index = page_index
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.name is not None:
            result['name'] = self.name
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page_index is not None:
            result['pageIndex'] = self.page_index
        if self.page_size is not None:
            result['pageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('pageIndex') is not None:
            self.page_index = m.get('pageIndex')
        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')
        return self


class ListPrivateTTSVoicesCustomResponseBodyDataData(TeaModel):
    def __init__(
        self,
        audio_url: str = None,
        censor_status: str = None,
        common: bool = None,
        create_time: str = None,
        description: str = None,
        error_detail: str = None,
        gender: str = None,
        id: str = None,
        language: str = None,
        modified_time: str = None,
        name: str = None,
        remain_seconds: int = None,
        status: str = None,
        text: str = None,
        voice_key: str = None,
    ):
        self.audio_url = audio_url
        self.censor_status = censor_status
        self.common = common
        self.create_time = create_time
        self.description = description
        self.error_detail = error_detail
        self.gender = gender
        self.id = id
        self.language = language
        self.modified_time = modified_time
        self.name = name
        self.remain_seconds = remain_seconds
        self.status = status
        self.text = text
        self.voice_key = voice_key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_url is not None:
            result['audioURL'] = self.audio_url
        if self.censor_status is not None:
            result['censorStatus'] = self.censor_status
        if self.common is not None:
            result['common'] = self.common
        if self.create_time is not None:
            result['createTime'] = self.create_time
        if self.description is not None:
            result['description'] = self.description
        if self.error_detail is not None:
            result['errorDetail'] = self.error_detail
        if self.gender is not None:
            result['gender'] = self.gender
        if self.id is not None:
            result['id'] = self.id
        if self.language is not None:
            result['language'] = self.language
        if self.modified_time is not None:
            result['modifiedTime'] = self.modified_time
        if self.name is not None:
            result['name'] = self.name
        if self.remain_seconds is not None:
            result['remainSeconds'] = self.remain_seconds
        if self.status is not None:
            result['status'] = self.status
        if self.text is not None:
            result['text'] = self.text
        if self.voice_key is not None:
            result['voiceKey'] = self.voice_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('audioURL') is not None:
            self.audio_url = m.get('audioURL')
        if m.get('censorStatus') is not None:
            self.censor_status = m.get('censorStatus')
        if m.get('common') is not None:
            self.common = m.get('common')
        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('errorDetail') is not None:
            self.error_detail = m.get('errorDetail')
        if m.get('gender') is not None:
            self.gender = m.get('gender')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('modifiedTime') is not None:
            self.modified_time = m.get('modifiedTime')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('remainSeconds') is not None:
            self.remain_seconds = m.get('remainSeconds')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('text') is not None:
            self.text = m.get('text')
        if m.get('voiceKey') is not None:
            self.voice_key = m.get('voiceKey')
        return self


class ListPrivateTTSVoicesCustomResponseBodyData(TeaModel):
    def __init__(
        self,
        data: List[ListPrivateTTSVoicesCustomResponseBodyDataData] = None,
        page: int = None,
        pages: int = None,
        size: int = None,
        total: int = None,
    ):
        self.data = data
        self.page = page
        self.pages = pages
        self.size = size
        self.total = total

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
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.page is not None:
            result['page'] = self.page
        if self.pages is not None:
            result['pages'] = self.pages
        if self.size is not None:
            result['size'] = self.size
        if self.total is not None:
            result['total'] = self.total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListPrivateTTSVoicesCustomResponseBodyDataData()
                self.data.append(temp_model.from_map(k))
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('pages') is not None:
            self.pages = m.get('pages')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('total') is not None:
            self.total = m.get('total')
        return self


class ListPrivateTTSVoicesCustomResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: ListPrivateTTSVoicesCustomResponseBodyData = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
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
            result['code'] = self.code
        if self.data is not None:
            result['data'] = self.data.to_map()
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.message is not None:
            result['message'] = self.message
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('data') is not None:
            temp_model = ListPrivateTTSVoicesCustomResponseBodyData()
            self.data = temp_model.from_map(m['data'])
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class ListPrivateTTSVoicesCustomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPrivateTTSVoicesCustomResponseBody = None,
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
            temp_model = ListPrivateTTSVoicesCustomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTemplateMaterialRequest(TeaModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        page: int = None,
        size: int = None,
        template_ids: str = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.size = size
        self.template_ids = template_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page is not None:
            result['page'] = self.page
        if self.size is not None:
            result['size'] = self.size
        if self.template_ids is not None:
            result['templateIds'] = self.template_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('templateIds') is not None:
            self.template_ids = m.get('templateIds')
        return self


class ListTemplateMaterialResponseBodyData(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        template_id: str = None,
        template_name: str = None,
        template_url: str = None,
    ):
        self.biz_type = biz_type
        self.template_id = template_id
        self.template_name = template_name
        self.template_url = template_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['bizType'] = self.biz_type
        if self.template_id is not None:
            result['templateId'] = self.template_id
        if self.template_name is not None:
            result['templateName'] = self.template_name
        if self.template_url is not None:
            result['templateURL'] = self.template_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bizType') is not None:
            self.biz_type = m.get('bizType')
        if m.get('templateId') is not None:
            self.template_id = m.get('templateId')
        if m.get('templateName') is not None:
            self.template_name = m.get('templateName')
        if m.get('templateURL') is not None:
            self.template_url = m.get('templateURL')
        return self


class ListTemplateMaterialResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ListTemplateMaterialResponseBodyData] = None,
        http_status_code: int = None,
        max_results: int = None,
        message: str = None,
        next_token: str = None,
        page: int = None,
        request_id: str = None,
        size: int = None,
        success: bool = None,
        total: int = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.max_results = max_results
        self.message = message
        self.next_token = next_token
        self.page = page
        self.request_id = request_id
        self.size = size
        self.success = success
        self.total = total
        self.total_count = total_count

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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.max_results is not None:
            result['maxResults'] = self.max_results
        if self.message is not None:
            result['message'] = self.message
        if self.next_token is not None:
            result['nextToken'] = self.next_token
        if self.page is not None:
            result['page'] = self.page
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.size is not None:
            result['size'] = self.size
        if self.success is not None:
            result['success'] = self.success
        if self.total is not None:
            result['total'] = self.total
        if self.total_count is not None:
            result['totalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ListTemplateMaterialResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')
        if m.get('page') is not None:
            self.page = m.get('page')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('total') is not None:
            self.total = m.get('total')
        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')
        return self


class ListTemplateMaterialResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTemplateMaterialResponseBody = None,
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
            temp_model = ListTemplateMaterialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryChatInstanceSessionsRequest(TeaModel):
    def __init__(
        self,
        session_ids: List[str] = None,
    ):
        self.session_ids = session_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_ids is not None:
            result['sessionIds'] = self.session_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionIds') is not None:
            self.session_ids = m.get('sessionIds')
        return self


class QueryChatInstanceSessionsShrinkRequest(TeaModel):
    def __init__(
        self,
        session_ids_shrink: str = None,
    ):
        self.session_ids_shrink = session_ids_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_ids_shrink is not None:
            result['sessionIds'] = self.session_ids_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sessionIds') is not None:
            self.session_ids_shrink = m.get('sessionIds')
        return self


class QueryChatInstanceSessionsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        data: List[ChatSessionInfo] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
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
            result['code'] = self.code
        result['data'] = []
        if self.data is not None:
            for k in self.data:
                result['data'].append(k.to_map() if k else None)
        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['message'] = self.message
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.success is not None:
            result['success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        self.data = []
        if m.get('data') is not None:
            for k in m.get('data'):
                temp_model = ChatSessionInfo()
                self.data.append(temp_model.from_map(k))
        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('success') is not None:
            self.success = m.get('success')
        return self


class QueryChatInstanceSessionsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryChatInstanceSessionsResponseBody = None,
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
            temp_model = QueryChatInstanceSessionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



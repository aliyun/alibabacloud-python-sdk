# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddMosaicsRequest(TeaModel):
    def __init__(
        self,
        mark_position: str = None,
        sub_scene_id: str = None,
    ):
        # 马赛克位置数据
        self.mark_position = mark_position
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mark_position is not None:
            result['MarkPosition'] = self.mark_position
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarkPosition') is not None:
            self.mark_position = m.get('MarkPosition')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class AddMosaicsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
        self.success = success
        # 任务ID
        self.task_id = task_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class AddMosaicsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddMosaicsResponseBody = None,
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
            temp_model = AddMosaicsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddProjectRequest(TeaModel):
    def __init__(
        self,
        business_id: int = None,
        name: str = None,
    ):
        # 业务id
        self.business_id = business_id
        # 项目名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class AddProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 项目ID
        self.id = id
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddProjectResponseBody = None,
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
            temp_model = AddProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddRelativePositionRequest(TeaModel):
    def __init__(
        self,
        relative_position: str = None,
        scene_id: str = None,
    ):
        # 相对位置信息
        self.relative_position = relative_position
        # 场景ID
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.relative_position is not None:
            result['RelativePosition'] = self.relative_position
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RelativePosition') is not None:
            self.relative_position = m.get('RelativePosition')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class AddRelativePositionResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddRelativePositionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddRelativePositionResponseBody = None,
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
            temp_model = AddRelativePositionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSceneRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        project_id: str = None,
        type: str = None,
    ):
        # 场景名称
        self.name = name
        # 项目ID
        self.project_id = project_id
        # 场景类型 3D模型：MODEL_3D  全景图片：PIC  全景视频：VIDEO
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class AddSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 场景ID
        self.id = id
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSceneResponseBody = None,
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
            temp_model = AddSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSubSceneRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        scene_id: str = None,
    ):
        # 子场景名称
        self.name = name
        # 场景ID
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class AddSubSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        id: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 子场景ID
        self.id = id
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddSubSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddSubSceneResponseBody = None,
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
            temp_model = AddSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckResourceRequest(TeaModel):
    def __init__(
        self,
        bid: str = None,
        country: str = None,
        gmt_wakeup: str = None,
        hid: int = None,
        interrupt: bool = None,
        invoker: str = None,
        level: int = None,
        message: str = None,
        pk: str = None,
        prompt: str = None,
        success: bool = None,
        task_extra_data: str = None,
        task_identifier: str = None,
        url: str = None,
    ):
        self.bid = bid
        self.country = country
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.interrupt = interrupt
        self.invoker = invoker
        self.level = level
        self.message = message
        self.pk = pk
        self.prompt = prompt
        self.success = success
        self.task_extra_data = task_extra_data
        self.task_identifier = task_identifier
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CheckResourceResponseBody(TeaModel):
    def __init__(
        self,
        bid: str = None,
        country: str = None,
        gmt_wakeup: str = None,
        hid: int = None,
        interrupt: bool = None,
        invoker: str = None,
        level: int = None,
        message: str = None,
        pk: str = None,
        prompt: str = None,
        request_id: str = None,
        success: bool = None,
        task_extra_data: str = None,
        task_identifier: str = None,
        url: str = None,
    ):
        self.bid = bid
        self.country = country
        self.gmt_wakeup = gmt_wakeup
        self.hid = hid
        self.interrupt = interrupt
        self.invoker = invoker
        self.level = level
        self.message = message
        self.pk = pk
        self.prompt = prompt
        self.request_id = request_id
        self.success = success
        self.task_extra_data = task_extra_data
        self.task_identifier = task_identifier
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['Bid'] = self.bid
        if self.country is not None:
            result['Country'] = self.country
        if self.gmt_wakeup is not None:
            result['GmtWakeup'] = self.gmt_wakeup
        if self.hid is not None:
            result['Hid'] = self.hid
        if self.interrupt is not None:
            result['Interrupt'] = self.interrupt
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        if self.level is not None:
            result['Level'] = self.level
        if self.message is not None:
            result['Message'] = self.message
        if self.pk is not None:
            result['Pk'] = self.pk
        if self.prompt is not None:
            result['Prompt'] = self.prompt
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_extra_data is not None:
            result['TaskExtraData'] = self.task_extra_data
        if self.task_identifier is not None:
            result['TaskIdentifier'] = self.task_identifier
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Bid') is not None:
            self.bid = m.get('Bid')
        if m.get('Country') is not None:
            self.country = m.get('Country')
        if m.get('GmtWakeup') is not None:
            self.gmt_wakeup = m.get('GmtWakeup')
        if m.get('Hid') is not None:
            self.hid = m.get('Hid')
        if m.get('Interrupt') is not None:
            self.interrupt = m.get('Interrupt')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
        if m.get('Level') is not None:
            self.level = m.get('Level')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Pk') is not None:
            self.pk = m.get('Pk')
        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskExtraData') is not None:
            self.task_extra_data = m.get('TaskExtraData')
        if m.get('TaskIdentifier') is not None:
            self.task_identifier = m.get('TaskIdentifier')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class CheckResourceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CheckResourceResponseBody = None,
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
            temp_model = CheckResourceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateProjectRequest(TeaModel):
    def __init__(
        self,
        builder_user_id_list: str = None,
        business_id: str = None,
        business_user_id_list: str = None,
        gather_user_id_list: str = None,
        name: str = None,
    ):
        self.builder_user_id_list = builder_user_id_list
        self.business_id = business_id
        self.business_user_id_list = business_user_id_list
        self.gather_user_id_list = gather_user_id_list
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.builder_user_id_list is not None:
            result['BuilderUserIdList'] = self.builder_user_id_list
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_user_id_list is not None:
            result['BusinessUserIdList'] = self.business_user_id_list
        if self.gather_user_id_list is not None:
            result['GatherUserIdList'] = self.gather_user_id_list
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuilderUserIdList') is not None:
            self.builder_user_id_list = m.get('BuilderUserIdList')
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessUserIdList') is not None:
            self.business_user_id_list = m.get('BusinessUserIdList')
        if m.get('GatherUserIdList') is not None:
            self.gather_user_id_list = m.get('GatherUserIdList')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class CreateProjectResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        id: int = None,
        name: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_message = err_message
        self.id = id
        self.name = name
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateProjectResponseBody = None,
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
            temp_model = CreateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSceneRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        project_id: str = None,
    ):
        self.name = name
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class CreateSceneResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        preview_token: str = None,
        request_id: str = None,
        scene_id: int = None,
        success: bool = None,
    ):
        self.err_message = err_message
        self.preview_token = preview_token
        self.request_id = request_id
        self.scene_id = scene_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreateSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateSceneResponseBody = None,
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
            temp_model = CreateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteFileRequest(TeaModel):
    def __init__(
        self,
        param_file: str = None,
        sub_scene_uuid: str = None,
    ):
        self.param_file = param_file
        self.sub_scene_uuid = sub_scene_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_file is not None:
            result['ParamFile'] = self.param_file
        if self.sub_scene_uuid is not None:
            result['SubSceneUuid'] = self.sub_scene_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamFile') is not None:
            self.param_file = m.get('ParamFile')
        if m.get('SubSceneUuid') is not None:
            self.sub_scene_uuid = m.get('SubSceneUuid')
        return self


class DeleteFileResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteFileResponseBody = None,
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
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DeleteProjectResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DeleteProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteProjectResponseBody = None,
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
            temp_model = DeleteProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetailProjectRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # 项目Id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DetailProjectResponseBody(TeaModel):
    def __init__(
        self,
        business_id: int = None,
        business_name: str = None,
        code: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        success: bool = None,
        token: str = None,
    ):
        # 业务ID
        self.business_id = business_id
        # 业务名称
        self.business_name = business_name
        # 返回码
        self.code = code
        # 创建时间
        self.gmt_create = gmt_create
        # 最后修改时间
        self.gmt_modified = gmt_modified
        # 项目ID
        self.id = id
        # 错误消息
        self.message = message
        # 项目名称
        self.name = name
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
        self.success = success
        # Token
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.code is not None:
            result['Code'] = self.code
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class DetailProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetailProjectResponseBody = None,
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
            temp_model = DetailProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetailSceneRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # 场景Id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DetailSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        message: str = None,
        name: str = None,
        preview_token: str = None,
        published: bool = None,
        request_id: str = None,
        source_num: int = None,
        sub_scene_num: int = None,
        success: bool = None,
        type: str = None,
    ):
        # 返回码
        self.code = code
        # 创建时间
        self.gmt_create = gmt_create
        # 最后修改时间
        self.gmt_modified = gmt_modified
        # 主场景Id
        self.id = id
        # 错误消息
        self.message = message
        # 场景名称
        self.name = name
        # 预览Token
        self.preview_token = preview_token
        # 是否已发布 true：已发布：false：未发布
        self.published = published
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 资源数
        self.source_num = source_num
        # 子场景数
        self.sub_scene_num = sub_scene_num
        # 是否请求成功
        self.success = success
        # 场景类型
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
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.published is not None:
            result['Published'] = self.published
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.source_num is not None:
            result['SourceNum'] = self.source_num
        if self.sub_scene_num is not None:
            result['SubSceneNum'] = self.sub_scene_num
        if self.success is not None:
            result['Success'] = self.success
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('Published') is not None:
            self.published = m.get('Published')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SourceNum') is not None:
            self.source_num = m.get('SourceNum')
        if m.get('SubSceneNum') is not None:
            self.sub_scene_num = m.get('SubSceneNum')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class DetailSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetailSceneResponseBody = None,
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
            temp_model = DetailSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetailSubSceneRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # 子场景ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DetailSubSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        cover_url: str = None,
        cubemap_path: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        message: str = None,
        name: str = None,
        request_id: str = None,
        resource_id: str = None,
        status: int = None,
        success: bool = None,
        url: str = None,
    ):
        # 返回码
        self.code = code
        # 图片路径/视频封面路径
        self.cover_url = cover_url
        # 切图路径
        self.cubemap_path = cubemap_path
        # 创建时间
        self.gmt_create = gmt_create
        # 最后修改时间
        self.gmt_modified = gmt_modified
        # 子场景id
        self.id = id
        # 错误消息
        self.message = message
        # 子场景名称
        self.name = name
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 图片ID/视频ID
        self.resource_id = resource_id
        # 子场景状态
        self.status = status
        # 是否请求成功
        self.success = success
        # 图片路径/视频路径
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.cubemap_path is not None:
            result['CubemapPath'] = self.cubemap_path
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.name is not None:
            result['Name'] = self.name
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CubemapPath') is not None:
            self.cubemap_path = m.get('CubemapPath')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class DetailSubSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DetailSubSceneResponseBody = None,
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
            temp_model = DetailSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DropProjectRequest(TeaModel):
    def __init__(
        self,
        project_id: str = None,
    ):
        # 项目ID
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class DropProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID与入参中requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DropProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DropProjectResponseBody = None,
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
            temp_model = DropProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DropSceneRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # 主场景id
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DropSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DropSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DropSceneResponseBody = None,
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
            temp_model = DropSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DropSubSceneRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # 子场景ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class DropSubSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DropSubSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DropSubSceneResponseBody = None,
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
            temp_model = DropSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConnDataRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景ID
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetConnDataResponseBodyList(TeaModel):
    def __init__(
        self,
        id: str = None,
        map_id: str = None,
        type: str = None,
    ):
        # ID
        self.id = id
        # 关联的ID
        self.map_id = map_id
        # outer:外关联 inner：内关联 stair：楼梯关联
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.map_id is not None:
            result['MapId'] = self.map_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MapId') is not None:
            self.map_id = m.get('MapId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetConnDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        extend: str = None,
        list: List[GetConnDataResponseBodyList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        version: str = None,
    ):
        # 返回码
        self.code = code
        # 扩展信息
        self.extend = extend
        # 关联信息
        self.list = list
        # 错误消息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # 是否请求成功
        self.success = success
        # 版本
        self.version = version

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.extend is not None:
            result['Extend'] = self.extend
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Extend') is not None:
            self.extend = m.get('Extend')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetConnDataResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetConnDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConnDataResponseBody = None,
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
            temp_model = GetConnDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotspotConfigRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        preview_token: str = None,
        type: int = None,
    ):
        self.domain = domain
        self.enabled = enabled
        self.preview_token = preview_token
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetHotspotConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        self.data = data
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotspotConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotspotConfigResponseBody = None,
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
            temp_model = GetHotspotConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotspotSceneDataRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        preview_token: str = None,
        type: int = None,
    ):
        # 自定义oss域名（可为cdn域名）
        self.domain = domain
        # 是否开启自用资源访问
        self.enabled = enabled
        # 预览token
        self.preview_token = preview_token
        # 0 未发布， 1 已发布
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetHotspotSceneDataResponseBodyData(TeaModel):
    def __init__(
        self,
        model_token: str = None,
        preview_data: str = None,
        preview_token: str = None,
        scene_type: str = None,
    ):
        # 模型token（sgm token）
        self.model_token = model_token
        # html转译后的预览数据，包含图片、子场景ID等信息
        self.preview_data = preview_data
        # 预览token
        self.preview_token = preview_token
        # 3D模型：MODEL_3D 全景图片：PIC 全景视频：VIDEO
        self.scene_type = scene_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_token is not None:
            result['ModelToken'] = self.model_token
        if self.preview_data is not None:
            result['PreviewData'] = self.preview_data
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.scene_type is not None:
            result['SceneType'] = self.scene_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelToken') is not None:
            self.model_token = m.get('ModelToken')
        if m.get('PreviewData') is not None:
            self.preview_data = m.get('PreviewData')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('SceneType') is not None:
            self.scene_type = m.get('SceneType')
        return self


class GetHotspotSceneDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetHotspotSceneDataResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        self.data = data
        # 错误消息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
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
            temp_model = GetHotspotSceneDataResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotspotSceneDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotspotSceneDataResponseBody = None,
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
            temp_model = GetHotspotSceneDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHotspotTagRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        preview_token: str = None,
        sub_scene_uuid: str = None,
        type: str = None,
    ):
        self.domain = domain
        self.enabled = enabled
        self.preview_token = preview_token
        self.sub_scene_uuid = sub_scene_uuid
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.sub_scene_uuid is not None:
            result['SubSceneUuid'] = self.sub_scene_uuid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('SubSceneUuid') is not None:
            self.sub_scene_uuid = m.get('SubSceneUuid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetHotspotTagResponseBody(TeaModel):
    def __init__(
        self,
        data: str = None,
        err_message: str = None,
        object_string: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.object_string = object_string
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.object_string is not None:
            result['ObjectString'] = self.object_string
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ObjectString') is not None:
            self.object_string = m.get('ObjectString')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetHotspotTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetHotspotTagResponseBody = None,
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
            temp_model = GetHotspotTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJobRequest(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
    ):
        # 任务实例ID
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        return self


class GetJobResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        status: int = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 任务运行状态
        self.status = status
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetJobResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetJobResponseBody = None,
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
            temp_model = GetJobResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLayoutDataRequest(TeaModel):
    def __init__(
        self,
        sub_scene_id: str = None,
    ):
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetLayoutDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 标注信息
        self.data = data
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetLayoutDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLayoutDataResponseBody = None,
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
            temp_model = GetLayoutDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOriginLayoutDataRequest(TeaModel):
    def __init__(
        self,
        sub_scene_id: str = None,
    ):
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetOriginLayoutDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 标注数据
        self.data = data
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOriginLayoutDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOriginLayoutDataResponseBody = None,
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
            temp_model = GetOriginLayoutDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetOssPolicyRequest(TeaModel):
    def __init__(
        self,
        sub_scene_id: str = None,
    ):
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetOssPolicyResponseBody(TeaModel):
    def __init__(
        self,
        access_id: str = None,
        callback: str = None,
        code: int = None,
        dir: str = None,
        expire: str = None,
        host: str = None,
        message: str = None,
        policy: str = None,
        request_id: str = None,
        signature: str = None,
        success: bool = None,
    ):
        # accessId
        self.access_id = access_id
        # 上传回调
        self.callback = callback
        # 返回码
        self.code = code
        # 授权路径
        self.dir = dir
        # 授权失效时间(s)
        self.expire = expire
        # 上传地址
        self.host = host
        # 错误消息
        self.message = message
        # 授权
        self.policy = policy
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 签名
        self.signature = signature
        # 是否请求成功
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
        if self.callback is not None:
            result['Callback'] = self.callback
        if self.code is not None:
            result['Code'] = self.code
        if self.dir is not None:
            result['Dir'] = self.dir
        if self.expire is not None:
            result['Expire'] = self.expire
        if self.host is not None:
            result['Host'] = self.host
        if self.message is not None:
            result['Message'] = self.message
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
        if m.get('Callback') is not None:
            self.callback = m.get('Callback')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Dir') is not None:
            self.dir = m.get('Dir')
        if m.get('Expire') is not None:
            self.expire = m.get('Expire')
        if m.get('Host') is not None:
            self.host = m.get('Host')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Policy') is not None:
            self.policy = m.get('Policy')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Signature') is not None:
            self.signature = m.get('Signature')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetOssPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetOssPolicyResponseBody = None,
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
            temp_model = GetOssPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPolicyRequest(TeaModel):
    def __init__(
        self,
        sub_scene_uuid: str = None,
        type: str = None,
    ):
        self.sub_scene_uuid = sub_scene_uuid
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_uuid is not None:
            result['SubSceneUuid'] = self.sub_scene_uuid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubSceneUuid') is not None:
            self.sub_scene_uuid = m.get('SubSceneUuid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetPolicyResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        err_message: str = None,
        object_string: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.object_string = object_string
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.object_string is not None:
            result['ObjectString'] = self.object_string
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ObjectString') is not None:
            self.object_string = m.get('ObjectString')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetPolicyResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetPolicyResponseBody = None,
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
            temp_model = GetPolicyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRectifyImageRequest(TeaModel):
    def __init__(
        self,
        sub_scene_id: str = None,
    ):
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetRectifyImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        url: str = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
        self.success = success
        # 图片地址
        self.url = url

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetRectifyImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRectifyImageResponseBody = None,
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
            temp_model = GetRectifyImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSceneBuildTaskStatusRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景ID
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class GetSceneBuildTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        error_code: str = None,
        error_msg: str = None,
        id: str = None,
        message: str = None,
        request_id: str = None,
        scene_id: str = None,
        status: str = None,
        success: bool = None,
        type: str = None,
    ):
        # 返回码
        self.code = code
        # 任务失败错误码
        self.error_code = error_code
        # 任务失败错误消息
        self.error_msg = error_msg
        # 任务ID
        self.id = id
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 场景ID
        self.scene_id = scene_id
        # 未开始  init 处理中 失败     failure   processing  完成     succeed 取消     canceled
        self.status = status
        # 是否请求成功
        self.success = success
        # 墙线预测: wall_line  切图: cut_image  重建: build  直角优化：right_angle_optimization 其他：other
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.id is not None:
            result['Id'] = self.id
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSceneBuildTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSceneBuildTaskStatusResponseBody = None,
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
            temp_model = GetSceneBuildTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScenePreviewInfoRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        enabled: bool = None,
        model_token: str = None,
    ):
        # 自定义oss域名（可为cdn域名）
        self.domain = domain
        # 是否开启自用资源访问
        self.enabled = enabled
        # 模型token
        self.model_token = model_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.enabled is not None:
            result['Enabled'] = self.enabled
        if self.model_token is not None:
            result['ModelToken'] = self.model_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Enabled') is not None:
            self.enabled = m.get('Enabled')
        if m.get('ModelToken') is not None:
            self.model_token = m.get('ModelToken')
        return self


class GetScenePreviewInfoResponseBodyData(TeaModel):
    def __init__(
        self,
        model_path: str = None,
        pano_list: str = None,
        texture_model_path: str = None,
        texture_pano_path: str = None,
    ):
        # 模型地址
        self.model_path = model_path
        # html转译后的预览数据
        self.pano_list = pano_list
        # 模型的贴图路径
        self.texture_model_path = texture_model_path
        # 漫游后预览图片路径
        self.texture_pano_path = texture_pano_path

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.model_path is not None:
            result['ModelPath'] = self.model_path
        if self.pano_list is not None:
            result['PanoList'] = self.pano_list
        if self.texture_model_path is not None:
            result['TextureModelPath'] = self.texture_model_path
        if self.texture_pano_path is not None:
            result['TexturePanoPath'] = self.texture_pano_path
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ModelPath') is not None:
            self.model_path = m.get('ModelPath')
        if m.get('PanoList') is not None:
            self.pano_list = m.get('PanoList')
        if m.get('TextureModelPath') is not None:
            self.texture_model_path = m.get('TextureModelPath')
        if m.get('TexturePanoPath') is not None:
            self.texture_pano_path = m.get('TexturePanoPath')
        return self


class GetScenePreviewInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: GetScenePreviewInfoResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        self.data = data
        # 错误消息
        self.message = message
        # Id of the request
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
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
            temp_model = GetScenePreviewInfoResponseBodyData()
            self.data = temp_model.from_map(m['Data'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetScenePreviewInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetScenePreviewInfoResponseBody = None,
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
            temp_model = GetScenePreviewInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSingleConnDataRequest(TeaModel):
    def __init__(
        self,
        sub_scene_id: str = None,
    ):
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetSingleConnDataResponseBodyList(TeaModel):
    def __init__(
        self,
        id: str = None,
        map_id: str = None,
        type: str = None,
    ):
        # ID
        self.id = id
        # 关联ID
        self.map_id = map_id
        # outer:外关联 inner：内关联 stair：楼梯关联
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.map_id is not None:
            result['MapId'] = self.map_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('MapId') is not None:
            self.map_id = m.get('MapId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSingleConnDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        list: List[GetSingleConnDataResponseBodyList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        version: str = None,
    ):
        # 返回码
        self.code = code
        # 关联信息
        self.list = list
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
        self.success = success
        # 版本
        self.version = version

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.version is not None:
            result['Version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetSingleConnDataResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Version') is not None:
            self.version = m.get('Version')
        return self


class GetSingleConnDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSingleConnDataResponseBody = None,
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
            temp_model = GetSingleConnDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSubSceneTaskStatusRequest(TeaModel):
    def __init__(
        self,
        sub_scene_id: str = None,
    ):
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class GetSubSceneTaskStatusResponseBodyList(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        id: str = None,
        scene_id: str = None,
        status: str = None,
        sub_scene_id: str = None,
        type: str = None,
    ):
        # 任务失败错误码
        self.error_code = error_code
        # 任务失败错误信息
        self.error_msg = error_msg
        # 任务ID
        self.id = id
        # 场景ID
        self.scene_id = scene_id
        # 未开始  init 处理中   processing   失败     failure  完成     succeed  取消     canceled
        self.status = status
        # 子场景ID
        self.sub_scene_id = sub_scene_id
        # 墙线预测: wall_line   切图: cut_image 重建: build  直角优化：right_angle_optimization 其他：other
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.id is not None:
            result['Id'] = self.id
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.status is not None:
            result['Status'] = self.status
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetSubSceneTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        list: List[GetSubSceneTaskStatusResponseBodyList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 任务信息
        self.list = list
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
        self.success = success

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = GetSubSceneTaskStatusResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetSubSceneTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetSubSceneTaskStatusResponseBody = None,
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
            temp_model = GetSubSceneTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatusRequest(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        # 任务ID
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: int = None,
        error_code: str = None,
        error_msg: str = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
        type: str = None,
    ):
        # 返回码
        self.code = code
        # 任务执行失败错误码
        self.error_code = error_code
        # 任务执行失败错误消息
        self.error_msg = error_msg
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 未开始 :init 处理中 : processing    失败 :failure   完成 :succeed  取消 :canceled
        self.status = status
        # 是否请求成功
        self.success = success
        # 墙线预测: wall_line 切图: cut_image   重建: build  直角优化：right_angle_optimization  其他：other
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
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('Type') is not None:
            self.type = m.get('Type')
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
            temp_model = GetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWindowConfigRequest(TeaModel):
    def __init__(
        self,
        preview_token: str = None,
    ):
        self.preview_token = preview_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        return self


class GetWindowConfigResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        err_message: str = None,
        object_string: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.object_string = object_string
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.object_string is not None:
            result['ObjectString'] = self.object_string
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('ObjectString') is not None:
            self.object_string = m.get('ObjectString')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetWindowConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetWindowConfigResponseBody = None,
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
            temp_model = GetWindowConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LabelBuildRequest(TeaModel):
    def __init__(
        self,
        mode: str = None,
        scene_id: str = None,
    ):
        self.mode = mode
        # 场景ID
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class LabelBuildResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
        self.success = success
        # 重建任务ID
        self.task_id = task_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class LabelBuildResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LabelBuildResponseBody = None,
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
            temp_model = LabelBuildResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LinkImageRequest(TeaModel):
    def __init__(
        self,
        camera_height: int = None,
        file_name: str = None,
        platform: str = None,
        sub_scene_id: str = None,
    ):
        # 相机高度 单位 cm
        self.camera_height = camera_height
        # 图片或者视频名称xxx.jpg
        self.file_name = file_name
        # 平台标识，默认PC
        self.platform = platform
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_height is not None:
            result['CameraHeight'] = self.camera_height
        if self.file_name is not None:
            result['FileName'] = self.file_name
        if self.platform is not None:
            result['Platform'] = self.platform
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraHeight') is not None:
            self.camera_height = m.get('CameraHeight')
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class LinkImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        resource_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 图片/视频ID
        self.resource_id = resource_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class LinkImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: LinkImageResponseBody = None,
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
            temp_model = LinkImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListProjectRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # 项目名称（使用name%搜索）
        self.name = name
        # 页码
        self.page_num = page_num
        # 页长
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListProjectResponseBodyList(TeaModel):
    def __init__(
        self,
        business_id: int = None,
        business_name: str = None,
        create_time: int = None,
        id: str = None,
        modified_time: int = None,
        name: str = None,
        token: str = None,
    ):
        # 业务ID
        self.business_id = business_id
        # 业务名称
        self.business_name = business_name
        # 创建时间
        self.create_time = create_time
        # 项目ID
        self.id = id
        # 最后修改时间
        self.modified_time = modified_time
        # 项目名称
        self.name = name
        # Token
        self.token = token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.business_name is not None:
            result['BusinessName'] = self.business_name
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.id is not None:
            result['Id'] = self.id
        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time
        if self.name is not None:
            result['Name'] = self.name
        if self.token is not None:
            result['Token'] = self.token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('BusinessName') is not None:
            self.business_name = m.get('BusinessName')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Token') is not None:
            self.token = m.get('Token')
        return self


class ListProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        count: int = None,
        current_page: int = None,
        has_next: bool = None,
        list: List[ListProjectResponseBodyList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_page: int = None,
    ):
        # 返回码
        self.code = code
        # count
        self.count = count
        # 当前页
        self.current_page = current_page
        # 是否有下一页
        self.has_next = has_next
        # 项目数据
        self.list = list
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
        self.success = success
        # 总页数
        self.total_page = total_page

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListProjectResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListProjectResponseBody = None,
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
            temp_model = ListProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSceneRequest(TeaModel):
    def __init__(
        self,
        name: str = None,
        page_num: int = None,
        page_size: int = None,
        project_id: str = None,
    ):
        # 主场景名称
        self.name = name
        # 当前页
        self.page_num = page_num
        # 页长
        self.page_size = page_size
        # 所有项目Id
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['Name'] = self.name
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListSceneResponseBodyList(TeaModel):
    def __init__(
        self,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        name: str = None,
        preview_token: str = None,
        published: bool = None,
        source_num: int = None,
        sub_scene_num: int = None,
        type: str = None,
    ):
        # 创建时间
        self.gmt_create = gmt_create
        # 最后修改时间
        self.gmt_modified = gmt_modified
        # 主场景Id
        self.id = id
        # 场景名称
        self.name = name
        # 预览Token
        self.preview_token = preview_token
        # 是否已发布 true：已发布：false：未发布
        self.published = published
        # 资源数
        self.source_num = source_num
        # 子场景数
        self.sub_scene_num = sub_scene_num
        # 场景类型 3D模型：MODEL_3D  全景图片：PIC  全景视频：VIDEO
        self.type = type

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
        if self.name is not None:
            result['Name'] = self.name
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        if self.published is not None:
            result['Published'] = self.published
        if self.source_num is not None:
            result['SourceNum'] = self.source_num
        if self.sub_scene_num is not None:
            result['SubSceneNum'] = self.sub_scene_num
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        if m.get('Published') is not None:
            self.published = m.get('Published')
        if m.get('SourceNum') is not None:
            self.source_num = m.get('SourceNum')
        if m.get('SubSceneNum') is not None:
            self.sub_scene_num = m.get('SubSceneNum')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        count: int = None,
        current_page: int = None,
        has_next: bool = None,
        list: List[ListSceneResponseBodyList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_page: int = None,
    ):
        # 返回码
        self.code = code
        # 数据总数
        self.count = count
        # 当前页
        self.current_page = current_page
        # 是否有下一页
        self.has_next = has_next
        # 主场景数据
        self.list = list
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
        self.success = success
        # 总页数
        self.total_page = total_page

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListSceneResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSceneResponseBody = None,
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
            temp_model = ListSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListScenesRequest(TeaModel):
    def __init__(
        self,
        is_publish_query: bool = None,
        project_id: str = None,
    ):
        self.is_publish_query = is_publish_query
        self.project_id = project_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.is_publish_query is not None:
            result['IsPublishQuery'] = self.is_publish_query
        if self.project_id is not None:
            result['ProjectId'] = self.project_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsPublishQuery') is not None:
            self.is_publish_query = m.get('IsPublishQuery')
        if m.get('ProjectId') is not None:
            self.project_id = m.get('ProjectId')
        return self


class ListScenesResponseBodyData(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ListScenesResponseBody(TeaModel):
    def __init__(
        self,
        data: List[ListScenesResponseBodyData] = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
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
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = ListScenesResponseBodyData()
                self.data.append(temp_model.from_map(k))
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListScenesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListScenesResponseBody = None,
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
            temp_model = ListScenesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubSceneRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        scene_id: str = None,
        show_layout_data: bool = None,
    ):
        # 页码
        self.page_num = page_num
        # 页长
        self.page_size = page_size
        # 场景ID
        self.scene_id = scene_id
        self.show_layout_data = show_layout_data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.show_layout_data is not None:
            result['ShowLayoutData'] = self.show_layout_data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('ShowLayoutData') is not None:
            self.show_layout_data = m.get('ShowLayoutData')
        return self


class ListSubSceneResponseBodyList(TeaModel):
    def __init__(
        self,
        base_image_url: str = None,
        cover_url: str = None,
        cubemap_path: str = None,
        deleted: bool = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: str = None,
        layout_data: str = None,
        name: str = None,
        origin_url: str = None,
        resource_id: str = None,
        resource_name: str = None,
        status: int = None,
        url: str = None,
    ):
        # 2k基准图路径
        self.base_image_url = base_image_url
        # 图片路径/视频封面路径
        self.cover_url = cover_url
        # 切图的路径
        self.cubemap_path = cubemap_path
        # 是否删除
        self.deleted = deleted
        # 创建时间
        self.gmt_create = gmt_create
        # 最后修改时间
        self.gmt_modified = gmt_modified
        # 子场景ID
        self.id = id
        # 标注数据
        self.layout_data = layout_data
        # 子场景名称
        self.name = name
        # 原图地址
        self.origin_url = origin_url
        # 图片ID/视频ID
        self.resource_id = resource_id
        # 资源名称
        self.resource_name = resource_name
        # 子场景状态 1.未重建，      * 2.中间模型重建中，      * 3.中间模型重建完成，      * 4.待重建，      * 5.服务商重建中，      * 6.服务商重建完成，      * 7.已发布      * 8.发布中
        self.status = status
        # 图片路径/视频路径
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.base_image_url is not None:
            result['BaseImageUrl'] = self.base_image_url
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.cubemap_path is not None:
            result['CubemapPath'] = self.cubemap_path
        if self.deleted is not None:
            result['Deleted'] = self.deleted
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified
        if self.id is not None:
            result['Id'] = self.id
        if self.layout_data is not None:
            result['LayoutData'] = self.layout_data
        if self.name is not None:
            result['Name'] = self.name
        if self.origin_url is not None:
            result['OriginUrl'] = self.origin_url
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name
        if self.status is not None:
            result['Status'] = self.status
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaseImageUrl') is not None:
            self.base_image_url = m.get('BaseImageUrl')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('CubemapPath') is not None:
            self.cubemap_path = m.get('CubemapPath')
        if m.get('Deleted') is not None:
            self.deleted = m.get('Deleted')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('LayoutData') is not None:
            self.layout_data = m.get('LayoutData')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('OriginUrl') is not None:
            self.origin_url = m.get('OriginUrl')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListSubSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        count: int = None,
        current_page: int = None,
        has_next: bool = None,
        list: List[ListSubSceneResponseBodyList] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        total_page: int = None,
    ):
        # 返回码
        self.code = code
        # 数据总条数
        self.count = count
        # 当前页
        self.current_page = current_page
        # 是否有下一页
        self.has_next = has_next
        # 子场景列表集
        self.list = list
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
        self.success = success
        # 总页数
        self.total_page = total_page

    def validate(self):
        if self.list:
            for k in self.list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.count is not None:
            result['Count'] = self.count
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.total_page is not None:
            result['TotalPage'] = self.total_page
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListSubSceneResponseBodyList()
                self.list.append(temp_model.from_map(k))
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TotalPage') is not None:
            self.total_page = m.get('TotalPage')
        return self


class ListSubSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListSubSceneResponseBody = None,
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
            temp_model = ListSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OptimizeRightAngleRequest(TeaModel):
    def __init__(
        self,
        sub_scene_id: str = None,
    ):
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class OptimizeRightAngleResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
        self.success = success
        # 任务ID
        self.task_id = task_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class OptimizeRightAngleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: OptimizeRightAngleResponseBody = None,
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
            temp_model = OptimizeRightAngleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredImageRequest(TeaModel):
    def __init__(
        self,
        correct_vertical: bool = None,
        count_detect_door: int = None,
        detect_door: bool = None,
        sub_scene_id: str = None,
    ):
        # 是否垂直矫正
        self.correct_vertical = correct_vertical
        # 门数量(DetectDoor为false时，可为0)
        self.count_detect_door = count_detect_door
        # 是否门预测
        self.detect_door = detect_door
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.correct_vertical is not None:
            result['CorrectVertical'] = self.correct_vertical
        if self.count_detect_door is not None:
            result['CountDetectDoor'] = self.count_detect_door
        if self.detect_door is not None:
            result['DetectDoor'] = self.detect_door
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CorrectVertical') is not None:
            self.correct_vertical = m.get('CorrectVertical')
        if m.get('CountDetectDoor') is not None:
            self.count_detect_door = m.get('CountDetectDoor')
        if m.get('DetectDoor') is not None:
            self.detect_door = m.get('DetectDoor')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class PredImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
        self.success = success
        # 任务ID
        self.task_id = task_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class PredImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PredImageResponseBody = None,
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
            temp_model = PredImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PredictionWallLineRequest(TeaModel):
    def __init__(
        self,
        camera_height: int = None,
        url: str = None,
    ):
        # 相机高度 单位 cm
        self.camera_height = camera_height
        # 图片地址
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_height is not None:
            result['CameraHeight'] = self.camera_height
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraHeight') is not None:
            self.camera_height = m.get('CameraHeight')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class PredictionWallLineResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        sub_scene_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 子场景ID
        self.sub_scene_id = sub_scene_id
        # 是否请求成功
        self.success = success
        # 任务ID
        self.task_id = task_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class PredictionWallLineResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PredictionWallLineResponseBody = None,
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
            temp_model = PredictionWallLineResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishHotspotRequest(TeaModel):
    def __init__(
        self,
        param_tag: str = None,
        sub_scene_uuid: str = None,
    ):
        self.param_tag = param_tag
        self.sub_scene_uuid = sub_scene_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_tag is not None:
            result['ParamTag'] = self.param_tag
        if self.sub_scene_uuid is not None:
            result['SubSceneUuid'] = self.sub_scene_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamTag') is not None:
            self.param_tag = m.get('ParamTag')
        if m.get('SubSceneUuid') is not None:
            self.sub_scene_uuid = m.get('SubSceneUuid')
        return self


class PublishHotspotResponseBody(TeaModel):
    def __init__(
        self,
        data: Dict[str, Any] = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PublishHotspotResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishHotspotResponseBody = None,
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
            temp_model = PublishHotspotResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishSceneRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景ID
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class PublishSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        instance_id: str = None,
        message: str = None,
        preview_url: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 任务实例id
        self.instance_id = instance_id
        # 错误消息
        self.message = message
        # 预览链接
        self.preview_url = preview_url
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message is not None:
            result['Message'] = self.message
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PublishSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishSceneResponseBody = None,
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
            temp_model = PublishSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecoveryOriginImageRequest(TeaModel):
    def __init__(
        self,
        sub_scene_id: str = None,
    ):
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class RecoveryOriginImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RecoveryOriginImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecoveryOriginImageResponseBody = None,
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
            temp_model = RecoveryOriginImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RectVerticalRequest(TeaModel):
    def __init__(
        self,
        count_detect_door: int = None,
        detect_door: bool = None,
        sub_scene_id: str = None,
        vertical_rect: str = None,
    ):
        # 需要预测的门的数量
        self.count_detect_door = count_detect_door
        # 是否开启门预测
        self.detect_door = detect_door
        # 子场景ID
        self.sub_scene_id = sub_scene_id
        # 矫正数据
        self.vertical_rect = vertical_rect

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count_detect_door is not None:
            result['CountDetectDoor'] = self.count_detect_door
        if self.detect_door is not None:
            result['DetectDoor'] = self.detect_door
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        if self.vertical_rect is not None:
            result['VerticalRect'] = self.vertical_rect
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CountDetectDoor') is not None:
            self.count_detect_door = m.get('CountDetectDoor')
        if m.get('DetectDoor') is not None:
            self.detect_door = m.get('DetectDoor')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        if m.get('VerticalRect') is not None:
            self.vertical_rect = m.get('VerticalRect')
        return self


class RectVerticalResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RectVerticalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RectVerticalResponseBody = None,
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
            temp_model = RectVerticalResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RectifyImageRequest(TeaModel):
    def __init__(
        self,
        camera_height: int = None,
        url: str = None,
    ):
        # 相机高度 单位 cm
        self.camera_height = camera_height
        # 图片地址
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.camera_height is not None:
            result['CameraHeight'] = self.camera_height
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CameraHeight') is not None:
            self.camera_height = m.get('CameraHeight')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class RectifyImageResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        sub_scene_id: str = None,
        success: bool = None,
        task_id: str = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 子场景ID
        self.sub_scene_id = sub_scene_id
        # 是否请求成功
        self.success = success
        # 任务ID
        self.task_id = task_id

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        if self.success is not None:
            result['Success'] = self.success
        if self.task_id is not None:
            result['TaskId'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')
        return self


class RectifyImageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RectifyImageResponseBody = None,
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
            temp_model = RectifyImageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RollbackSubSceneRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
    ):
        # 子场景ID
        self.id = id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        return self


class RollbackSubSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RollbackSubSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RollbackSubSceneResponseBody = None,
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
            temp_model = RollbackSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveHotspotConfigRequest(TeaModel):
    def __init__(
        self,
        param_tag: str = None,
        preview_token: str = None,
    ):
        self.param_tag = param_tag
        self.preview_token = preview_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_tag is not None:
            result['ParamTag'] = self.param_tag
        if self.preview_token is not None:
            result['PreviewToken'] = self.preview_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamTag') is not None:
            self.param_tag = m.get('ParamTag')
        if m.get('PreviewToken') is not None:
            self.preview_token = m.get('PreviewToken')
        return self


class SaveHotspotConfigResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveHotspotConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveHotspotConfigResponseBody = None,
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
            temp_model = SaveHotspotConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SaveHotspotTagRequest(TeaModel):
    def __init__(
        self,
        param_tag: str = None,
        sub_scene_uuid: str = None,
    ):
        self.param_tag = param_tag
        self.sub_scene_uuid = sub_scene_uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.param_tag is not None:
            result['ParamTag'] = self.param_tag
        if self.sub_scene_uuid is not None:
            result['SubSceneUuid'] = self.sub_scene_uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParamTag') is not None:
            self.param_tag = m.get('ParamTag')
        if m.get('SubSceneUuid') is not None:
            self.sub_scene_uuid = m.get('SubSceneUuid')
        return self


class SaveHotspotTagResponseBody(TeaModel):
    def __init__(
        self,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.err_message = err_message
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.err_message is not None:
            result['ErrMessage'] = self.err_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SaveHotspotTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SaveHotspotTagResponseBody = None,
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
            temp_model = SaveHotspotTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScenePublishRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景ID
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class ScenePublishResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        preview_url: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 预览链接
        self.preview_url = preview_url
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ScenePublishResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ScenePublishResponseBody = None,
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
            temp_model = ScenePublishResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TempPreviewRequest(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
    ):
        # 场景ID
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class TempPreviewResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        key: str = None,
        message: str = None,
        preview_url: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 任务ID
        self.key = key
        # 错误消息
        self.message = message
        # 预览链接
        self.preview_url = preview_url
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.key is not None:
            result['Key'] = self.key
        if self.message is not None:
            result['Message'] = self.message
        if self.preview_url is not None:
            result['PreviewUrl'] = self.preview_url
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PreviewUrl') is not None:
            self.preview_url = m.get('PreviewUrl')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TempPreviewResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TempPreviewResponseBody = None,
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
            temp_model = TempPreviewResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TempPreviewStatusRequest(TeaModel):
    def __init__(
        self,
        key: str = None,
    ):
        # 任务ID
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        return self


class TempPreviewStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        status: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # processing：处理中 success：成功 failed：失败
        self.status = status
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.status is not None:
            result['Status'] = self.status
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class TempPreviewStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: TempPreviewStatusResponseBody = None,
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
            temp_model = TempPreviewStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConnDataRequest(TeaModel):
    def __init__(
        self,
        conn_data: str = None,
        scene_id: str = None,
    ):
        # 关联数据
        self.conn_data = conn_data
        # 场景ID
        self.scene_id = scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conn_data is not None:
            result['ConnData'] = self.conn_data
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConnData') is not None:
            self.conn_data = m.get('ConnData')
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        return self


class UpdateConnDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateConnDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateConnDataResponseBody = None,
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
            temp_model = UpdateConnDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLayoutDataRequest(TeaModel):
    def __init__(
        self,
        layout_data: str = None,
        sub_scene_id: str = None,
    ):
        # 标注数据
        self.layout_data = layout_data
        # 子场景ID
        self.sub_scene_id = sub_scene_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.layout_data is not None:
            result['LayoutData'] = self.layout_data
        if self.sub_scene_id is not None:
            result['SubSceneId'] = self.sub_scene_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LayoutData') is not None:
            self.layout_data = m.get('LayoutData')
        if m.get('SubSceneId') is not None:
            self.sub_scene_id = m.get('SubSceneId')
        return self


class UpdateLayoutDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateLayoutDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLayoutDataResponseBody = None,
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
            temp_model = UpdateLayoutDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateProjectRequest(TeaModel):
    def __init__(
        self,
        business_id: str = None,
        id: str = None,
        name: str = None,
    ):
        # 业务Id
        self.business_id = business_id
        # 项目id
        self.id = id
        # 项目名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.business_id is not None:
            result['BusinessId'] = self.business_id
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BusinessId') is not None:
            self.business_id = m.get('BusinessId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateProjectResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateProjectResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateProjectResponseBody = None,
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
            temp_model = UpdateProjectResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSceneRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # 场景Id
        self.id = id
        # 场景名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSceneResponseBody = None,
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
            temp_model = UpdateSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateSubSceneRequest(TeaModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        # 子场景ID
        self.id = id
        # 子场景名称
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class UpdateSubSceneResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 错误消息
        self.message = message
        # 请求ID，与入参requestId对应
        self.request_id = request_id
        # 是否请求成功
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
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateSubSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateSubSceneResponseBody = None,
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
            temp_model = UpdateSubSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



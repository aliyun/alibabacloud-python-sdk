# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class AddGroupMembersRequestRequestParamsInitMembers(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        role: int = None,
        nick: str = None,
        join_time: int = None,
        extensions: Dict[str, str] = None,
    ):
        self.app_uid = app_uid
        # 1群主，2管理员，3普通
        self.role = role
        self.nick = nick
        # unix毫秒数
        self.join_time = join_time
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.role is not None:
            result['Role'] = self.role
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class AddGroupMembersRequestRequestParams(TeaModel):
    def __init__(
        self,
        operator_app_uid: str = None,
        app_cid: str = None,
        init_members: List[AddGroupMembersRequestRequestParamsInitMembers] = None,
    ):
        # 操作者
        self.operator_app_uid = operator_app_uid
        # 会话id
        self.app_cid = app_cid
        # 初始化成员
        self.init_members = init_members

    def validate(self):
        if self.init_members:
            for k in self.init_members:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        result['InitMembers'] = []
        if self.init_members is not None:
            for k in self.init_members:
                result['InitMembers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        self.init_members = []
        if m.get('InitMembers') is not None:
            for k in m.get('InitMembers'):
                temp_model = AddGroupMembersRequestRequestParamsInitMembers()
                self.init_members.append(temp_model.from_map(k))
        return self


class AddGroupMembersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: AddGroupMembersRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 群加人请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = AddGroupMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class AddGroupMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 群加人请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class AddGroupMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddGroupMembersResponseBody = None,
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
            temp_model = AddGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGroupSilenceBlacklistRequestRequestParams(TeaModel):
    def __init__(
        self,
        operator_app_uid: str = None,
        app_cid: str = None,
        members: List[str] = None,
        silence_duration: int = None,
    ):
        # 操作者
        self.operator_app_uid = operator_app_uid
        # 群会话id
        self.app_cid = app_cid
        # 禁言用户列表
        self.members = members
        # 禁言时长
        self.silence_duration = silence_duration

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        return self


class AddGroupSilenceBlacklistRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: AddGroupSilenceBlacklistRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 群禁言添加白名单请求体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = AddGroupSilenceBlacklistRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class AddGroupSilenceBlacklistShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 群禁言添加白名单请求体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class AddGroupSilenceBlacklistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddGroupSilenceBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddGroupSilenceBlacklistResponseBody = None,
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
            temp_model = AddGroupSilenceBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGroupSilenceWhitelistRequestRequestParams(TeaModel):
    def __init__(
        self,
        operator_app_uid: str = None,
        app_cid: str = None,
        members: List[str] = None,
    ):
        # 操作者
        self.operator_app_uid = operator_app_uid
        # 群会话id
        self.app_cid = app_cid
        # 禁言用户列表
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class AddGroupSilenceWhitelistRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: AddGroupSilenceWhitelistRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 群禁言添加白名单请求体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = AddGroupSilenceWhitelistRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class AddGroupSilenceWhitelistShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 群禁言添加白名单请求体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class AddGroupSilenceWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddGroupSilenceWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddGroupSilenceWhitelistResponseBody = None,
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
            temp_model = AddGroupSilenceWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelSilenceAllGroupMembersRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        operator_app_uid: str = None,
    ):
        # 会话ID
        self.app_cid = app_cid
        # 操作者uid
        self.operator_app_uid = operator_app_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        return self


class CancelSilenceAllGroupMembersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: CancelSilenceAllGroupMembersRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = CancelSilenceAllGroupMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class CancelSilenceAllGroupMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class CancelSilenceAllGroupMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class CancelSilenceAllGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelSilenceAllGroupMembersResponseBody = None,
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
            temp_model = CancelSilenceAllGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequestRequestParamsInitMembers(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        role: int = None,
        nick: str = None,
        join_time: int = None,
        extensions: Dict[str, str] = None,
    ):
        self.app_uid = app_uid
        # 1群主，2管理员，3普通
        self.role = role
        self.nick = nick
        # unix时间毫秒数
        self.join_time = join_time
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.role is not None:
            result['Role'] = self.role
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class CreateGroupRequestRequestParams(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        creator_app_uid: str = None,
        title: str = None,
        icon_media_id: str = None,
        extensions: Dict[str, str] = None,
        init_members: List[CreateGroupRequestRequestParamsInitMembers] = None,
    ):
        # UUID(不可重复)
        self.uuid = uuid
        # 创建者
        self.creator_app_uid = creator_app_uid
        # 群标题
        self.title = title
        # 图标的id
        self.icon_media_id = icon_media_id
        # 拓展字段
        self.extensions = extensions
        # 初始化成员
        self.init_members = init_members

    def validate(self):
        if self.init_members:
            for k in self.init_members:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.creator_app_uid is not None:
            result['CreatorAppUid'] = self.creator_app_uid
        if self.title is not None:
            result['Title'] = self.title
        if self.icon_media_id is not None:
            result['IconMediaId'] = self.icon_media_id
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        result['InitMembers'] = []
        if self.init_members is not None:
            for k in self.init_members:
                result['InitMembers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('CreatorAppUid') is not None:
            self.creator_app_uid = m.get('CreatorAppUid')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('IconMediaId') is not None:
            self.icon_media_id = m.get('IconMediaId')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        self.init_members = []
        if m.get('InitMembers') is not None:
            for k in m.get('InitMembers'):
                temp_model = CreateGroupRequestRequestParamsInitMembers()
                self.init_members.append(temp_model.from_map(k))
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: CreateGroupRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 创建群聊请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = CreateGroupRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class CreateGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 创建群聊请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class CreateGroupResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
    ):
        self.app_cid = app_cid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class CreateGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result: CreateGroupResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = CreateGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateGroupResponseBody = None,
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
            temp_model = CreateGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoomRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        owner_id: str = None,
        owner_nick: str = None,
        title: str = None,
    ):
        self.domain = domain
        self.owner_id = owner_id
        self.owner_nick = owner_nick
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.owner_id is not None:
            result['ownerId'] = self.owner_id
        if self.owner_nick is not None:
            result['ownerNick'] = self.owner_nick
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('ownerId') is not None:
            self.owner_id = m.get('ownerId')
        if m.get('ownerNick') is not None:
            self.owner_nick = m.get('ownerNick')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class CreateRoomRequest(TeaModel):
    def __init__(
        self,
        request: CreateRoomRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = CreateRoomRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class CreateRoomResponseBodyResult(TeaModel):
    def __init__(
        self,
        room_id: str = None,
    ):
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.room_id is not None:
            result['roomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('roomId') is not None:
            self.room_id = m.get('roomId')
        return self


class CreateRoomResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: CreateRoomResponseBodyResult = None,
        request_id: str = None,
    ):
        # Id of the request
        self.success = success
        self.error_code = error_code
        self.error_msg = error_msg
        self.result = result
        self.request_id = request_id

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('Result') is not None:
            temp_model = CreateRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateRoomResponseBody = None,
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
            temp_model = CreateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DestroyRoomRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        room_id: str = None,
        open_id: str = None,
    ):
        self.domain = domain
        self.room_id = room_id
        self.open_id = open_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.room_id is not None:
            result['roomId'] = self.room_id
        if self.open_id is not None:
            result['openId'] = self.open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('roomId') is not None:
            self.room_id = m.get('roomId')
        if m.get('openId') is not None:
            self.open_id = m.get('openId')
        return self


class DestroyRoomRequest(TeaModel):
    def __init__(
        self,
        request: DestroyRoomRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = DestroyRoomRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class DestroyRoomResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        request_id: str = None,
        result: bool = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class DestroyRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DestroyRoomResponseBody = None,
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
            temp_model = DestroyRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DismissGroupRequestRequestParams(TeaModel):
    def __init__(
        self,
        operator_app_uid: str = None,
        app_cid: str = None,
    ):
        # 操作用户
        self.operator_app_uid = operator_app_uid
        # 会话id
        self.app_cid = app_cid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class DismissGroupRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: DismissGroupRequestRequestParams = None,
    ):
        self.app_id = app_id
        # 解散群聊请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = DismissGroupRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class DismissGroupShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        # 解散群聊请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class DismissGroupResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DismissGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DismissGroupResponseBody = None,
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
            temp_model = DismissGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupMemberByIdsRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uids: List[str] = None,
    ):
        # 会话id
        self.app_cid = app_cid
        # appUid
        self.app_uids = app_uids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        return self


class GetGroupMemberByIdsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: GetGroupMemberByIdsRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 群聊设置扩展字段请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetGroupMemberByIdsRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetGroupMemberByIdsShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 群聊设置扩展字段请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetGroupMemberByIdsResponseBodyResultMembers(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        role: int = None,
        nick: str = None,
        join_time: int = None,
        extensions: Dict[str, str] = None,
    ):
        self.app_uid = app_uid
        self.role = role
        self.nick = nick
        self.join_time = join_time
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.role is not None:
            result['Role'] = self.role
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class GetGroupMemberByIdsResponseBodyResult(TeaModel):
    def __init__(
        self,
        members: List[GetGroupMemberByIdsResponseBodyResultMembers] = None,
    ):
        # 群成员
        self.members = members

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Members'] = []
        if self.members is not None:
            for k in self.members:
                result['Members'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.members = []
        if m.get('Members') is not None:
            for k in m.get('Members'):
                temp_model = GetGroupMemberByIdsResponseBodyResultMembers()
                self.members.append(temp_model.from_map(k))
        return self


class GetGroupMemberByIdsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result: GetGroupMemberByIdsResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetGroupMemberByIdsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetGroupMemberByIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetGroupMemberByIdsResponseBody = None,
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
            temp_model = GetGroupMemberByIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginTokenRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        app_key: str = None,
        device_id: str = None,
    ):
        # 用户ID
        self.app_uid = app_uid
        # AppKey
        self.app_key = app_key
        # 设备ID
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class GetLoginTokenRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: GetLoginTokenRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetLoginTokenRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetLoginTokenShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetLoginTokenResponseBodyResult(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        refresh_token: str = None,
        access_token_expired_time: int = None,
    ):
        # 登录Tokon
        self.access_token = access_token
        # 更新Token
        self.refresh_token = refresh_token
        # 登录Token过期时间
        self.access_token_expired_time = access_token_expired_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        return self


class GetLoginTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result: GetLoginTokenResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetLoginTokenResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLoginTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLoginTokenResponseBody = None,
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
            temp_model = GetLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaUploadUrlRequestRequestParams(TeaModel):
    def __init__(
        self,
        type: int = None,
    ):
        # 多媒体资源类型(取值参照文档中类型枚举值)
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetMediaUploadUrlRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: GetMediaUploadUrlRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetMediaUploadUrlRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetMediaUploadUrlShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetMediaUploadUrlResponseBodyResult(TeaModel):
    def __init__(
        self,
        upload_url: str = None,
        media_id: str = None,
    ):
        # 上传Url
        self.upload_url = upload_url
        # 多媒体文件ID
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        return self


class GetMediaUploadUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result: GetMediaUploadUrlResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        # 调用返回值
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetMediaUploadUrlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMediaUploadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMediaUploadUrlResponseBody = None,
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
            temp_model = GetMediaUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaUrlRequestRequestParams(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        url_expire_time: int = None,
    ):
        # 多媒体资源ID
        self.media_id = media_id
        # URL过期时间(秒，最大86400)
        self.url_expire_time = url_expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.url_expire_time is not None:
            result['UrlExpireTime'] = self.url_expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('UrlExpireTime') is not None:
            self.url_expire_time = m.get('UrlExpireTime')
        return self


class GetMediaUrlRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: GetMediaUrlRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetMediaUrlRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetMediaUrlShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetMediaUrlResponseBodyResult(TeaModel):
    def __init__(
        self,
        url: str = None,
    ):
        # 文件Url
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class GetMediaUrlResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result: GetMediaUrlResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetMediaUrlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMediaUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMediaUrlResponseBody = None,
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
            temp_model = GetMediaUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageByIdRequestRequestParams(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        # 消息Id
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class GetMessageByIdRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: GetMessageByIdRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = GetMessageByIdRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetMessageByIdShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class GetMessageByIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
        app_cid: str = None,
        conversation_type: int = None,
        create_time: int = None,
        sender_id: str = None,
        content_type: int = None,
        content: str = None,
        extensions: Dict[str, str] = None,
    ):
        # 消息Id
        self.msg_id = msg_id
        # 会话Id
        self.app_cid = app_cid
        # 会话类型
        self.conversation_type = conversation_type
        # 创建时间
        self.create_time = create_time
        # 发送者的用户Id
        self.sender_id = sender_id
        # 消息类型
        self.content_type = content_type
        # 消息体
        self.content = content
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.conversation_type is not None:
            result['ConversationType'] = self.conversation_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content is not None:
            result['Content'] = self.content
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('ConversationType') is not None:
            self.conversation_type = m.get('ConversationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class GetMessageByIdResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result: GetMessageByIdResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = GetMessageByIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMessageByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetMessageByIdResponseBody = None,
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
            temp_model = GetMessageByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportGroupChatConversationRequestRequestParams(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        owner_app_uid: str = None,
        title: str = None,
        icon_media_id: str = None,
        member_limit: int = None,
        extensions: Dict[str, str] = None,
        create_time: int = None,
        silence_all: bool = None,
    ):
        # 唯一标识，用于重入
        self.uuid = uuid
        # 群主uid
        self.owner_app_uid = owner_app_uid
        # 群标题
        self.title = title
        # 群头像
        self.icon_media_id = icon_media_id
        # 群上限
        self.member_limit = member_limit
        # 扩展字段
        self.extensions = extensions
        # 创建时间
        self.create_time = create_time
        # 是否全员禁言
        self.silence_all = silence_all

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.owner_app_uid is not None:
            result['OwnerAppUid'] = self.owner_app_uid
        if self.title is not None:
            result['Title'] = self.title
        if self.icon_media_id is not None:
            result['IconMediaId'] = self.icon_media_id
        if self.member_limit is not None:
            result['MemberLimit'] = self.member_limit
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.silence_all is not None:
            result['SilenceAll'] = self.silence_all
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('OwnerAppUid') is not None:
            self.owner_app_uid = m.get('OwnerAppUid')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('IconMediaId') is not None:
            self.icon_media_id = m.get('IconMediaId')
        if m.get('MemberLimit') is not None:
            self.member_limit = m.get('MemberLimit')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SilenceAll') is not None:
            self.silence_all = m.get('SilenceAll')
        return self


class ImportGroupChatConversationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: ImportGroupChatConversationRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ImportGroupChatConversationRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ImportGroupChatConversationShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ImportGroupChatConversationResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
    ):
        # 群ID
        self.app_cid = app_cid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class ImportGroupChatConversationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result: ImportGroupChatConversationResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = ImportGroupChatConversationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ImportGroupChatConversationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportGroupChatConversationResponseBody = None,
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
            temp_model = ImportGroupChatConversationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportGroupChatMemberRequestRequestParamsGroupChatMembers(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        role: int = None,
        nick: str = None,
        top: bool = None,
        red_point: int = None,
        mute: bool = None,
        visible: bool = None,
        join_time: int = None,
        modify_time: int = None,
        extensions: Dict[str, str] = None,
    ):
        # 用户ID
        self.app_uid = app_uid
        # 成员权限
        self.role = role
        # 昵称
        self.nick = nick
        # 是否置顶
        self.top = top
        # 未读数
        self.red_point = red_point
        # 是否免打扰
        self.mute = mute
        # 是否可见
        self.visible = visible
        # 入群时间戳
        self.join_time = join_time
        # 最后修改时间
        self.modify_time = modify_time
        # 自定义信息
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.role is not None:
            result['Role'] = self.role
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.top is not None:
            result['Top'] = self.top
        if self.red_point is not None:
            result['RedPoint'] = self.red_point
        if self.mute is not None:
            result['Mute'] = self.mute
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('RedPoint') is not None:
            self.red_point = m.get('RedPoint')
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class ImportGroupChatMemberRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        group_chat_members: List[ImportGroupChatMemberRequestRequestParamsGroupChatMembers] = None,
    ):
        # 群ID
        self.app_cid = app_cid
        self.group_chat_members = group_chat_members

    def validate(self):
        if self.group_chat_members:
            for k in self.group_chat_members:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        result['GroupChatMembers'] = []
        if self.group_chat_members is not None:
            for k in self.group_chat_members:
                result['GroupChatMembers'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        self.group_chat_members = []
        if m.get('GroupChatMembers') is not None:
            for k in m.get('GroupChatMembers'):
                temp_model = ImportGroupChatMemberRequestRequestParamsGroupChatMembers()
                self.group_chat_members.append(temp_model.from_map(k))
        return self


class ImportGroupChatMemberRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: ImportGroupChatMemberRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ImportGroupChatMemberRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ImportGroupChatMemberShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ImportGroupChatMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ImportGroupChatMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportGroupChatMemberResponseBody = None,
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
            temp_model = ImportGroupChatMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportMessageRequestRequestParamsMessages(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        app_cid: str = None,
        conversation_type: int = None,
        sender_id: str = None,
        receiver_ids: List[str] = None,
        content_type: int = None,
        content: str = None,
        create_time: int = None,
        extensions: Dict[str, str] = None,
    ):
        # 唯一标识，用于重入
        self.uuid = uuid
        # 会话ID
        self.app_cid = app_cid
        # 会话类型1 单聊 2 群聊
        self.conversation_type = conversation_type
        # 发送者ID
        self.sender_id = sender_id
        # 接受者列表, 群聊如果列表为空者全员接收
        self.receiver_ids = receiver_ids
        # 消息类型
        self.content_type = content_type
        # 消息内容
        self.content = content
        # 消息发送时间戳
        self.create_time = create_time
        # 自定义信息
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.conversation_type is not None:
            result['ConversationType'] = self.conversation_type
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.receiver_ids is not None:
            result['ReceiverIds'] = self.receiver_ids
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content is not None:
            result['Content'] = self.content
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('ConversationType') is not None:
            self.conversation_type = m.get('ConversationType')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('ReceiverIds') is not None:
            self.receiver_ids = m.get('ReceiverIds')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class ImportMessageRequestRequestParams(TeaModel):
    def __init__(
        self,
        messages: List[ImportMessageRequestRequestParamsMessages] = None,
    ):
        self.messages = messages

    def validate(self):
        if self.messages:
            for k in self.messages:
                if k:
                    k.validate()

    def to_map(self):
        result = dict()
        result['Messages'] = []
        if self.messages is not None:
            for k in self.messages:
                result['Messages'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.messages = []
        if m.get('Messages') is not None:
            for k in m.get('Messages'):
                temp_model = ImportMessageRequestRequestParamsMessages()
                self.messages.append(temp_model.from_map(k))
        return self


class ImportMessageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: ImportMessageRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ImportMessageRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ImportMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ResultImportMessageResultValue(TeaModel):
    def __init__(
        self,
        result: int = None,
        msg_id: str = None,
    ):
        # 0 成功
        self.result = result
        # 消息ID
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.result is not None:
            result['result'] = self.result
        if self.msg_id is not None:
            result['msgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('msgId') is not None:
            self.msg_id = m.get('msgId')
        return self


class ImportMessageResponseBodyResult(TeaModel):
    def __init__(
        self,
        import_message_result: Dict[str, ResultImportMessageResultValue] = None,
    ):
        self.import_message_result = import_message_result

    def validate(self):
        if self.import_message_result:
            for v in self.import_message_result.values():
                if v:
                    v.validate()

    def to_map(self):
        result = dict()
        result['ImportMessageResult'] = {}
        if self.import_message_result is not None:
            for k, v in self.import_message_result.items():
                result['ImportMessageResult'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.import_message_result = {}
        if m.get('ImportMessageResult') is not None:
            for k, v in m.get('ImportMessageResult').items():
                temp_model = ResultImportMessageResultValue()
                self.import_message_result[k] = temp_model.from_map(v)
        return self


class ImportMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result: ImportMessageResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = ImportMessageResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ImportMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportMessageResponseBody = None,
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
            temp_model = ImportMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportSingleConversationRequestRequestParamsConversation(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uids: List[str] = None,
        extensions: Dict[str, str] = None,
        create_time: int = None,
    ):
        # 会话ID
        self.app_cid = app_cid
        # 用户ID列表
        self.app_uids = app_uids
        # 扩展字段
        self.extensions = extensions
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class RequestParamsUserConversationsValue(TeaModel):
    def __init__(
        self,
        top: bool = None,
        red_point: int = None,
        mute: bool = None,
        visible: bool = None,
        create_time: int = None,
        modify_time: int = None,
        user_extensions: Dict[str, str] = None,
    ):
        # 是否置顶
        self.top = top
        # 未读数
        self.red_point = red_point
        # 是否免打扰
        self.mute = mute
        # 是否可见
        self.visible = visible
        # 创建时间戳
        self.create_time = create_time
        # 修改时间戳
        self.modify_time = modify_time
        # 自定义信息
        self.user_extensions = user_extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.top is not None:
            result['Top'] = self.top
        if self.red_point is not None:
            result['RedPoint'] = self.red_point
        if self.mute is not None:
            result['Mute'] = self.mute
        if self.visible is not None:
            result['Visible'] = self.visible
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.user_extensions is not None:
            result['UserExtensions'] = self.user_extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('RedPoint') is not None:
            self.red_point = m.get('RedPoint')
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('UserExtensions') is not None:
            self.user_extensions = m.get('UserExtensions')
        return self


class ImportSingleConversationRequestRequestParams(TeaModel):
    def __init__(
        self,
        conversation: ImportSingleConversationRequestRequestParamsConversation = None,
        user_conversations: Dict[str, RequestParamsUserConversationsValue] = None,
    ):
        # 会话基础信息
        self.conversation = conversation
        # 用户会话视图
        self.user_conversations = user_conversations

    def validate(self):
        if self.conversation:
            self.conversation.validate()
        if self.user_conversations:
            for v in self.user_conversations.values():
                if v:
                    v.validate()

    def to_map(self):
        result = dict()
        if self.conversation is not None:
            result['Conversation'] = self.conversation.to_map()
        result['UserConversations'] = {}
        if self.user_conversations is not None:
            for k, v in self.user_conversations.items():
                result['UserConversations'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Conversation') is not None:
            temp_model = ImportSingleConversationRequestRequestParamsConversation()
            self.conversation = temp_model.from_map(m['Conversation'])
        self.user_conversations = {}
        if m.get('UserConversations') is not None:
            for k, v in m.get('UserConversations').items():
                temp_model = RequestParamsUserConversationsValue()
                self.user_conversations[k] = temp_model.from_map(v)
        return self


class ImportSingleConversationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: ImportSingleConversationRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ImportSingleConversationRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ImportSingleConversationShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ImportSingleConversationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ImportSingleConversationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ImportSingleConversationResponseBody = None,
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
            temp_model = ImportSingleConversationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InitTenantRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
    ):
        self.domain = domain

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        return self


class InitTenantRequest(TeaModel):
    def __init__(
        self,
        request: InitTenantRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = InitTenantRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class InitTenantResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: bool = None,
        request_id: str = None,
    ):
        # Id of the request
        self.success = success
        self.error_code = error_code
        self.error_msg = error_msg
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class InitTenantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: InitTenantResponseBody = None,
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
            temp_model = InitTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KickOffRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        app_keys: List[str] = None,
        information: str = None,
    ):
        # 用户ID
        self.app_uid = app_uid
        # 被踢下线的App的AppKey列表，为空时全部踢下线
        self.app_keys = app_keys
        # 下线文案
        self.information = information

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_keys is not None:
            result['AppKeys'] = self.app_keys
        if self.information is not None:
            result['Information'] = self.information
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppKeys') is not None:
            self.app_keys = m.get('AppKeys')
        if m.get('Information') is not None:
            self.information = m.get('Information')
        return self


class KickOffRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: KickOffRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = KickOffRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class KickOffShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class KickOffResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class KickOffResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: KickOffResponseBody = None,
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
            temp_model = KickOffResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupSilenceMembersRequestRequestParams(TeaModel):
    def __init__(
        self,
        operator_app_uid: str = None,
        app_cid: str = None,
    ):
        # 操作者
        self.operator_app_uid = operator_app_uid
        # 群会话id
        self.app_cid = app_cid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class ListGroupSilenceMembersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: ListGroupSilenceMembersRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 群禁言添加白名单请求体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = ListGroupSilenceMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ListGroupSilenceMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 群禁言添加白名单请求体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ListGroupSilenceMembersResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        whitelist: List[str] = None,
        blacklist: Dict[str, str] = None,
    ):
        # 群会话id
        self.app_cid = app_cid
        # 禁言白名单
        self.whitelist = whitelist
        # 禁言黑名单用户及对应禁言时长
        self.blacklist = blacklist

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        if self.blacklist is not None:
            result['Blacklist'] = self.blacklist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        if m.get('Blacklist') is not None:
            self.blacklist = m.get('Blacklist')
        return self


class ListGroupSilenceMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result: ListGroupSilenceMembersResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = ListGroupSilenceMembersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListGroupSilenceMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListGroupSilenceMembersResponseBody = None,
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
            temp_model = ListGroupSilenceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecallMessageRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        app_cid: str = None,
        msg_id: str = None,
        type: int = None,
        operator_type: int = None,
        extensions: Dict[str, str] = None,
    ):
        # 操作者ID
        self.app_uid = app_uid
        # 会话ID
        self.app_cid = app_cid
        # 消息ID
        self.msg_id = msg_id
        # 撤回显示类型（默认为0)。0：静默撤回，不显示撤回信息，1：普通撤回，显示撤回信息；
        self.type = type
        # 操作者类型(默认为0)。0: 发送者; 1: 群主; 2: 系统; 3: 安全合规; 101: 业务自定义类型
        self.operator_type = operator_type
        # 业务自定义扩展字段
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.type is not None:
            result['Type'] = self.type
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class RecallMessageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RecallMessageRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RecallMessageRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RecallMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RecallMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RecallMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RecallMessageResponseBody = None,
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
            temp_model = RecallMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: Dict[str, Any] = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params = m.get('RequestParams')
        return self


class RemoveExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveExtensionByKeysResponseBody = None,
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
            temp_model = RemoveExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        keys: List[str] = None,
    ):
        # 会话id
        self.app_cid = app_cid
        # 拓展字段的key
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class RemoveGroupExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveGroupExtensionByKeysRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 移除群聊拓展字段请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveGroupExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveGroupExtensionByKeysShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 移除群聊拓展字段请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveGroupExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveGroupExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveGroupExtensionByKeysResponseBody = None,
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
            temp_model = RemoveGroupExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupMembersRequestRequestParams(TeaModel):
    def __init__(
        self,
        operator_app_uid: str = None,
        app_cid: str = None,
        app_uids_removed: List[str] = None,
    ):
        self.operator_app_uid = operator_app_uid
        self.app_cid = app_cid
        self.app_uids_removed = app_uids_removed

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uids_removed is not None:
            result['AppUidsRemoved'] = self.app_uids_removed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUidsRemoved') is not None:
            self.app_uids_removed = m.get('AppUidsRemoved')
        return self


class RemoveGroupMembersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveGroupMembersRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 群踢人请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveGroupMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveGroupMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 群踢人请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveGroupMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveGroupMembersResponseBody = None,
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
            temp_model = RemoveGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupSilenceBlacklistRequestRequestParams(TeaModel):
    def __init__(
        self,
        operator_app_uid: str = None,
        app_cid: str = None,
        members: List[str] = None,
    ):
        # 操作者
        self.operator_app_uid = operator_app_uid
        # 群会话id
        self.app_cid = app_cid
        # 禁言用户列表
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class RemoveGroupSilenceBlacklistRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveGroupSilenceBlacklistRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 群禁言删除黑名单请求体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveGroupSilenceBlacklistRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveGroupSilenceBlacklistShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 群禁言删除黑名单请求体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveGroupSilenceBlacklistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveGroupSilenceBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveGroupSilenceBlacklistResponseBody = None,
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
            temp_model = RemoveGroupSilenceBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupSilenceWhitelistRequestRequestParams(TeaModel):
    def __init__(
        self,
        operator_app_uid: str = None,
        app_cid: str = None,
        members: List[str] = None,
    ):
        # 操作者
        self.operator_app_uid = operator_app_uid
        # 群会话id
        self.app_cid = app_cid
        # 禁言用户列表
        self.members = members

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        return self


class RemoveGroupSilenceWhitelistRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveGroupSilenceWhitelistRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 群禁言添加白名单请求体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveGroupSilenceWhitelistRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveGroupSilenceWhitelistShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 群禁言添加白名单请求体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveGroupSilenceWhitelistResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveGroupSilenceWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveGroupSilenceWhitelistResponseBody = None,
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
            temp_model = RemoveGroupSilenceWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveMessageExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        msg_id: str = None,
        keys: List[str] = None,
    ):
        # 会话ID
        self.app_cid = app_cid
        # 消息ID
        self.msg_id = msg_id
        # 需删除的Key
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class RemoveMessageExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveMessageExtensionByKeysRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveMessageExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveMessageExtensionByKeysShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveMessageExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 错误码，成功时为0
        self.code = code
        # 错误信息，成功时为0	空
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveMessageExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveMessageExtensionByKeysResponseBody = None,
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
            temp_model = RemoveMessageExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSingleChatExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        app_cid: str = None,
        keys: List[str] = None,
    ):
        # 用户id
        self.app_uid = app_uid
        # 会话id
        self.app_cid = app_cid
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class RemoveSingleChatExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveSingleChatExtensionByKeysRequestRequestParams = None,
    ):
        self.app_id = app_id
        # 单聊移除拓展字段请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveSingleChatExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveSingleChatExtensionByKeysShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        # 单聊移除拓展字段请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveSingleChatExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveSingleChatExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveSingleChatExtensionByKeysResponseBody = None,
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
            temp_model = RemoveSingleChatExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserConversationExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        app_cid: str = None,
        keys: List[str] = None,
    ):
        # 用户id
        self.app_uid = app_uid
        # 会话id
        self.app_cid = app_cid
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class RemoveUserConversationExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveUserConversationExtensionByKeysRequestRequestParams = None,
    ):
        self.app_id = app_id
        # 移除用户拓展字段请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = RemoveUserConversationExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveUserConversationExtensionByKeysShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        # 移除用户拓展字段请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class RemoveUserConversationExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveUserConversationExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveUserConversationExtensionByKeysResponseBody = None,
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
            temp_model = RemoveUserConversationExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: Dict[str, Any] = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params = m.get('RequestParams')
        return self


class RemoveUserExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class RemoveUserExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveUserExtensionByKeysResponseBody = None,
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
            temp_model = RemoveUserExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequestRequestParamsOptionsReceiveScopeOption(TeaModel):
    def __init__(
        self,
        receiver_ids: List[str] = None,
        exclude_receiver_ids: List[str] = None,
        receive_scope: int = None,
    ):
        # 接受者列表
        self.receiver_ids = receiver_ids
        # 不接收者列表
        self.exclude_receiver_ids = exclude_receiver_ids
        # 消息获取控制。0: 会话内除指定ExcludeReceivers均可获取；1: 会话内仅指定ReceiverIds可获取
        self.receive_scope = receive_scope

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.receiver_ids is not None:
            result['ReceiverIds'] = self.receiver_ids
        if self.exclude_receiver_ids is not None:
            result['ExcludeReceiverIds'] = self.exclude_receiver_ids
        if self.receive_scope is not None:
            result['ReceiveScope'] = self.receive_scope
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiverIds') is not None:
            self.receiver_ids = m.get('ReceiverIds')
        if m.get('ExcludeReceiverIds') is not None:
            self.exclude_receiver_ids = m.get('ExcludeReceiverIds')
        if m.get('ReceiveScope') is not None:
            self.receive_scope = m.get('ReceiveScope')
        return self


class RequestParamsOptionsSingleChatCreateRequestUserConversationValue(TeaModel):
    def __init__(
        self,
        user_extensions: Dict[str, str] = None,
    ):
        # 扩展信息
        self.user_extensions = user_extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.user_extensions is not None:
            result['UserExtensions'] = self.user_extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserExtensions') is not None:
            self.user_extensions = m.get('UserExtensions')
        return self


class SendMessageRequestRequestParamsOptionsSingleChatCreateRequest(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uids: List[str] = None,
        extensions: Dict[str, str] = None,
        user_conversation: Dict[str, RequestParamsOptionsSingleChatCreateRequestUserConversationValue] = None,
    ):
        # 单聊会话ID
        self.app_cid = app_cid
        # 用户ID列表
        self.app_uids = app_uids
        # 扩展信息
        self.extensions = extensions
        # 用户会话视图信息
        self.user_conversation = user_conversation

    def validate(self):
        if self.user_conversation:
            for v in self.user_conversation.values():
                if v:
                    v.validate()

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        result['UserConversation'] = {}
        if self.user_conversation is not None:
            for k, v in self.user_conversation.items():
                result['UserConversation'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        self.user_conversation = {}
        if m.get('UserConversation') is not None:
            for k, v in m.get('UserConversation').items():
                temp_model = RequestParamsOptionsSingleChatCreateRequestUserConversationValue()
                self.user_conversation[k] = temp_model.from_map(v)
        return self


class SendMessageRequestRequestParamsOptions(TeaModel):
    def __init__(
        self,
        red_point_policy: int = None,
        receive_scope_option: SendMessageRequestRequestParamsOptionsReceiveScopeOption = None,
        single_chat_create_request: SendMessageRequestRequestParamsOptionsSingleChatCreateRequest = None,
    ):
        # 未读消息小红点控制。0:增加小红点; 1:不增加小红点
        self.red_point_policy = red_point_policy
        # 接受相关设置
        self.receive_scope_option = receive_scope_option
        # 单聊会话不存在时新建自定义单聊请求体
        self.single_chat_create_request = single_chat_create_request

    def validate(self):
        if self.receive_scope_option:
            self.receive_scope_option.validate()
        if self.single_chat_create_request:
            self.single_chat_create_request.validate()

    def to_map(self):
        result = dict()
        if self.red_point_policy is not None:
            result['RedPointPolicy'] = self.red_point_policy
        if self.receive_scope_option is not None:
            result['ReceiveScopeOption'] = self.receive_scope_option.to_map()
        if self.single_chat_create_request is not None:
            result['SingleChatCreateRequest'] = self.single_chat_create_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RedPointPolicy') is not None:
            self.red_point_policy = m.get('RedPointPolicy')
        if m.get('ReceiveScopeOption') is not None:
            temp_model = SendMessageRequestRequestParamsOptionsReceiveScopeOption()
            self.receive_scope_option = temp_model.from_map(m['ReceiveScopeOption'])
        if m.get('SingleChatCreateRequest') is not None:
            temp_model = SendMessageRequestRequestParamsOptionsSingleChatCreateRequest()
            self.single_chat_create_request = temp_model.from_map(m['SingleChatCreateRequest'])
        return self


class SendMessageRequestRequestParams(TeaModel):
    def __init__(
        self,
        uuid: str = None,
        app_cid: str = None,
        conversation_type: int = None,
        sender_id: str = None,
        content_type: int = None,
        content: str = None,
        extensions: Dict[str, str] = None,
        options: SendMessageRequestRequestParamsOptions = None,
    ):
        # 消息UUID
        self.uuid = uuid
        # 会话ID
        self.app_cid = app_cid
        # 会话类型
        self.conversation_type = conversation_type
        # 发送者UID
        self.sender_id = sender_id
        # 消息内容类型
        self.content_type = content_type
        # 消息内容Json
        self.content = content
        # 消息扩展字段
        self.extensions = extensions
        # 消息设置
        self.options = options

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        result = dict()
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.conversation_type is not None:
            result['ConversationType'] = self.conversation_type
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.content is not None:
            result['Content'] = self.content
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.options is not None:
            result['Options'] = self.options.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('ConversationType') is not None:
            self.conversation_type = m.get('ConversationType')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('Options') is not None:
            temp_model = SendMessageRequestRequestParamsOptions()
            self.options = temp_model.from_map(m['Options'])
        return self


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SendMessageRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 消息发送请求体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SendMessageRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SendMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 消息发送请求体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SendMessageResponseBodyResult(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
        create_time: int = None,
    ):
        # 消息ID
        self.msg_id = msg_id
        # 消息创建时间戳(毫秒)
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
        result: SendMessageResponseBodyResult = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            temp_model = SendMessageResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendMessageResponseBody = None,
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: Dict[str, Any] = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params = m.get('RequestParams')
        return self


class SetExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetExtensionByKeysResponseBody = None,
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
            temp_model = SetExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGroupExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        extensions: Dict[str, str] = None,
    ):
        self.app_cid = app_cid
        # 扩展字段
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class SetGroupExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SetGroupExtensionByKeysRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 群聊设置扩展字段请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SetGroupExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetGroupExtensionByKeysShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 群聊设置扩展字段请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SetGroupExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetGroupExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetGroupExtensionByKeysResponseBody = None,
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
            temp_model = SetGroupExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMessageExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        msg_id: str = None,
        extensions: Dict[str, str] = None,
    ):
        # 会话ID
        self.app_cid = app_cid
        # 消息ID
        self.msg_id = msg_id
        # 需设置的K-V对
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class SetMessageExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SetMessageExtensionByKeysRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SetMessageExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetMessageExtensionByKeysShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SetMessageExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 错误码，成功时为0
        self.code = code
        # 错误信息，成功时为空
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetMessageExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetMessageExtensionByKeysResponseBody = None,
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
            temp_model = SetMessageExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSingleChatExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        app_cid: str = None,
        extensions: Dict[str, str] = None,
    ):
        # 用户id
        self.app_uid = app_uid
        # 会话id
        self.app_cid = app_cid
        # 拓展字段
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class SetSingleChatExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SetSingleChatExtensionByKeysRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        # 创建群聊请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SetSingleChatExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetSingleChatExtensionByKeysShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        # 创建群聊请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SetSingleChatExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetSingleChatExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetSingleChatExtensionByKeysResponseBody = None,
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
            temp_model = SetSingleChatExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserConversationExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        app_cid: str = None,
        extensions: Dict[str, str] = None,
    ):
        # 用户id
        self.app_uid = app_uid
        # 会话id
        self.app_cid = app_cid
        # 拓展字段
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class SetUserConversationExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SetUserConversationExtensionByKeysRequestRequestParams = None,
    ):
        self.app_id = app_id
        # 设置用户拓展字段请求实体
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SetUserConversationExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetUserConversationExtensionByKeysShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        # 设置用户拓展字段请求实体
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SetUserConversationExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SetUserConversationExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetUserConversationExtensionByKeysResponseBody = None,
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
            temp_model = SetUserConversationExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: Dict[str, Any] = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params = m.get('RequestParams')
        return self


class SetUserExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        message: str = None,
        request_id: str = None,
        code: str = None,
        success: bool = None,
    ):
        self.message = message
        self.request_id = request_id
        self.code = code
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class SetUserExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SetUserExtensionByKeysResponseBody = None,
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
            temp_model = SetUserExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SilenceAllGroupMembersRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        operator_app_uid: str = None,
    ):
        # 会话ID
        self.app_cid = app_cid
        # 操作者uid
        self.operator_app_uid = operator_app_uid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        return self


class SilenceAllGroupMembersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SilenceAllGroupMembersRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = SilenceAllGroupMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SilenceAllGroupMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class SilenceAllGroupMembersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class SilenceAllGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SilenceAllGroupMembersResponseBody = None,
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
            temp_model = SilenceAllGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupIconRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        operator_app_uid: str = None,
        icon_media_id: str = None,
    ):
        # 会话ID
        self.app_cid = app_cid
        # 操作者用户ID
        self.operator_app_uid = operator_app_uid
        # 群聊头像文件MediaID
        self.icon_media_id = icon_media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.icon_media_id is not None:
            result['IconMediaId'] = self.icon_media_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('IconMediaId') is not None:
            self.icon_media_id = m.get('IconMediaId')
        return self


class UpdateGroupIconRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: UpdateGroupIconRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = UpdateGroupIconRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateGroupIconShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class UpdateGroupIconResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateGroupIconResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupIconResponseBody = None,
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
            temp_model = UpdateGroupIconResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupMembersRoleRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        operator_app_uid: str = None,
        rrole: int = None,
        app_uids: List[str] = None,
    ):
        # 会话ID
        self.app_cid = app_cid
        # 操作者uid
        self.operator_app_uid = operator_app_uid
        # 角色
        self.rrole = rrole
        # 需要更改的uids
        self.app_uids = app_uids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.rrole is not None:
            result['Rrole'] = self.rrole
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('Rrole') is not None:
            self.rrole = m.get('Rrole')
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        return self


class UpdateGroupMembersRoleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: UpdateGroupMembersRoleRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = UpdateGroupMembersRoleRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateGroupMembersRoleShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class UpdateGroupMembersRoleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateGroupMembersRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupMembersRoleResponseBody = None,
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
            temp_model = UpdateGroupMembersRoleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupTitleRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        operator_app_uid: str = None,
        title: str = None,
    ):
        # 会话ID
        self.app_cid = app_cid
        # 操作者用户ID
        self.operator_app_uid = operator_app_uid
        # 群聊标题
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateGroupTitleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: UpdateGroupTitleRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            temp_model = UpdateGroupTitleRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateGroupTitleShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class UpdateGroupTitleResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        code: str = None,
        message: str = None,
    ):
        self.request_id = request_id
        self.code = code
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class UpdateGroupTitleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateGroupTitleResponseBody = None,
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
            temp_model = UpdateGroupTitleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateTenantStatusRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        status: int = None,
    ):
        self.domain = domain
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class UpdateTenantStatusRequest(TeaModel):
    def __init__(
        self,
        request: UpdateTenantStatusRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = UpdateTenantStatusRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class UpdateTenantStatusResponseBody(TeaModel):
    def __init__(
        self,
        success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: bool = None,
        request_id: str = None,
    ):
        # Id of the request
        self.success = success
        self.error_code = error_code
        self.error_msg = error_msg
        self.result = result
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        if self.success is not None:
            result['success'] = self.success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.result is not None:
            result['result'] = self.result
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('success') is not None:
            self.success = m.get('success')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('result') is not None:
            self.result = m.get('result')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateTenantStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateTenantStatusResponseBody = None,
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
            temp_model = UpdateTenantStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



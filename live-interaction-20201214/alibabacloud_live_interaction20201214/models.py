# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List, Any


class ResultUserMuteSettingsValue(TeaModel):
    def __init__(
        self,
        mute: bool = None,
        expire_time: int = None,
    ):
        self.mute = mute
        self.expire_time = expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mute is not None:
            result['Mute'] = self.mute
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        return self


class ResultImportMessageResultValue(TeaModel):
    def __init__(
        self,
        result: int = None,
        msg_id: str = None,
    ):
        self.result = result
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.top = top
        self.red_point = red_point
        self.mute = mute
        self.visible = visible
        self.create_time = create_time
        self.modify_time = modify_time
        self.user_extensions = user_extensions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class RequestParamsOptionsSingleChatCreateRequestUserConversationValue(TeaModel):
    def __init__(
        self,
        user_extensions: Dict[str, str] = None,
    ):
        self.user_extensions = user_extensions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_extensions is not None:
            result['UserExtensions'] = self.user_extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserExtensions') is not None:
            self.user_extensions = m.get('UserExtensions')
        return self


class AddGroupMembersRequestRequestParamsInitMembers(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        extensions: Dict[str, str] = None,
        join_time: int = None,
        nick: str = None,
        role: int = None,
    ):
        self.app_uid = app_uid
        self.extensions = extensions
        self.join_time = join_time
        self.nick = nick
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class AddGroupMembersRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        init_members: List[AddGroupMembersRequestRequestParamsInitMembers] = None,
        operator_app_uid: str = None,
    ):
        self.app_cid = app_cid
        self.init_members = init_members
        self.operator_app_uid = operator_app_uid

    def validate(self):
        if self.init_members:
            for k in self.init_members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        result['InitMembers'] = []
        if self.init_members is not None:
            for k in self.init_members:
                result['InitMembers'].append(k.to_map() if k else None)
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        self.init_members = []
        if m.get('InitMembers') is not None:
            for k in m.get('InitMembers'):
                temp_model = AddGroupMembersRequestRequestParamsInitMembers()
                self.init_members.append(temp_model.from_map(k))
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        return self


class AddGroupMembersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: AddGroupMembersRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddGroupMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AddGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGroupSilenceBlacklistRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        members: List[str] = None,
        operator_app_uid: str = None,
        silence_duration: int = None,
    ):
        self.app_cid = app_cid
        self.members = members
        self.operator_app_uid = operator_app_uid
        self.silence_duration = silence_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.silence_duration is not None:
            result['SilenceDuration'] = self.silence_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('SilenceDuration') is not None:
            self.silence_duration = m.get('SilenceDuration')
        return self


class AddGroupSilenceBlacklistRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: AddGroupSilenceBlacklistRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddGroupSilenceBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddGroupSilenceBlacklistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AddGroupSilenceBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddGroupSilenceWhitelistRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        members: List[str] = None,
        operator_app_uid: str = None,
    ):
        self.app_cid = app_cid
        self.members = members
        self.operator_app_uid = operator_app_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        return self


class AddGroupSilenceWhitelistRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: AddGroupSilenceWhitelistRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddGroupSilenceWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddGroupSilenceWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = AddGroupSilenceWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindInterconnectionCidRequestRequestParams(TeaModel):
    def __init__(
        self,
        aim_app_cid: str = None,
        ding_talk_cid: str = None,
    ):
        self.aim_app_cid = aim_app_cid
        self.ding_talk_cid = ding_talk_cid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aim_app_cid is not None:
            result['AimAppCid'] = self.aim_app_cid
        if self.ding_talk_cid is not None:
            result['DingTalkCid'] = self.ding_talk_cid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AimAppCid') is not None:
            self.aim_app_cid = m.get('AimAppCid')
        if m.get('DingTalkCid') is not None:
            self.ding_talk_cid = m.get('DingTalkCid')
        return self


class BindInterconnectionCidRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: BindInterconnectionCidRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = BindInterconnectionCidRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class BindInterconnectionCidShrinkRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class BindInterconnectionCidResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindInterconnectionCidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindInterconnectionCidResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = BindInterconnectionCidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class BindInterconnectionUidRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        ding_talk_uid: str = None,
    ):
        self.app_uid = app_uid
        self.ding_talk_uid = ding_talk_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.ding_talk_uid is not None:
            result['DingTalkUid'] = self.ding_talk_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('DingTalkUid') is not None:
            self.ding_talk_uid = m.get('DingTalkUid')
        return self


class BindInterconnectionUidRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: BindInterconnectionUidRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = BindInterconnectionUidRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class BindInterconnectionUidShrinkRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class BindInterconnectionUidResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class BindInterconnectionUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BindInterconnectionUidResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = BindInterconnectionUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelSilenceAllGroupMembersRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        operator_app_uid: str = None,
    ):
        self.app_cid = app_cid
        self.operator_app_uid = operator_app_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelSilenceAllGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CancelSilenceAllGroupMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CancelSilenceAllGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequestRequestParamsInitMembers(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        extensions: Dict[str, str] = None,
        join_time: int = None,
        nick: str = None,
        role: int = None,
    ):
        self.app_uid = app_uid
        self.extensions = extensions
        self.join_time = join_time
        self.nick = nick
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class CreateGroupRequestRequestParams(TeaModel):
    def __init__(
        self,
        creator_app_uid: str = None,
        entrance_id: str = None,
        extensions: Dict[str, str] = None,
        icon_media_id: str = None,
        init_members: List[CreateGroupRequestRequestParamsInitMembers] = None,
        title: str = None,
        uuid: str = None,
    ):
        self.creator_app_uid = creator_app_uid
        self.entrance_id = entrance_id
        self.extensions = extensions
        self.icon_media_id = icon_media_id
        self.init_members = init_members
        self.title = title
        self.uuid = uuid

    def validate(self):
        if self.init_members:
            for k in self.init_members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_app_uid is not None:
            result['CreatorAppUid'] = self.creator_app_uid
        if self.entrance_id is not None:
            result['EntranceId'] = self.entrance_id
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.icon_media_id is not None:
            result['IconMediaId'] = self.icon_media_id
        result['InitMembers'] = []
        if self.init_members is not None:
            for k in self.init_members:
                result['InitMembers'].append(k.to_map() if k else None)
        if self.title is not None:
            result['Title'] = self.title
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatorAppUid') is not None:
            self.creator_app_uid = m.get('CreatorAppUid')
        if m.get('EntranceId') is not None:
            self.entrance_id = m.get('EntranceId')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('IconMediaId') is not None:
            self.icon_media_id = m.get('IconMediaId')
        self.init_members = []
        if m.get('InitMembers') is not None:
            for k in m.get('InitMembers'):
                temp_model = CreateGroupRequestRequestParamsInitMembers()
                self.init_members.append(temp_model.from_map(k))
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: CreateGroupRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: CreateGroupResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateGroupResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        request_id: str = None,
        response_success: bool = None,
        result: CreateRoomResponseBodyResult = None,
        error_code: str = None,
        error_msg: str = None,
    ):
        self.request_id = request_id
        self.response_success = response_success
        self.result = result
        self.error_code = error_code
        self.error_msg = error_msg

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('Result') is not None:
            temp_model = CreateRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        return self


class CreateRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = CreateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class DeleteAppResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
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


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAppResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DestroyRoomRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        open_id: str = None,
        room_id: str = None,
    ):
        self.domain = domain
        self.open_id = open_id
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['domain'] = self.domain
        if self.open_id is not None:
            result['openId'] = self.open_id
        if self.room_id is not None:
            result['roomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain') is not None:
            self.domain = m.get('domain')
        if m.get('openId') is not None:
            self.open_id = m.get('openId')
        if m.get('roomId') is not None:
            self.room_id = m.get('roomId')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.response_success = response_success
        self.error_code = error_code
        self.error_msg = error_msg
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class DestroyRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DestroyRoomResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DestroyRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DismissGroupRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        operator_app_uid: str = None,
    ):
        self.app_cid = app_cid
        self.operator_app_uid = operator_app_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class DismissGroupRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: DismissGroupRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DismissGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DismissGroupResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = DismissGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCommonConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetCommonConfigResponseBodyResultCommonConfigAppConfigs(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        platform: str = None,
    ):
        # appKey
        self.app_key = app_key
        self.platform = platform

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.platform is not None:
            result['Platform'] = self.platform
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('Platform') is not None:
            self.platform = m.get('Platform')
        return self


class GetCommonConfigResponseBodyResultCommonConfigLoginConfig(TeaModel):
    def __init__(
        self,
        login_type: int = None,
    ):
        self.login_type = login_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_type is not None:
            result['LoginType'] = self.login_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginType') is not None:
            self.login_type = m.get('LoginType')
        return self


class GetCommonConfigResponseBodyResultCommonConfig(TeaModel):
    def __init__(
        self,
        app_configs: List[GetCommonConfigResponseBodyResultCommonConfigAppConfigs] = None,
        login_config: GetCommonConfigResponseBodyResultCommonConfigLoginConfig = None,
    ):
        self.app_configs = app_configs
        self.login_config = login_config

    def validate(self):
        if self.app_configs:
            for k in self.app_configs:
                if k:
                    k.validate()
        if self.login_config:
            self.login_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppConfigs'] = []
        if self.app_configs is not None:
            for k in self.app_configs:
                result['AppConfigs'].append(k.to_map() if k else None)
        if self.login_config is not None:
            result['LoginConfig'] = self.login_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_configs = []
        if m.get('AppConfigs') is not None:
            for k in m.get('AppConfigs'):
                temp_model = GetCommonConfigResponseBodyResultCommonConfigAppConfigs()
                self.app_configs.append(temp_model.from_map(k))
        if m.get('LoginConfig') is not None:
            temp_model = GetCommonConfigResponseBodyResultCommonConfigLoginConfig()
            self.login_config = temp_model.from_map(m['LoginConfig'])
        return self


class GetCommonConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        common_config: GetCommonConfigResponseBodyResultCommonConfig = None,
    ):
        self.common_config = common_config

    def validate(self):
        if self.common_config:
            self.common_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_config is not None:
            result['CommonConfig'] = self.common_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommonConfig') is not None:
            temp_model = GetCommonConfigResponseBodyResultCommonConfig()
            self.common_config = temp_model.from_map(m['CommonConfig'])
        return self


class GetCommonConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: GetCommonConfigResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
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
        if m.get('Result') is not None:
            temp_model = GetCommonConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCommonConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCommonConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetCommonConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupByIdRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
    ):
        self.app_cid = app_cid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class GetGroupByIdRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: GetGroupByIdRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetGroupByIdRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetGroupByIdShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetGroupByIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        ceate_time: int = None,
        extensions: Dict[str, str] = None,
        icon_media_id: str = None,
        member_count: int = None,
        member_limit: int = None,
        owner_app_uid: str = None,
        title: str = None,
    ):
        self.app_cid = app_cid
        self.ceate_time = ceate_time
        self.extensions = extensions
        self.icon_media_id = icon_media_id
        self.member_count = member_count
        self.member_limit = member_limit
        self.owner_app_uid = owner_app_uid
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.ceate_time is not None:
            result['CeateTime'] = self.ceate_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.icon_media_id is not None:
            result['IconMediaId'] = self.icon_media_id
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.member_limit is not None:
            result['MemberLimit'] = self.member_limit
        if self.owner_app_uid is not None:
            result['OwnerAppUid'] = self.owner_app_uid
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('CeateTime') is not None:
            self.ceate_time = m.get('CeateTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('IconMediaId') is not None:
            self.icon_media_id = m.get('IconMediaId')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('MemberLimit') is not None:
            self.member_limit = m.get('MemberLimit')
        if m.get('OwnerAppUid') is not None:
            self.owner_app_uid = m.get('OwnerAppUid')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetGroupByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: GetGroupByIdResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetGroupByIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetGroupByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGroupByIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetGroupByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupMemberByIdsRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uids: List[str] = None,
    ):
        self.app_cid = app_cid
        self.app_uids = app_uids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        extensions: Dict[str, str] = None,
        join_time: int = None,
        nick: str = None,
        role: int = None,
    ):
        self.app_uid = app_uid
        self.extensions = extensions
        self.join_time = join_time
        self.nick = nick
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class GetGroupMemberByIdsResponseBodyResult(TeaModel):
    def __init__(
        self,
        members: List[GetGroupMemberByIdsResponseBodyResultMembers] = None,
    ):
        self.members = members

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: GetGroupMemberByIdsResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetGroupMemberByIdsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetGroupMemberByIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetGroupMemberByIdsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetGroupMemberByIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIMConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        self.app_id = app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        return self


class GetIMConfigResponseBodyResultImConfigCallbackConfig(TeaModel):
    def __init__(
        self,
        apis: Dict[str, bool] = None,
        callback_url: str = None,
        events: Dict[str, bool] = None,
        signature_key: str = None,
        signature_value: str = None,
        spis: Dict[str, bool] = None,
    ):
        self.apis = apis
        self.callback_url = callback_url
        self.events = events
        self.signature_key = signature_key
        self.signature_value = signature_value
        self.spis = spis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apis is not None:
            result['Apis'] = self.apis
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.events is not None:
            result['Events'] = self.events
        if self.signature_key is not None:
            result['SignatureKey'] = self.signature_key
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        if self.spis is not None:
            result['Spis'] = self.spis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apis') is not None:
            self.apis = m.get('Apis')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('SignatureKey') is not None:
            self.signature_key = m.get('SignatureKey')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        if m.get('Spis') is not None:
            self.spis = m.get('Spis')
        return self


class GetIMConfigResponseBodyResultImConfigMsgConfig(TeaModel):
    def __init__(
        self,
        client_msg_recall_time_interval_minute: int = None,
    ):
        self.client_msg_recall_time_interval_minute = client_msg_recall_time_interval_minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_msg_recall_time_interval_minute is not None:
            result['ClientMsgRecallTimeIntervalMinute'] = self.client_msg_recall_time_interval_minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientMsgRecallTimeIntervalMinute') is not None:
            self.client_msg_recall_time_interval_minute = m.get('ClientMsgRecallTimeIntervalMinute')
        return self


class GetIMConfigResponseBodyResultImConfig(TeaModel):
    def __init__(
        self,
        callback_config: GetIMConfigResponseBodyResultImConfigCallbackConfig = None,
        msg_config: GetIMConfigResponseBodyResultImConfigMsgConfig = None,
    ):
        self.callback_config = callback_config
        self.msg_config = msg_config

    def validate(self):
        if self.callback_config:
            self.callback_config.validate()
        if self.msg_config:
            self.msg_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_config is not None:
            result['CallbackConfig'] = self.callback_config.to_map()
        if self.msg_config is not None:
            result['MsgConfig'] = self.msg_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackConfig') is not None:
            temp_model = GetIMConfigResponseBodyResultImConfigCallbackConfig()
            self.callback_config = temp_model.from_map(m['CallbackConfig'])
        if m.get('MsgConfig') is not None:
            temp_model = GetIMConfigResponseBodyResultImConfigMsgConfig()
            self.msg_config = temp_model.from_map(m['MsgConfig'])
        return self


class GetIMConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        im_config: GetIMConfigResponseBodyResultImConfig = None,
    ):
        self.im_config = im_config

    def validate(self):
        if self.im_config:
            self.im_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.im_config is not None:
            result['ImConfig'] = self.im_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImConfig') is not None:
            temp_model = GetIMConfigResponseBodyResultImConfig()
            self.im_config = temp_model.from_map(m['ImConfig'])
        return self


class GetIMConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        messaage: str = None,
        request_id: str = None,
        result: GetIMConfigResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.messaage = messaage
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.messaage is not None:
            result['Messaage'] = self.messaage
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Messaage') is not None:
            self.messaage = m.get('Messaage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetIMConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetIMConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetIMConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetIMConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLoginTokenRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_key: str = None,
        app_uid: str = None,
        device_id: str = None,
    ):
        self.app_key = app_key
        self.app_uid = app_uid
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class GetLoginTokenRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: GetLoginTokenRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        access_token_expired_time: int = None,
        refresh_token: str = None,
    ):
        self.access_token = access_token
        self.access_token_expired_time = access_token_expired_time
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.access_token_expired_time is not None:
            result['AccessTokenExpiredTime'] = self.access_token_expired_time
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('AccessTokenExpiredTime') is not None:
            self.access_token_expired_time = m.get('AccessTokenExpiredTime')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class GetLoginTokenResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: GetLoginTokenResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetLoginTokenResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLoginTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLoginTokenResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetLoginTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaUploadUrlRequestRequestParams(TeaModel):
    def __init__(
        self,
        mime_type: str = None,
    ):
        self.mime_type = mime_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.mime_type is not None:
            result['MimeType'] = self.mime_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MimeType') is not None:
            self.mime_type = m.get('MimeType')
        return self


class GetMediaUploadUrlRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: GetMediaUploadUrlRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        media_id: str = None,
        upload_url: str = None,
    ):
        self.media_id = media_id
        self.upload_url = upload_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.media_id is not None:
            result['MediaId'] = self.media_id
        if self.upload_url is not None:
            result['UploadUrl'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')
        if m.get('UploadUrl') is not None:
            self.upload_url = m.get('UploadUrl')
        return self


class GetMediaUploadUrlResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: GetMediaUploadUrlResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetMediaUploadUrlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMediaUploadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMediaUploadUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetMediaUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMediaUrlRequestRequestParams(TeaModel):
    def __init__(
        self,
        media_id: str = None,
        url_expire_time: int = None,
    ):
        self.media_id = media_id
        self.url_expire_time = url_expire_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: GetMediaUrlResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetMediaUrlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMediaUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMediaUrlResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetMediaUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetMessageByIdRequestRequestParams(TeaModel):
    def __init__(
        self,
        msg_id: str = None,
    ):
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        app_cid: str = None,
        content: str = None,
        content_type: int = None,
        conversation_type: int = None,
        create_time: int = None,
        extensions: Dict[str, str] = None,
        msg_id: str = None,
        sender_id: str = None,
    ):
        self.app_cid = app_cid
        self.content = content
        self.content_type = content_type
        self.conversation_type = conversation_type
        self.create_time = create_time
        self.extensions = extensions
        self.msg_id = msg_id
        self.sender_id = sender_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.conversation_type is not None:
            result['ConversationType'] = self.conversation_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ConversationType') is not None:
            self.conversation_type = m.get('ConversationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        return self


class GetMessageByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: GetMessageByIdResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetMessageByIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetMessageByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetMessageByIdResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetMessageByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoomStatisticsRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        room_id: str = None,
    ):
        self.domain = domain
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class GetRoomStatisticsRequest(TeaModel):
    def __init__(
        self,
        request: GetRoomStatisticsRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = GetRoomStatisticsRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class GetRoomStatisticsResponseBodyResult(TeaModel):
    def __init__(
        self,
        online_count: int = None,
        pv: int = None,
        uv: int = None,
    ):
        self.online_count = online_count
        self.pv = pv
        self.uv = uv

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        if self.pv is not None:
            result['PV'] = self.pv
        if self.uv is not None:
            result['UV'] = self.uv
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        if m.get('PV') is not None:
            self.pv = m.get('PV')
        if m.get('UV') is not None:
            self.uv = m.get('UV')
        return self


class GetRoomStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        response_success: bool = None,
        result: GetRoomStatisticsResponseBodyResult = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.response_success = response_success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('Result') is not None:
            temp_model = GetRoomStatisticsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRoomStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetRoomStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetRoomStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserMuteSettingRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uids: List[str] = None,
    ):
        self.app_uids = app_uids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        return self


class GetUserMuteSettingRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: GetUserMuteSettingRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = GetUserMuteSettingRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class GetUserMuteSettingShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetUserMuteSettingResponseBodyResult(TeaModel):
    def __init__(
        self,
        user_mute_settings: Dict[str, ResultUserMuteSettingsValue] = None,
    ):
        self.user_mute_settings = user_mute_settings

    def validate(self):
        if self.user_mute_settings:
            for v in self.user_mute_settings.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserMuteSettings'] = {}
        if self.user_mute_settings is not None:
            for k, v in self.user_mute_settings.items():
                result['UserMuteSettings'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_mute_settings = {}
        if m.get('UserMuteSettings') is not None:
            for k, v in m.get('UserMuteSettings').items():
                temp_model = ResultUserMuteSettingsValue()
                self.user_mute_settings[k] = temp_model.from_map(v)
        return self


class GetUserMuteSettingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: GetUserMuteSettingResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetUserMuteSettingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetUserMuteSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserMuteSettingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = GetUserMuteSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportGroupChatConversationRequestRequestParams(TeaModel):
    def __init__(
        self,
        create_time: int = None,
        extensions: Dict[str, str] = None,
        icon_media_id: str = None,
        member_limit: int = None,
        owner_app_uid: str = None,
        silence_all: bool = None,
        title: str = None,
        uuid: str = None,
    ):
        self.create_time = create_time
        self.extensions = extensions
        self.icon_media_id = icon_media_id
        self.member_limit = member_limit
        self.owner_app_uid = owner_app_uid
        self.silence_all = silence_all
        self.title = title
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.icon_media_id is not None:
            result['IconMediaId'] = self.icon_media_id
        if self.member_limit is not None:
            result['MemberLimit'] = self.member_limit
        if self.owner_app_uid is not None:
            result['OwnerAppUid'] = self.owner_app_uid
        if self.silence_all is not None:
            result['SilenceAll'] = self.silence_all
        if self.title is not None:
            result['Title'] = self.title
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('IconMediaId') is not None:
            self.icon_media_id = m.get('IconMediaId')
        if m.get('MemberLimit') is not None:
            self.member_limit = m.get('MemberLimit')
        if m.get('OwnerAppUid') is not None:
            self.owner_app_uid = m.get('OwnerAppUid')
        if m.get('SilenceAll') is not None:
            self.silence_all = m.get('SilenceAll')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class ImportGroupChatConversationRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: ImportGroupChatConversationRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_cid = app_cid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ImportGroupChatConversationResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ImportGroupChatConversationResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ImportGroupChatConversationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportGroupChatConversationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ImportGroupChatConversationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportGroupChatMemberRequestRequestParamsGroupChatMembers(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        extensions: Dict[str, str] = None,
        join_time: int = None,
        modify_time: int = None,
        mute: bool = None,
        nick: str = None,
        red_point: int = None,
        role: int = None,
        top: bool = None,
        visible: bool = None,
    ):
        self.app_uid = app_uid
        self.extensions = extensions
        self.join_time = join_time
        self.modify_time = modify_time
        self.mute = mute
        self.nick = nick
        self.red_point = red_point
        self.role = role
        self.top = top
        self.visible = visible

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time
        if self.mute is not None:
            result['Mute'] = self.mute
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.red_point is not None:
            result['RedPoint'] = self.red_point
        if self.role is not None:
            result['Role'] = self.role
        if self.top is not None:
            result['Top'] = self.top
        if self.visible is not None:
            result['Visible'] = self.visible
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('RedPoint') is not None:
            self.red_point = m.get('RedPoint')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Visible') is not None:
            self.visible = m.get('Visible')
        return self


class ImportGroupChatMemberRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        group_chat_members: List[ImportGroupChatMemberRequestRequestParamsGroupChatMembers] = None,
    ):
        self.app_cid = app_cid
        self.group_chat_members = group_chat_members

    def validate(self):
        if self.group_chat_members:
            for k in self.group_chat_members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportGroupChatMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportGroupChatMemberResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ImportGroupChatMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportMessageRequestRequestParamsMessages(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        content: str = None,
        content_type: int = None,
        conversation_type: int = None,
        create_time: int = None,
        extensions: Dict[str, str] = None,
        receiver_ids: List[str] = None,
        sender_id: str = None,
        uuid: str = None,
    ):
        self.app_cid = app_cid
        self.content = content
        self.content_type = content_type
        self.conversation_type = conversation_type
        self.create_time = create_time
        self.extensions = extensions
        self.receiver_ids = receiver_ids
        self.sender_id = sender_id
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.conversation_type is not None:
            result['ConversationType'] = self.conversation_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.receiver_ids is not None:
            result['ReceiverIds'] = self.receiver_ids
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ConversationType') is not None:
            self.conversation_type = m.get('ConversationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('ReceiverIds') is not None:
            self.receiver_ids = m.get('ReceiverIds')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ImportMessageResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ImportMessageResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ImportMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ImportMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ImportSingleConversationRequestRequestParamsConversation(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uids: List[str] = None,
        create_time: int = None,
        extensions: Dict[str, str] = None,
    ):
        self.app_cid = app_cid
        self.app_uids = app_uids
        self.create_time = create_time
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class ImportSingleConversationRequestRequestParams(TeaModel):
    def __init__(
        self,
        conversation: ImportSingleConversationRequestRequestParamsConversation = None,
        user_conversations: Dict[str, RequestParamsUserConversationsValue] = None,
    ):
        self.conversation = conversation
        self.user_conversations = user_conversations

    def validate(self):
        if self.conversation:
            self.conversation.validate()
        if self.user_conversations:
            for v in self.user_conversations.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ImportSingleConversationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ImportSingleConversationResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.response_success = response_success
        self.error_code = error_code
        self.error_msg = error_msg
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class InitTenantResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InitTenantResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = InitTenantResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class KickOffRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_keys: List[str] = None,
        app_uid: str = None,
        information: str = None,
    ):
        self.app_keys = app_keys
        self.app_uid = app_uid
        self.information = information

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_keys is not None:
            result['AppKeys'] = self.app_keys
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.information is not None:
            result['Information'] = self.information
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppKeys') is not None:
            self.app_keys = m.get('AppKeys')
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Information') is not None:
            self.information = m.get('Information')
        return self


class KickOffRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: KickOffRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class KickOffResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: KickOffResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = KickOffResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppInfosRequestRequestParams(TeaModel):
    def __init__(
        self,
        keyword: str = None,
        page_number: int = None,
        page_size: int = None,
        type: str = None,
    ):
        self.keyword = keyword
        self.page_number = page_number
        self.page_size = page_size
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keyword is not None:
            result['Keyword'] = self.keyword
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Keyword') is not None:
            self.keyword = m.get('Keyword')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListAppInfosRequest(TeaModel):
    def __init__(
        self,
        request_params: ListAppInfosRequestRequestParams = None,
    ):
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_params is not None:
            result['RequestParams'] = self.request_params.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestParams') is not None:
            temp_model = ListAppInfosRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ListAppInfosShrinkRequest(TeaModel):
    def __init__(
        self,
        request_params_shrink: str = None,
    ):
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_params_shrink is not None:
            result['RequestParams'] = self.request_params_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestParams') is not None:
            self.request_params_shrink = m.get('RequestParams')
        return self


class ListAppInfosResponseBodyResultAppInfos(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_status: int = None,
        create_time: str = None,
        instance_id: str = None,
        prod_version: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_status = app_status
        self.create_time = create_time
        self.instance_id = instance_id
        self.prod_version = prod_version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.prod_version is not None:
            result['ProdVersion'] = self.prod_version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('ProdVersion') is not None:
            self.prod_version = m.get('ProdVersion')
        return self


class ListAppInfosResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_infos: List[ListAppInfosResponseBodyResultAppInfos] = None,
        total_count: int = None,
    ):
        self.app_infos = app_infos
        self.total_count = total_count

    def validate(self):
        if self.app_infos:
            for k in self.app_infos:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AppInfos'] = []
        if self.app_infos is not None:
            for k in self.app_infos:
                result['AppInfos'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.app_infos = []
        if m.get('AppInfos') is not None:
            for k in m.get('AppInfos'):
                temp_model = ListAppInfosResponseBodyResultAppInfos()
                self.app_infos.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAppInfosResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListAppInfosResponseBodyResult = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # httpStatusCode
        self.http_status_code = http_status_code
        # desc
        self.message = message
        # requestId
        self.request_id = request_id
        # result
        self.result = result
        # success
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListAppInfosResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListAppInfosResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAppInfosResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListAppInfosResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCallbackApiIdsResponseBodyResult(TeaModel):
    def __init__(
        self,
        events: Dict[str, bool] = None,
        spis: Dict[str, bool] = None,
    ):
        self.events = events
        self.spis = spis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.events is not None:
            result['Events'] = self.events
        if self.spis is not None:
            result['Spis'] = self.spis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('Spis') is not None:
            self.spis = m.get('Spis')
        return self


class ListCallbackApiIdsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListCallbackApiIdsResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListCallbackApiIdsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListCallbackApiIdsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCallbackApiIdsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListCallbackApiIdsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDetailReportStatisticsRequestRequestParams(TeaModel):
    def __init__(
        self,
        end_time: str = None,
        report_statistics_type: str = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.report_statistics_type = report_statistics_type
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.report_statistics_type is not None:
            result['ReportStatisticsType'] = self.report_statistics_type
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('ReportStatisticsType') is not None:
            self.report_statistics_type = m.get('ReportStatisticsType')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        return self


class ListDetailReportStatisticsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: ListDetailReportStatisticsRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListDetailReportStatisticsRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ListDetailReportStatisticsShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListDetailReportStatisticsResponseBodyResult(TeaModel):
    def __init__(
        self,
        data: List[Dict[str, Any]] = None,
    ):
        self.data = data

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data is not None:
            result['Data'] = self.data
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            self.data = m.get('Data')
        return self


class ListDetailReportStatisticsResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListDetailReportStatisticsResponseBodyResult = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # httpStatusCode
        self.http_status_code = http_status_code
        # desc
        self.message = message
        # requestId
        self.request_id = request_id
        # result
        self.result = result
        # success
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListDetailReportStatisticsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ListDetailReportStatisticsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDetailReportStatisticsResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListDetailReportStatisticsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupAllMembersRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
    ):
        self.app_cid = app_cid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        return self


class ListGroupAllMembersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: ListGroupAllMembersRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = ListGroupAllMembersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class ListGroupAllMembersShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListGroupAllMembersResponseBodyResultMembers(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        extensions: Dict[str, str] = None,
        join_time: int = None,
        nick: str = None,
        role: int = None,
    ):
        self.app_uid = app_uid
        self.extensions = extensions
        self.join_time = join_time
        self.nick = nick
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.join_time is not None:
            result['JoinTime'] = self.join_time
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('JoinTime') is not None:
            self.join_time = m.get('JoinTime')
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class ListGroupAllMembersResponseBodyResult(TeaModel):
    def __init__(
        self,
        members: List[ListGroupAllMembersResponseBodyResultMembers] = None,
    ):
        self.members = members

    def validate(self):
        if self.members:
            for k in self.members:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
                temp_model = ListGroupAllMembersResponseBodyResultMembers()
                self.members.append(temp_model.from_map(k))
        return self


class ListGroupAllMembersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ListGroupAllMembersResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListGroupAllMembersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListGroupAllMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupAllMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListGroupAllMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupSilenceMembersRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        operator_app_uid: str = None,
    ):
        self.app_cid = app_cid
        self.operator_app_uid = operator_app_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListGroupSilenceMembersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: ListGroupSilenceMembersRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        blacklist: Dict[str, int] = None,
        whitelist: List[str] = None,
    ):
        self.app_cid = app_cid
        self.blacklist = blacklist
        self.whitelist = whitelist

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.blacklist is not None:
            result['Blacklist'] = self.blacklist
        if self.whitelist is not None:
            result['Whitelist'] = self.whitelist
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Blacklist') is not None:
            self.blacklist = m.get('Blacklist')
        if m.get('Whitelist') is not None:
            self.whitelist = m.get('Whitelist')
        return self


class ListGroupSilenceMembersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: ListGroupSilenceMembersResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListGroupSilenceMembersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListGroupSilenceMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupSilenceMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListGroupSilenceMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoomMessagesRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        page_number: int = None,
        page_size: int = None,
        room_id: str = None,
        sub_type: int = None,
    ):
        self.domain = domain
        self.page_number = page_number
        self.page_size = page_size
        self.room_id = room_id
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class ListRoomMessagesRequest(TeaModel):
    def __init__(
        self,
        request: ListRoomMessagesRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = ListRoomMessagesRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class ListRoomMessagesResponseBodyResultRoomMessageList(TeaModel):
    def __init__(
        self,
        body: str = None,
        message_id: str = None,
        room_id: str = None,
        send_time_millis: int = None,
        sender_id: str = None,
        sub_type: int = None,
    ):
        self.body = body
        self.message_id = message_id
        self.room_id = room_id
        self.send_time_millis = send_time_millis
        self.sender_id = sender_id
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.send_time_millis is not None:
            result['SendTimeMillis'] = self.send_time_millis
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SendTimeMillis') is not None:
            self.send_time_millis = m.get('SendTimeMillis')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class ListRoomMessagesResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        room_message_list: List[ListRoomMessagesResponseBodyResultRoomMessageList] = None,
        total_count: int = None,
    ):
        self.has_more = has_more
        self.room_message_list = room_message_list
        self.total_count = total_count

    def validate(self):
        if self.room_message_list:
            for k in self.room_message_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['RoomMessageList'] = []
        if self.room_message_list is not None:
            for k in self.room_message_list:
                result['RoomMessageList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.room_message_list = []
        if m.get('RoomMessageList') is not None:
            for k in m.get('RoomMessageList'):
                temp_model = ListRoomMessagesResponseBodyResultRoomMessageList()
                self.room_message_list.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRoomMessagesResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        response_success: bool = None,
        result: ListRoomMessagesResponseBodyResult = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.response_success = response_success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('Result') is not None:
            temp_model = ListRoomMessagesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRoomMessagesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRoomMessagesResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRoomMessagesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoomUsersRequestRequest(TeaModel):
    def __init__(
        self,
        domain: str = None,
        page_number: int = None,
        page_size: int = None,
        room_id: str = None,
    ):
        self.domain = domain
        self.page_number = page_number
        self.page_size = page_size
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class ListRoomUsersRequest(TeaModel):
    def __init__(
        self,
        request: ListRoomUsersRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = ListRoomUsersRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class ListRoomUsersResponseBodyResultRoomUserVOList(TeaModel):
    def __init__(
        self,
        nick: str = None,
        room_id: str = None,
        user_id: str = None,
    ):
        self.nick = nick
        self.room_id = room_id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.nick is not None:
            result['Nick'] = self.nick
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Nick') is not None:
            self.nick = m.get('Nick')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListRoomUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        room_user_volist: List[ListRoomUsersResponseBodyResultRoomUserVOList] = None,
        total_count: int = None,
    ):
        self.has_more = has_more
        self.room_user_volist = room_user_volist
        self.total_count = total_count

    def validate(self):
        if self.room_user_volist:
            for k in self.room_user_volist:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['RoomUserVOList'] = []
        if self.room_user_volist is not None:
            for k in self.room_user_volist:
                result['RoomUserVOList'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.room_user_volist = []
        if m.get('RoomUserVOList') is not None:
            for k in m.get('RoomUserVOList'):
                temp_model = ListRoomUsersResponseBodyResultRoomUserVOList()
                self.room_user_volist.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListRoomUsersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        response_success: bool = None,
        result: ListRoomUsersResponseBodyResult = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.response_success = response_success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('Result') is not None:
            temp_model = ListRoomUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRoomUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRoomUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = ListRoomUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MuteUsersRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uids: List[str] = None,
        mute: bool = None,
        mute_duration: int = None,
    ):
        self.app_uids = app_uids
        self.mute = mute
        self.mute_duration = mute_duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        if self.mute is not None:
            result['Mute'] = self.mute
        if self.mute_duration is not None:
            result['MuteDuration'] = self.mute_duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        if m.get('Mute') is not None:
            self.mute = m.get('Mute')
        if m.get('MuteDuration') is not None:
            self.mute_duration = m.get('MuteDuration')
        return self


class MuteUsersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: MuteUsersRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = MuteUsersRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class MuteUsersShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class MuteUsersResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class MuteUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MuteUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = MuteUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryInterconnectionCidMappingRequestRequestParams(TeaModel):
    def __init__(
        self,
        src_cid: str = None,
        type: int = None,
    ):
        self.src_cid = src_cid
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.src_cid is not None:
            result['SrcCid'] = self.src_cid
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SrcCid') is not None:
            self.src_cid = m.get('SrcCid')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class QueryInterconnectionCidMappingRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: QueryInterconnectionCidMappingRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = QueryInterconnectionCidMappingRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class QueryInterconnectionCidMappingShrinkRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class QueryInterconnectionCidMappingResponseBodyResult(TeaModel):
    def __init__(
        self,
        dst_cid: str = None,
    ):
        self.dst_cid = dst_cid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.dst_cid is not None:
            result['DstCid'] = self.dst_cid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DstCid') is not None:
            self.dst_cid = m.get('DstCid')
        return self


class QueryInterconnectionCidMappingResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: QueryInterconnectionCidMappingResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = QueryInterconnectionCidMappingResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class QueryInterconnectionCidMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryInterconnectionCidMappingResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = QueryInterconnectionCidMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RecallMessageRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uid: str = None,
        extensions: Dict[str, str] = None,
        msg_id: str = None,
        operator_type: int = None,
        type: int = None,
    ):
        self.app_cid = app_cid
        self.app_uid = app_uid
        self.extensions = extensions
        self.msg_id = msg_id
        self.operator_type = operator_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class RecallMessageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RecallMessageRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RecallMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RecallMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RecallMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        keys: List[str] = None,
    ):
        self.app_cid = app_cid
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveGroupExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveGroupExtensionByKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemoveGroupExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupMemberExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uid: str = None,
        keys: List[str] = None,
    ):
        self.app_cid = app_cid
        self.app_uid = app_uid
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class RemoveGroupMemberExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveGroupMemberExtensionByKeysRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = RemoveGroupMemberExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class RemoveGroupMemberExtensionByKeysShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class RemoveGroupMemberExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveGroupMemberExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveGroupMemberExtensionByKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemoveGroupMemberExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupMembersRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uids_removed: List[str] = None,
        operator_app_uid: str = None,
    ):
        self.app_cid = app_cid
        self.app_uids_removed = app_uids_removed
        self.operator_app_uid = operator_app_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uids_removed is not None:
            result['AppUidsRemoved'] = self.app_uids_removed
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUidsRemoved') is not None:
            self.app_uids_removed = m.get('AppUidsRemoved')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        return self


class RemoveGroupMembersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveGroupMembersRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveGroupMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemoveGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupSilenceBlacklistRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        members: List[str] = None,
        operator_app_uid: str = None,
    ):
        self.app_cid = app_cid
        self.members = members
        self.operator_app_uid = operator_app_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        return self


class RemoveGroupSilenceBlacklistRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveGroupSilenceBlacklistRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveGroupSilenceBlacklistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveGroupSilenceBlacklistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemoveGroupSilenceBlacklistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveGroupSilenceWhitelistRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        members: List[str] = None,
        operator_app_uid: str = None,
    ):
        self.app_cid = app_cid
        self.members = members
        self.operator_app_uid = operator_app_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.members is not None:
            result['Members'] = self.members
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Members') is not None:
            self.members = m.get('Members')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        return self


class RemoveGroupSilenceWhitelistRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveGroupSilenceWhitelistRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveGroupSilenceWhitelistResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveGroupSilenceWhitelistResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemoveGroupSilenceWhitelistResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveMessageExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        keys: List[str] = None,
        msg_id: str = None,
    ):
        self.app_cid = app_cid
        self.keys = keys
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.keys is not None:
            result['Keys'] = self.keys
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class RemoveMessageExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: RemoveMessageExtensionByKeysRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveMessageExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveMessageExtensionByKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemoveMessageExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveSingleChatExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uid: str = None,
        keys: List[str] = None,
    ):
        self.app_cid = app_cid
        self.app_uid = app_uid
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
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
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveSingleChatExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveSingleChatExtensionByKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemoveSingleChatExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUserConversationExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uid: str = None,
        keys: List[str] = None,
    ):
        self.app_cid = app_cid
        self.app_uid = app_uid
        self.keys = keys

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
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
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveUserConversationExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveUserConversationExtensionByKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = RemoveUserConversationExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomMessageRequestRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        domain: str = None,
        room_id: str = None,
        sender_id: str = None,
        sub_type: int = None,
    ):
        self.body = body
        self.domain = domain
        self.room_id = room_id
        self.sender_id = sender_id
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class SendCustomMessageRequest(TeaModel):
    def __init__(
        self,
        request: SendCustomMessageRequestRequest = None,
    ):
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Request') is not None:
            temp_model = SendCustomMessageRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class SendCustomMessageResponseBodyResult(TeaModel):
    def __init__(
        self,
        message_id: str = None,
    ):
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class SendCustomMessageResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        response_success: bool = None,
        result: SendCustomMessageResponseBodyResult = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.response_success = response_success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('Result') is not None:
            temp_model = SendCustomMessageResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCustomMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendCustomMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SendCustomMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomMessageToRoomUsersRequestRequest(TeaModel):
    def __init__(
        self,
        body: str = None,
        domain: str = None,
        room_id: str = None,
        sender_id: str = None,
        sub_type: int = None,
    ):
        self.body = body
        self.domain = domain
        self.room_id = room_id
        self.sender_id = sender_id
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['Body'] = self.body
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.sub_type is not None:
            result['SubType'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')
        return self


class SendCustomMessageToRoomUsersRequest(TeaModel):
    def __init__(
        self,
        receivers: List[str] = None,
        request: SendCustomMessageToRoomUsersRequestRequest = None,
    ):
        self.receivers = receivers
        self.request = request

    def validate(self):
        if self.request:
            self.request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receivers is not None:
            result['Receivers'] = self.receivers
        if self.request is not None:
            result['Request'] = self.request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Receivers') is not None:
            self.receivers = m.get('Receivers')
        if m.get('Request') is not None:
            temp_model = SendCustomMessageToRoomUsersRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        return self


class SendCustomMessageToRoomUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        message_id: str = None,
    ):
        self.message_id = message_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        return self


class SendCustomMessageToRoomUsersResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        request_id: str = None,
        response_success: bool = None,
        result: SendCustomMessageToRoomUsersResponseBodyResult = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.request_id = request_id
        self.response_success = response_success
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('Result') is not None:
            temp_model = SendCustomMessageToRoomUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCustomMessageToRoomUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendCustomMessageToRoomUsersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SendCustomMessageToRoomUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageRequestRequestParamsOptionsReceiveScopeOption(TeaModel):
    def __init__(
        self,
        exclude_receiver_ids: List[str] = None,
        receive_scope: int = None,
        receiver_ids: List[str] = None,
    ):
        self.exclude_receiver_ids = exclude_receiver_ids
        self.receive_scope = receive_scope
        self.receiver_ids = receiver_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exclude_receiver_ids is not None:
            result['ExcludeReceiverIds'] = self.exclude_receiver_ids
        if self.receive_scope is not None:
            result['ReceiveScope'] = self.receive_scope
        if self.receiver_ids is not None:
            result['ReceiverIds'] = self.receiver_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExcludeReceiverIds') is not None:
            self.exclude_receiver_ids = m.get('ExcludeReceiverIds')
        if m.get('ReceiveScope') is not None:
            self.receive_scope = m.get('ReceiveScope')
        if m.get('ReceiverIds') is not None:
            self.receiver_ids = m.get('ReceiverIds')
        return self


class SendMessageRequestRequestParamsOptionsSingleChatCreateRequest(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uids: List[str] = None,
        extensions: Dict[str, str] = None,
        user_conversation: Dict[str, RequestParamsOptionsSingleChatCreateRequestUserConversationValue] = None,
    ):
        self.app_cid = app_cid
        self.app_uids = app_uids
        self.extensions = extensions
        self.user_conversation = user_conversation

    def validate(self):
        if self.user_conversation:
            for v in self.user_conversation.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        receive_scope_option: SendMessageRequestRequestParamsOptionsReceiveScopeOption = None,
        red_point_policy: int = None,
        single_chat_create_request: SendMessageRequestRequestParamsOptionsSingleChatCreateRequest = None,
    ):
        self.receive_scope_option = receive_scope_option
        self.red_point_policy = red_point_policy
        self.single_chat_create_request = single_chat_create_request

    def validate(self):
        if self.receive_scope_option:
            self.receive_scope_option.validate()
        if self.single_chat_create_request:
            self.single_chat_create_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.receive_scope_option is not None:
            result['ReceiveScopeOption'] = self.receive_scope_option.to_map()
        if self.red_point_policy is not None:
            result['RedPointPolicy'] = self.red_point_policy
        if self.single_chat_create_request is not None:
            result['SingleChatCreateRequest'] = self.single_chat_create_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReceiveScopeOption') is not None:
            temp_model = SendMessageRequestRequestParamsOptionsReceiveScopeOption()
            self.receive_scope_option = temp_model.from_map(m['ReceiveScopeOption'])
        if m.get('RedPointPolicy') is not None:
            self.red_point_policy = m.get('RedPointPolicy')
        if m.get('SingleChatCreateRequest') is not None:
            temp_model = SendMessageRequestRequestParamsOptionsSingleChatCreateRequest()
            self.single_chat_create_request = temp_model.from_map(m['SingleChatCreateRequest'])
        return self


class SendMessageRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        content: str = None,
        content_type: int = None,
        conversation_type: int = None,
        extensions: Dict[str, str] = None,
        options: SendMessageRequestRequestParamsOptions = None,
        sender_id: str = None,
        uuid: str = None,
    ):
        self.app_cid = app_cid
        self.content = content
        self.content_type = content_type
        self.conversation_type = conversation_type
        self.extensions = extensions
        self.options = options
        self.sender_id = sender_id
        self.uuid = uuid

    def validate(self):
        if self.options:
            self.options.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.content is not None:
            result['Content'] = self.content
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.conversation_type is not None:
            result['ConversationType'] = self.conversation_type
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.options is not None:
            result['Options'] = self.options.to_map()
        if self.sender_id is not None:
            result['SenderId'] = self.sender_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ConversationType') is not None:
            self.conversation_type = m.get('ConversationType')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('Options') is not None:
            temp_model = SendMessageRequestRequestParamsOptions()
            self.options = temp_model.from_map(m['Options'])
        if m.get('SenderId') is not None:
            self.sender_id = m.get('SenderId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SendMessageRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        create_time: int = None,
        msg_id: str = None,
    ):
        self.create_time = create_time
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: SendMessageResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = SendMessageResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SendMessageResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SendMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGroupExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        extensions: Dict[str, str] = None,
    ):
        self.app_cid = app_cid
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetGroupExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetGroupExtensionByKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SetGroupExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGroupMemberExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uid: str = None,
        extensions: Dict[str, str] = None,
    ):
        self.app_cid = app_cid
        self.app_uid = app_uid
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class SetGroupMemberExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SetGroupMemberExtensionByKeysRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SetGroupMemberExtensionByKeysRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetGroupMemberExtensionByKeysShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class SetGroupMemberExtensionByKeysResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetGroupMemberExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetGroupMemberExtensionByKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SetGroupMemberExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetGroupOwnerRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        new_owner_app_uid: str = None,
    ):
        self.app_cid = app_cid
        self.new_owner_app_uid = new_owner_app_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.new_owner_app_uid is not None:
            result['NewOwnerAppUid'] = self.new_owner_app_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('NewOwnerAppUid') is not None:
            self.new_owner_app_uid = m.get('NewOwnerAppUid')
        return self


class SetGroupOwnerRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SetGroupOwnerRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SetGroupOwnerRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetGroupOwnerShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class SetGroupOwnerResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetGroupOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetGroupOwnerResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SetGroupOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMessageExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        extensions: Dict[str, str] = None,
        msg_id: str = None,
    ):
        self.app_cid = app_cid
        self.extensions = extensions
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SetMessageExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SetMessageExtensionByKeysRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetMessageExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetMessageExtensionByKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SetMessageExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetMessageReadRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        msg_id: str = None,
    ):
        self.app_uid = app_uid
        self.msg_id = msg_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.msg_id is not None:
            result['MsgId'] = self.msg_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('MsgId') is not None:
            self.msg_id = m.get('MsgId')
        return self


class SetMessageReadRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SetMessageReadRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = SetMessageReadRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class SetMessageReadShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class SetMessageReadResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetMessageReadResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetMessageReadResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SetMessageReadResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetSingleChatExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uid: str = None,
        extensions: Dict[str, str] = None,
    ):
        self.app_cid = app_cid
        self.app_uid = app_uid
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('Extensions') is not None:
            self.extensions = m.get('Extensions')
        return self


class SetSingleChatExtensionByKeysRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: SetSingleChatExtensionByKeysRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetSingleChatExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetSingleChatExtensionByKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SetSingleChatExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SetUserConversationExtensionByKeysRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uid: str = None,
        extensions: Dict[str, str] = None,
    ):
        self.app_cid = app_cid
        self.app_uid = app_uid
        self.extensions = extensions

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.extensions is not None:
            result['Extensions'] = self.extensions
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
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
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SetUserConversationExtensionByKeysResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetUserConversationExtensionByKeysResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SetUserConversationExtensionByKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SilenceAllGroupMembersRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        operator_app_uid: str = None,
    ):
        self.app_cid = app_cid
        self.operator_app_uid = operator_app_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class SilenceAllGroupMembersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SilenceAllGroupMembersResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = SilenceAllGroupMembersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindInterconnectionUidRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_uid: str = None,
        ding_talk_uid: str = None,
    ):
        self.app_uid = app_uid
        self.ding_talk_uid = ding_talk_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_uid is not None:
            result['AppUid'] = self.app_uid
        if self.ding_talk_uid is not None:
            result['DingTalkUid'] = self.ding_talk_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppUid') is not None:
            self.app_uid = m.get('AppUid')
        if m.get('DingTalkUid') is not None:
            self.ding_talk_uid = m.get('DingTalkUid')
        return self


class UnbindInterconnectionUidRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: UnbindInterconnectionUidRequestRequestParams = None,
    ):
        # AppId
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UnbindInterconnectionUidRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UnbindInterconnectionUidShrinkRequest(TeaModel):
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
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UnbindInterconnectionUidResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UnbindInterconnectionUidResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindInterconnectionUidResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UnbindInterconnectionUidResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppNameRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_name: str = None,
    ):
        self.app_name = app_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        return self


class UpdateAppNameRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: UpdateAppNameRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateAppNameRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateAppNameShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateAppNameResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # httpStatusCode
        self.http_status_code = http_status_code
        # desc
        self.message = message
        # requestId
        self.request_id = request_id
        # success
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
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
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateAppNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppNameResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateAppNameResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppStatusRequestRequestParams(TeaModel):
    def __init__(
        self,
        enable: bool = None,
    ):
        self.enable = enable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable is not None:
            result['Enable'] = self.enable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Enable') is not None:
            self.enable = m.get('Enable')
        return self


class UpdateAppStatusRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: UpdateAppStatusRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateAppStatusRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateAppStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateAppStatusResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
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


class UpdateAppStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAppStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateAppStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateCallbackConfigRequestRequestParams(TeaModel):
    def __init__(
        self,
        apis: Dict[str, bool] = None,
        callback_url: str = None,
        events: Dict[str, bool] = None,
        signature_key: str = None,
        signature_value: str = None,
        spis: Dict[str, bool] = None,
    ):
        self.apis = apis
        self.callback_url = callback_url
        self.events = events
        self.signature_key = signature_key
        self.signature_value = signature_value
        self.spis = spis

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apis is not None:
            result['Apis'] = self.apis
        if self.callback_url is not None:
            result['CallbackUrl'] = self.callback_url
        if self.events is not None:
            result['Events'] = self.events
        if self.signature_key is not None:
            result['SignatureKey'] = self.signature_key
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        if self.spis is not None:
            result['Spis'] = self.spis
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apis') is not None:
            self.apis = m.get('Apis')
        if m.get('CallbackUrl') is not None:
            self.callback_url = m.get('CallbackUrl')
        if m.get('Events') is not None:
            self.events = m.get('Events')
        if m.get('SignatureKey') is not None:
            self.signature_key = m.get('SignatureKey')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        if m.get('Spis') is not None:
            self.spis = m.get('Spis')
        return self


class UpdateCallbackConfigRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: UpdateCallbackConfigRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateCallbackConfigRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateCallbackConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateCallbackConfigResponseBodyResultImConfigCallbackConfig(TeaModel):
    def __init__(
        self,
        api_ids: List[str] = None,
        backend_url: str = None,
        signature_key: str = None,
        signature_value: str = None,
    ):
        self.api_ids = api_ids
        self.backend_url = backend_url
        self.signature_key = signature_key
        self.signature_value = signature_value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.api_ids is not None:
            result['ApiIds'] = self.api_ids
        if self.backend_url is not None:
            result['BackendUrl'] = self.backend_url
        if self.signature_key is not None:
            result['SignatureKey'] = self.signature_key
        if self.signature_value is not None:
            result['SignatureValue'] = self.signature_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiIds') is not None:
            self.api_ids = m.get('ApiIds')
        if m.get('BackendUrl') is not None:
            self.backend_url = m.get('BackendUrl')
        if m.get('SignatureKey') is not None:
            self.signature_key = m.get('SignatureKey')
        if m.get('SignatureValue') is not None:
            self.signature_value = m.get('SignatureValue')
        return self


class UpdateCallbackConfigResponseBodyResultImConfigMsgConfig(TeaModel):
    def __init__(
        self,
        msg_recall_time_interval: int = None,
    ):
        self.msg_recall_time_interval = msg_recall_time_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.msg_recall_time_interval is not None:
            result['MsgRecallTimeInterval'] = self.msg_recall_time_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MsgRecallTimeInterval') is not None:
            self.msg_recall_time_interval = m.get('MsgRecallTimeInterval')
        return self


class UpdateCallbackConfigResponseBodyResultImConfig(TeaModel):
    def __init__(
        self,
        callback_config: UpdateCallbackConfigResponseBodyResultImConfigCallbackConfig = None,
        msg_config: UpdateCallbackConfigResponseBodyResultImConfigMsgConfig = None,
    ):
        self.callback_config = callback_config
        self.msg_config = msg_config

    def validate(self):
        if self.callback_config:
            self.callback_config.validate()
        if self.msg_config:
            self.msg_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.callback_config is not None:
            result['CallbackConfig'] = self.callback_config.to_map()
        if self.msg_config is not None:
            result['MsgConfig'] = self.msg_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallbackConfig') is not None:
            temp_model = UpdateCallbackConfigResponseBodyResultImConfigCallbackConfig()
            self.callback_config = temp_model.from_map(m['CallbackConfig'])
        if m.get('MsgConfig') is not None:
            temp_model = UpdateCallbackConfigResponseBodyResultImConfigMsgConfig()
            self.msg_config = temp_model.from_map(m['MsgConfig'])
        return self


class UpdateCallbackConfigResponseBodyResult(TeaModel):
    def __init__(
        self,
        im_config: UpdateCallbackConfigResponseBodyResultImConfig = None,
    ):
        self.im_config = im_config

    def validate(self):
        if self.im_config:
            self.im_config.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.im_config is not None:
            result['ImConfig'] = self.im_config.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ImConfig') is not None:
            temp_model = UpdateCallbackConfigResponseBodyResultImConfig()
            self.im_config = temp_model.from_map(m['ImConfig'])
        return self


class UpdateCallbackConfigResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result: UpdateCallbackConfigResponseBodyResult = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # httpStatusCode
        self.http_status_code = http_status_code
        # desc
        self.message = message
        # requestId
        self.request_id = request_id
        # result
        self.result = result
        # success
        self.success = success

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = UpdateCallbackConfigResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateCallbackConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateCallbackConfigResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateCallbackConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupIconRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        icon_media_id: str = None,
        operator_app_uid: str = None,
    ):
        self.app_cid = app_cid
        self.icon_media_id = icon_media_id
        self.operator_app_uid = operator_app_uid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.icon_media_id is not None:
            result['IconMediaId'] = self.icon_media_id
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('IconMediaId') is not None:
            self.icon_media_id = m.get('IconMediaId')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        return self


class UpdateGroupIconRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: UpdateGroupIconRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGroupIconResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGroupIconResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateGroupIconResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupMembersRoleRequestRequestParams(TeaModel):
    def __init__(
        self,
        app_cid: str = None,
        app_uids: List[str] = None,
        operator_app_uid: str = None,
        role: int = None,
    ):
        self.app_cid = app_cid
        self.app_uids = app_uids
        self.operator_app_uid = operator_app_uid
        self.role = role

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_cid is not None:
            result['AppCid'] = self.app_cid
        if self.app_uids is not None:
            result['AppUids'] = self.app_uids
        if self.operator_app_uid is not None:
            result['OperatorAppUid'] = self.operator_app_uid
        if self.role is not None:
            result['Role'] = self.role
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppCid') is not None:
            self.app_cid = m.get('AppCid')
        if m.get('AppUids') is not None:
            self.app_uids = m.get('AppUids')
        if m.get('OperatorAppUid') is not None:
            self.operator_app_uid = m.get('OperatorAppUid')
        if m.get('Role') is not None:
            self.role = m.get('Role')
        return self


class UpdateGroupMembersRoleRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: UpdateGroupMembersRoleRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGroupMembersRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGroupMembersRoleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
        self.app_cid = app_cid
        self.operator_app_uid = operator_app_uid
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
        code: str = None,
        message: str = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateGroupTitleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateGroupTitleResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateGroupTitleResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateMsgRecallIntervalRequestRequestParams(TeaModel):
    def __init__(
        self,
        client_msg_recall_interval_minute: int = None,
    ):
        self.client_msg_recall_interval_minute = client_msg_recall_interval_minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_msg_recall_interval_minute is not None:
            result['ClientMsgRecallIntervalMinute'] = self.client_msg_recall_interval_minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientMsgRecallIntervalMinute') is not None:
            self.client_msg_recall_interval_minute = m.get('ClientMsgRecallIntervalMinute')
        return self


class UpdateMsgRecallIntervalRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params: UpdateMsgRecallIntervalRequestRequestParams = None,
    ):
        self.app_id = app_id
        self.request_params = request_params

    def validate(self):
        if self.request_params:
            self.request_params.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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
            temp_model = UpdateMsgRecallIntervalRequestRequestParams()
            self.request_params = temp_model.from_map(m['RequestParams'])
        return self


class UpdateMsgRecallIntervalShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        request_params_shrink: str = None,
    ):
        self.app_id = app_id
        self.request_params_shrink = request_params_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class UpdateMsgRecallIntervalResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
        success: bool = None,
    ):
        # code
        self.code = code
        # httpStatusCode
        self.http_status_code = http_status_code
        # desc
        self.message = message
        # requestId
        self.request_id = request_id
        # result
        self.result = result
        # success
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
        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code
        if self.message is not None:
            result['Message'] = self.message
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class UpdateMsgRecallIntervalResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateMsgRecallIntervalResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateMsgRecallIntervalResponseBody()
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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        _map = super().to_map()
        if _map is not None:
            return _map

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
        request_id: str = None,
        response_success: bool = None,
        error_code: str = None,
        error_msg: str = None,
        result: bool = None,
    ):
        self.request_id = request_id
        self.response_success = response_success
        self.error_code = error_code
        self.error_msg = error_msg
        self.result = result

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.response_success is not None:
            result['ResponseSuccess'] = self.response_success
        if self.error_code is not None:
            result['errorCode'] = self.error_code
        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg
        if self.result is not None:
            result['result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResponseSuccess') is not None:
            self.response_success = m.get('ResponseSuccess')
        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')
        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')
        if m.get('result') is not None:
            self.result = m.get('result')
        return self


class UpdateTenantStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateTenantStatusResponseBody = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
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
            temp_model = UpdateTenantStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



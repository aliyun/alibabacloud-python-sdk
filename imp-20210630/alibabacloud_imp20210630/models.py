# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, List


class VerifyDomainOwnerRequest(TeaModel):
    def __init__(
        self,
        live_domain_name: str = None,
    ):
        # 直播域名
        self.live_domain_name = live_domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_domain_name is not None:
            result['LiveDomainName'] = self.live_domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveDomainName') is not None:
            self.live_domain_name = m.get('LiveDomainName')
        return self


class VerifyDomainOwnerResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果
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
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class VerifyDomainOwnerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: VerifyDomainOwnerResponseBody = None,
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
            temp_model = VerifyDomainOwnerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateLiveRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        user_id: str = None,
        live_id: str = None,
        title: str = None,
        introduction: str = None,
        anchor_id: str = None,
        code_level: int = None,
    ):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id
        # 房间ID，最大长度36个字符，传空值，则随机生成一个房间ID。
        self.room_id = room_id
        # 创建直播用户。
        self.user_id = user_id
        # 直播资源的唯一标识ID，缺省时系统自动生成36位随机uuid字符串。
        self.live_id = live_id
        # 直播标题，支持中英文，最大长度256位。
        self.title = title
        # 直播简介，支持中英文，最大长度2048位。
        self.introduction = introduction
        # 主播ID，支持中英文，最大长度128位，缺省时主播为当前创建直播用户。
        self.anchor_id = anchor_id
        # 直播推流码率，缺省时默认为3。取值：  -1：流畅lld。 1：标清lsd。 2：高清lhd。 3：超清lud。
        self.code_level = code_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.title is not None:
            result['Title'] = self.title
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.code_level is not None:
            result['CodeLevel'] = self.code_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('CodeLevel') is not None:
            self.code_level = m.get('CodeLevel')
        return self


class CreateLiveResponseBodyResult(TeaModel):
    def __init__(
        self,
        live_id: str = None,
    ):
        # 直播的唯一标识ID。
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class CreateLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateLiveResponseBodyResult = None,
    ):
        # 请求ID。
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateLiveResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateLiveResponseBody = None,
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
            temp_model = CreateLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveMemberRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        to_user_id: str = None,
        from_user_id: str = None,
    ):
        # 会议唯一标识
        self.conference_id = conference_id
        # 被邀请用户ID
        self.to_user_id = to_user_id
        # 邀请者用户ID
        self.from_user_id = from_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        return self


class RemoveMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RemoveMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RemoveMemberResponseBody = None,
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
            temp_model = RemoveMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # 应用唯一标识
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
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAppResponseBody = None,
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
            temp_model = DeleteAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApplyLinkMicUsersRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 会议唯一标识符
        self.conference_id = conference_id
        # 查询页码，从第1页开始。
        self.page_number = page_number
        # 每页显示个数，最大显示个数为100。
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListApplyLinkMicUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        apply_link_mic_user_list: List[str] = None,
        has_more: bool = None,
        total_count: int = None,
        page_total: int = None,
    ):
        # 会议申请连麦用户列表。
        self.apply_link_mic_user_list = apply_link_mic_user_list
        # 是否还有下一页成员列表。
        self.has_more = has_more
        # 该会议的申请连麦成员总数。
        self.total_count = total_count
        # 改会议的申请连麦成员总页数。
        self.page_total = page_total

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_link_mic_user_list is not None:
            result['ApplyLinkMicUserList'] = self.apply_link_mic_user_list
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplyLinkMicUserList') is not None:
            self.apply_link_mic_user_list = m.get('ApplyLinkMicUserList')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        return self


class ListApplyLinkMicUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListApplyLinkMicUsersResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListApplyLinkMicUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListApplyLinkMicUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListApplyLinkMicUsersResponseBody = None,
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
            temp_model = ListApplyLinkMicUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoomLivesRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        status: int = None,
        query_timestamp: int = None,
        size: int = None,
    ):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id
        # 房间ID，最大长度36个字符。
        self.room_id = room_id
        # 直播状态筛选条件，0-直播 1-下播，不传则返回全部状态
        self.status = status
        # 拉取在这个时间戳之前创建的直播，单位毫秒，不传则默认拉取最新创建的。
        self.query_timestamp = query_timestamp
        # 拉取直播数量。
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.status is not None:
            result['Status'] = self.status
        if self.query_timestamp is not None:
            result['QueryTimestamp'] = self.query_timestamp
        if self.size is not None:
            result['Size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('QueryTimestamp') is not None:
            self.query_timestamp = m.get('QueryTimestamp')
        if m.get('Size') is not None:
            self.size = m.get('Size')
        return self


class ListRoomLivesResponseBodyResultLiveList(TeaModel):
    def __init__(
        self,
        room_id: str = None,
        title: str = None,
        room_owner_id: str = None,
        notice: str = None,
        uv: int = None,
        app_id: str = None,
        extension: Dict[str, str] = None,
        live_id: str = None,
        status: int = None,
    ):
        # 房间唯一标识。
        self.room_id = room_id
        # 房间标题。
        self.title = title
        # 房主用户id。
        self.room_owner_id = room_owner_id
        # 房间公告。
        self.notice = notice
        # 用户访问数。
        self.uv = uv
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id
        # 房间拓展字段。
        self.extension = extension
        # 直播id。
        self.live_id = live_id
        # 直播状态，0-在播 1-不在播。
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.uv is not None:
            result['Uv'] = self.uv
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.extension is not None:
            result['Extension'] = self.extension
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListRoomLivesResponseBodyResult(TeaModel):
    def __init__(
        self,
        has_more: bool = None,
        live_list: List[ListRoomLivesResponseBodyResultLiveList] = None,
        next_query_timestamp: int = None,
    ):
        # 是否还有下一页直播列表。
        self.has_more = has_more
        # 直播列表信息。
        self.live_list = live_list
        # 下一个拉取的时间戳，单位毫秒。
        self.next_query_timestamp = next_query_timestamp

    def validate(self):
        if self.live_list:
            for k in self.live_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['LiveList'] = []
        if self.live_list is not None:
            for k in self.live_list:
                result['LiveList'].append(k.to_map() if k else None)
        if self.next_query_timestamp is not None:
            result['NextQueryTimestamp'] = self.next_query_timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.live_list = []
        if m.get('LiveList') is not None:
            for k in m.get('LiveList'):
                temp_model = ListRoomLivesResponseBodyResultLiveList()
                self.live_list.append(temp_model.from_map(k))
        if m.get('NextQueryTimestamp') is not None:
            self.next_query_timestamp = m.get('NextQueryTimestamp')
        return self


class ListRoomLivesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListRoomLivesResponseBodyResult = None,
    ):
        # 请求ID。
        self.request_id = request_id
        # API请求的返回结果结构体。
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListRoomLivesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRoomLivesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRoomLivesResponseBody = None,
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
            temp_model = ListRoomLivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        title: str = None,
        notice: str = None,
        room_owner_id: str = None,
        extension: Dict[str, str] = None,
    ):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id
        # 房间唯一标识。
        self.room_id = room_id
        # 房间标题，支持中英文，最大长度32位。
        self.title = title
        # 房间公告，支持中英文，最大长度256位。
        self.notice = notice
        # 房主用户id，仅支持英文和数字，最大长度36位。
        self.room_owner_id = room_owner_id
        # 拓展字段，按需传递，需要额外记录的房间属性。
        self.extension = extension

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class UpdateRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateRoomResponseBody = None,
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
            temp_model = UpdateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppTemplateRequest(TeaModel):
    def __init__(
        self,
        app_template_id: str = None,
    ):
        # 应用模板唯一标识
        self.app_template_id = app_template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        return self


class GetAppTemplateResponseBodyResultConfigList(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 配置项
        self.key = key
        # 配置项内容
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class GetAppTemplateResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_template_name: str = None,
        app_template_creator: str = None,
        status: str = None,
        component_list: List[str] = None,
        create_time: str = None,
        sdk_info: str = None,
        config_list: List[GetAppTemplateResponseBodyResultConfigList] = None,
    ):
        # 应用模板名称
        self.app_template_name = app_template_name
        # 应用模板创建者
        self.app_template_creator = app_template_creator
        # 应用模板使用状态
        self.status = status
        # 组件列表
        self.component_list = component_list
        # 创建时间
        self.create_time = create_time
        self.sdk_info = sdk_info
        # 配置列表
        self.config_list = config_list

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.app_template_creator is not None:
            result['AppTemplateCreator'] = self.app_template_creator
        if self.status is not None:
            result['Status'] = self.status
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sdk_info is not None:
            result['SdkInfo'] = self.sdk_info
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('AppTemplateCreator') is not None:
            self.app_template_creator = m.get('AppTemplateCreator')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SdkInfo') is not None:
            self.sdk_info = m.get('SdkInfo')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = GetAppTemplateResponseBodyResultConfigList()
                self.config_list.append(temp_model.from_map(k))
        return self


class GetAppTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetAppTemplateResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetAppTemplateResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAppTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAppTemplateResponseBody = None,
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
            temp_model = GetAppTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
    ):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位。
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList(TeaModel):
    def __init__(
        self,
        plugin_type: str = None,
        plugin_id: str = None,
        create_time: int = None,
        extension: Dict[str, str] = None,
    ):
        # 插件唯一标识，取值：live-直播，wb-白板，chat-聊天，rtc。
        self.plugin_type = plugin_type
        # 插件实例唯一标识。
        self.plugin_id = plugin_id
        # 插件实例创建时间戳，单位：毫秒。
        self.create_time = create_time
        # 插件拓展字段。
        self.extension = extension

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class GetRoomResponseBodyResultRoomInfo(TeaModel):
    def __init__(
        self,
        room_id: str = None,
        title: str = None,
        create_time: int = None,
        notice: str = None,
        room_owner_id: str = None,
        uv: int = None,
        online_count: int = None,
        plugin_instance_info_list: List[GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList] = None,
        app_id: str = None,
        template_id: str = None,
        extension: Dict[str, str] = None,
    ):
        # 房间唯一标识。
        self.room_id = room_id
        # 房间标题。
        self.title = title
        # 房间创建时间戳，单位：毫秒。
        self.create_time = create_time
        # 房间公告。
        self.notice = notice
        # 房主用户id。
        self.room_owner_id = room_owner_id
        # 访问用户数。
        self.uv = uv
        # 在线用户数。
        self.online_count = online_count
        # 活跃插件列表。
        self.plugin_instance_info_list = plugin_instance_info_list
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id
        # 创建房间使用的模板id。
        self.template_id = template_id
        # 房间拓展字段。
        self.extension = extension

    def validate(self):
        if self.plugin_instance_info_list:
            for k in self.plugin_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.uv is not None:
            result['Uv'] = self.uv
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = GetRoomResponseBodyResultRoomInfoPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class GetRoomResponseBodyResult(TeaModel):
    def __init__(
        self,
        room_info: GetRoomResponseBodyResultRoomInfo = None,
    ):
        # 房间信息。
        self.room_info = room_info

    def validate(self):
        if self.room_info:
            self.room_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_info is not None:
            result['RoomInfo'] = self.room_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomInfo') is not None:
            temp_model = GetRoomResponseBodyResultRoomInfo()
            self.room_info = temp_model.from_map(m['RoomInfo'])
        return self


class GetRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetRoomResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        # 查询房间信息返回结果。
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetRoomResponseBody = None,
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
            temp_model = GetRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppTemplateRequest(TeaModel):
    def __init__(
        self,
        app_template_name: str = None,
        component_list: List[str] = None,
    ):
        # 应用模板名称
        self.app_template_name = app_template_name
        # 组件列表
        self.component_list = component_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        return self


class CreateAppTemplateShrinkRequest(TeaModel):
    def __init__(
        self,
        app_template_name: str = None,
        component_list_shrink: str = None,
    ):
        # 应用模板名称
        self.app_template_name = app_template_name
        # 组件列表
        self.component_list_shrink = component_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.component_list_shrink is not None:
            result['ComponentList'] = self.component_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('ComponentList') is not None:
            self.component_list_shrink = m.get('ComponentList')
        return self


class CreateAppTemplateResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_template_id: str = None,
    ):
        # 应用模板唯一标示
        self.app_template_id = app_template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        return self


class CreateAppTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAppTemplateResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAppTemplateResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAppTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppTemplateResponseBody = None,
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
            temp_model = CreateAppTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetConferenceRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
    ):
        # 会议资源唯一标识。
        self.conference_id = conference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class GetConferenceResponseBodyResult(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        title: str = None,
        status: str = None,
        room_id: str = None,
        user_id: str = None,
        app_id: str = None,
        create_time: int = None,
    ):
        # 会议资源唯一标识。
        self.conference_id = conference_id
        # 会议标题。
        self.title = title
        # 会议状态。
        self.status = status
        # 房间ID。
        self.room_id = room_id
        # 创建会议用户。
        self.user_id = user_id
        # 租户名
        self.app_id = app_id
        # 会议创建时间戳，单位：毫秒。
        self.create_time = create_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.title is not None:
            result['Title'] = self.title
        if self.status is not None:
            result['Status'] = self.status
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        return self


class GetConferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetConferenceResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetConferenceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetConferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetConferenceResponseBody = None,
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
            temp_model = GetConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectLinkMicRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        to_user_id: str = None,
        from_user_id: str = None,
    ):
        # 会议唯一标识
        self.conference_id = conference_id
        # 被同意用户ID
        self.to_user_id = to_user_id
        # 同意者用户ID
        self.from_user_id = from_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        return self


class RejectLinkMicResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class RejectLinkMicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: RejectLinkMicResponseBody = None,
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
            temp_model = RejectLinkMicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppsRequest(TeaModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
    ):
        # 查询页码，参数为空默认查询第1页。
        self.page_number = page_number
        # 每页显示个数，参数为空默认显示个数为10。
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListAppsResponseBodyResultAppInfoList(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_template_id: str = None,
        app_template_name: str = None,
        app_key: str = None,
        app_status: str = None,
        create_time: str = None,
        component_list: List[str] = None,
    ):
        # 应用唯一标识符
        self.app_id = app_id
        # 应用名称
        self.app_name = app_name
        # 模板唯一标识
        self.app_template_id = app_template_id
        # 模板名称
        self.app_template_name = app_template_name
        # 应用Key
        self.app_key = app_key
        # 应用状态
        self.app_status = app_status
        # 应用创建时间
        self.create_time = create_time
        # 应用组件列表
        self.component_list = component_list

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
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        return self


class ListAppsResponseBodyResult(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_total: int = None,
        app_info_list: List[ListAppsResponseBodyResultAppInfoList] = None,
    ):
        # 总条目数
        self.total_count = total_count
        # 总页数
        self.page_total = page_total
        # App信息列表
        self.app_info_list = app_info_list

    def validate(self):
        if self.app_info_list:
            for k in self.app_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        result['AppInfoList'] = []
        if self.app_info_list is not None:
            for k in self.app_info_list:
                result['AppInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        self.app_info_list = []
        if m.get('AppInfoList') is not None:
            for k in m.get('AppInfoList'):
                temp_model = ListAppsResponseBodyResultAppInfoList()
                self.app_info_list.append(temp_model.from_map(k))
        return self


class ListAppsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListAppsResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果体
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListAppsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListAppsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppsResponseBody = None,
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
            temp_model = ListAppsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddMemberRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        to_user_id: str = None,
        from_user_id: str = None,
    ):
        # 会议唯一标识
        self.conference_id = conference_id
        # 被邀请用户ID
        self.to_user_id = to_user_id
        # 邀请者用户ID
        self.from_user_id = from_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        return self


class AddMemberResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AddMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AddMemberResponseBody = None,
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
            temp_model = AddMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRoomsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id
        # 查询页码，从1开始，传空默认查询第1页。
        self.page_number = page_number
        # 每页显示个数，最大支持50，参数为空默认显示个数为10。
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList(TeaModel):
    def __init__(
        self,
        plugin_type: str = None,
        plugin_id: str = None,
        create_time: int = None,
        extension: Dict[str, str] = None,
    ):
        # 插件唯一标识，取值：live-直播，wb-白板，chat-聊天，rtc。
        self.plugin_type = plugin_type
        # 插件实例唯一标识。
        self.plugin_id = plugin_id
        # 插件实例创建时间戳，单位：毫秒。
        self.create_time = create_time
        # 插件拓展字段。
        self.extension = extension

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.plugin_type is not None:
            result['PluginType'] = self.plugin_type
        if self.plugin_id is not None:
            result['PluginId'] = self.plugin_id
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PluginType') is not None:
            self.plugin_type = m.get('PluginType')
        if m.get('PluginId') is not None:
            self.plugin_id = m.get('PluginId')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class ListRoomsResponseBodyResultRoomInfoList(TeaModel):
    def __init__(
        self,
        room_id: str = None,
        title: str = None,
        room_owner_id: str = None,
        notice: str = None,
        uv: int = None,
        online_count: int = None,
        plugin_instance_info_list: List[ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList] = None,
        create_time: str = None,
        app_id: str = None,
        template_id: str = None,
        extension: Dict[str, str] = None,
    ):
        # 房间唯一标识。
        self.room_id = room_id
        # 房间标题。
        self.title = title
        # 房主用户id。
        self.room_owner_id = room_owner_id
        # 房间公告。
        self.notice = notice
        # 用户访问数。
        self.uv = uv
        # 用户在线数。
        self.online_count = online_count
        # 活跃插件列表。
        self.plugin_instance_info_list = plugin_instance_info_list
        # 房间创建时间戳，单位：毫秒。
        self.create_time = create_time
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id
        # 创建房间使用的模板id。
        self.template_id = template_id
        # 房间拓展字段。
        self.extension = extension

    def validate(self):
        if self.plugin_instance_info_list:
            for k in self.plugin_instance_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.uv is not None:
            result['Uv'] = self.uv
        if self.online_count is not None:
            result['OnlineCount'] = self.online_count
        result['PluginInstanceInfoList'] = []
        if self.plugin_instance_info_list is not None:
            for k in self.plugin_instance_info_list:
                result['PluginInstanceInfoList'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('Uv') is not None:
            self.uv = m.get('Uv')
        if m.get('OnlineCount') is not None:
            self.online_count = m.get('OnlineCount')
        self.plugin_instance_info_list = []
        if m.get('PluginInstanceInfoList') is not None:
            for k in m.get('PluginInstanceInfoList'):
                temp_model = ListRoomsResponseBodyResultRoomInfoListPluginInstanceInfoList()
                self.plugin_instance_info_list.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class ListRoomsResponseBodyResult(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_total: int = None,
        has_more: bool = None,
        room_info_list: List[ListRoomsResponseBodyResultRoomInfoList] = None,
    ):
        # 该应用的房间总数。
        self.total_count = total_count
        # 该应用的房间总页数。
        self.page_total = page_total
        # 是否还有下一页房间列表。
        self.has_more = has_more
        # 房间列表信息。
        self.room_info_list = room_info_list

    def validate(self):
        if self.room_info_list:
            for k in self.room_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        result['RoomInfoList'] = []
        if self.room_info_list is not None:
            for k in self.room_info_list:
                result['RoomInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        self.room_info_list = []
        if m.get('RoomInfoList') is not None:
            for k in m.get('RoomInfoList'):
                temp_model = ListRoomsResponseBodyResultRoomInfoList()
                self.room_info_list.append(temp_model.from_map(k))
        return self


class ListRoomsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListRoomsResponseBodyResult = None,
    ):
        # 请求ID。
        self.request_id = request_id
        # API请求的返回结果结构体。
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListRoomsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListRoomsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListRoomsResponseBody = None,
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
            temp_model = ListRoomsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAppTemplateRequest(TeaModel):
    def __init__(
        self,
        app_template_id: str = None,
    ):
        # 模板唯一标识
        self.app_template_id = app_template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        return self


class DeleteAppTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteAppTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteAppTemplateResponseBody = None,
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
            temp_model = DeleteAppTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListConferenceUsersRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # 会议唯一标识符
        self.conference_id = conference_id
        # 查询页码，从第1页开始。
        self.page_number = page_number
        # 每页显示个数，最大显示个数为100。
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListConferenceUsersResponseBodyResultConferenceUserList(TeaModel):
    def __init__(
        self,
        user_id: str = None,
        status: str = None,
    ):
        # 用户ID。
        self.user_id = user_id
        # 用户状态。
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListConferenceUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        conference_user_list: List[ListConferenceUsersResponseBodyResultConferenceUserList] = None,
        has_more: bool = None,
        total_count: int = None,
        page_total: int = None,
    ):
        # 会议用户列表。
        self.conference_user_list = conference_user_list
        # 是否还有数据
        self.has_more = has_more
        # 总条目数
        self.total_count = total_count
        # 总页数
        self.page_total = page_total

    def validate(self):
        if self.conference_user_list:
            for k in self.conference_user_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ConferenceUserList'] = []
        if self.conference_user_list is not None:
            for k in self.conference_user_list:
                result['ConferenceUserList'].append(k.to_map() if k else None)
        if self.has_more is not None:
            result['HasMore'] = self.has_more
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.conference_user_list = []
        if m.get('ConferenceUserList') is not None:
            for k in m.get('ConferenceUserList'):
                temp_model = ListConferenceUsersResponseBodyResultConferenceUserList()
                self.conference_user_list.append(temp_model.from_map(k))
        if m.get('HasMore') is not None:
            self.has_more = m.get('HasMore')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        return self


class ListConferenceUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListConferenceUsersResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListConferenceUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListConferenceUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListConferenceUsersResponseBody = None,
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
            temp_model = ListConferenceUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAppTemplatesRequest(TeaModel):
    def __init__(
        self,
        page_number: str = None,
        page_size: str = None,
    ):
        # 查询页码，参数为空默认查询第1页。
        self.page_number = page_number
        # 每页显示个数，参数为空默认显示个数为10。
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class ListAppTemplatesResponseBodyResultAppTemplateInfoListConfigList(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # 配置项
        self.key = key
        # 配置项内容
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListAppTemplatesResponseBodyResultAppTemplateInfoList(TeaModel):
    def __init__(
        self,
        app_template_id: str = None,
        app_template_name: str = None,
        app_template_creator: str = None,
        status: str = None,
        component_list: List[str] = None,
        create_time: str = None,
        sdk_info: str = None,
        config_list: List[ListAppTemplatesResponseBodyResultAppTemplateInfoListConfigList] = None,
    ):
        # 应用模板唯一标识
        self.app_template_id = app_template_id
        # 应用模板名称
        self.app_template_name = app_template_name
        # 应用模板创建者
        self.app_template_creator = app_template_creator
        # 应用模板使用状态
        self.status = status
        # 组件列表
        self.component_list = component_list
        # 创建时间
        self.create_time = create_time
        # SDK信息
        self.sdk_info = sdk_info
        # 配置列表
        self.config_list = config_list

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.app_template_creator is not None:
            result['AppTemplateCreator'] = self.app_template_creator
        if self.status is not None:
            result['Status'] = self.status
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.sdk_info is not None:
            result['SdkInfo'] = self.sdk_info
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('AppTemplateCreator') is not None:
            self.app_template_creator = m.get('AppTemplateCreator')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('SdkInfo') is not None:
            self.sdk_info = m.get('SdkInfo')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = ListAppTemplatesResponseBodyResultAppTemplateInfoListConfigList()
                self.config_list.append(temp_model.from_map(k))
        return self


class ListAppTemplatesResponseBodyResult(TeaModel):
    def __init__(
        self,
        total_count: int = None,
        page_total: int = None,
        app_template_info_list: List[ListAppTemplatesResponseBodyResultAppTemplateInfoList] = None,
    ):
        # 总条目数
        self.total_count = total_count
        # 总页数
        self.page_total = page_total
        # 应用模板信息列表
        self.app_template_info_list = app_template_info_list

    def validate(self):
        if self.app_template_info_list:
            for k in self.app_template_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.page_total is not None:
            result['PageTotal'] = self.page_total
        result['AppTemplateInfoList'] = []
        if self.app_template_info_list is not None:
            for k in self.app_template_info_list:
                result['AppTemplateInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('PageTotal') is not None:
            self.page_total = m.get('PageTotal')
        self.app_template_info_list = []
        if m.get('AppTemplateInfoList') is not None:
            for k in m.get('AppTemplateInfoList'):
                temp_model = ListAppTemplatesResponseBodyResultAppTemplateInfoList()
                self.app_template_info_list.append(temp_model.from_map(k))
        return self


class ListAppTemplatesResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListAppTemplatesResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListAppTemplatesResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListAppTemplatesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListAppTemplatesResponseBody = None,
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
            temp_model = ListAppTemplatesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListComponentsRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_template_id: str = None,
    ):
        # 应用唯一标识
        self.app_id = app_id
        # 应用模板唯一标识
        self.app_template_id = app_template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        return self


class ListComponentsResponseBodyResultComponentCategoryList(TeaModel):
    def __init__(
        self,
        component_type: str = None,
        component_name: str = None,
        in_use: str = None,
    ):
        # 组件类型
        self.component_type = component_type
        # 组件名称
        self.component_name = component_name
        # 是否使用
        self.in_use = in_use

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_type is not None:
            result['ComponentType'] = self.component_type
        if self.component_name is not None:
            result['ComponentName'] = self.component_name
        if self.in_use is not None:
            result['InUse'] = self.in_use
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ComponentType') is not None:
            self.component_type = m.get('ComponentType')
        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')
        if m.get('InUse') is not None:
            self.in_use = m.get('InUse')
        return self


class ListComponentsResponseBodyResultComponentCategory(TeaModel):
    def __init__(
        self,
        type: str = None,
        list: List[ListComponentsResponseBodyResultComponentCategoryList] = None,
    ):
        # 组件类别
        self.type = type
        # 类别下的组件列表
        self.list = list

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
        if self.type is not None:
            result['Type'] = self.type
        result['List'] = []
        if self.list is not None:
            for k in self.list:
                result['List'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        self.list = []
        if m.get('List') is not None:
            for k in m.get('List'):
                temp_model = ListComponentsResponseBodyResultComponentCategoryList()
                self.list.append(temp_model.from_map(k))
        return self


class ListComponentsResponseBodyResultConfigGroup(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
        category: str = None,
    ):
        self.key = key
        self.value = value
        self.category = category

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        if self.category is not None:
            result['Category'] = self.category
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        return self


class ListComponentsResponseBodyResult(TeaModel):
    def __init__(
        self,
        component_category: List[ListComponentsResponseBodyResultComponentCategory] = None,
        config_group: List[ListComponentsResponseBodyResultConfigGroup] = None,
    ):
        # 组件信息
        self.component_category = component_category
        # 配置信息
        self.config_group = config_group

    def validate(self):
        if self.component_category:
            for k in self.component_category:
                if k:
                    k.validate()
        if self.config_group:
            for k in self.config_group:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ComponentCategory'] = []
        if self.component_category is not None:
            for k in self.component_category:
                result['ComponentCategory'].append(k.to_map() if k else None)
        result['ConfigGroup'] = []
        if self.config_group is not None:
            for k in self.config_group:
                result['ConfigGroup'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.component_category = []
        if m.get('ComponentCategory') is not None:
            for k in m.get('ComponentCategory'):
                temp_model = ListComponentsResponseBodyResultComponentCategory()
                self.component_category.append(temp_model.from_map(k))
        self.config_group = []
        if m.get('ConfigGroup') is not None:
            for k in m.get('ConfigGroup'):
                temp_model = ListComponentsResponseBodyResultConfigGroup()
                self.config_group.append(temp_model.from_map(k))
        return self


class ListComponentsResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: ListComponentsResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果体
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = ListComponentsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListComponentsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ListComponentsResponseBody = None,
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
            temp_model = ListComponentsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateLiveRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        title: str = None,
        introduction: str = None,
    ):
        # 直播资源的唯一标识ID
        self.live_id = live_id
        # 直播标题，支持中英文，最大长度256位
        self.title = title
        # 直播简介，支持中英文，最大长度2048位
        self.introduction = introduction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.title is not None:
            result['Title'] = self.title
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        return self


class UpdateLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateLiveResponseBody = None,
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
            temp_model = UpdateLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppTemplateConfigRequestConfigList(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class UpdateAppTemplateConfigRequest(TeaModel):
    def __init__(
        self,
        app_template_id: str = None,
        config_list: List[UpdateAppTemplateConfigRequestConfigList] = None,
    ):
        # 应用模板唯一标识
        self.app_template_id = app_template_id
        # 更新配置
        self.config_list = config_list

    def validate(self):
        if self.config_list:
            for k in self.config_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        result['ConfigList'] = []
        if self.config_list is not None:
            for k in self.config_list:
                result['ConfigList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        self.config_list = []
        if m.get('ConfigList') is not None:
            for k in m.get('ConfigList'):
                temp_model = UpdateAppTemplateConfigRequestConfigList()
                self.config_list.append(temp_model.from_map(k))
        return self


class UpdateAppTemplateConfigShrinkRequest(TeaModel):
    def __init__(
        self,
        app_template_id: str = None,
        config_list_shrink: str = None,
    ):
        # 应用模板唯一标识
        self.app_template_id = app_template_id
        # 更新配置
        self.config_list_shrink = config_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.config_list_shrink is not None:
            result['ConfigList'] = self.config_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('ConfigList') is not None:
            self.config_list_shrink = m.get('ConfigList')
        return self


class UpdateAppTemplateConfigResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppTemplateConfigResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppTemplateConfigResponseBody = None,
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
            temp_model = UpdateAppTemplateConfigResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ApplyLinkMicRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        user_id: str = None,
    ):
        # 会议唯一标识
        self.conference_id = conference_id
        # 申请连麦用户
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ApplyLinkMicResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ApplyLinkMicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: ApplyLinkMicResponseBody = None,
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
            temp_model = ApplyLinkMicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelApplyLinkMicRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        user_id: str = None,
    ):
        # 会议唯一标识
        self.conference_id = conference_id
        # 申请连麦用户
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CancelApplyLinkMicResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CancelApplyLinkMicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CancelApplyLinkMicResponseBody = None,
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
            temp_model = CancelApplyLinkMicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StopLiveRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        user_id: str = None,
        live_id: str = None,
    ):
        # 租户名
        self.app_id = app_id
        # 房间ID，最大长度36位
        self.room_id = room_id
        # 创建直播用户ID
        self.user_id = user_id
        # 直播资源的唯一标识ID
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class StopLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StopLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: StopLiveResponseBody = None,
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
            temp_model = StopLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # 应用唯一标识
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


class GetAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_template_id: str = None,
        app_template_name: str = None,
        app_status: str = None,
        app_key: str = None,
        create_time: str = None,
        component_list: List[str] = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 模板唯一标识
        self.app_template_id = app_template_id
        # 模板名称
        self.app_template_name = app_template_name
        # 应用状态
        self.app_status = app_status
        # 应用Key
        self.app_key = app_key
        # 创建时间
        self.create_time = create_time
        # 组件列表。
        self.component_list = component_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        if self.app_status is not None:
            result['AppStatus'] = self.app_status
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.component_list is not None:
            result['ComponentList'] = self.component_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ComponentList') is not None:
            self.component_list = m.get('ComponentList')
        return self


class GetAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetAppResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetAppResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAppResponseBody = None,
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
            temp_model = GetAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateConferenceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        user_id: str = None,
        title: str = None,
    ):
        # 应用唯一标识，可以包含小写字母、数字，长度为6个字符。
        self.app_id = app_id
        # 房间ID，最大长度36个字符，传空值，则随机生成一个房间ID。
        self.room_id = room_id
        # 创建会议用户。
        self.user_id = user_id
        # 会议标题，支持中英文，最大长度256位。
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class CreateConferenceResponseBodyResult(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
    ):
        # 会议的唯一标识ID。
        self.conference_id = conference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class CreateConferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateConferenceResponseBodyResult = None,
    ):
        # 请求ID。
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateConferenceResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateConferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateConferenceResponseBody = None,
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
            temp_model = CreateConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteLiveRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
    ):
        # 直播资源的唯一标识ID
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class DeleteLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteLiveResponseBody = None,
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
            temp_model = DeleteLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveDomainStatusRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_domain_list: List[str] = None,
    ):
        # 应用唯一标识
        self.app_id = app_id
        # 直播域名列表
        self.live_domain_list = live_domain_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_domain_list is not None:
            result['LiveDomainList'] = self.live_domain_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveDomainList') is not None:
            self.live_domain_list = m.get('LiveDomainList')
        return self


class GetLiveDomainStatusShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        live_domain_list_shrink: str = None,
    ):
        # 应用唯一标识
        self.app_id = app_id
        # 直播域名列表
        self.live_domain_list_shrink = live_domain_list_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.live_domain_list_shrink is not None:
            result['LiveDomainList'] = self.live_domain_list_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('LiveDomainList') is not None:
            self.live_domain_list_shrink = m.get('LiveDomainList')
        return self


class GetLiveDomainStatusResponseBodyResultLiveDomainInfoList(TeaModel):
    def __init__(
        self,
        domain: str = None,
        cname: str = None,
        status: str = None,
    ):
        # 直播域名
        self.domain = domain
        # 直播域名CNAME
        self.cname = cname
        # 直播域名状态
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.cname is not None:
            result['Cname'] = self.cname
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('Cname') is not None:
            self.cname = m.get('Cname')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetLiveDomainStatusResponseBodyResult(TeaModel):
    def __init__(
        self,
        live_domain_info_list: List[GetLiveDomainStatusResponseBodyResultLiveDomainInfoList] = None,
    ):
        # 直播域名信息列表
        self.live_domain_info_list = live_domain_info_list

    def validate(self):
        if self.live_domain_info_list:
            for k in self.live_domain_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['LiveDomainInfoList'] = []
        if self.live_domain_info_list is not None:
            for k in self.live_domain_info_list:
                result['LiveDomainInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.live_domain_info_list = []
        if m.get('LiveDomainInfoList') is not None:
            for k in m.get('LiveDomainInfoList'):
                temp_model = GetLiveDomainStatusResponseBodyResultLiveDomainInfoList()
                self.live_domain_info_list.append(temp_model.from_map(k))
        return self


class GetLiveDomainStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetLiveDomainStatusResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetLiveDomainStatusResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveDomainStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLiveDomainStatusResponseBody = None,
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
            temp_model = GetLiveDomainStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomMessageToAllRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        body: str = None,
    ):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id
        # 消息体内容。
        self.body = body

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.body is not None:
            result['Body'] = self.body
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        return self


class SendCustomMessageToAllResponseBodyResult(TeaModel):
    def __init__(
        self,
        message_id: str = None,
    ):
        # 消息的唯一ID标识。由数字、大小写字母组成，长度不超过20。
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


class SendCustomMessageToAllResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: SendCustomMessageToAllResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        # API请求的返回结果结构体。
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = SendCustomMessageToAllResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCustomMessageToAllResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendCustomMessageToAllResponseBody = None,
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
            temp_model = SendCustomMessageToAllResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AgreeLinkMicRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        to_user_id: str = None,
        from_user_id: str = None,
    ):
        # 会议唯一标识
        self.conference_id = conference_id
        # 被同意用户ID
        self.to_user_id = to_user_id
        # 同意者用户ID
        self.from_user_id = from_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.to_user_id is not None:
            result['ToUserId'] = self.to_user_id
        if self.from_user_id is not None:
            result['FromUserId'] = self.from_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('ToUserId') is not None:
            self.to_user_id = m.get('ToUserId')
        if m.get('FromUserId') is not None:
            self.from_user_id = m.get('FromUserId')
        return self


class AgreeLinkMicResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AgreeLinkMicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: AgreeLinkMicResponseBody = None,
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
            temp_model = AgreeLinkMicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainOwnerVerifyContentRequest(TeaModel):
    def __init__(
        self,
        live_domain_name: str = None,
    ):
        # 直播域名
        self.live_domain_name = live_domain_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_domain_name is not None:
            result['LiveDomainName'] = self.live_domain_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveDomainName') is not None:
            self.live_domain_name = m.get('LiveDomainName')
        return self


class GetDomainOwnerVerifyContentResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
    ):
        # 域名归属校验内容
        self.content = content

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        return self


class GetDomainOwnerVerifyContentResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetDomainOwnerVerifyContentResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetDomainOwnerVerifyContentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDomainOwnerVerifyContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetDomainOwnerVerifyContentResponseBody = None,
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
            temp_model = GetDomainOwnerVerifyContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendCustomMessageToUsersRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        body: str = None,
        receiver_list: List[str] = None,
    ):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id
        # 房间唯一标识，由调用CreateRoom返回。
        self.room_id = room_id
        # 消息体内容。
        self.body = body
        # 消息指定的接收人ID列表。
        self.receiver_list = receiver_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.body is not None:
            result['Body'] = self.body
        if self.receiver_list is not None:
            result['ReceiverList'] = self.receiver_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Body') is not None:
            self.body = m.get('Body')
        if m.get('ReceiverList') is not None:
            self.receiver_list = m.get('ReceiverList')
        return self


class SendCustomMessageToUsersResponseBodyResult(TeaModel):
    def __init__(
        self,
        message_id: str = None,
    ):
        # 消息的唯一ID标识。由数字、大小写字母组成，长度不超过20。
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


class SendCustomMessageToUsersResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: SendCustomMessageToUsersResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        # API请求的返回结果结构体。
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = SendCustomMessageToUsersResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class SendCustomMessageToUsersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: SendCustomMessageToUsersResponseBody = None,
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
            temp_model = SendCustomMessageToUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAuthTokenRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        user_id: str = None,
        app_key: str = None,
        device_id: str = None,
    ):
        # 用户的应用ID，在控制台创建应用时生成
        self.app_id = app_id
        # 用户UserId,在AppId下单独唯一
        self.user_id = user_id
        # 终端设备类型,通过控制台创建和查询
        self.app_key = app_key
        # 终端设备ID
        self.device_id = device_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        return self


class GetAuthTokenResponseBodyResult(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        refresh_token: str = None,
        access_token_expired_time: int = None,
    ):
        # 用于长链接建连的token
        self.access_token = access_token
        # 更新Token，若AccessToken过期，则可以使用RefreshToken再次获取新Token
        self.refresh_token = refresh_token
        # 登录token过期时间(毫秒)
        self.access_token_expired_time = access_token_expired_time

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

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


class GetAuthTokenResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetAuthTokenResponseBodyResult = None,
    ):
        # Id of the request
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetAuthTokenResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAuthTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetAuthTokenResponseBody = None,
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
            temp_model = GetAuthTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppTemplateRequest(TeaModel):
    def __init__(
        self,
        app_template_id: str = None,
        app_template_name: str = None,
    ):
        # 应用模板唯一标识
        self.app_template_id = app_template_id
        # 应用模板名称
        self.app_template_name = app_template_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        if self.app_template_name is not None:
            result['AppTemplateName'] = self.app_template_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        if m.get('AppTemplateName') is not None:
            self.app_template_name = m.get('AppTemplateName')
        return self


class UpdateAppTemplateResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppTemplateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppTemplateResponseBody = None,
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
            temp_model = UpdateAppTemplateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetImpProductStatusResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: bool = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 开通状态
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
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetImpProductStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetImpProductStatusResponseBody = None,
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
            temp_model = GetImpProductStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PublishLiveRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        user_id: str = None,
    ):
        # 直播资源的唯一标识ID
        self.live_id = live_id
        # 当前用户Id
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class PublishLiveResponseBodyResult(TeaModel):
    def __init__(
        self,
        live_id: str = None,
        anchor_id: str = None,
        status: str = None,
        push_url: str = None,
        live_url: str = None,
    ):
        # 直播资源的唯一标识ID
        self.live_id = live_id
        # 主播ID
        self.anchor_id = anchor_id
        # 直播状态：Created-已创建未开播，Living-直播中，End-直播结束
        self.status = status
        # 直播推流地址
        self.push_url = push_url
        # 直播拉流地址
        self.live_url = live_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.status is not None:
            result['Status'] = self.status
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        return self


class PublishLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: PublishLiveResponseBodyResult = None,
    ):
        # Id of the request
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = PublishLiveResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class PublishLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: PublishLiveResponseBody = None,
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
            temp_model = PublishLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLiveRequest(TeaModel):
    def __init__(
        self,
        live_id: str = None,
    ):
        # 直播资源的唯一标识ID
        self.live_id = live_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        return self


class GetLiveResponseBodyResultPlayUrlInfoList(TeaModel):
    def __init__(
        self,
        code_level: int = None,
        flv_url: str = None,
        hls_url: str = None,
        rtmp_url: str = None,
    ):
        # 直播拉取分辨率 -1:lld 1:lsd 2:lhd 3:lud
        self.code_level = code_level
        # flv拉流地址
        self.flv_url = flv_url
        # hls拉流地址
        self.hls_url = hls_url
        # rtmp拉流地址
        self.rtmp_url = rtmp_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code_level is not None:
            result['CodeLevel'] = self.code_level
        if self.flv_url is not None:
            result['FlvUrl'] = self.flv_url
        if self.hls_url is not None:
            result['HlsUrl'] = self.hls_url
        if self.rtmp_url is not None:
            result['RtmpUrl'] = self.rtmp_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeLevel') is not None:
            self.code_level = m.get('CodeLevel')
        if m.get('FlvUrl') is not None:
            self.flv_url = m.get('FlvUrl')
        if m.get('HlsUrl') is not None:
            self.hls_url = m.get('HlsUrl')
        if m.get('RtmpUrl') is not None:
            self.rtmp_url = m.get('RtmpUrl')
        return self


class GetLiveResponseBodyResult(TeaModel):
    def __init__(
        self,
        anchor_id: str = None,
        live_id: str = None,
        title: str = None,
        playback_url: str = None,
        create_time: int = None,
        end_time: int = None,
        duration: int = None,
        push_url: str = None,
        live_url: str = None,
        status: str = None,
        introduction: str = None,
        room_id: str = None,
        app_id: str = None,
        user_id: str = None,
        code_level: int = None,
        play_url_info_list: List[GetLiveResponseBodyResultPlayUrlInfoList] = None,
    ):
        # 主播ID
        self.anchor_id = anchor_id
        # 直播资源的唯一标识ID
        self.live_id = live_id
        # 直播标题
        self.title = title
        # 直播回放地址
        self.playback_url = playback_url
        # 直播创建时间（毫秒ms）
        self.create_time = create_time
        # 直播结束时间（毫秒ms）
        self.end_time = end_time
        # 直播持续时间（毫秒ms）
        self.duration = duration
        # 直播推流地址
        self.push_url = push_url
        # 直播拉流地址
        self.live_url = live_url
        # 直播状态：Created-已创建，未开播，Living-直播中，End-直播结束
        self.status = status
        # 直播简介
        self.introduction = introduction
        # 房间id
        self.room_id = room_id
        # 租户名
        self.app_id = app_id
        # 创建直播用户
        self.user_id = user_id
        # 直播推送分辨率 -1:lld 1:lsd 2:lhd 3:lud
        self.code_level = code_level
        # 多分辨率多协议播放信息
        self.play_url_info_list = play_url_info_list

    def validate(self):
        if self.play_url_info_list:
            for k in self.play_url_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.anchor_id is not None:
            result['AnchorId'] = self.anchor_id
        if self.live_id is not None:
            result['LiveId'] = self.live_id
        if self.title is not None:
            result['Title'] = self.title
        if self.playback_url is not None:
            result['PlaybackUrl'] = self.playback_url
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.end_time is not None:
            result['EndTime'] = self.end_time
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.push_url is not None:
            result['PushUrl'] = self.push_url
        if self.live_url is not None:
            result['LiveUrl'] = self.live_url
        if self.status is not None:
            result['Status'] = self.status
        if self.introduction is not None:
            result['Introduction'] = self.introduction
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.code_level is not None:
            result['CodeLevel'] = self.code_level
        result['PlayUrlInfoList'] = []
        if self.play_url_info_list is not None:
            for k in self.play_url_info_list:
                result['PlayUrlInfoList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AnchorId') is not None:
            self.anchor_id = m.get('AnchorId')
        if m.get('LiveId') is not None:
            self.live_id = m.get('LiveId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('PlaybackUrl') is not None:
            self.playback_url = m.get('PlaybackUrl')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('PushUrl') is not None:
            self.push_url = m.get('PushUrl')
        if m.get('LiveUrl') is not None:
            self.live_url = m.get('LiveUrl')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Introduction') is not None:
            self.introduction = m.get('Introduction')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('CodeLevel') is not None:
            self.code_level = m.get('CodeLevel')
        self.play_url_info_list = []
        if m.get('PlayUrlInfoList') is not None:
            for k in m.get('PlayUrlInfoList'):
                temp_model = GetLiveResponseBodyResultPlayUrlInfoList()
                self.play_url_info_list.append(temp_model.from_map(k))
        return self


class GetLiveResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: GetLiveResponseBodyResult = None,
    ):
        # Id of the request
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetLiveResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetLiveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: GetLiveResponseBody = None,
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
            temp_model = GetLiveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
    ):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位。
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class DeleteRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteRoomResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteRoomResponseBody = None,
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
            temp_model = DeleteRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAppRequest(TeaModel):
    def __init__(
        self,
        app_name: str = None,
        app_template_id: str = None,
    ):
        # 应用名称
        self.app_name = app_name
        # 模板ID
        self.app_template_id = app_template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_name is not None:
            result['AppName'] = self.app_name
        if self.app_template_id is not None:
            result['AppTemplateId'] = self.app_template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppTemplateId') is not None:
            self.app_template_id = m.get('AppTemplateId')
        return self


class CreateAppResponseBodyResult(TeaModel):
    def __init__(
        self,
        app_id: str = None,
    ):
        # 应用唯一标示
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


class CreateAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateAppResponseBodyResult = None,
    ):
        # 请求ID
        self.request_id = request_id
        # 返回结果
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateAppResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CreateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: CreateAppResponseBody = None,
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
            temp_model = CreateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateRoomRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        template_id: str = None,
        room_id: str = None,
        title: str = None,
        notice: str = None,
        room_owner_id: str = None,
        extension: Dict[str, str] = None,
    ):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id
        # 房间模板唯一标识，当前支持的取值：default，传空默认为default。
        self.template_id = template_id
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位，传空则随机生成一个房间id。
        self.room_id = room_id
        # 房间标题，支持中英文，最大长度32位。
        self.title = title
        # 房间公告，支持中英文，最大长度256位。
        self.notice = notice
        # 房主用户id，仅支持英文和数字，最大长度36位。
        self.room_owner_id = room_owner_id
        # 拓展字段，按需传递，需要额外记录的房间属性。
        self.extension = extension

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.extension is not None:
            result['Extension'] = self.extension
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Extension') is not None:
            self.extension = m.get('Extension')
        return self


class CreateRoomShrinkRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        template_id: str = None,
        room_id: str = None,
        title: str = None,
        notice: str = None,
        room_owner_id: str = None,
        extension_shrink: str = None,
    ):
        # 应用唯一标识，由6位小写字母、数字组成。
        self.app_id = app_id
        # 房间模板唯一标识，当前支持的取值：default，传空默认为default。
        self.template_id = template_id
        # 房间唯一标识，由字母、数字、符号.和-组成，最大长度36位，传空则随机生成一个房间id。
        self.room_id = room_id
        # 房间标题，支持中英文，最大长度32位。
        self.title = title
        # 房间公告，支持中英文，最大长度256位。
        self.notice = notice
        # 房主用户id，仅支持英文和数字，最大长度36位。
        self.room_owner_id = room_owner_id
        # 拓展字段，按需传递，需要额外记录的房间属性。
        self.extension_shrink = extension_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.template_id is not None:
            result['TemplateId'] = self.template_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.title is not None:
            result['Title'] = self.title
        if self.notice is not None:
            result['Notice'] = self.notice
        if self.room_owner_id is not None:
            result['RoomOwnerId'] = self.room_owner_id
        if self.extension_shrink is not None:
            result['Extension'] = self.extension_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Notice') is not None:
            self.notice = m.get('Notice')
        if m.get('RoomOwnerId') is not None:
            self.room_owner_id = m.get('RoomOwnerId')
        if m.get('Extension') is not None:
            self.extension_shrink = m.get('Extension')
        return self


class CreateRoomResponseBodyResult(TeaModel):
    def __init__(
        self,
        room_id: str = None,
    ):
        # 房间id
        self.room_id = room_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        return self


class CreateRoomResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        result: CreateRoomResponseBodyResult = None,
    ):
        # Id of the request
        self.request_id = request_id
        # API请求的返回结果结构体。
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = CreateRoomResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
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
            temp_model = CreateRoomResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateConferenceRequest(TeaModel):
    def __init__(
        self,
        conference_id: str = None,
        title: str = None,
    ):
        # 会议唯一标识
        self.conference_id = conference_id
        # 会议标题
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class UpdateConferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateConferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateConferenceResponseBody = None,
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
            temp_model = UpdateConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteConferenceRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        room_id: str = None,
        user_id: str = None,
        conference_id: str = None,
    ):
        # 租户名
        self.app_id = app_id
        # 房间ID，最大长度36位
        self.room_id = room_id
        # 创建会议用户ID
        self.user_id = user_id
        # 会议资源的唯一标识ID
        self.conference_id = conference_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['AppId'] = self.app_id
        if self.room_id is not None:
            result['RoomId'] = self.room_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.conference_id is not None:
            result['ConferenceId'] = self.conference_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('RoomId') is not None:
            self.room_id = m.get('RoomId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('ConferenceId') is not None:
            self.conference_id = m.get('ConferenceId')
        return self


class DeleteConferenceResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteConferenceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: DeleteConferenceResponseBody = None,
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
            temp_model = DeleteConferenceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAppRequest(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_status: str = None,
    ):
        # 应用唯一标识
        self.app_id = app_id
        # 应用名称
        self.app_name = app_name
        # 应用状态
        self.app_status = app_status

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')
        if m.get('AppStatus') is not None:
            self.app_status = m.get('AppStatus')
        return self


class UpdateAppResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        # 请求ID
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class UpdateAppResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        body: UpdateAppResponseBody = None,
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
            temp_model = UpdateAppResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



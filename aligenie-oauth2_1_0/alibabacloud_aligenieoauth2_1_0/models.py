# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class CreatePlayingListRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.id_type = id_type
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class CreatePlayingListRequestOpenCreatePlayingListRequestContentList(TeaModel):
    def __init__(
        self,
        raw_id: str = None,
        source: str = None,
    ):
        # This parameter is required.
        self.raw_id = raw_id
        # This parameter is required.
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class CreatePlayingListRequestOpenCreatePlayingListRequest(TeaModel):
    def __init__(
        self,
        content_list: List[CreatePlayingListRequestOpenCreatePlayingListRequestContentList] = None,
        content_type: str = None,
        extend_info: Dict[str, Any] = None,
        index: int = None,
        need_album_continued: bool = None,
        play_from: str = None,
        play_mode: str = None,
    ):
        # This parameter is required.
        self.content_list = content_list
        # This parameter is required.
        self.content_type = content_type
        self.extend_info = extend_info
        self.index = index
        self.need_album_continued = need_album_continued
        self.play_from = play_from
        self.play_mode = play_mode

    def validate(self):
        if self.content_list:
            for k in self.content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ContentList'] = []
        if self.content_list is not None:
            for k in self.content_list:
                result['ContentList'].append(k.to_map() if k else None)
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.index is not None:
            result['Index'] = self.index
        if self.need_album_continued is not None:
            result['NeedAlbumContinued'] = self.need_album_continued
        if self.play_from is not None:
            result['PlayFrom'] = self.play_from
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.content_list = []
        if m.get('ContentList') is not None:
            for k in m.get('ContentList'):
                temp_model = CreatePlayingListRequestOpenCreatePlayingListRequestContentList()
                self.content_list.append(temp_model.from_map(k))
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('NeedAlbumContinued') is not None:
            self.need_album_continued = m.get('NeedAlbumContinued')
        if m.get('PlayFrom') is not None:
            self.play_from = m.get('PlayFrom')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        return self


class CreatePlayingListRequest(TeaModel):
    def __init__(
        self,
        device_info: CreatePlayingListRequestDeviceInfo = None,
        open_create_playing_list_request: CreatePlayingListRequestOpenCreatePlayingListRequest = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.open_create_playing_list_request = open_create_playing_list_request

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_create_playing_list_request:
            self.open_create_playing_list_request.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_create_playing_list_request is not None:
            result['OpenCreatePlayingListRequest'] = self.open_create_playing_list_request.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = CreatePlayingListRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenCreatePlayingListRequest') is not None:
            temp_model = CreatePlayingListRequestOpenCreatePlayingListRequest()
            self.open_create_playing_list_request = temp_model.from_map(m['OpenCreatePlayingListRequest'])
        return self


class CreatePlayingListShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        open_create_playing_list_request_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.open_create_playing_list_request_shrink = open_create_playing_list_request_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_create_playing_list_request_shrink is not None:
            result['OpenCreatePlayingListRequest'] = self.open_create_playing_list_request_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenCreatePlayingListRequest') is not None:
            self.open_create_playing_list_request_shrink = m.get('OpenCreatePlayingListRequest')
        return self


class CreatePlayingListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class CreatePlayingListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePlayingListResponseBody = None,
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
            temp_model = CreatePlayingListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ExecuteSceneRequest(TeaModel):
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


class ExecuteSceneResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
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


class ExecuteSceneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ExecuteSceneResponseBody = None,
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
            temp_model = ExecuteSceneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetSceneListResponseBodySceneList(TeaModel):
    def __init__(
        self,
        scene_id: str = None,
        scene_name: str = None,
    ):
        self.scene_id = scene_id
        self.scene_name = scene_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_id is not None:
            result['SceneId'] = self.scene_id
        if self.scene_name is not None:
            result['SceneName'] = self.scene_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneId') is not None:
            self.scene_id = m.get('SceneId')
        if m.get('SceneName') is not None:
            self.scene_name = m.get('SceneName')
        return self


class GetSceneListResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        scene_list: List[GetSceneListResponseBodySceneList] = None,
    ):
        self.request_id = request_id
        self.scene_list = scene_list

    def validate(self):
        if self.scene_list:
            for k in self.scene_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SceneList'] = []
        if self.scene_list is not None:
            for k in self.scene_list:
                result['SceneList'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.scene_list = []
        if m.get('SceneList') is not None:
            for k in m.get('SceneList'):
                temp_model = GetSceneListResponseBodySceneList()
                self.scene_list.append(temp_model.from_map(k))
        return self


class GetSceneListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetSceneListResponseBody = None,
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
            temp_model = GetSceneListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserBasicInfoResponseBodyUnionIds(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        union_id: str = None,
    ):
        self.organization_id = organization_id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.union_id is not None:
            result['UnionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')
        return self


class GetUserBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        avatar_url: str = None,
        nickname: str = None,
        open_id: str = None,
        request_id: str = None,
        union_ids: List[GetUserBasicInfoResponseBodyUnionIds] = None,
    ):
        self.avatar_url = avatar_url
        self.nickname = nickname
        self.open_id = open_id
        self.request_id = request_id
        self.union_ids = union_ids

    def validate(self):
        if self.union_ids:
            for k in self.union_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar_url is not None:
            result['AvatarUrl'] = self.avatar_url
        if self.nickname is not None:
            result['Nickname'] = self.nickname
        if self.open_id is not None:
            result['OpenId'] = self.open_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['UnionIds'] = []
        if self.union_ids is not None:
            for k in self.union_ids:
                result['UnionIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvatarUrl') is not None:
            self.avatar_url = m.get('AvatarUrl')
        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')
        if m.get('OpenId') is not None:
            self.open_id = m.get('OpenId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.union_ids = []
        if m.get('UnionIds') is not None:
            for k in m.get('UnionIds'):
                temp_model = GetUserBasicInfoResponseBodyUnionIds()
                self.union_ids.append(temp_model.from_map(k))
        return self


class GetUserBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserBasicInfoResponseBody = None,
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
            temp_model = GetUserBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserPhoneResponseBody(TeaModel):
    def __init__(
        self,
        phone: str = None,
        request_id: str = None,
    ):
        self.phone = phone
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone is not None:
            result['Phone'] = self.phone
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Phone') is not None:
            self.phone = m.get('Phone')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetUserPhoneResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserPhoneResponseBody = None,
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
            temp_model = GetUserPhoneResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OAuth2RevocationEndpointHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class OAuth2RevocationEndpointRequest(TeaModel):
    def __init__(
        self,
        token: str = None,
        token_type_hint: str = None,
    ):
        self.token = token
        self.token_type_hint = token_type_hint

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.token is not None:
            result['Token'] = self.token
        if self.token_type_hint is not None:
            result['TokenTypeHint'] = self.token_type_hint
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Token') is not None:
            self.token = m.get('Token')
        if m.get('TokenTypeHint') is not None:
            self.token_type_hint = m.get('TokenTypeHint')
        return self


class OAuth2RevocationEndpointResponseBody(TeaModel):
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


class OAuth2RevocationEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OAuth2RevocationEndpointResponseBody = None,
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
            temp_model = OAuth2RevocationEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class OAuth2TokenEndpointHeaders(TeaModel):
    def __init__(
        self,
        common_headers: Dict[str, str] = None,
        x_acs_aligenie_access_token: str = None,
        authorization: str = None,
    ):
        self.common_headers = common_headers
        self.x_acs_aligenie_access_token = x_acs_aligenie_access_token
        self.authorization = authorization

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.common_headers is not None:
            result['commonHeaders'] = self.common_headers
        if self.x_acs_aligenie_access_token is not None:
            result['x-acs-aligenie-access-token'] = self.x_acs_aligenie_access_token
        if self.authorization is not None:
            result['Authorization'] = self.authorization
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('commonHeaders') is not None:
            self.common_headers = m.get('commonHeaders')
        if m.get('x-acs-aligenie-access-token') is not None:
            self.x_acs_aligenie_access_token = m.get('x-acs-aligenie-access-token')
        if m.get('Authorization') is not None:
            self.authorization = m.get('Authorization')
        return self


class OAuth2TokenEndpointRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        grant_type: str = None,
        redirect_uri: str = None,
        refresh_token: str = None,
    ):
        self.code = code
        self.grant_type = grant_type
        self.redirect_uri = redirect_uri
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.grant_type is not None:
            result['GrantType'] = self.grant_type
        if self.redirect_uri is not None:
            result['RedirectUri'] = self.redirect_uri
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('GrantType') is not None:
            self.grant_type = m.get('GrantType')
        if m.get('RedirectUri') is not None:
            self.redirect_uri = m.get('RedirectUri')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        return self


class OAuth2TokenEndpointResponseBody(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        expires_in: int = None,
        refresh_token: str = None,
        request_id: str = None,
        scope: str = None,
        token_type: str = None,
    ):
        self.access_token = access_token
        self.expires_in = expires_in
        self.refresh_token = refresh_token
        self.request_id = request_id
        self.scope = scope
        self.token_type = token_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['AccessToken'] = self.access_token
        if self.expires_in is not None:
            result['ExpiresIn'] = self.expires_in
        if self.refresh_token is not None:
            result['RefreshToken'] = self.refresh_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.scope is not None:
            result['Scope'] = self.scope
        if self.token_type is not None:
            result['TokenType'] = self.token_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessToken') is not None:
            self.access_token = m.get('AccessToken')
        if m.get('ExpiresIn') is not None:
            self.expires_in = m.get('ExpiresIn')
        if m.get('RefreshToken') is not None:
            self.refresh_token = m.get('RefreshToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Scope') is not None:
            self.scope = m.get('Scope')
        if m.get('TokenType') is not None:
            self.token_type = m.get('TokenType')
        return self


class OAuth2TokenEndpointResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: OAuth2TokenEndpointResponseBody = None,
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
            temp_model = OAuth2TokenEndpointResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushDeviceNotificationRequestTenantInfo(TeaModel):
    def __init__(
        self,
        subject_id: str = None,
    ):
        self.subject_id = subject_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.subject_id is not None:
            result['SubjectId'] = self.subject_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubjectId') is not None:
            self.subject_id = m.get('SubjectId')
        return self


class PushDeviceNotificationRequestBodySendTarget(TeaModel):
    def __init__(
        self,
        target_identity: str = None,
        target_type: str = None,
    ):
        self.target_identity = target_identity
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.target_identity is not None:
            result['TargetIdentity'] = self.target_identity
        if self.target_type is not None:
            result['TargetType'] = self.target_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetIdentity') is not None:
            self.target_identity = m.get('TargetIdentity')
        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')
        return self


class PushDeviceNotificationRequestBody(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        is_debug: bool = None,
        message_template_id: str = None,
        organization_id: str = None,
        place_holder: Dict[str, str] = None,
        send_target: PushDeviceNotificationRequestBodySendTarget = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        self.is_debug = is_debug
        # This parameter is required.
        self.message_template_id = message_template_id
        self.organization_id = organization_id
        self.place_holder = place_holder
        # This parameter is required.
        self.send_target = send_target

    def validate(self):
        if self.send_target:
            self.send_target.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.is_debug is not None:
            result['IsDebug'] = self.is_debug
        if self.message_template_id is not None:
            result['MessageTemplateId'] = self.message_template_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.place_holder is not None:
            result['PlaceHolder'] = self.place_holder
        if self.send_target is not None:
            result['SendTarget'] = self.send_target.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IsDebug') is not None:
            self.is_debug = m.get('IsDebug')
        if m.get('MessageTemplateId') is not None:
            self.message_template_id = m.get('MessageTemplateId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('PlaceHolder') is not None:
            self.place_holder = m.get('PlaceHolder')
        if m.get('SendTarget') is not None:
            temp_model = PushDeviceNotificationRequestBodySendTarget()
            self.send_target = temp_model.from_map(m['SendTarget'])
        return self


class PushDeviceNotificationRequest(TeaModel):
    def __init__(
        self,
        tenant_info: PushDeviceNotificationRequestTenantInfo = None,
        body: PushDeviceNotificationRequestBody = None,
    ):
        self.tenant_info = tenant_info
        self.body = body

    def validate(self):
        if self.tenant_info:
            self.tenant_info.validate()
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_info is not None:
            result['TenantInfo'] = self.tenant_info.to_map()
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantInfo') is not None:
            temp_model = PushDeviceNotificationRequestTenantInfo()
            self.tenant_info = temp_model.from_map(m['TenantInfo'])
        if m.get('body') is not None:
            temp_model = PushDeviceNotificationRequestBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PushDeviceNotificationShrinkRequest(TeaModel):
    def __init__(
        self,
        tenant_info_shrink: str = None,
        body_shrink: str = None,
    ):
        self.tenant_info_shrink = tenant_info_shrink
        self.body_shrink = body_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tenant_info_shrink is not None:
            result['TenantInfo'] = self.tenant_info_shrink
        if self.body_shrink is not None:
            result['body'] = self.body_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TenantInfo') is not None:
            self.tenant_info_shrink = m.get('TenantInfo')
        if m.get('body') is not None:
            self.body_shrink = m.get('body')
        return self


class PushDeviceNotificationResponseBody(TeaModel):
    def __init__(
        self,
        request_id: str = None,
    ):
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class PushDeviceNotificationResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PushDeviceNotificationResponseBody = None,
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
            temp_model = PushDeviceNotificationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryDeviceListResponseBodyDeviceListDeviceUnionIds(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        union_id: str = None,
    ):
        self.organization_id = organization_id
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.union_id is not None:
            result['UnionId'] = self.union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')
        return self


class QueryDeviceListResponseBodyDeviceList(TeaModel):
    def __init__(
        self,
        device_icon_url: str = None,
        device_name: str = None,
        device_open_id: str = None,
        device_union_ids: List[QueryDeviceListResponseBodyDeviceListDeviceUnionIds] = None,
        online: str = None,
    ):
        self.device_icon_url = device_icon_url
        self.device_name = device_name
        self.device_open_id = device_open_id
        self.device_union_ids = device_union_ids
        self.online = online

    def validate(self):
        if self.device_union_ids:
            for k in self.device_union_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_icon_url is not None:
            result['DeviceIconUrl'] = self.device_icon_url
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k in self.device_union_ids:
                result['DeviceUnionIds'].append(k.to_map() if k else None)
        if self.online is not None:
            result['Online'] = self.online
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIconUrl') is not None:
            self.device_icon_url = m.get('DeviceIconUrl')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k in m.get('DeviceUnionIds'):
                temp_model = QueryDeviceListResponseBodyDeviceListDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k))
        if m.get('Online') is not None:
            self.online = m.get('Online')
        return self


class QueryDeviceListResponseBody(TeaModel):
    def __init__(
        self,
        device_list: List[QueryDeviceListResponseBodyDeviceList] = None,
        encode_key: str = None,
        encode_type: str = None,
        request_id: str = None,
    ):
        self.device_list = device_list
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.request_id = request_id

    def validate(self):
        if self.device_list:
            for k in self.device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DeviceList'] = []
        if self.device_list is not None:
            for k in self.device_list:
                result['DeviceList'].append(k.to_map() if k else None)
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.device_list = []
        if m.get('DeviceList') is not None:
            for k in m.get('DeviceList'):
                temp_model = QueryDeviceListResponseBodyDeviceList()
                self.device_list.append(temp_model.from_map(k))
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class QueryDeviceListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryDeviceListResponseBody = None,
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
            temp_model = QueryDeviceListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class LoginStateInfo(TeaModel):
    def __init__(
        self,
        scene_code: str = None,
        third_user_identifier: str = None,
        third_user_type: str = None,
        user_id: str = None,
    ):
        self.scene_code = scene_code
        self.third_user_identifier = third_user_identifier
        self.third_user_type = third_user_type
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.third_user_identifier is not None:
            result['ThirdUserIdentifier'] = self.third_user_identifier
        if self.third_user_type is not None:
            result['ThirdUserType'] = self.third_user_type
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('ThirdUserIdentifier') is not None:
            self.third_user_identifier = m.get('ThirdUserIdentifier')
        if m.get('ThirdUserType') is not None:
            self.third_user_type = m.get('ThirdUserType')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ResultValueDeviceUnionIds(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        device_union_id: str = None,
    ):
        self.organization_id = organization_id
        self.device_union_id = device_union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')
        return self


class ResultValue(TeaModel):
    def __init__(
        self,
        device_open_id: str = None,
        device_union_ids: List[ResultValueDeviceUnionIds] = None,
        name: str = None,
        firmware_version: str = None,
        mac: str = None,
        sn: str = None,
    ):
        self.device_open_id = device_open_id
        self.device_union_ids = device_union_ids
        self.name = name
        self.firmware_version = firmware_version
        self.mac = mac
        self.sn = sn

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
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k in self.device_union_ids:
                result['DeviceUnionIds'].append(k.to_map() if k else None)
        if self.name is not None:
            result['Name'] = self.name
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k in m.get('DeviceUnionIds'):
                temp_model = ResultValueDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k))
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class AddAndRemoveFavoriteContentHeaders(TeaModel):
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


class AddAndRemoveFavoriteContentRequestDeviceInfo(TeaModel):
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


class AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequestOpenSourceRawIdPair(TeaModel):
    def __init__(
        self,
        extend_info: Dict[str, Any] = None,
        raw_id: str = None,
        source: str = None,
    ):
        self.extend_info = extend_info
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
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        return self


class AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequest(TeaModel):
    def __init__(
        self,
        favorite_cmd: str = None,
        open_source_raw_id_pair: AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequestOpenSourceRawIdPair = None,
        package_type: str = None,
    ):
        # This parameter is required.
        self.favorite_cmd = favorite_cmd
        # This parameter is required.
        self.open_source_raw_id_pair = open_source_raw_id_pair
        # This parameter is required.
        self.package_type = package_type

    def validate(self):
        if self.open_source_raw_id_pair:
            self.open_source_raw_id_pair.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.favorite_cmd is not None:
            result['FavoriteCmd'] = self.favorite_cmd
        if self.open_source_raw_id_pair is not None:
            result['OpenSourceRawIdPair'] = self.open_source_raw_id_pair.to_map()
        if self.package_type is not None:
            result['PackageType'] = self.package_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FavoriteCmd') is not None:
            self.favorite_cmd = m.get('FavoriteCmd')
        if m.get('OpenSourceRawIdPair') is not None:
            temp_model = AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequestOpenSourceRawIdPair()
            self.open_source_raw_id_pair = temp_model.from_map(m['OpenSourceRawIdPair'])
        if m.get('PackageType') is not None:
            self.package_type = m.get('PackageType')
        return self


class AddAndRemoveFavoriteContentRequestUserInfo(TeaModel):
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


class AddAndRemoveFavoriteContentRequest(TeaModel):
    def __init__(
        self,
        device_info: AddAndRemoveFavoriteContentRequestDeviceInfo = None,
        open_add_and_remove_favorite_content_request: AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequest = None,
        user_info: AddAndRemoveFavoriteContentRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.open_add_and_remove_favorite_content_request = open_add_and_remove_favorite_content_request
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_add_and_remove_favorite_content_request:
            self.open_add_and_remove_favorite_content_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_add_and_remove_favorite_content_request is not None:
            result['OpenAddAndRemoveFavoriteContentRequest'] = self.open_add_and_remove_favorite_content_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = AddAndRemoveFavoriteContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenAddAndRemoveFavoriteContentRequest') is not None:
            temp_model = AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequest()
            self.open_add_and_remove_favorite_content_request = temp_model.from_map(m['OpenAddAndRemoveFavoriteContentRequest'])
        if m.get('UserInfo') is not None:
            temp_model = AddAndRemoveFavoriteContentRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class AddAndRemoveFavoriteContentShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        open_add_and_remove_favorite_content_request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.open_add_and_remove_favorite_content_request_shrink = open_add_and_remove_favorite_content_request_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_add_and_remove_favorite_content_request_shrink is not None:
            result['OpenAddAndRemoveFavoriteContentRequest'] = self.open_add_and_remove_favorite_content_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenAddAndRemoveFavoriteContentRequest') is not None:
            self.open_add_and_remove_favorite_content_request_shrink = m.get('OpenAddAndRemoveFavoriteContentRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class AddAndRemoveFavoriteContentResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AddAndRemoveFavoriteContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddAndRemoveFavoriteContentResponseBody = None,
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
            temp_model = AddAndRemoveFavoriteContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddSubHeaders(TeaModel):
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


class AddSubRequestAddSubscriptionInfoRequestScheduleInfo(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class AddSubRequestAddSubscriptionInfoRequest(TeaModel):
    def __init__(
        self,
        album_id: str = None,
        daily_study_cnt: int = None,
        play_mode: str = None,
        schedule_info: AddSubRequestAddSubscriptionInfoRequestScheduleInfo = None,
    ):
        self.album_id = album_id
        self.daily_study_cnt = daily_study_cnt
        self.play_mode = play_mode
        self.schedule_info = schedule_info

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.daily_study_cnt is not None:
            result['DailyStudyCnt'] = self.daily_study_cnt
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('DailyStudyCnt') is not None:
            self.daily_study_cnt = m.get('DailyStudyCnt')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('ScheduleInfo') is not None:
            temp_model = AddSubRequestAddSubscriptionInfoRequestScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        return self


class AddSubRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class AddSubRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class AddSubRequest(TeaModel):
    def __init__(
        self,
        add_subscription_info_request: AddSubRequestAddSubscriptionInfoRequest = None,
        device_info: AddSubRequestDeviceInfo = None,
        user_info: AddSubRequestUserInfo = None,
    ):
        self.add_subscription_info_request = add_subscription_info_request
        self.device_info = device_info
        self.user_info = user_info

    def validate(self):
        if self.add_subscription_info_request:
            self.add_subscription_info_request.validate()
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_subscription_info_request is not None:
            result['AddSubscriptionInfoRequest'] = self.add_subscription_info_request.to_map()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSubscriptionInfoRequest') is not None:
            temp_model = AddSubRequestAddSubscriptionInfoRequest()
            self.add_subscription_info_request = temp_model.from_map(m['AddSubscriptionInfoRequest'])
        if m.get('DeviceInfo') is not None:
            temp_model = AddSubRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = AddSubRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class AddSubShrinkRequest(TeaModel):
    def __init__(
        self,
        add_subscription_info_request_shrink: str = None,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.add_subscription_info_request_shrink = add_subscription_info_request_shrink
        self.device_info_shrink = device_info_shrink
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.add_subscription_info_request_shrink is not None:
            result['AddSubscriptionInfoRequest'] = self.add_subscription_info_request_shrink
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddSubscriptionInfoRequest') is not None:
            self.add_subscription_info_request_shrink = m.get('AddSubscriptionInfoRequest')
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class AddSubResponseBodyResultScheduleInfo(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class AddSubResponseBodyResult(TeaModel):
    def __init__(
        self,
        album_id: str = None,
        daily_study_cnt: int = None,
        device_id: str = None,
        id: int = None,
        play_mode: str = None,
        schedule_info: AddSubResponseBodyResultScheduleInfo = None,
        user_id: str = None,
    ):
        self.album_id = album_id
        self.daily_study_cnt = daily_study_cnt
        self.device_id = device_id
        self.id = id
        self.play_mode = play_mode
        self.schedule_info = schedule_info
        self.user_id = user_id

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.daily_study_cnt is not None:
            result['DailyStudyCnt'] = self.daily_study_cnt
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id is not None:
            result['Id'] = self.id
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('DailyStudyCnt') is not None:
            self.daily_study_cnt = m.get('DailyStudyCnt')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('ScheduleInfo') is not None:
            temp_model = AddSubResponseBodyResultScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddSubResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: AddSubResponseBodyResult = None,
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
            temp_model = AddSubResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class AddSubResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddSubResponseBody = None,
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
            temp_model = AddSubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthLoginWithAligenieUserInfoHeaders(TeaModel):
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


class AuthLoginWithAligenieUserInfoRequest(TeaModel):
    def __init__(
        self,
        encrypted_aligenie_user_identifier: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.encrypted_aligenie_user_identifier = encrypted_aligenie_user_identifier
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_aligenie_user_identifier is not None:
            result['EncryptedAligenieUserIdentifier'] = self.encrypted_aligenie_user_identifier
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedAligenieUserIdentifier') is not None:
            self.encrypted_aligenie_user_identifier = m.get('EncryptedAligenieUserIdentifier')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AuthLoginWithAligenieUserInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        expired_time_long: int = None,
        login_state_access_token: str = None,
    ):
        self.expired_time_long = expired_time_long
        self.login_state_access_token = login_state_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time_long is not None:
            result['ExpiredTimeLong'] = self.expired_time_long
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTimeLong') is not None:
            self.expired_time_long = m.get('ExpiredTimeLong')
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class AuthLoginWithAligenieUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: AuthLoginWithAligenieUserInfoResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = AuthLoginWithAligenieUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthLoginWithAligenieUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthLoginWithAligenieUserInfoResponseBody = None,
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
            temp_model = AuthLoginWithAligenieUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberHeaders(TeaModel):
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


class AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberRequest(TeaModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBodyResult(TeaModel):
    def __init__(
        self,
        expired_time_long: int = None,
        login_state_access_token: str = None,
    ):
        self.expired_time_long = expired_time_long
        self.login_state_access_token = login_state_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time_long is not None:
            result['ExpiredTimeLong'] = self.expired_time_long
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTimeLong') is not None:
            self.expired_time_long = m.get('ExpiredTimeLong')
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBody = None,
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
            temp_model = AuthLoginWithAligenieUserInfoGeneratedByPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthLoginWithTaobaoUserInfoHeaders(TeaModel):
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


class AuthLoginWithTaobaoUserInfoRequest(TeaModel):
    def __init__(
        self,
        encrypted_taobao_user_identifier: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.encrypted_taobao_user_identifier = encrypted_taobao_user_identifier
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.encrypted_taobao_user_identifier is not None:
            result['EncryptedTaobaoUserIdentifier'] = self.encrypted_taobao_user_identifier
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncryptedTaobaoUserIdentifier') is not None:
            self.encrypted_taobao_user_identifier = m.get('EncryptedTaobaoUserIdentifier')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AuthLoginWithTaobaoUserInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        expired_time_long: int = None,
        login_state_access_token: str = None,
    ):
        self.expired_time_long = expired_time_long
        self.login_state_access_token = login_state_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time_long is not None:
            result['ExpiredTimeLong'] = self.expired_time_long
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTimeLong') is not None:
            self.expired_time_long = m.get('ExpiredTimeLong')
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class AuthLoginWithTaobaoUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: AuthLoginWithTaobaoUserInfoResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = AuthLoginWithTaobaoUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthLoginWithTaobaoUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthLoginWithTaobaoUserInfoResponseBody = None,
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
            temp_model = AuthLoginWithTaobaoUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AuthLoginWithThirdUserInfoHeaders(TeaModel):
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


class AuthLoginWithThirdUserInfoRequest(TeaModel):
    def __init__(
        self,
        ext_info: Dict[str, Any] = None,
        scene_code: str = None,
        third_user_identifier: str = None,
        third_user_type: str = None,
    ):
        self.ext_info = ext_info
        # This parameter is required.
        self.scene_code = scene_code
        # This parameter is required.
        self.third_user_identifier = third_user_identifier
        # This parameter is required.
        self.third_user_type = third_user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.third_user_identifier is not None:
            result['ThirdUserIdentifier'] = self.third_user_identifier
        if self.third_user_type is not None:
            result['ThirdUserType'] = self.third_user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('ThirdUserIdentifier') is not None:
            self.third_user_identifier = m.get('ThirdUserIdentifier')
        if m.get('ThirdUserType') is not None:
            self.third_user_type = m.get('ThirdUserType')
        return self


class AuthLoginWithThirdUserInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        ext_info_shrink: str = None,
        scene_code: str = None,
        third_user_identifier: str = None,
        third_user_type: str = None,
    ):
        self.ext_info_shrink = ext_info_shrink
        # This parameter is required.
        self.scene_code = scene_code
        # This parameter is required.
        self.third_user_identifier = third_user_identifier
        # This parameter is required.
        self.third_user_type = third_user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ext_info_shrink is not None:
            result['ExtInfo'] = self.ext_info_shrink
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.third_user_identifier is not None:
            result['ThirdUserIdentifier'] = self.third_user_identifier
        if self.third_user_type is not None:
            result['ThirdUserType'] = self.third_user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtInfo') is not None:
            self.ext_info_shrink = m.get('ExtInfo')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('ThirdUserIdentifier') is not None:
            self.third_user_identifier = m.get('ThirdUserIdentifier')
        if m.get('ThirdUserType') is not None:
            self.third_user_type = m.get('ThirdUserType')
        return self


class AuthLoginWithThirdUserInfoResponseBodyDataObj(TeaModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class AuthLoginWithThirdUserInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        expired_time_long: int = None,
        login_state_access_token: str = None,
    ):
        self.expired_time_long = expired_time_long
        self.login_state_access_token = login_state_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expired_time_long is not None:
            result['ExpiredTimeLong'] = self.expired_time_long
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpiredTimeLong') is not None:
            self.expired_time_long = m.get('ExpiredTimeLong')
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class AuthLoginWithThirdUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data_obj: AuthLoginWithThirdUserInfoResponseBodyDataObj = None,
        message: str = None,
        request_id: str = None,
        result: AuthLoginWithThirdUserInfoResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.data_obj = data_obj
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.data_obj:
            self.data_obj.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data_obj is not None:
            result['DataObj'] = self.data_obj.to_map()
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
        if m.get('DataObj') is not None:
            temp_model = AuthLoginWithThirdUserInfoResponseBodyDataObj()
            self.data_obj = temp_model.from_map(m['DataObj'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = AuthLoginWithThirdUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class AuthLoginWithThirdUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AuthLoginWithThirdUserInfoResponseBody = None,
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
            temp_model = AuthLoginWithThirdUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAndDoVoipCallForHotelHeaders(TeaModel):
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


class CheckAndDoVoipCallForHotelRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class CheckAndDoVoipCallForHotelRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class CheckAndDoVoipCallForHotelRequest(TeaModel):
    def __init__(
        self,
        biz_data: str = None,
        callee_nick: str = None,
        callee_phone_num: str = None,
        device_info: CheckAndDoVoipCallForHotelRequestDeviceInfo = None,
        user_info: CheckAndDoVoipCallForHotelRequestUserInfo = None,
    ):
        self.biz_data = biz_data
        self.callee_nick = callee_nick
        self.callee_phone_num = callee_phone_num
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_data is not None:
            result['BizData'] = self.biz_data
        if self.callee_nick is not None:
            result['CalleeNick'] = self.callee_nick
        if self.callee_phone_num is not None:
            result['CalleePhoneNum'] = self.callee_phone_num
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')
        if m.get('CalleeNick') is not None:
            self.callee_nick = m.get('CalleeNick')
        if m.get('CalleePhoneNum') is not None:
            self.callee_phone_num = m.get('CalleePhoneNum')
        if m.get('DeviceInfo') is not None:
            temp_model = CheckAndDoVoipCallForHotelRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = CheckAndDoVoipCallForHotelRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CheckAndDoVoipCallForHotelShrinkRequest(TeaModel):
    def __init__(
        self,
        biz_data: str = None,
        callee_nick: str = None,
        callee_phone_num: str = None,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.biz_data = biz_data
        self.callee_nick = callee_nick
        self.callee_phone_num = callee_phone_num
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_data is not None:
            result['BizData'] = self.biz_data
        if self.callee_nick is not None:
            result['CalleeNick'] = self.callee_nick
        if self.callee_phone_num is not None:
            result['CalleePhoneNum'] = self.callee_phone_num
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')
        if m.get('CalleeNick') is not None:
            self.callee_nick = m.get('CalleeNick')
        if m.get('CalleePhoneNum') is not None:
            self.callee_phone_num = m.get('CalleePhoneNum')
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargetsData(TeaModel):
    def __init__(
        self,
        device_icon: str = None,
        device_name: str = None,
        device_type: str = None,
        online: bool = None,
        uuid: str = None,
    ):
        self.device_icon = device_icon
        self.device_name = device_name
        self.device_type = device_type
        self.online = online
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_icon is not None:
            result['DeviceIcon'] = self.device_icon
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.device_type is not None:
            result['DeviceType'] = self.device_type
        if self.online is not None:
            result['Online'] = self.online
        if self.uuid is not None:
            result['Uuid'] = self.uuid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceIcon') is not None:
            self.device_icon = m.get('DeviceIcon')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('DeviceType') is not None:
            self.device_type = m.get('DeviceType')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
        return self


class CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargets(TeaModel):
    def __init__(
        self,
        code: int = None,
        data: List[CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargetsData] = None,
        msg: str = None,
    ):
        self.code = code
        self.data = data
        self.msg = msg

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
            result['Code'] = self.code
        result['Data'] = []
        if self.data is not None:
            for k in self.data:
                result['Data'].append(k.to_map() if k else None)
        if self.msg is not None:
            result['Msg'] = self.msg
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.data = []
        if m.get('Data') is not None:
            for k in m.get('Data'):
                temp_model = CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargetsData()
                self.data.append(temp_model.from_map(k))
        if m.get('Msg') is not None:
            self.msg = m.get('Msg')
        return self


class CheckAndDoVoipCallForHotelResponseBodyResultStartCallResult(TeaModel):
    def __init__(
        self,
        message: str = None,
        ret_code: int = None,
        ret_value: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        self.message = message
        self.ret_code = ret_code
        self.ret_value = ret_value
        self.success = success
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message is not None:
            result['Message'] = self.message
        if self.ret_code is not None:
            result['RetCode'] = self.ret_code
        if self.ret_value is not None:
            result['RetValue'] = self.ret_value
        if self.success is not None:
            result['Success'] = self.success
        if self.trace_id is not None:
            result['TraceId'] = self.trace_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RetCode') is not None:
            self.ret_code = m.get('RetCode')
        if m.get('RetValue') is not None:
            self.ret_value = m.get('RetValue')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')
        return self


class CheckAndDoVoipCallForHotelResponseBodyResult(TeaModel):
    def __init__(
        self,
        device_targets: CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargets = None,
        is_start_call: bool = None,
        passed: bool = None,
        start_call_result: CheckAndDoVoipCallForHotelResponseBodyResultStartCallResult = None,
    ):
        self.device_targets = device_targets
        self.is_start_call = is_start_call
        self.passed = passed
        self.start_call_result = start_call_result

    def validate(self):
        if self.device_targets:
            self.device_targets.validate()
        if self.start_call_result:
            self.start_call_result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_targets is not None:
            result['DeviceTargets'] = self.device_targets.to_map()
        if self.is_start_call is not None:
            result['IsStartCall'] = self.is_start_call
        if self.passed is not None:
            result['Passed'] = self.passed
        if self.start_call_result is not None:
            result['StartCallResult'] = self.start_call_result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTargets') is not None:
            temp_model = CheckAndDoVoipCallForHotelResponseBodyResultDeviceTargets()
            self.device_targets = temp_model.from_map(m['DeviceTargets'])
        if m.get('IsStartCall') is not None:
            self.is_start_call = m.get('IsStartCall')
        if m.get('Passed') is not None:
            self.passed = m.get('Passed')
        if m.get('StartCallResult') is not None:
            temp_model = CheckAndDoVoipCallForHotelResponseBodyResultStartCallResult()
            self.start_call_result = temp_model.from_map(m['StartCallResult'])
        return self


class CheckAndDoVoipCallForHotelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: CheckAndDoVoipCallForHotelResponseBodyResult = None,
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
            temp_model = CheckAndDoVoipCallForHotelResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckAndDoVoipCallForHotelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckAndDoVoipCallForHotelResponseBody = None,
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
            temp_model = CheckAndDoVoipCallForHotelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckAuthCodeBindForExtHeaders(TeaModel):
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


class CheckAuthCodeBindForExtRequestUserInfo(TeaModel):
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


class CheckAuthCodeBindForExtRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        encode_key: str = None,
        encode_type: str = None,
        user_info: CheckAuthCodeBindForExtRequestUserInfo = None,
    ):
        # This parameter is required.
        self.auth_code = auth_code
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('UserInfo') is not None:
            temp_model = CheckAuthCodeBindForExtRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CheckAuthCodeBindForExtShrinkRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        encode_key: str = None,
        encode_type: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.auth_code = auth_code
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auth_code is not None:
            result['AuthCode'] = self.auth_code
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthCode') is not None:
            self.auth_code = m.get('AuthCode')
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CheckAuthCodeBindForExtResponseBodyResultDeviceOpenInfo(TeaModel):
    def __init__(
        self,
        id: str = None,
        id_type: str = None,
    ):
        self.id = id
        # DEVICE_ID
        self.id_type = id_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        return self


class CheckAuthCodeBindForExtResponseBodyResultUserOpenInfo(TeaModel):
    def __init__(
        self,
        id: str = None,
        id_type: str = None,
    ):
        self.id = id
        # USER_ID
        self.id_type = id_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.id_type is not None:
            result['IdType'] = self.id_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        return self


class CheckAuthCodeBindForExtResponseBodyResult(TeaModel):
    def __init__(
        self,
        device_open_info: CheckAuthCodeBindForExtResponseBodyResultDeviceOpenInfo = None,
        user_open_info: CheckAuthCodeBindForExtResponseBodyResultUserOpenInfo = None,
    ):
        self.device_open_info = device_open_info
        self.user_open_info = user_open_info

    def validate(self):
        if self.device_open_info:
            self.device_open_info.validate()
        if self.user_open_info:
            self.user_open_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_open_info is not None:
            result['DeviceOpenInfo'] = self.device_open_info.to_map()
        if self.user_open_info is not None:
            result['UserOpenInfo'] = self.user_open_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceOpenInfo') is not None:
            temp_model = CheckAuthCodeBindForExtResponseBodyResultDeviceOpenInfo()
            self.device_open_info = temp_model.from_map(m['DeviceOpenInfo'])
        if m.get('UserOpenInfo') is not None:
            temp_model = CheckAuthCodeBindForExtResponseBodyResultUserOpenInfo()
            self.user_open_info = temp_model.from_map(m['UserOpenInfo'])
        return self


class CheckAuthCodeBindForExtResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: CheckAuthCodeBindForExtResponseBodyResult = None,
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
            temp_model = CheckAuthCodeBindForExtResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class CheckAuthCodeBindForExtResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CheckAuthCodeBindForExtResponseBody = None,
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
            temp_model = CheckAuthCodeBindForExtResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CloudPlayerHeaders(TeaModel):
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


class CloudPlayerRequestDeviceInfo(TeaModel):
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


class CloudPlayerRequestUserInfo(TeaModel):
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


class CloudPlayerRequest(TeaModel):
    def __init__(
        self,
        cur_play_index: int = None,
        device_info: CloudPlayerRequestDeviceInfo = None,
        play_mode: str = None,
        song_id: str = None,
        song_id_list: List[str] = None,
        source: str = None,
        user_info: CloudPlayerRequestUserInfo = None,
    ):
        # This parameter is required.
        self.cur_play_index = cur_play_index
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.play_mode = play_mode
        self.song_id = song_id
        # This parameter is required.
        self.song_id_list = song_id_list
        # This parameter is required.
        self.source = source
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_play_index is not None:
            result['CurPlayIndex'] = self.cur_play_index
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.song_id is not None:
            result['SongId'] = self.song_id
        if self.song_id_list is not None:
            result['SongIdList'] = self.song_id_list
        if self.source is not None:
            result['Source'] = self.source
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurPlayIndex') is not None:
            self.cur_play_index = m.get('CurPlayIndex')
        if m.get('DeviceInfo') is not None:
            temp_model = CloudPlayerRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('SongId') is not None:
            self.song_id = m.get('SongId')
        if m.get('SongIdList') is not None:
            self.song_id_list = m.get('SongIdList')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserInfo') is not None:
            temp_model = CloudPlayerRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CloudPlayerShrinkRequest(TeaModel):
    def __init__(
        self,
        cur_play_index: int = None,
        device_info_shrink: str = None,
        play_mode: str = None,
        song_id: str = None,
        song_id_list_shrink: str = None,
        source: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.cur_play_index = cur_play_index
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.play_mode = play_mode
        self.song_id = song_id
        # This parameter is required.
        self.song_id_list_shrink = song_id_list_shrink
        # This parameter is required.
        self.source = source
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cur_play_index is not None:
            result['CurPlayIndex'] = self.cur_play_index
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.song_id is not None:
            result['SongId'] = self.song_id
        if self.song_id_list_shrink is not None:
            result['SongIdList'] = self.song_id_list_shrink
        if self.source is not None:
            result['Source'] = self.source
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurPlayIndex') is not None:
            self.cur_play_index = m.get('CurPlayIndex')
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('SongId') is not None:
            self.song_id = m.get('SongId')
        if m.get('SongIdList') is not None:
            self.song_id_list_shrink = m.get('SongIdList')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CloudPlayerResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class CloudPlayerResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CloudPlayerResponseBody = None,
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
            temp_model = CloudPlayerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateAlarmHeaders(TeaModel):
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


class CreateAlarmRequestDeviceInfo(TeaModel):
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


class CreateAlarmRequestPayloadMusicInfo(TeaModel):
    def __init__(
        self,
        music_id: int = None,
        music_name: str = None,
        music_type: int = None,
        music_type_name: str = None,
        music_url: str = None,
    ):
        # This parameter is required.
        self.music_id = music_id
        # This parameter is required.
        self.music_name = music_name
        # This parameter is required.
        self.music_type = music_type
        # This parameter is required.
        self.music_type_name = music_type_name
        self.music_url = music_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        return self


class CreateAlarmRequestPayloadScheduleInfoOnce(TeaModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class CreateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay(TeaModel):
    def __init__(
        self,
        hour: int = None,
        minute: int = None,
    ):
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class CreateAlarmRequestPayloadScheduleInfoWeekly(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class CreateAlarmRequestPayloadScheduleInfo(TeaModel):
    def __init__(
        self,
        once: CreateAlarmRequestPayloadScheduleInfoOnce = None,
        statutory_working_day: CreateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay = None,
        type: str = None,
        weekly: CreateAlarmRequestPayloadScheduleInfoWeekly = None,
    ):
        self.once = once
        self.statutory_working_day = statutory_working_day
        # This parameter is required.
        self.type = type
        self.weekly = weekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.statutory_working_day:
            self.statutory_working_day.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = CreateAlarmRequestPayloadScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('StatutoryWorkingDay') is not None:
            temp_model = CreateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m['StatutoryWorkingDay'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = CreateAlarmRequestPayloadScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class CreateAlarmRequestPayload(TeaModel):
    def __init__(
        self,
        music_info: CreateAlarmRequestPayloadMusicInfo = None,
        schedule_info: CreateAlarmRequestPayloadScheduleInfo = None,
        volume: int = None,
    ):
        # This parameter is required.
        self.music_info = music_info
        # This parameter is required.
        self.schedule_info = schedule_info
        self.volume = volume

    def validate(self):
        if self.music_info:
            self.music_info.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_info is not None:
            result['MusicInfo'] = self.music_info.to_map()
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MusicInfo') is not None:
            temp_model = CreateAlarmRequestPayloadMusicInfo()
            self.music_info = temp_model.from_map(m['MusicInfo'])
        if m.get('ScheduleInfo') is not None:
            temp_model = CreateAlarmRequestPayloadScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class CreateAlarmRequestUserInfo(TeaModel):
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


class CreateAlarmRequest(TeaModel):
    def __init__(
        self,
        device_info: CreateAlarmRequestDeviceInfo = None,
        payload: CreateAlarmRequestPayload = None,
        user_info: CreateAlarmRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = CreateAlarmRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = CreateAlarmRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = CreateAlarmRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CreateAlarmShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CreateAlarmResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class CreateAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateAlarmResponseBody = None,
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
            temp_model = CreateAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreatePlayingListHeaders(TeaModel):
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


class CreatePlayingListRequestUserInfo(TeaModel):
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


class CreatePlayingListRequest(TeaModel):
    def __init__(
        self,
        device_info: CreatePlayingListRequestDeviceInfo = None,
        open_create_playing_list_request: CreatePlayingListRequestOpenCreatePlayingListRequest = None,
        user_info: CreatePlayingListRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.open_create_playing_list_request = open_create_playing_list_request
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_create_playing_list_request:
            self.open_create_playing_list_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_create_playing_list_request is not None:
            result['OpenCreatePlayingListRequest'] = self.open_create_playing_list_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = CreatePlayingListRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenCreatePlayingListRequest') is not None:
            temp_model = CreatePlayingListRequestOpenCreatePlayingListRequest()
            self.open_create_playing_list_request = temp_model.from_map(m['OpenCreatePlayingListRequest'])
        if m.get('UserInfo') is not None:
            temp_model = CreatePlayingListRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CreatePlayingListShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        open_create_playing_list_request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.open_create_playing_list_request_shrink = open_create_playing_list_request_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

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
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenCreatePlayingListRequest') is not None:
            self.open_create_playing_list_request_shrink = m.get('OpenCreatePlayingListRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CreatePlayingListResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.mediam = mediam
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class CreatePlayingListResponseBodyResult(TeaModel):
    def __init__(
        self,
        album_name: str = None,
        album_raw_id: str = None,
        audio_length: int = None,
        copyright: int = None,
        cover: CreatePlayingListResponseBodyResultCover = None,
        default_play_order: int = None,
        item_url: str = None,
        liked: bool = None,
        lyric_url: str = None,
        play_mode: str = None,
        pos: int = None,
        progress: int = None,
        raw_id: str = None,
        singer: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        self.album_name = album_name
        self.album_raw_id = album_raw_id
        self.audio_length = audio_length
        self.copyright = copyright
        self.cover = cover
        self.default_play_order = default_play_order
        self.item_url = item_url
        self.liked = liked
        self.lyric_url = lyric_url
        self.play_mode = play_mode
        self.pos = pos
        self.progress = progress
        self.raw_id = raw_id
        self.singer = singer
        self.source = source
        self.title = title
        self.type = type
        self.valid = valid

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.liked is not None:
            result['Liked'] = self.liked
        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singer is not None:
            result['Singer'] = self.singer
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('Cover') is not None:
            temp_model = CreatePlayingListResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')
        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singer') is not None:
            self.singer = m.get('Singer')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class CreatePlayingListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: CreatePlayingListResponseBodyResult = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = CreatePlayingListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
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


class CreatePlayingListOAuth2RequestDeviceInfo(TeaModel):
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


class CreatePlayingListOAuth2RequestOpenCreatePlayingListRequestContentList(TeaModel):
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


class CreatePlayingListOAuth2RequestOpenCreatePlayingListRequest(TeaModel):
    def __init__(
        self,
        content_list: List[CreatePlayingListOAuth2RequestOpenCreatePlayingListRequestContentList] = None,
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
                temp_model = CreatePlayingListOAuth2RequestOpenCreatePlayingListRequestContentList()
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


class CreatePlayingListOAuth2Request(TeaModel):
    def __init__(
        self,
        device_info: CreatePlayingListOAuth2RequestDeviceInfo = None,
        open_create_playing_list_request: CreatePlayingListOAuth2RequestOpenCreatePlayingListRequest = None,
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
            temp_model = CreatePlayingListOAuth2RequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenCreatePlayingListRequest') is not None:
            temp_model = CreatePlayingListOAuth2RequestOpenCreatePlayingListRequest()
            self.open_create_playing_list_request = temp_model.from_map(m['OpenCreatePlayingListRequest'])
        return self


class CreatePlayingListOAuth2ShrinkRequest(TeaModel):
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


class CreatePlayingListOAuth2ResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.mediam = mediam
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class CreatePlayingListOAuth2ResponseBodyResult(TeaModel):
    def __init__(
        self,
        album_name: str = None,
        album_raw_id: str = None,
        audio_length: int = None,
        copyright: int = None,
        cover: CreatePlayingListOAuth2ResponseBodyResultCover = None,
        default_play_order: int = None,
        item_url: str = None,
        liked: bool = None,
        lyric_url: str = None,
        play_mode: str = None,
        pos: int = None,
        progress: int = None,
        raw_id: str = None,
        singer: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        self.album_name = album_name
        self.album_raw_id = album_raw_id
        self.audio_length = audio_length
        self.copyright = copyright
        self.cover = cover
        self.default_play_order = default_play_order
        self.item_url = item_url
        self.liked = liked
        self.lyric_url = lyric_url
        self.play_mode = play_mode
        self.pos = pos
        self.progress = progress
        self.raw_id = raw_id
        self.singer = singer
        self.source = source
        self.title = title
        self.type = type
        self.valid = valid

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.liked is not None:
            result['Liked'] = self.liked
        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singer is not None:
            result['Singer'] = self.singer
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('Cover') is not None:
            temp_model = CreatePlayingListOAuth2ResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')
        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singer') is not None:
            self.singer = m.get('Singer')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class CreatePlayingListOAuth2ResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: CreatePlayingListOAuth2ResponseBodyResult = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = CreatePlayingListOAuth2ResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class CreatePlayingListOAuth2Response(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreatePlayingListOAuth2ResponseBody = None,
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
            temp_model = CreatePlayingListOAuth2ResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateScheduleTaskHeaders(TeaModel):
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


class CreateScheduleTaskRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class CreateScheduleTaskRequestPayloadActionDTOs(TeaModel):
    def __init__(
        self,
        custom_action: Dict[str, Any] = None,
    ):
        self.custom_action = custom_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_action is not None:
            result['customAction'] = self.custom_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('customAction') is not None:
            self.custom_action = m.get('customAction')
        return self


class CreateScheduleTaskRequestPayloadScheduleDTOOnce(TeaModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class CreateScheduleTaskRequestPayloadScheduleDTOStatutoryWorkingDay(TeaModel):
    def __init__(
        self,
        hours: List[int] = None,
        minutes: List[int] = None,
    ):
        self.hours = hours
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hours is not None:
            result['Hours'] = self.hours
        if self.minutes is not None:
            result['Minutes'] = self.minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hours') is not None:
            self.hours = m.get('Hours')
        if m.get('Minutes') is not None:
            self.minutes = m.get('Minutes')
        return self


class CreateScheduleTaskRequestPayloadScheduleDTOWeekly(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hours: List[int] = None,
        minutes: List[int] = None,
    ):
        self.days_of_week = days_of_week
        self.hours = hours
        self.minutes = minutes

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hours is not None:
            result['Hours'] = self.hours
        if self.minutes is not None:
            result['Minutes'] = self.minutes
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hours') is not None:
            self.hours = m.get('Hours')
        if m.get('Minutes') is not None:
            self.minutes = m.get('Minutes')
        return self


class CreateScheduleTaskRequestPayloadScheduleDTO(TeaModel):
    def __init__(
        self,
        once: CreateScheduleTaskRequestPayloadScheduleDTOOnce = None,
        schedule_end_time: int = None,
        schedule_start_time: int = None,
        schedule_type: str = None,
        statutory_working_day: CreateScheduleTaskRequestPayloadScheduleDTOStatutoryWorkingDay = None,
        weekly: CreateScheduleTaskRequestPayloadScheduleDTOWeekly = None,
    ):
        self.once = once
        # This parameter is required.
        self.schedule_end_time = schedule_end_time
        # This parameter is required.
        self.schedule_start_time = schedule_start_time
        # This parameter is required.
        self.schedule_type = schedule_type
        self.statutory_working_day = statutory_working_day
        self.weekly = weekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.statutory_working_day:
            self.statutory_working_day.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.schedule_end_time is not None:
            result['ScheduleEndTime'] = self.schedule_end_time
        if self.schedule_start_time is not None:
            result['ScheduleStartTime'] = self.schedule_start_time
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = CreateScheduleTaskRequestPayloadScheduleDTOOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('ScheduleEndTime') is not None:
            self.schedule_end_time = m.get('ScheduleEndTime')
        if m.get('ScheduleStartTime') is not None:
            self.schedule_start_time = m.get('ScheduleStartTime')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        if m.get('StatutoryWorkingDay') is not None:
            temp_model = CreateScheduleTaskRequestPayloadScheduleDTOStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m['StatutoryWorkingDay'])
        if m.get('Weekly') is not None:
            temp_model = CreateScheduleTaskRequestPayloadScheduleDTOWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class CreateScheduleTaskRequestPayload(TeaModel):
    def __init__(
        self,
        action_dtos: List[CreateScheduleTaskRequestPayloadActionDTOs] = None,
        idempotent_id: str = None,
        schedule_dto: CreateScheduleTaskRequestPayloadScheduleDTO = None,
    ):
        # This parameter is required.
        self.action_dtos = action_dtos
        self.idempotent_id = idempotent_id
        # This parameter is required.
        self.schedule_dto = schedule_dto

    def validate(self):
        if self.action_dtos:
            for k in self.action_dtos:
                if k:
                    k.validate()
        if self.schedule_dto:
            self.schedule_dto.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActionDTOs'] = []
        if self.action_dtos is not None:
            for k in self.action_dtos:
                result['ActionDTOs'].append(k.to_map() if k else None)
        if self.idempotent_id is not None:
            result['IdempotentId'] = self.idempotent_id
        if self.schedule_dto is not None:
            result['ScheduleDTO'] = self.schedule_dto.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_dtos = []
        if m.get('ActionDTOs') is not None:
            for k in m.get('ActionDTOs'):
                temp_model = CreateScheduleTaskRequestPayloadActionDTOs()
                self.action_dtos.append(temp_model.from_map(k))
        if m.get('IdempotentId') is not None:
            self.idempotent_id = m.get('IdempotentId')
        if m.get('ScheduleDTO') is not None:
            temp_model = CreateScheduleTaskRequestPayloadScheduleDTO()
            self.schedule_dto = temp_model.from_map(m['ScheduleDTO'])
        return self


class CreateScheduleTaskRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class CreateScheduleTaskRequest(TeaModel):
    def __init__(
        self,
        device_info: CreateScheduleTaskRequestDeviceInfo = None,
        payload: CreateScheduleTaskRequestPayload = None,
        user_info: CreateScheduleTaskRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = CreateScheduleTaskRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = CreateScheduleTaskRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = CreateScheduleTaskRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class CreateScheduleTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class CreateScheduleTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: int = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class CreateScheduleTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateScheduleTaskResponseBody = None,
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
            temp_model = CreateScheduleTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteAlarmsHeaders(TeaModel):
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


class DeleteAlarmsRequestDeviceInfo(TeaModel):
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


class DeleteAlarmsRequestPayload(TeaModel):
    def __init__(
        self,
        alarm_ids: List[int] = None,
    ):
        # This parameter is required.
        self.alarm_ids = alarm_ids

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_ids is not None:
            result['AlarmIds'] = self.alarm_ids
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmIds') is not None:
            self.alarm_ids = m.get('AlarmIds')
        return self


class DeleteAlarmsRequestUserInfo(TeaModel):
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


class DeleteAlarmsRequest(TeaModel):
    def __init__(
        self,
        device_info: DeleteAlarmsRequestDeviceInfo = None,
        payload: DeleteAlarmsRequestPayload = None,
        user_info: DeleteAlarmsRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = DeleteAlarmsRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = DeleteAlarmsRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = DeleteAlarmsRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class DeleteAlarmsShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class DeleteAlarmsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class DeleteAlarmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteAlarmsResponseBody = None,
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
            temp_model = DeleteAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteScheduleTaskHeaders(TeaModel):
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


class DeleteScheduleTaskRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class DeleteScheduleTaskRequestPayload(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
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


class DeleteScheduleTaskRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class DeleteScheduleTaskRequest(TeaModel):
    def __init__(
        self,
        device_info: DeleteScheduleTaskRequestDeviceInfo = None,
        payload: DeleteScheduleTaskRequestPayload = None,
        user_info: DeleteScheduleTaskRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = DeleteScheduleTaskRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = DeleteScheduleTaskRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = DeleteScheduleTaskRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class DeleteScheduleTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class DeleteScheduleTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class DeleteScheduleTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteScheduleTaskResponseBody = None,
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
            temp_model = DeleteScheduleTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteSubHeaders(TeaModel):
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


class DeleteSubRequest(TeaModel):
    def __init__(
        self,
        sub_id: int = None,
    ):
        # This parameter is required.
        self.sub_id = sub_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sub_id is not None:
            result['SubId'] = self.sub_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SubId') is not None:
            self.sub_id = m.get('SubId')
        return self


class DeleteSubResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class DeleteSubResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteSubResponseBody = None,
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
            temp_model = DeleteSubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeviceControlHeaders(TeaModel):
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


class DeviceControlRequestControlRequest(TeaModel):
    def __init__(
        self,
        muted: bool = None,
        volume: int = None,
    ):
        self.muted = muted
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.muted is not None:
            result['Muted'] = self.muted
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Muted') is not None:
            self.muted = m.get('Muted')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class DeviceControlRequestDeviceInfo(TeaModel):
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


class DeviceControlRequest(TeaModel):
    def __init__(
        self,
        control_request: DeviceControlRequestControlRequest = None,
        device_info: DeviceControlRequestDeviceInfo = None,
    ):
        self.control_request = control_request
        # This parameter is required.
        self.device_info = device_info

    def validate(self):
        if self.control_request:
            self.control_request.validate()
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_request is not None:
            result['ControlRequest'] = self.control_request.to_map()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlRequest') is not None:
            temp_model = DeviceControlRequestControlRequest()
            self.control_request = temp_model.from_map(m['ControlRequest'])
        if m.get('DeviceInfo') is not None:
            temp_model = DeviceControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class DeviceControlShrinkRequest(TeaModel):
    def __init__(
        self,
        control_request_shrink: str = None,
        device_info_shrink: str = None,
    ):
        self.control_request_shrink = control_request_shrink
        # This parameter is required.
        self.device_info_shrink = device_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.control_request_shrink is not None:
            result['ControlRequest'] = self.control_request_shrink
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlRequest') is not None:
            self.control_request_shrink = m.get('ControlRequest')
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class DeviceControlResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class DeviceControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeviceControlResponseBody = None,
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
            temp_model = DeviceControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EcologyOpennessAuthenticateHeaders(TeaModel):
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


class EcologyOpennessAuthenticateRequest(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        login_state_access_token: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.login_state_access_token = login_state_access_token

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
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class EcologyOpennessAuthenticateResponseBodyResult(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        scene_code: str = None,
        third_user_identifier: str = None,
        third_user_type: str = None,
        user_open_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.scene_code = scene_code
        self.third_user_identifier = third_user_identifier
        self.third_user_type = third_user_type
        self.user_open_id = user_open_id

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
        if self.scene_code is not None:
            result['SceneCode'] = self.scene_code
        if self.third_user_identifier is not None:
            result['ThirdUserIdentifier'] = self.third_user_identifier
        if self.third_user_type is not None:
            result['ThirdUserType'] = self.third_user_type
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('SceneCode') is not None:
            self.scene_code = m.get('SceneCode')
        if m.get('ThirdUserIdentifier') is not None:
            self.third_user_identifier = m.get('ThirdUserIdentifier')
        if m.get('ThirdUserType') is not None:
            self.third_user_type = m.get('ThirdUserType')
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class EcologyOpennessAuthenticateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: EcologyOpennessAuthenticateResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = EcologyOpennessAuthenticateResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EcologyOpennessAuthenticateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EcologyOpennessAuthenticateResponseBody = None,
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
            temp_model = EcologyOpennessAuthenticateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EcologyOpennessSendVerificationCodeHeaders(TeaModel):
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


class EcologyOpennessSendVerificationCodeRequest(TeaModel):
    def __init__(
        self,
        phone_number: str = None,
        region: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.region is not None:
            result['Region'] = self.region
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class EcologyOpennessSendVerificationCodeResponseBodyResult(TeaModel):
    def __init__(
        self,
        expire_in: int = None,
        repeat_interval: int = None,
    ):
        self.expire_in = expire_in
        self.repeat_interval = repeat_interval

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_in is not None:
            result['ExpireIn'] = self.expire_in
        if self.repeat_interval is not None:
            result['RepeatInterval'] = self.repeat_interval
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireIn') is not None:
            self.expire_in = m.get('ExpireIn')
        if m.get('RepeatInterval') is not None:
            self.repeat_interval = m.get('RepeatInterval')
        return self


class EcologyOpennessSendVerificationCodeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: EcologyOpennessSendVerificationCodeResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = EcologyOpennessSendVerificationCodeResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class EcologyOpennessSendVerificationCodeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: EcologyOpennessSendVerificationCodeResponseBody = None,
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
            temp_model = EcologyOpennessSendVerificationCodeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FindUserlistToAuthLoginWithPhoneNumberHeaders(TeaModel):
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


class FindUserlistToAuthLoginWithPhoneNumberRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        phone_number: str = None,
        region: str = None,
        session_id: str = None,
    ):
        # This parameter is required.
        self.code = code
        # This parameter is required.
        self.phone_number = phone_number
        # This parameter is required.
        self.region = region
        # This parameter is required.
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.phone_number is not None:
            result['PhoneNumber'] = self.phone_number
        if self.region is not None:
            result['Region'] = self.region
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('PhoneNumber') is not None:
            self.phone_number = m.get('PhoneNumber')
        if m.get('Region') is not None:
            self.region = m.get('Region')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class FindUserlistToAuthLoginWithPhoneNumberResponseBodyDataObj(TeaModel):
    def __init__(
        self,
        session_id: str = None,
    ):
        self.session_id = session_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        return self


class FindUserlistToAuthLoginWithPhoneNumberResponseBodyResultUserListToAuthLogin(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        encrypted_user_identifier: str = None,
        finding_type: str = None,
        nickname: str = None,
        user_type: str = None,
    ):
        self.avatar = avatar
        self.encrypted_user_identifier = encrypted_user_identifier
        self.finding_type = finding_type
        self.nickname = nickname
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.encrypted_user_identifier is not None:
            result['EncryptedUserIdentifier'] = self.encrypted_user_identifier
        if self.finding_type is not None:
            result['FindingType'] = self.finding_type
        if self.nickname is not None:
            result['Nickname'] = self.nickname
        if self.user_type is not None:
            result['UserType'] = self.user_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('EncryptedUserIdentifier') is not None:
            self.encrypted_user_identifier = m.get('EncryptedUserIdentifier')
        if m.get('FindingType') is not None:
            self.finding_type = m.get('FindingType')
        if m.get('Nickname') is not None:
            self.nickname = m.get('Nickname')
        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')
        return self


class FindUserlistToAuthLoginWithPhoneNumberResponseBodyResult(TeaModel):
    def __init__(
        self,
        user_list_to_auth_login: List[FindUserlistToAuthLoginWithPhoneNumberResponseBodyResultUserListToAuthLogin] = None,
    ):
        self.user_list_to_auth_login = user_list_to_auth_login

    def validate(self):
        if self.user_list_to_auth_login:
            for k in self.user_list_to_auth_login:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['UserListToAuthLogin'] = []
        if self.user_list_to_auth_login is not None:
            for k in self.user_list_to_auth_login:
                result['UserListToAuthLogin'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.user_list_to_auth_login = []
        if m.get('UserListToAuthLogin') is not None:
            for k in m.get('UserListToAuthLogin'):
                temp_model = FindUserlistToAuthLoginWithPhoneNumberResponseBodyResultUserListToAuthLogin()
                self.user_list_to_auth_login.append(temp_model.from_map(k))
        return self


class FindUserlistToAuthLoginWithPhoneNumberResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        data_obj: FindUserlistToAuthLoginWithPhoneNumberResponseBodyDataObj = None,
        message: str = None,
        request_id: str = None,
        result: FindUserlistToAuthLoginWithPhoneNumberResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.data_obj = data_obj
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.data_obj:
            self.data_obj.validate()
        if self.result:
            self.result.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.data_obj is not None:
            result['DataObj'] = self.data_obj.to_map()
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
        if m.get('DataObj') is not None:
            temp_model = FindUserlistToAuthLoginWithPhoneNumberResponseBodyDataObj()
            self.data_obj = temp_model.from_map(m['DataObj'])
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = FindUserlistToAuthLoginWithPhoneNumberResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class FindUserlistToAuthLoginWithPhoneNumberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FindUserlistToAuthLoginWithPhoneNumberResponseBody = None,
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
            temp_model = FindUserlistToAuthLoginWithPhoneNumberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlarmHeaders(TeaModel):
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


class GetAlarmRequestDeviceInfo(TeaModel):
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


class GetAlarmRequestPayload(TeaModel):
    def __init__(
        self,
        alarm_id: int = None,
    ):
        # This parameter is required.
        self.alarm_id = alarm_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        return self


class GetAlarmRequestUserInfo(TeaModel):
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


class GetAlarmRequest(TeaModel):
    def __init__(
        self,
        device_info: GetAlarmRequestDeviceInfo = None,
        payload: GetAlarmRequestPayload = None,
        user_info: GetAlarmRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetAlarmRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetAlarmRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetAlarmRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetAlarmShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetAlarmResponseBodyResultMusicInfo(TeaModel):
    def __init__(
        self,
        music_id: int = None,
        music_name: str = None,
        music_type: int = None,
        music_type_name: str = None,
        music_url: str = None,
    ):
        self.music_id = music_id
        self.music_name = music_name
        self.music_type = music_type
        self.music_type_name = music_type_name
        self.music_url = music_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        return self


class GetAlarmResponseBodyResultScheduleInfoOnce(TeaModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class GetAlarmResponseBodyResultScheduleInfoStatutoryWorkingDay(TeaModel):
    def __init__(
        self,
        hour: int = None,
        minute: int = None,
    ):
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class GetAlarmResponseBodyResultScheduleInfoWeekly(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class GetAlarmResponseBodyResultScheduleInfo(TeaModel):
    def __init__(
        self,
        once: GetAlarmResponseBodyResultScheduleInfoOnce = None,
        statutory_working_day: GetAlarmResponseBodyResultScheduleInfoStatutoryWorkingDay = None,
        type: str = None,
        weekly: GetAlarmResponseBodyResultScheduleInfoWeekly = None,
    ):
        self.once = once
        self.statutory_working_day = statutory_working_day
        self.type = type
        self.weekly = weekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.statutory_working_day:
            self.statutory_working_day.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = GetAlarmResponseBodyResultScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('StatutoryWorkingDay') is not None:
            temp_model = GetAlarmResponseBodyResultScheduleInfoStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m['StatutoryWorkingDay'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = GetAlarmResponseBodyResultScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class GetAlarmResponseBodyResult(TeaModel):
    def __init__(
        self,
        alarm_id: int = None,
        music_info: GetAlarmResponseBodyResultMusicInfo = None,
        schedule_info: GetAlarmResponseBodyResultScheduleInfo = None,
        schedule_type_desc: str = None,
        status: int = None,
        trigger_date_desc: str = None,
        trigger_time_desc: str = None,
        volume: int = None,
    ):
        self.alarm_id = alarm_id
        self.music_info = music_info
        self.schedule_info = schedule_info
        self.schedule_type_desc = schedule_type_desc
        self.status = status
        self.trigger_date_desc = trigger_date_desc
        self.trigger_time_desc = trigger_time_desc
        self.volume = volume

    def validate(self):
        if self.music_info:
            self.music_info.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.music_info is not None:
            result['MusicInfo'] = self.music_info.to_map()
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.schedule_type_desc is not None:
            result['ScheduleTypeDesc'] = self.schedule_type_desc
        if self.status is not None:
            result['Status'] = self.status
        if self.trigger_date_desc is not None:
            result['TriggerDateDesc'] = self.trigger_date_desc
        if self.trigger_time_desc is not None:
            result['TriggerTimeDesc'] = self.trigger_time_desc
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('MusicInfo') is not None:
            temp_model = GetAlarmResponseBodyResultMusicInfo()
            self.music_info = temp_model.from_map(m['MusicInfo'])
        if m.get('ScheduleInfo') is not None:
            temp_model = GetAlarmResponseBodyResultScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('ScheduleTypeDesc') is not None:
            self.schedule_type_desc = m.get('ScheduleTypeDesc')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TriggerDateDesc') is not None:
            self.trigger_date_desc = m.get('TriggerDateDesc')
        if m.get('TriggerTimeDesc') is not None:
            self.trigger_time_desc = m.get('TriggerTimeDesc')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class GetAlarmResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetAlarmResponseBodyResult = None,
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
            temp_model = GetAlarmResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAlarmResponseBody = None,
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
            temp_model = GetAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlbumHeaders(TeaModel):
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


class GetAlbumRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
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
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetAlbumResponseBodyResultAuthors(TeaModel):
    def __init__(
        self,
        author_types: List[str] = None,
        gender: str = None,
        id: int = None,
        online: bool = None,
        source: str = None,
        title: str = None,
    ):
        self.author_types = author_types
        self.gender = gender
        self.id = id
        self.online = online
        self.source = source
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetAlbumResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class GetAlbumResponseBodyResult(TeaModel):
    def __init__(
        self,
        alias: List[str] = None,
        audition: bool = None,
        authors: List[GetAlbumResponseBodyResultAuthors] = None,
        category: str = None,
        charge: bool = None,
        comm_cate_id: int = None,
        cover: GetAlbumResponseBodyResultCover = None,
        description: str = None,
        finished: str = None,
        hot_score: float = None,
        id: int = None,
        item_type: str = None,
        raw_id: str = None,
        source: str = None,
        title: str = None,
        total_episode: int = None,
        type: str = None,
        valid: str = None,
    ):
        self.alias = alias
        self.audition = audition
        self.authors = authors
        self.category = category
        self.charge = charge
        self.comm_cate_id = comm_cate_id
        self.cover = cover
        self.description = description
        self.finished = finished
        self.hot_score = hot_score
        self.id = id
        self.item_type = item_type
        self.raw_id = raw_id
        self.source = source
        self.title = title
        self.total_episode = total_episode
        self.type = type
        self.valid = valid

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.finished is not None:
            result['Finished'] = self.finished
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.total_episode is not None:
            result['TotalEpisode'] = self.total_episode
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = GetAlbumResponseBodyResultAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = GetAlbumResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Finished') is not None:
            self.finished = m.get('Finished')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TotalEpisode') is not None:
            self.total_episode = m.get('TotalEpisode')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class GetAlbumResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        request_id: str = None,
        result: GetAlbumResponseBodyResult = None,
    ):
        self.code = code
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
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.result is not None:
            result['Result'] = self.result.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Result') is not None:
            temp_model = GetAlbumResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAlbumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAlbumResponseBody = None,
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
            temp_model = GetAlbumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAlbumDetailByIdHeaders(TeaModel):
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


class GetAlbumDetailByIdRequest(TeaModel):
    def __init__(
        self,
        album_id: str = None,
    ):
        self.album_id = album_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        return self


class GetAlbumDetailByIdResponseBodyResultAlbumContentList(TeaModel):
    def __init__(
        self,
        duration: str = None,
        id: str = None,
        order_index: str = None,
        title: str = None,
    ):
        self.duration = duration
        self.id = id
        self.order_index = order_index
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.id is not None:
            result['Id'] = self.id
        if self.order_index is not None:
            result['OrderIndex'] = self.order_index
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetAlbumDetailByIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        album_content_list: List[GetAlbumDetailByIdResponseBodyResultAlbumContentList] = None,
        album_cover_url: str = None,
        album_description: str = None,
        album_id: str = None,
        album_title: str = None,
    ):
        self.album_content_list = album_content_list
        self.album_cover_url = album_cover_url
        self.album_description = album_description
        self.album_id = album_id
        self.album_title = album_title

    def validate(self):
        if self.album_content_list:
            for k in self.album_content_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AlbumContentList'] = []
        if self.album_content_list is not None:
            for k in self.album_content_list:
                result['AlbumContentList'].append(k.to_map() if k else None)
        if self.album_cover_url is not None:
            result['AlbumCoverUrl'] = self.album_cover_url
        if self.album_description is not None:
            result['AlbumDescription'] = self.album_description
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.album_title is not None:
            result['AlbumTitle'] = self.album_title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.album_content_list = []
        if m.get('AlbumContentList') is not None:
            for k in m.get('AlbumContentList'):
                temp_model = GetAlbumDetailByIdResponseBodyResultAlbumContentList()
                self.album_content_list.append(temp_model.from_map(k))
        if m.get('AlbumCoverUrl') is not None:
            self.album_cover_url = m.get('AlbumCoverUrl')
        if m.get('AlbumDescription') is not None:
            self.album_description = m.get('AlbumDescription')
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('AlbumTitle') is not None:
            self.album_title = m.get('AlbumTitle')
        return self


class GetAlbumDetailByIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetAlbumDetailByIdResponseBodyResult = None,
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
            temp_model = GetAlbumDetailByIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetAlbumDetailByIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAlbumDetailByIdResponseBody = None,
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
            temp_model = GetAlbumDetailByIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetAligenieUserInfoHeaders(TeaModel):
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


class GetAligenieUserInfoRequest(TeaModel):
    def __init__(
        self,
        login_state_access_token: str = None,
    ):
        # This parameter is required.
        self.login_state_access_token = login_state_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class GetAligenieUserInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        aligenie_nickname: str = None,
        avatar: str = None,
        deletable: bool = None,
    ):
        self.aligenie_nickname = aligenie_nickname
        self.avatar = avatar
        self.deletable = deletable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aligenie_nickname is not None:
            result['AligenieNickname'] = self.aligenie_nickname
        if self.avatar is not None:
            result['Avatar'] = self.avatar
        if self.deletable is not None:
            result['Deletable'] = self.deletable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AligenieNickname') is not None:
            self.aligenie_nickname = m.get('AligenieNickname')
        if m.get('Avatar') is not None:
            self.avatar = m.get('Avatar')
        if m.get('Deletable') is not None:
            self.deletable = m.get('Deletable')
        return self


class GetAligenieUserInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetAligenieUserInfoResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = GetAligenieUserInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetAligenieUserInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAligenieUserInfoResponseBody = None,
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
            temp_model = GetAligenieUserInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCodeEnhanceHeaders(TeaModel):
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


class GetCodeEnhanceRequestChannelInfo(TeaModel):
    def __init__(
        self,
        channel: str = None,
        ext_info: str = None,
    ):
        # This parameter is required.
        self.channel = channel
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class GetCodeEnhanceRequestUserInfo(TeaModel):
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


class GetCodeEnhanceRequest(TeaModel):
    def __init__(
        self,
        channel_info: GetCodeEnhanceRequestChannelInfo = None,
        user_info: GetCodeEnhanceRequestUserInfo = None,
    ):
        # This parameter is required.
        self.channel_info = channel_info
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.channel_info:
            self.channel_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_info is not None:
            result['ChannelInfo'] = self.channel_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelInfo') is not None:
            temp_model = GetCodeEnhanceRequestChannelInfo()
            self.channel_info = temp_model.from_map(m['ChannelInfo'])
        if m.get('UserInfo') is not None:
            temp_model = GetCodeEnhanceRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetCodeEnhanceShrinkRequest(TeaModel):
    def __init__(
        self,
        channel_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.channel_info_shrink = channel_info_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_info_shrink is not None:
            result['ChannelInfo'] = self.channel_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelInfo') is not None:
            self.channel_info_shrink = m.get('ChannelInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetCodeEnhanceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class GetCodeEnhanceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCodeEnhanceResponseBody = None,
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
            temp_model = GetCodeEnhanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetContentHeaders(TeaModel):
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


class GetContentRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        type: str = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
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
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class GetContentResponseBodyResultAuthors(TeaModel):
    def __init__(
        self,
        author_types: List[str] = None,
        gender: str = None,
        id: int = None,
        online: bool = None,
        source: str = None,
        title: str = None,
    ):
        self.author_types = author_types
        self.gender = gender
        self.id = id
        self.online = online
        self.source = source
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class GetContentResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class GetContentResponseBodyResult(TeaModel):
    def __init__(
        self,
        album_id: str = None,
        alias: List[str] = None,
        audition: bool = None,
        authors: List[GetContentResponseBodyResultAuthors] = None,
        category: str = None,
        charge: bool = None,
        comm_cate_id: int = None,
        cover: GetContentResponseBodyResultCover = None,
        description: str = None,
        duration: int = None,
        hot_score: float = None,
        id: int = None,
        item_type: str = None,
        lyric: str = None,
        raw_id: str = None,
        source: str = None,
        styles: List[str] = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        self.album_id = album_id
        self.alias = alias
        self.audition = audition
        self.authors = authors
        self.category = category
        self.charge = charge
        self.comm_cate_id = comm_cate_id
        self.cover = cover
        self.description = description
        self.duration = duration
        self.hot_score = hot_score
        self.id = id
        self.item_type = item_type
        self.lyric = lyric
        self.raw_id = raw_id
        self.source = source
        self.styles = styles
        self.title = title
        self.type = type
        self.valid = valid

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.lyric is not None:
            result['Lyric'] = self.lyric
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.styles is not None:
            result['Styles'] = self.styles
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = GetContentResponseBodyResultAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = GetContentResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Lyric') is not None:
            self.lyric = m.get('Lyric')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Styles') is not None:
            self.styles = m.get('Styles')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class GetContentResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetContentResponseBodyResult = None,
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
            temp_model = GetContentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetContentResponseBody = None,
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
            temp_model = GetContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCurrentPlayingItemHeaders(TeaModel):
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


class GetCurrentPlayingItemRequestDeviceInfo(TeaModel):
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


class GetCurrentPlayingItemRequestUserInfo(TeaModel):
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


class GetCurrentPlayingItemRequest(TeaModel):
    def __init__(
        self,
        device_info: GetCurrentPlayingItemRequestDeviceInfo = None,
        user_info: GetCurrentPlayingItemRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetCurrentPlayingItemRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = GetCurrentPlayingItemRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetCurrentPlayingItemShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetCurrentPlayingItemResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.mediam = mediam
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class GetCurrentPlayingItemResponseBodyResult(TeaModel):
    def __init__(
        self,
        album_name: str = None,
        album_raw_id: str = None,
        audio_length: int = None,
        copyright: int = None,
        cover: GetCurrentPlayingItemResponseBodyResultCover = None,
        default_play_order: int = None,
        item_url: str = None,
        liked: str = None,
        lyric_url: str = None,
        play_mode: str = None,
        pos: int = None,
        progress: int = None,
        raw_id: str = None,
        singer: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        self.album_name = album_name
        self.album_raw_id = album_raw_id
        self.audio_length = audio_length
        self.copyright = copyright
        self.cover = cover
        self.default_play_order = default_play_order
        self.item_url = item_url
        self.liked = liked
        self.lyric_url = lyric_url
        self.play_mode = play_mode
        self.pos = pos
        self.progress = progress
        self.raw_id = raw_id
        self.singer = singer
        self.source = source
        self.title = title
        self.type = type
        self.valid = valid

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.liked is not None:
            result['Liked'] = self.liked
        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singer is not None:
            result['Singer'] = self.singer
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('Cover') is not None:
            temp_model = GetCurrentPlayingItemResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')
        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singer') is not None:
            self.singer = m.get('Singer')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class GetCurrentPlayingItemResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetCurrentPlayingItemResponseBodyResult = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = GetCurrentPlayingItemResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCurrentPlayingItemResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCurrentPlayingItemResponseBody = None,
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
            temp_model = GetCurrentPlayingItemResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetCurrentPlayingListHeaders(TeaModel):
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


class GetCurrentPlayingListRequestDeviceInfo(TeaModel):
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


class GetCurrentPlayingListRequestOpenQueryPlayListRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class GetCurrentPlayingListRequestUserInfo(TeaModel):
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


class GetCurrentPlayingListRequest(TeaModel):
    def __init__(
        self,
        device_info: GetCurrentPlayingListRequestDeviceInfo = None,
        open_query_play_list_request: GetCurrentPlayingListRequestOpenQueryPlayListRequest = None,
        user_info: GetCurrentPlayingListRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.open_query_play_list_request = open_query_play_list_request
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_query_play_list_request:
            self.open_query_play_list_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_query_play_list_request is not None:
            result['OpenQueryPlayListRequest'] = self.open_query_play_list_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetCurrentPlayingListRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenQueryPlayListRequest') is not None:
            temp_model = GetCurrentPlayingListRequestOpenQueryPlayListRequest()
            self.open_query_play_list_request = temp_model.from_map(m['OpenQueryPlayListRequest'])
        if m.get('UserInfo') is not None:
            temp_model = GetCurrentPlayingListRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetCurrentPlayingListShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        open_query_play_list_request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.open_query_play_list_request_shrink = open_query_play_list_request_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_query_play_list_request_shrink is not None:
            result['OpenQueryPlayListRequest'] = self.open_query_play_list_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenQueryPlayListRequest') is not None:
            self.open_query_play_list_request_shrink = m.get('OpenQueryPlayListRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetCurrentPlayingListResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.mediam = mediam
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class GetCurrentPlayingListResponseBodyResult(TeaModel):
    def __init__(
        self,
        album_name: str = None,
        album_raw_id: str = None,
        audio_length: int = None,
        copyright: int = None,
        cover: GetCurrentPlayingListResponseBodyResultCover = None,
        default_play_order: int = None,
        item_url: str = None,
        liked: bool = None,
        lyric_url: str = None,
        play_mode: str = None,
        pos: int = None,
        progress: int = None,
        raw_id: str = None,
        singer: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        self.album_name = album_name
        self.album_raw_id = album_raw_id
        self.audio_length = audio_length
        self.copyright = copyright
        self.cover = cover
        self.default_play_order = default_play_order
        self.item_url = item_url
        self.liked = liked
        self.lyric_url = lyric_url
        self.play_mode = play_mode
        self.pos = pos
        self.progress = progress
        self.raw_id = raw_id
        self.singer = singer
        self.source = source
        self.title = title
        self.type = type
        self.valid = valid

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.liked is not None:
            result['Liked'] = self.liked
        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singer is not None:
            result['Singer'] = self.singer
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('Cover') is not None:
            temp_model = GetCurrentPlayingListResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')
        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singer') is not None:
            self.singer = m.get('Singer')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class GetCurrentPlayingListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[GetCurrentPlayingListResponseBodyResult] = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
        self.success = success

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
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
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = GetCurrentPlayingListResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class GetCurrentPlayingListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetCurrentPlayingListResponseBody = None,
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
            temp_model = GetCurrentPlayingListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceBasicInfoHeaders(TeaModel):
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


class GetDeviceBasicInfoRequestDeviceInfo(TeaModel):
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


class GetDeviceBasicInfoRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceBasicInfoRequestDeviceInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceBasicInfoRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class GetDeviceBasicInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class GetDeviceBasicInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        firmware_version: str = None,
        mac: str = None,
        name: str = None,
        sn: str = None,
    ):
        self.firmware_version = firmware_version
        self.mac = mac
        self.name = name
        self.sn = sn

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.firmware_version is not None:
            result['FirmwareVersion'] = self.firmware_version
        if self.mac is not None:
            result['Mac'] = self.mac
        if self.name is not None:
            result['Name'] = self.name
        if self.sn is not None:
            result['Sn'] = self.sn
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirmwareVersion') is not None:
            self.firmware_version = m.get('FirmwareVersion')
        if m.get('Mac') is not None:
            self.mac = m.get('Mac')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        if m.get('Sn') is not None:
            self.sn = m.get('Sn')
        return self


class GetDeviceBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetDeviceBasicInfoResponseBodyResult = None,
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
            temp_model = GetDeviceBasicInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceBasicInfoResponseBody = None,
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
            temp_model = GetDeviceBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceIdByIdentityHeaders(TeaModel):
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


class GetDeviceIdByIdentityRequest(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        identity_id: str = None,
        identity_type: str = None,
        product_key: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.identity_id = identity_id
        # This parameter is required.
        self.identity_type = identity_type
        self.product_key = product_key

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
        if self.identity_id is not None:
            result['IdentityId'] = self.identity_id
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdentityId') is not None:
            self.identity_id = m.get('IdentityId')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds(TeaModel):
    def __init__(
        self,
        device_union_id: str = None,
        organization_id: str = None,
    ):
        self.device_union_id = device_union_id
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class GetDeviceIdByIdentityResponseBodyResult(TeaModel):
    def __init__(
        self,
        device_open_id: str = None,
        device_union_ids: List[GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds] = None,
    ):
        self.device_open_id = device_open_id
        self.device_union_ids = device_union_ids

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
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k in self.device_union_ids:
                result['DeviceUnionIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k in m.get('DeviceUnionIds'):
                temp_model = GetDeviceIdByIdentityResponseBodyResultDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k))
        return self


class GetDeviceIdByIdentityResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetDeviceIdByIdentityResponseBodyResult = None,
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
            temp_model = GetDeviceIdByIdentityResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceIdByIdentityResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceIdByIdentityResponseBody = None,
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
            temp_model = GetDeviceIdByIdentityResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceSettingHeaders(TeaModel):
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


class GetDeviceSettingRequestDeviceInfo(TeaModel):
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


class GetDeviceSettingRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceSettingRequestDeviceInfo = None,
        keys: List[str] = None,
    ):
        self.device_info = device_info
        # This parameter is required.
        self.keys = keys

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceSettingRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class GetDeviceSettingShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        keys_shrink: str = None,
    ):
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.keys_shrink = keys_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.keys_shrink is not None:
            result['Keys'] = self.keys_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Keys') is not None:
            self.keys_shrink = m.get('Keys')
        return self


class GetDeviceSettingResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, Any] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class GetDeviceSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceSettingResponseBody = None,
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
            temp_model = GetDeviceSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceStatusDetailHeaders(TeaModel):
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


class GetDeviceStatusDetailRequestDeviceInfo(TeaModel):
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


class GetDeviceStatusDetailRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceStatusDetailRequestDeviceInfo = None,
        keys: List[str] = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.keys = keys

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.keys is not None:
            result['Keys'] = self.keys
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceStatusDetailRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Keys') is not None:
            self.keys = m.get('Keys')
        return self


class GetDeviceStatusDetailShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        keys_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.keys_shrink = keys_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.keys_shrink is not None:
            result['Keys'] = self.keys_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Keys') is not None:
            self.keys_shrink = m.get('Keys')
        return self


class GetDeviceStatusDetailResponseBodyResultPlayer(TeaModel):
    def __init__(
        self,
        audio_album: str = None,
        audio_anchor: str = None,
        audio_ext: str = None,
        audio_id: str = None,
        audio_length: str = None,
        audio_name: str = None,
        audio_source: str = None,
        audio_url: str = None,
        format: str = None,
        progress: str = None,
        source: str = None,
        status: str = None,
        timestamp: str = None,
    ):
        self.audio_album = audio_album
        self.audio_anchor = audio_anchor
        self.audio_ext = audio_ext
        self.audio_id = audio_id
        self.audio_length = audio_length
        self.audio_name = audio_name
        self.audio_source = audio_source
        self.audio_url = audio_url
        self.format = format
        self.progress = progress
        self.source = source
        self.status = status
        self.timestamp = timestamp

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.audio_album is not None:
            result['AudioAlbum'] = self.audio_album
        if self.audio_anchor is not None:
            result['AudioAnchor'] = self.audio_anchor
        if self.audio_ext is not None:
            result['AudioExt'] = self.audio_ext
        if self.audio_id is not None:
            result['AudioId'] = self.audio_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.audio_name is not None:
            result['AudioName'] = self.audio_name
        if self.audio_source is not None:
            result['AudioSource'] = self.audio_source
        if self.audio_url is not None:
            result['AudioUrl'] = self.audio_url
        if self.format is not None:
            result['Format'] = self.format
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.source is not None:
            result['Source'] = self.source
        if self.status is not None:
            result['Status'] = self.status
        if self.timestamp is not None:
            result['Timestamp'] = self.timestamp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioAlbum') is not None:
            self.audio_album = m.get('AudioAlbum')
        if m.get('AudioAnchor') is not None:
            self.audio_anchor = m.get('AudioAnchor')
        if m.get('AudioExt') is not None:
            self.audio_ext = m.get('AudioExt')
        if m.get('AudioId') is not None:
            self.audio_id = m.get('AudioId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('AudioName') is not None:
            self.audio_name = m.get('AudioName')
        if m.get('AudioSource') is not None:
            self.audio_source = m.get('AudioSource')
        if m.get('AudioUrl') is not None:
            self.audio_url = m.get('AudioUrl')
        if m.get('Format') is not None:
            self.format = m.get('Format')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Timestamp') is not None:
            self.timestamp = m.get('Timestamp')
        return self


class GetDeviceStatusDetailResponseBodyResultPower(TeaModel):
    def __init__(
        self,
        quantity: int = None,
        status: str = None,
    ):
        self.quantity = quantity
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.quantity is not None:
            result['Quantity'] = self.quantity
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Quantity') is not None:
            self.quantity = m.get('Quantity')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class GetDeviceStatusDetailResponseBodyResultSpeaker(TeaModel):
    def __init__(
        self,
        muted: bool = None,
        volume: int = None,
    ):
        self.muted = muted
        self.volume = volume

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.muted is not None:
            result['Muted'] = self.muted
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Muted') is not None:
            self.muted = m.get('Muted')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class GetDeviceStatusDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        player: GetDeviceStatusDetailResponseBodyResultPlayer = None,
        power: GetDeviceStatusDetailResponseBodyResultPower = None,
        speaker: GetDeviceStatusDetailResponseBodyResultSpeaker = None,
    ):
        self.player = player
        self.power = power
        self.speaker = speaker

    def validate(self):
        if self.player:
            self.player.validate()
        if self.power:
            self.power.validate()
        if self.speaker:
            self.speaker.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.player is not None:
            result['Player'] = self.player.to_map()
        if self.power is not None:
            result['Power'] = self.power.to_map()
        if self.speaker is not None:
            result['Speaker'] = self.speaker.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Player') is not None:
            temp_model = GetDeviceStatusDetailResponseBodyResultPlayer()
            self.player = temp_model.from_map(m['Player'])
        if m.get('Power') is not None:
            temp_model = GetDeviceStatusDetailResponseBodyResultPower()
            self.power = temp_model.from_map(m['Power'])
        if m.get('Speaker') is not None:
            temp_model = GetDeviceStatusDetailResponseBodyResultSpeaker()
            self.speaker = temp_model.from_map(m['Speaker'])
        return self


class GetDeviceStatusDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetDeviceStatusDetailResponseBodyResult = None,
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
            temp_model = GetDeviceStatusDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceStatusDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceStatusDetailResponseBody = None,
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
            temp_model = GetDeviceStatusDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceStatusInfoHeaders(TeaModel):
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


class GetDeviceStatusInfoRequestDeviceInfo(TeaModel):
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


class GetDeviceStatusInfoRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceStatusInfoRequestDeviceInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceStatusInfoRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class GetDeviceStatusInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class GetDeviceStatusInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        online: int = None,
    ):
        self.online = online

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.online is not None:
            result['Online'] = self.online
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Online') is not None:
            self.online = m.get('Online')
        return self


class GetDeviceStatusInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetDeviceStatusInfoResponseBodyResult = None,
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
            temp_model = GetDeviceStatusInfoResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceStatusInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceStatusInfoResponseBody = None,
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
            temp_model = GetDeviceStatusInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDeviceTagHeaders(TeaModel):
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


class GetDeviceTagRequestDeviceInfo(TeaModel):
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


class GetDeviceTagRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceTagRequestDeviceInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetDeviceTagRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class GetDeviceTagShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class GetDeviceTagResponseBodyResult(TeaModel):
    def __init__(
        self,
        device_tags: Dict[str, Any] = None,
    ):
        self.device_tags = device_tags

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_tags is not None:
            result['DeviceTags'] = self.device_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceTags') is not None:
            self.device_tags = m.get('DeviceTags')
        return self


class GetDeviceTagResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetDeviceTagResponseBodyResult = None,
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
            temp_model = GetDeviceTagResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetDeviceTagResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDeviceTagResponseBody = None,
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
            temp_model = GetDeviceTagResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetJiangSuTelecomDataHeaders(TeaModel):
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


class GetJiangSuTelecomDataRequest(TeaModel):
    def __init__(
        self,
        date: str = None,
    ):
        self.date = date

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.date is not None:
            result['Date'] = self.date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Date') is not None:
            self.date = m.get('Date')
        return self


class GetJiangSuTelecomDataResponseBodyResult(TeaModel):
    def __init__(
        self,
        oss_url: str = None,
    ):
        self.oss_url = oss_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')
        return self


class GetJiangSuTelecomDataResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetJiangSuTelecomDataResponseBodyResult = None,
    ):
        self.code = code
        # Id of the request
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
            temp_model = GetJiangSuTelecomDataResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetJiangSuTelecomDataResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetJiangSuTelecomDataResponseBody = None,
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
            temp_model = GetJiangSuTelecomDataResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetScheduleTaskHeaders(TeaModel):
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


class GetScheduleTaskRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class GetScheduleTaskRequestPayload(TeaModel):
    def __init__(
        self,
        id: int = None,
    ):
        # This parameter is required.
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


class GetScheduleTaskRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class GetScheduleTaskRequest(TeaModel):
    def __init__(
        self,
        device_info: GetScheduleTaskRequestDeviceInfo = None,
        payload: GetScheduleTaskRequestPayload = None,
        user_info: GetScheduleTaskRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetScheduleTaskRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetScheduleTaskRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetScheduleTaskRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetScheduleTaskShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetScheduleTaskResponseBodyResultActionTopicList(TeaModel):
    def __init__(
        self,
        custom_action: Dict[str, Any] = None,
    ):
        self.custom_action = custom_action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_action is not None:
            result['CustomAction'] = self.custom_action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomAction') is not None:
            self.custom_action = m.get('CustomAction')
        return self


class GetScheduleTaskResponseBodyResult(TeaModel):
    def __init__(
        self,
        action_topic_list: List[GetScheduleTaskResponseBodyResultActionTopicList] = None,
        cron: str = None,
        schedule_end_time: str = None,
        schedule_id: int = None,
        schedule_start_time: str = None,
        schedule_type: str = None,
    ):
        self.action_topic_list = action_topic_list
        self.cron = cron
        self.schedule_end_time = schedule_end_time
        self.schedule_id = schedule_id
        self.schedule_start_time = schedule_start_time
        self.schedule_type = schedule_type

    def validate(self):
        if self.action_topic_list:
            for k in self.action_topic_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ActionTopicList'] = []
        if self.action_topic_list is not None:
            for k in self.action_topic_list:
                result['ActionTopicList'].append(k.to_map() if k else None)
        if self.cron is not None:
            result['Cron'] = self.cron
        if self.schedule_end_time is not None:
            result['ScheduleEndTime'] = self.schedule_end_time
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        if self.schedule_start_time is not None:
            result['ScheduleStartTime'] = self.schedule_start_time
        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_topic_list = []
        if m.get('ActionTopicList') is not None:
            for k in m.get('ActionTopicList'):
                temp_model = GetScheduleTaskResponseBodyResultActionTopicList()
                self.action_topic_list.append(temp_model.from_map(k))
        if m.get('Cron') is not None:
            self.cron = m.get('Cron')
        if m.get('ScheduleEndTime') is not None:
            self.schedule_end_time = m.get('ScheduleEndTime')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        if m.get('ScheduleStartTime') is not None:
            self.schedule_start_time = m.get('ScheduleStartTime')
        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')
        return self


class GetScheduleTaskResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetScheduleTaskResponseBodyResult = None,
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
            temp_model = GetScheduleTaskResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetScheduleTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetScheduleTaskResponseBody = None,
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
            temp_model = GetScheduleTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUnreadMessageCountHeaders(TeaModel):
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


class GetUnreadMessageCountRequestUserInfo(TeaModel):
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


class GetUnreadMessageCountRequest(TeaModel):
    def __init__(
        self,
        user_info: GetUnreadMessageCountRequestUserInfo = None,
    ):
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = GetUnreadMessageCountRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetUnreadMessageCountShrinkRequest(TeaModel):
    def __init__(
        self,
        user_info_shrink: str = None,
    ):
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetUnreadMessageCountResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        result: int = None,
    ):
        self.code = code
        self.message = message
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class GetUnreadMessageCountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUnreadMessageCountResponseBody = None,
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
            temp_model = GetUnreadMessageCountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserByDeviceIdHeaders(TeaModel):
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


class GetUserByDeviceIdRequestDeviceInfo(TeaModel):
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


class GetUserByDeviceIdRequest(TeaModel):
    def __init__(
        self,
        device_info: GetUserByDeviceIdRequestDeviceInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetUserByDeviceIdRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        return self


class GetUserByDeviceIdShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        return self


class GetUserByDeviceIdResponseBodyResultUserUnionIds(TeaModel):
    def __init__(
        self,
        organization_id: str = None,
        user_union_id: str = None,
    ):
        self.organization_id = organization_id
        self.user_union_id = user_union_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        if self.user_union_id is not None:
            result['UserUnionId'] = self.user_union_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        if m.get('UserUnionId') is not None:
            self.user_union_id = m.get('UserUnionId')
        return self


class GetUserByDeviceIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        user_open_id: str = None,
        user_union_ids: List[GetUserByDeviceIdResponseBodyResultUserUnionIds] = None,
    ):
        self.user_open_id = user_open_id
        self.user_union_ids = user_union_ids

    def validate(self):
        if self.user_union_ids:
            for k in self.user_union_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        result['UserUnionIds'] = []
        if self.user_union_ids is not None:
            for k in self.user_union_ids:
                result['UserUnionIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        self.user_union_ids = []
        if m.get('UserUnionIds') is not None:
            for k in m.get('UserUnionIds'):
                temp_model = GetUserByDeviceIdResponseBodyResultUserUnionIds()
                self.user_union_ids.append(temp_model.from_map(k))
        return self


class GetUserByDeviceIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetUserByDeviceIdResponseBodyResult = None,
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
            temp_model = GetUserByDeviceIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetUserByDeviceIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUserByDeviceIdResponseBody = None,
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
            temp_model = GetUserByDeviceIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetWeatherHeaders(TeaModel):
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


class GetWeatherRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class GetWeatherRequestPayload(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class GetWeatherRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class GetWeatherRequest(TeaModel):
    def __init__(
        self,
        device_info: GetWeatherRequestDeviceInfo = None,
        payload: GetWeatherRequestPayload = None,
        user_info: GetWeatherRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = GetWeatherRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = GetWeatherRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = GetWeatherRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class GetWeatherShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class GetWeatherResponseBodyResultCurrentMeteorologyTemperature(TeaModel):
    def __init__(
        self,
        current: str = None,
        current_desc: str = None,
        high: str = None,
        high_desc: str = None,
        logical: str = None,
        low: str = None,
        low_desc: str = None,
    ):
        self.current = current
        self.current_desc = current_desc
        self.high = high
        self.high_desc = high_desc
        self.logical = logical
        self.low = low
        self.low_desc = low_desc

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current is not None:
            result['Current'] = self.current
        if self.current_desc is not None:
            result['CurrentDesc'] = self.current_desc
        if self.high is not None:
            result['High'] = self.high
        if self.high_desc is not None:
            result['HighDesc'] = self.high_desc
        if self.logical is not None:
            result['Logical'] = self.logical
        if self.low is not None:
            result['Low'] = self.low
        if self.low_desc is not None:
            result['LowDesc'] = self.low_desc
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')
        if m.get('CurrentDesc') is not None:
            self.current_desc = m.get('CurrentDesc')
        if m.get('High') is not None:
            self.high = m.get('High')
        if m.get('HighDesc') is not None:
            self.high_desc = m.get('HighDesc')
        if m.get('Logical') is not None:
            self.logical = m.get('Logical')
        if m.get('Low') is not None:
            self.low = m.get('Low')
        if m.get('LowDesc') is not None:
            self.low_desc = m.get('LowDesc')
        return self


class GetWeatherResponseBodyResultCurrentMeteorologyWeather(TeaModel):
    def __init__(
        self,
        code: str = None,
        name: str = None,
    ):
        self.code = code
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.name is not None:
            result['Name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Name') is not None:
            self.name = m.get('Name')
        return self


class GetWeatherResponseBodyResultCurrentMeteorology(TeaModel):
    def __init__(
        self,
        temperature: GetWeatherResponseBodyResultCurrentMeteorologyTemperature = None,
        weather: GetWeatherResponseBodyResultCurrentMeteorologyWeather = None,
    ):
        self.temperature = temperature
        self.weather = weather

    def validate(self):
        if self.temperature:
            self.temperature.validate()
        if self.weather:
            self.weather.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.temperature is not None:
            result['Temperature'] = self.temperature.to_map()
        if self.weather is not None:
            result['Weather'] = self.weather.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Temperature') is not None:
            temp_model = GetWeatherResponseBodyResultCurrentMeteorologyTemperature()
            self.temperature = temp_model.from_map(m['Temperature'])
        if m.get('Weather') is not None:
            temp_model = GetWeatherResponseBodyResultCurrentMeteorologyWeather()
            self.weather = temp_model.from_map(m['Weather'])
        return self


class GetWeatherResponseBodyResult(TeaModel):
    def __init__(
        self,
        current_meteorology: GetWeatherResponseBodyResultCurrentMeteorology = None,
    ):
        self.current_meteorology = current_meteorology

    def validate(self):
        if self.current_meteorology:
            self.current_meteorology.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_meteorology is not None:
            result['CurrentMeteorology'] = self.current_meteorology.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentMeteorology') is not None:
            temp_model = GetWeatherResponseBodyResultCurrentMeteorology()
            self.current_meteorology = temp_model.from_map(m['CurrentMeteorology'])
        return self


class GetWeatherResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: GetWeatherResponseBodyResult = None,
    ):
        # HttpCode
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
            temp_model = GetWeatherResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class GetWeatherResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetWeatherResponseBody = None,
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
            temp_model = GetWeatherResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class IndexControlPlayingListHeaders(TeaModel):
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


class IndexControlPlayingListRequestDeviceInfo(TeaModel):
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


class IndexControlPlayingListRequestOpenIndexControlRequest(TeaModel):
    def __init__(
        self,
        extend_info: Dict[str, Any] = None,
        index: int = None,
        need_content_continued: bool = None,
    ):
        self.extend_info = extend_info
        # This parameter is required.
        self.index = index
        self.need_content_continued = need_content_continued

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.index is not None:
            result['Index'] = self.index
        if self.need_content_continued is not None:
            result['NeedContentContinued'] = self.need_content_continued
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Index') is not None:
            self.index = m.get('Index')
        if m.get('NeedContentContinued') is not None:
            self.need_content_continued = m.get('NeedContentContinued')
        return self


class IndexControlPlayingListRequestUserInfo(TeaModel):
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


class IndexControlPlayingListRequest(TeaModel):
    def __init__(
        self,
        device_info: IndexControlPlayingListRequestDeviceInfo = None,
        open_index_control_request: IndexControlPlayingListRequestOpenIndexControlRequest = None,
        user_info: IndexControlPlayingListRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.open_index_control_request = open_index_control_request
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_index_control_request:
            self.open_index_control_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_index_control_request is not None:
            result['OpenIndexControlRequest'] = self.open_index_control_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = IndexControlPlayingListRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenIndexControlRequest') is not None:
            temp_model = IndexControlPlayingListRequestOpenIndexControlRequest()
            self.open_index_control_request = temp_model.from_map(m['OpenIndexControlRequest'])
        if m.get('UserInfo') is not None:
            temp_model = IndexControlPlayingListRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class IndexControlPlayingListShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        open_index_control_request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.open_index_control_request_shrink = open_index_control_request_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_index_control_request_shrink is not None:
            result['OpenIndexControlRequest'] = self.open_index_control_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenIndexControlRequest') is not None:
            self.open_index_control_request_shrink = m.get('OpenIndexControlRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class IndexControlPlayingListResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.mediam = mediam
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class IndexControlPlayingListResponseBodyResult(TeaModel):
    def __init__(
        self,
        album_name: str = None,
        album_raw_id: str = None,
        audio_length: int = None,
        copyright: int = None,
        cover: IndexControlPlayingListResponseBodyResultCover = None,
        default_play_order: int = None,
        item_url: str = None,
        liked: bool = None,
        lyric_url: str = None,
        play_mode: str = None,
        pos: int = None,
        progress: int = None,
        raw_id: str = None,
        singer: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        self.album_name = album_name
        self.album_raw_id = album_raw_id
        self.audio_length = audio_length
        self.copyright = copyright
        self.cover = cover
        self.default_play_order = default_play_order
        self.item_url = item_url
        self.liked = liked
        self.lyric_url = lyric_url
        self.play_mode = play_mode
        self.pos = pos
        self.progress = progress
        self.raw_id = raw_id
        self.singer = singer
        self.source = source
        self.title = title
        self.type = type
        self.valid = valid

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.liked is not None:
            result['Liked'] = self.liked
        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singer is not None:
            result['Singer'] = self.singer
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('Cover') is not None:
            temp_model = IndexControlPlayingListResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')
        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singer') is not None:
            self.singer = m.get('Singer')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class IndexControlPlayingListResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: IndexControlPlayingListResponseBodyResult = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = IndexControlPlayingListResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class IndexControlPlayingListResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IndexControlPlayingListResponseBody = None,
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
            temp_model = IndexControlPlayingListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class InvalidateThirdPartyAppLoginStateHeaders(TeaModel):
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


class InvalidateThirdPartyAppLoginStateRequestDeviceInfo(TeaModel):
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


class InvalidateThirdPartyAppLoginStateRequest(TeaModel):
    def __init__(
        self,
        device_info: InvalidateThirdPartyAppLoginStateRequestDeviceInfo = None,
        third_party_app_id: str = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.third_party_app_id = third_party_app_id

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.third_party_app_id is not None:
            result['ThirdPartyAppId'] = self.third_party_app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = InvalidateThirdPartyAppLoginStateRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('ThirdPartyAppId') is not None:
            self.third_party_app_id = m.get('ThirdPartyAppId')
        return self


class InvalidateThirdPartyAppLoginStateShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        third_party_app_id: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.third_party_app_id = third_party_app_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.third_party_app_id is not None:
            result['ThirdPartyAppId'] = self.third_party_app_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('ThirdPartyAppId') is not None:
            self.third_party_app_id = m.get('ThirdPartyAppId')
        return self


class InvalidateThirdPartyAppLoginStateResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
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


class InvalidateThirdPartyAppLoginStateResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: InvalidateThirdPartyAppLoginStateResponseBody = None,
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
            temp_model = InvalidateThirdPartyAppLoginStateResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlarmsHeaders(TeaModel):
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


class ListAlarmsRequestDeviceInfo(TeaModel):
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


class ListAlarmsRequestPayload(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAlarmsRequestUserInfo(TeaModel):
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


class ListAlarmsRequest(TeaModel):
    def __init__(
        self,
        device_info: ListAlarmsRequestDeviceInfo = None,
        payload: ListAlarmsRequestPayload = None,
        user_info: ListAlarmsRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListAlarmsRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = ListAlarmsRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = ListAlarmsRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListAlarmsShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListAlarmsResponseBodyResultModelMusicInfo(TeaModel):
    def __init__(
        self,
        music_id: int = None,
        music_name: str = None,
        music_type: int = None,
        music_type_name: str = None,
        music_url: str = None,
    ):
        self.music_id = music_id
        self.music_name = music_name
        self.music_type = music_type
        self.music_type_name = music_type_name
        self.music_url = music_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        return self


class ListAlarmsResponseBodyResultModelScheduleInfoOnce(TeaModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class ListAlarmsResponseBodyResultModelScheduleInfoStatutoryWorkingDay(TeaModel):
    def __init__(
        self,
        hour: int = None,
        minute: int = None,
    ):
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class ListAlarmsResponseBodyResultModelScheduleInfoWeekly(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class ListAlarmsResponseBodyResultModelScheduleInfo(TeaModel):
    def __init__(
        self,
        once: ListAlarmsResponseBodyResultModelScheduleInfoOnce = None,
        statutory_working_day: ListAlarmsResponseBodyResultModelScheduleInfoStatutoryWorkingDay = None,
        type: str = None,
        weekly: ListAlarmsResponseBodyResultModelScheduleInfoWeekly = None,
    ):
        self.once = once
        self.statutory_working_day = statutory_working_day
        self.type = type
        self.weekly = weekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.statutory_working_day:
            self.statutory_working_day.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = ListAlarmsResponseBodyResultModelScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('StatutoryWorkingDay') is not None:
            temp_model = ListAlarmsResponseBodyResultModelScheduleInfoStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m['StatutoryWorkingDay'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = ListAlarmsResponseBodyResultModelScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class ListAlarmsResponseBodyResultModel(TeaModel):
    def __init__(
        self,
        alarm_id: int = None,
        music_info: ListAlarmsResponseBodyResultModelMusicInfo = None,
        schedule_info: ListAlarmsResponseBodyResultModelScheduleInfo = None,
        schedule_type_desc: str = None,
        status: int = None,
        trigger_date_desc: str = None,
        trigger_time_desc: str = None,
        volume: int = None,
    ):
        self.alarm_id = alarm_id
        self.music_info = music_info
        self.schedule_info = schedule_info
        self.schedule_type_desc = schedule_type_desc
        self.status = status
        self.trigger_date_desc = trigger_date_desc
        self.trigger_time_desc = trigger_time_desc
        self.volume = volume

    def validate(self):
        if self.music_info:
            self.music_info.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.music_info is not None:
            result['MusicInfo'] = self.music_info.to_map()
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.schedule_type_desc is not None:
            result['ScheduleTypeDesc'] = self.schedule_type_desc
        if self.status is not None:
            result['Status'] = self.status
        if self.trigger_date_desc is not None:
            result['TriggerDateDesc'] = self.trigger_date_desc
        if self.trigger_time_desc is not None:
            result['TriggerTimeDesc'] = self.trigger_time_desc
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('MusicInfo') is not None:
            temp_model = ListAlarmsResponseBodyResultModelMusicInfo()
            self.music_info = temp_model.from_map(m['MusicInfo'])
        if m.get('ScheduleInfo') is not None:
            temp_model = ListAlarmsResponseBodyResultModelScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('ScheduleTypeDesc') is not None:
            self.schedule_type_desc = m.get('ScheduleTypeDesc')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('TriggerDateDesc') is not None:
            self.trigger_date_desc = m.get('TriggerDateDesc')
        if m.get('TriggerTimeDesc') is not None:
            self.trigger_time_desc = m.get('TriggerTimeDesc')
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class ListAlarmsResponseBodyResult(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        model: List[ListAlarmsResponseBodyResultModel] = None,
        page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.model = model
        self.page_count = page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = ListAlarmsResponseBodyResultModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListAlarmsResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListAlarmsResponseBodyResult = None,
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
            temp_model = ListAlarmsResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListAlarmsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlarmsResponseBody = None,
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
            temp_model = ListAlarmsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlbumDetailHeaders(TeaModel):
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


class ListAlbumDetailRequest(TeaModel):
    def __init__(
        self,
        id: int = None,
        page_num: int = None,
        page_size: int = None,
    ):
        # This parameter is required.
        self.id = id
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListAlbumDetailResponseBodyResultOpenDataItemListAuthors(TeaModel):
    def __init__(
        self,
        author_types: List[str] = None,
        gender: str = None,
        id: int = None,
        online: bool = None,
        source: str = None,
        title: str = None,
    ):
        self.author_types = author_types
        self.gender = gender
        self.id = id
        self.online = online
        self.source = source
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListAlbumDetailResponseBodyResultOpenDataItemListCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListAlbumDetailResponseBodyResultOpenDataItemList(TeaModel):
    def __init__(
        self,
        alias: List[str] = None,
        audition: bool = None,
        authors: List[ListAlbumDetailResponseBodyResultOpenDataItemListAuthors] = None,
        category: str = None,
        charge: bool = None,
        comm_cate_id: int = None,
        cover: ListAlbumDetailResponseBodyResultOpenDataItemListCover = None,
        description: str = None,
        duration: int = None,
        hot_score: float = None,
        id: int = None,
        item_type: str = None,
        order_index: int = None,
        raw_id: str = None,
        source: str = None,
        styles: List[str] = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        self.alias = alias
        self.audition = audition
        self.authors = authors
        self.category = category
        self.charge = charge
        self.comm_cate_id = comm_cate_id
        self.cover = cover
        self.description = description
        self.duration = duration
        self.hot_score = hot_score
        self.id = id
        self.item_type = item_type
        self.order_index = order_index
        self.raw_id = raw_id
        self.source = source
        self.styles = styles
        self.title = title
        self.type = type
        self.valid = valid

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.order_index is not None:
            result['OrderIndex'] = self.order_index
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.styles is not None:
            result['Styles'] = self.styles
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = ListAlbumDetailResponseBodyResultOpenDataItemListAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = ListAlbumDetailResponseBodyResultOpenDataItemListCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Styles') is not None:
            self.styles = m.get('Styles')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class ListAlbumDetailResponseBodyResult(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        open_data_item_list: List[ListAlbumDetailResponseBodyResultOpenDataItemList] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.current_page_num = current_page_num
        self.open_data_item_list = open_data_item_list
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.open_data_item_list:
            for k in self.open_data_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['OpenDataItemList'] = []
        if self.open_data_item_list is not None:
            for k in self.open_data_item_list:
                result['OpenDataItemList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.open_data_item_list = []
        if m.get('OpenDataItemList') is not None:
            for k in m.get('OpenDataItemList'):
                temp_model = ListAlbumDetailResponseBodyResultOpenDataItemList()
                self.open_data_item_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListAlbumDetailResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListAlbumDetailResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = ListAlbumDetailResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListAlbumDetailResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlbumDetailResponseBody = None,
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
            temp_model = ListAlbumDetailResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAlbumIsAddedHeaders(TeaModel):
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


class ListAlbumIsAddedRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class ListAlbumIsAddedRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class ListAlbumIsAddedRequest(TeaModel):
    def __init__(
        self,
        album_id_list: List[str] = None,
        device_info: ListAlbumIsAddedRequestDeviceInfo = None,
        user_info: ListAlbumIsAddedRequestUserInfo = None,
    ):
        self.album_id_list = album_id_list
        self.device_info = device_info
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id_list is not None:
            result['AlbumIdList'] = self.album_id_list
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumIdList') is not None:
            self.album_id_list = m.get('AlbumIdList')
        if m.get('DeviceInfo') is not None:
            temp_model = ListAlbumIsAddedRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = ListAlbumIsAddedRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListAlbumIsAddedShrinkRequest(TeaModel):
    def __init__(
        self,
        album_id_list_shrink: str = None,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.album_id_list_shrink = album_id_list_shrink
        self.device_info_shrink = device_info_shrink
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id_list_shrink is not None:
            result['AlbumIdList'] = self.album_id_list_shrink
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumIdList') is not None:
            self.album_id_list_shrink = m.get('AlbumIdList')
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListAlbumIsAddedResponseBodyResult(TeaModel):
    def __init__(
        self,
        album_id: str = None,
        is_added: str = None,
    ):
        self.album_id = album_id
        self.is_added = is_added

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.is_added is not None:
            result['IsAdded'] = self.is_added
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('IsAdded') is not None:
            self.is_added = m.get('IsAdded')
        return self


class ListAlbumIsAddedResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListAlbumIsAddedResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListAlbumIsAddedResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListAlbumIsAddedResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAlbumIsAddedResponseBody = None,
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
            temp_model = ListAlbumIsAddedResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCateContentHeaders(TeaModel):
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


class ListCateContentRequestDeviceInfo(TeaModel):
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


class ListCateContentRequestRequest(TeaModel):
    def __init__(
        self,
        cate_id: int = None,
        is_album: bool = None,
        page_num: int = None,
        page_size: int = None,
        sort_by: str = None,
        sort_order: str = None,
    ):
        # This parameter is required.
        self.cate_id = cate_id
        # This parameter is required.
        self.is_album = is_album
        # This parameter is required.
        self.page_num = page_num
        # This parameter is required.
        self.page_size = page_size
        self.sort_by = sort_by
        # This parameter is required.
        self.sort_order = sort_order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.is_album is not None:
            result['IsAlbum'] = self.is_album
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.sort_by is not None:
            result['SortBy'] = self.sort_by
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('IsAlbum') is not None:
            self.is_album = m.get('IsAlbum')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('SortBy') is not None:
            self.sort_by = m.get('SortBy')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        return self


class ListCateContentRequestUserInfo(TeaModel):
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


class ListCateContentRequest(TeaModel):
    def __init__(
        self,
        device_info: ListCateContentRequestDeviceInfo = None,
        request: ListCateContentRequestRequest = None,
        user_info: ListCateContentRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.request = request
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.request:
            self.request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListCateContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Request') is not None:
            temp_model = ListCateContentRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        if m.get('UserInfo') is not None:
            temp_model = ListCateContentRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListCateContentShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.request_shrink = request_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListCateContentResponseBodyResultOpenDataItemListAuthorsCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.mediam = mediam
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListCateContentResponseBodyResultOpenDataItemListAuthors(TeaModel):
    def __init__(
        self,
        author_types: List[str] = None,
        cover: ListCateContentResponseBodyResultOpenDataItemListAuthorsCover = None,
        description: str = None,
        gender: str = None,
        id: int = None,
        online: bool = None,
        raw_id: str = None,
        source: str = None,
        title: str = None,
    ):
        self.author_types = author_types
        self.cover = cover
        self.description = description
        self.gender = gender
        self.id = id
        self.online = online
        self.raw_id = raw_id
        self.source = source
        self.title = title

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Cover') is not None:
            temp_model = ListCateContentResponseBodyResultOpenDataItemListAuthorsCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListCateContentResponseBodyResultOpenDataItemListCover(TeaModel):
    def __init__(
        self,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
        can_resize: bool = None,
    ):
        self.img = img
        self.large = large
        self.mediam = mediam
        self.medium = medium
        self.small = small
        self.can_resize = can_resize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        if self.can_resize is not None:
            result['canResize'] = self.can_resize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        if m.get('canResize') is not None:
            self.can_resize = m.get('canResize')
        return self


class ListCateContentResponseBodyResultOpenDataItemList(TeaModel):
    def __init__(
        self,
        alias: List[str] = None,
        audition: bool = None,
        authors: List[ListCateContentResponseBodyResultOpenDataItemListAuthors] = None,
        category: str = None,
        charge: bool = None,
        comm_cate_id: str = None,
        cover: ListCateContentResponseBodyResultOpenDataItemListCover = None,
        description: str = None,
        hot_score: float = None,
        item_type: str = None,
        raw_id: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        valid: str = None,
        id: int = None,
    ):
        self.alias = alias
        self.audition = audition
        self.authors = authors
        self.category = category
        self.charge = charge
        self.comm_cate_id = comm_cate_id
        self.cover = cover
        self.description = description
        self.hot_score = hot_score
        self.item_type = item_type
        self.raw_id = raw_id
        self.source = source
        self.title = title
        self.type = type
        self.valid = valid
        self.id = id

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        if self.id is not None:
            result['id'] = self.id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = ListCateContentResponseBodyResultOpenDataItemListAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = ListCateContentResponseBodyResultOpenDataItemListCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        if m.get('id') is not None:
            self.id = m.get('id')
        return self


class ListCateContentResponseBodyResult(TeaModel):
    def __init__(
        self,
        current_page_num: int = None,
        open_data_item_list: List[ListCateContentResponseBodyResultOpenDataItemList] = None,
        page_size: int = None,
        total_size: int = None,
    ):
        self.current_page_num = current_page_num
        self.open_data_item_list = open_data_item_list
        self.page_size = page_size
        self.total_size = total_size

    def validate(self):
        if self.open_data_item_list:
            for k in self.open_data_item_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page_num is not None:
            result['CurrentPageNum'] = self.current_page_num
        result['OpenDataItemList'] = []
        if self.open_data_item_list is not None:
            for k in self.open_data_item_list:
                result['OpenDataItemList'].append(k.to_map() if k else None)
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_size is not None:
            result['TotalSize'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPageNum') is not None:
            self.current_page_num = m.get('CurrentPageNum')
        self.open_data_item_list = []
        if m.get('OpenDataItemList') is not None:
            for k in m.get('OpenDataItemList'):
                temp_model = ListCateContentResponseBodyResultOpenDataItemList()
                self.open_data_item_list.append(temp_model.from_map(k))
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')
        return self


class ListCateContentResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListCateContentResponseBodyResult = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = ListCateContentResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListCateContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCateContentResponseBody = None,
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
            temp_model = ListCateContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCateInfoHeaders(TeaModel):
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


class ListCateInfoRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListCateInfoResponseBodyResult(TeaModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
        parent_cate_id: int = None,
    ):
        self.cate_id = cate_id
        self.cate_name = cate_name
        self.parent_cate_id = parent_cate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.parent_cate_id is not None:
            result['ParentCateId'] = self.parent_cate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('ParentCateId') is not None:
            self.parent_cate_id = m.get('ParentCateId')
        return self


class ListCateInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListCateInfoResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCateInfoResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListCateInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCateInfoResponseBody = None,
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
            temp_model = ListCateInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommonCateFirstFloorHeaders(TeaModel):
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


class ListCommonCateFirstFloorRequest(TeaModel):
    def __init__(
        self,
        type: str = None,
    ):
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListCommonCateFirstFloorResponseBodyResult(TeaModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
        parent_cate_id: int = None,
    ):
        self.cate_id = cate_id
        self.cate_name = cate_name
        self.parent_cate_id = parent_cate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.parent_cate_id is not None:
            result['ParentCateId'] = self.parent_cate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('ParentCateId') is not None:
            self.parent_cate_id = m.get('ParentCateId')
        return self


class ListCommonCateFirstFloorResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListCommonCateFirstFloorResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCommonCateFirstFloorResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListCommonCateFirstFloorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCommonCateFirstFloorResponseBody = None,
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
            temp_model = ListCommonCateFirstFloorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListCommonCateSecondFloorHeaders(TeaModel):
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


class ListCommonCateSecondFloorRequest(TeaModel):
    def __init__(
        self,
        parent_cate_id: int = None,
    ):
        self.parent_cate_id = parent_cate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.parent_cate_id is not None:
            result['ParentCateId'] = self.parent_cate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ParentCateId') is not None:
            self.parent_cate_id = m.get('ParentCateId')
        return self


class ListCommonCateSecondFloorResponseBodyResult(TeaModel):
    def __init__(
        self,
        cate_id: int = None,
        cate_name: str = None,
        parent_cate_id: int = None,
    ):
        self.cate_id = cate_id
        self.cate_name = cate_name
        self.parent_cate_id = parent_cate_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate_id is not None:
            result['CateId'] = self.cate_id
        if self.cate_name is not None:
            result['CateName'] = self.cate_name
        if self.parent_cate_id is not None:
            result['ParentCateId'] = self.parent_cate_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CateId') is not None:
            self.cate_id = m.get('CateId')
        if m.get('CateName') is not None:
            self.cate_name = m.get('CateName')
        if m.get('ParentCateId') is not None:
            self.parent_cate_id = m.get('ParentCateId')
        return self


class ListCommonCateSecondFloorResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListCommonCateSecondFloorResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListCommonCateSecondFloorResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListCommonCateSecondFloorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListCommonCateSecondFloorResponseBody = None,
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
            temp_model = ListCommonCateSecondFloorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceBasicInfoHeaders(TeaModel):
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


class ListDeviceBasicInfoRequestDeviceInfos(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id_type: str = None,
        ids: List[str] = None,
        organization_id: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        # This parameter is required.
        self.id_type = id_type
        self.ids = ids
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
        if self.id_type is not None:
            result['IdType'] = self.id_type
        if self.ids is not None:
            result['Ids'] = self.ids
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdType') is not None:
            self.id_type = m.get('IdType')
        if m.get('Ids') is not None:
            self.ids = m.get('Ids')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListDeviceBasicInfoRequest(TeaModel):
    def __init__(
        self,
        device_infos: ListDeviceBasicInfoRequestDeviceInfos = None,
    ):
        self.device_infos = device_infos

    def validate(self):
        if self.device_infos:
            self.device_infos.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_infos is not None:
            result['DeviceInfos'] = self.device_infos.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfos') is not None:
            temp_model = ListDeviceBasicInfoRequestDeviceInfos()
            self.device_infos = temp_model.from_map(m['DeviceInfos'])
        return self


class ListDeviceBasicInfoShrinkRequest(TeaModel):
    def __init__(
        self,
        device_infos_shrink: str = None,
    ):
        self.device_infos_shrink = device_infos_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_infos_shrink is not None:
            result['DeviceInfos'] = self.device_infos_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfos') is not None:
            self.device_infos_shrink = m.get('DeviceInfos')
        return self


class ListDeviceBasicInfoResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, ResultValue] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for v in self.result.values():
                if v:
                    v.validate()

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
        result['Result'] = {}
        if self.result is not None:
            for k, v in self.result.items():
                result['Result'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = {}
        if m.get('Result') is not None:
            for k, v in m.get('Result').items():
                temp_model = ResultValue()
                self.result[k] = temp_model.from_map(v)
        return self


class ListDeviceBasicInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceBasicInfoResponseBody = None,
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
            temp_model = ListDeviceBasicInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceByUserIdHeaders(TeaModel):
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


class ListDeviceByUserIdRequestUserInfo(TeaModel):
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


class ListDeviceByUserIdRequest(TeaModel):
    def __init__(
        self,
        user_info: ListDeviceByUserIdRequestUserInfo = None,
    ):
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            temp_model = ListDeviceByUserIdRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListDeviceByUserIdShrinkRequest(TeaModel):
    def __init__(
        self,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListDeviceByUserIdResponseBodyResultDeviceUnionIds(TeaModel):
    def __init__(
        self,
        device_union_id: str = None,
        organization_id: str = None,
    ):
        self.device_union_id = device_union_id
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListDeviceByUserIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        device_open_id: str = None,
        device_union_ids: List[ListDeviceByUserIdResponseBodyResultDeviceUnionIds] = None,
    ):
        self.device_open_id = device_open_id
        self.device_union_ids = device_union_ids

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
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k in self.device_union_ids:
                result['DeviceUnionIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k in m.get('DeviceUnionIds'):
                temp_model = ListDeviceByUserIdResponseBodyResultDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k))
        return self


class ListDeviceByUserIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListDeviceByUserIdResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDeviceByUserIdResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDeviceByUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceByUserIdResponseBody = None,
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
            temp_model = ListDeviceByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceByUserIdAndChanelHeaders(TeaModel):
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


class ListDeviceByUserIdAndChanelRequestChannelInfo(TeaModel):
    def __init__(
        self,
        channel: str = None,
        ext_info: str = None,
    ):
        # This parameter is required.
        self.channel = channel
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel is not None:
            result['Channel'] = self.channel
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Channel') is not None:
            self.channel = m.get('Channel')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class ListDeviceByUserIdAndChanelRequestUserInfo(TeaModel):
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


class ListDeviceByUserIdAndChanelRequest(TeaModel):
    def __init__(
        self,
        channel_info: ListDeviceByUserIdAndChanelRequestChannelInfo = None,
        user_info: ListDeviceByUserIdAndChanelRequestUserInfo = None,
    ):
        # This parameter is required.
        self.channel_info = channel_info
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.channel_info:
            self.channel_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_info is not None:
            result['ChannelInfo'] = self.channel_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelInfo') is not None:
            temp_model = ListDeviceByUserIdAndChanelRequestChannelInfo()
            self.channel_info = temp_model.from_map(m['ChannelInfo'])
        if m.get('UserInfo') is not None:
            temp_model = ListDeviceByUserIdAndChanelRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListDeviceByUserIdAndChanelShrinkRequest(TeaModel):
    def __init__(
        self,
        channel_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.channel_info_shrink = channel_info_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.channel_info_shrink is not None:
            result['ChannelInfo'] = self.channel_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChannelInfo') is not None:
            self.channel_info_shrink = m.get('ChannelInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListDeviceByUserIdAndChanelResponseBodyResultDeviceUnionIds(TeaModel):
    def __init__(
        self,
        device_union_id: str = None,
        organization_id: str = None,
    ):
        self.device_union_id = device_union_id
        self.organization_id = organization_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_union_id is not None:
            result['DeviceUnionId'] = self.device_union_id
        if self.organization_id is not None:
            result['OrganizationId'] = self.organization_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceUnionId') is not None:
            self.device_union_id = m.get('DeviceUnionId')
        if m.get('OrganizationId') is not None:
            self.organization_id = m.get('OrganizationId')
        return self


class ListDeviceByUserIdAndChanelResponseBodyResult(TeaModel):
    def __init__(
        self,
        device_open_id: str = None,
        device_union_ids: List[ListDeviceByUserIdAndChanelResponseBodyResultDeviceUnionIds] = None,
    ):
        self.device_open_id = device_open_id
        self.device_union_ids = device_union_ids

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
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        result['DeviceUnionIds'] = []
        if self.device_union_ids is not None:
            for k in self.device_union_ids:
                result['DeviceUnionIds'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        self.device_union_ids = []
        if m.get('DeviceUnionIds') is not None:
            for k in m.get('DeviceUnionIds'):
                temp_model = ListDeviceByUserIdAndChanelResponseBodyResultDeviceUnionIds()
                self.device_union_ids.append(temp_model.from_map(k))
        return self


class ListDeviceByUserIdAndChanelResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListDeviceByUserIdAndChanelResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListDeviceByUserIdAndChanelResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListDeviceByUserIdAndChanelResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceByUserIdAndChanelResponseBody = None,
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
            temp_model = ListDeviceByUserIdAndChanelResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeviceIdByIdentitiesHeaders(TeaModel):
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


class ListDeviceIdByIdentitiesRequest(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        identity_ids: List[str] = None,
        identity_type: str = None,
        product_key: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        self.identity_ids = identity_ids
        # This parameter is required.
        self.identity_type = identity_type
        # This parameter is required.
        self.product_key = product_key

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
        if self.identity_ids is not None:
            result['IdentityIds'] = self.identity_ids
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdentityIds') is not None:
            self.identity_ids = m.get('IdentityIds')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ListDeviceIdByIdentitiesShrinkRequest(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        identity_ids_shrink: str = None,
        identity_type: str = None,
        product_key: str = None,
    ):
        # This parameter is required.
        self.encode_key = encode_key
        # This parameter is required.
        self.encode_type = encode_type
        self.identity_ids_shrink = identity_ids_shrink
        # This parameter is required.
        self.identity_type = identity_type
        # This parameter is required.
        self.product_key = product_key

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
        if self.identity_ids_shrink is not None:
            result['IdentityIds'] = self.identity_ids_shrink
        if self.identity_type is not None:
            result['IdentityType'] = self.identity_type
        if self.product_key is not None:
            result['ProductKey'] = self.product_key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('IdentityIds') is not None:
            self.identity_ids_shrink = m.get('IdentityIds')
        if m.get('IdentityType') is not None:
            self.identity_type = m.get('IdentityType')
        if m.get('ProductKey') is not None:
            self.product_key = m.get('ProductKey')
        return self


class ListDeviceIdByIdentitiesResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: Dict[str, ResultValue] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for v in self.result.values():
                if v:
                    v.validate()

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
        result['Result'] = {}
        if self.result is not None:
            for k, v in self.result.items():
                result['Result'][k] = v.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = {}
        if m.get('Result') is not None:
            for k, v in m.get('Result').items():
                temp_model = ResultValue()
                self.result[k] = temp_model.from_map(v)
        return self


class ListDeviceIdByIdentitiesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeviceIdByIdentitiesResponseBody = None,
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
            temp_model = ListDeviceIdByIdentitiesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMusicHeaders(TeaModel):
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


class ListMusicRequestDeviceInfo(TeaModel):
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


class ListMusicRequestPayload(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        music_id: int = None,
        music_name: str = None,
        music_type: int = None,
        music_type_name: str = None,
        page_size: int = None,
    ):
        self.current_page = current_page
        self.music_id = music_id
        self.music_name = music_name
        # This parameter is required.
        self.music_type = music_type
        # This parameter is required.
        self.music_type_name = music_type_name
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListMusicRequestUserInfo(TeaModel):
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


class ListMusicRequest(TeaModel):
    def __init__(
        self,
        device_info: ListMusicRequestDeviceInfo = None,
        payload: ListMusicRequestPayload = None,
        user_info: ListMusicRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListMusicRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = ListMusicRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = ListMusicRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListMusicShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListMusicResponseBodyResultModel(TeaModel):
    def __init__(
        self,
        music_id: int = None,
        music_name: str = None,
        music_type: int = None,
        music_type_name: str = None,
        music_url: str = None,
    ):
        self.music_id = music_id
        self.music_name = music_name
        self.music_type = music_type
        self.music_type_name = music_type_name
        self.music_url = music_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        return self


class ListMusicResponseBodyResult(TeaModel):
    def __init__(
        self,
        current_page: int = None,
        model: List[ListMusicResponseBodyResultModel] = None,
        page_count: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.model = model
        self.page_count = page_count
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.model:
            for k in self.model:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page
        result['Model'] = []
        if self.model is not None:
            for k in self.model:
                result['Model'].append(k.to_map() if k else None)
        if self.page_count is not None:
            result['PageCount'] = self.page_count
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')
        self.model = []
        if m.get('Model') is not None:
            for k in m.get('Model'):
                temp_model = ListMusicResponseBodyResultModel()
                self.model.append(temp_model.from_map(k))
        if m.get('PageCount') is not None:
            self.page_count = m.get('PageCount')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListMusicResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListMusicResponseBodyResult = None,
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
            temp_model = ListMusicResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListMusicResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMusicResponseBody = None,
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
            temp_model = ListMusicResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPlayHistoryHeaders(TeaModel):
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


class ListPlayHistoryRequestDeviceInfo(TeaModel):
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
        # This parameter is required.
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


class ListPlayHistoryRequestRequest(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
        type: str = None,
    ):
        self.page_num = page_num
        self.page_size = page_size
        self.type = type

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
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListPlayHistoryRequestUserInfo(TeaModel):
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
        # This parameter is required.
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


class ListPlayHistoryRequest(TeaModel):
    def __init__(
        self,
        device_info: ListPlayHistoryRequestDeviceInfo = None,
        request: ListPlayHistoryRequestRequest = None,
        user_info: ListPlayHistoryRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.request = request
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.request:
            self.request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListPlayHistoryRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Request') is not None:
            temp_model = ListPlayHistoryRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        if m.get('UserInfo') is not None:
            temp_model = ListPlayHistoryRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListPlayHistoryShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.request_shrink = request_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListPlayHistoryResponseBodyResultAuthorsCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListPlayHistoryResponseBodyResultAuthors(TeaModel):
    def __init__(
        self,
        author_types: List[str] = None,
        cover: ListPlayHistoryResponseBodyResultAuthorsCover = None,
        description: str = None,
        gender: str = None,
        id: int = None,
        online: bool = None,
        raw_id: str = None,
        source: str = None,
        title: str = None,
    ):
        self.author_types = author_types
        self.cover = cover
        self.description = description
        self.gender = gender
        self.id = id
        self.online = online
        self.raw_id = raw_id
        self.source = source
        self.title = title

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Cover') is not None:
            temp_model = ListPlayHistoryResponseBodyResultAuthorsCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListPlayHistoryResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.mediam = mediam
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListPlayHistoryResponseBodyResult(TeaModel):
    def __init__(
        self,
        alias: List[str] = None,
        audition: bool = None,
        authors: List[ListPlayHistoryResponseBodyResultAuthors] = None,
        category: str = None,
        charge: bool = None,
        comm_cate_id: int = None,
        cover: ListPlayHistoryResponseBodyResultCover = None,
        description: str = None,
        hot_score: float = None,
        id: int = None,
        item_type: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        self.alias = alias
        self.audition = audition
        self.authors = authors
        self.category = category
        self.charge = charge
        self.comm_cate_id = comm_cate_id
        self.cover = cover
        self.description = description
        self.hot_score = hot_score
        self.id = id
        self.item_type = item_type
        self.source = source
        self.title = title
        self.type = type
        self.valid = valid

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = ListPlayHistoryResponseBodyResultAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = ListPlayHistoryResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class ListPlayHistoryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        result: List[ListPlayHistoryResponseBodyResult] = None,
        request_id: str = None,
    ):
        self.code = code
        self.message = message
        self.result = result
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListPlayHistoryResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        return self


class ListPlayHistoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListPlayHistoryResponseBody = None,
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
            temp_model = ListPlayHistoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecommendContentHeaders(TeaModel):
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


class ListRecommendContentRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class ListRecommendContentRequestRequest(TeaModel):
    def __init__(
        self,
        count: int = None,
        type: str = None,
    ):
        self.count = count
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['Count'] = self.count
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ListRecommendContentRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class ListRecommendContentRequest(TeaModel):
    def __init__(
        self,
        device_info: ListRecommendContentRequestDeviceInfo = None,
        request: ListRecommendContentRequestRequest = None,
        user_info: ListRecommendContentRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.request = request
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.request:
            self.request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListRecommendContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Request') is not None:
            temp_model = ListRecommendContentRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        if m.get('UserInfo') is not None:
            temp_model = ListRecommendContentRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListRecommendContentShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.request_shrink = request_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListRecommendContentResponseBodyResultAuthorsCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListRecommendContentResponseBodyResultAuthors(TeaModel):
    def __init__(
        self,
        author_types: List[str] = None,
        cover: ListRecommendContentResponseBodyResultAuthorsCover = None,
        description: str = None,
        gender: str = None,
        id: int = None,
        online: bool = None,
        raw_id: str = None,
        source: str = None,
        title: str = None,
    ):
        self.author_types = author_types
        self.cover = cover
        self.description = description
        self.gender = gender
        self.id = id
        self.online = online
        self.raw_id = raw_id
        self.source = source
        self.title = title

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Cover') is not None:
            temp_model = ListRecommendContentResponseBodyResultAuthorsCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListRecommendContentResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.mediam = mediam
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class ListRecommendContentResponseBodyResult(TeaModel):
    def __init__(
        self,
        alias: List[str] = None,
        audition: bool = None,
        authors: List[ListRecommendContentResponseBodyResultAuthors] = None,
        category: str = None,
        charge: bool = None,
        comm_cate_id: int = None,
        cover: ListRecommendContentResponseBodyResultCover = None,
        description: str = None,
        hot_score: float = None,
        id: int = None,
        item_type: str = None,
        raw_id: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        self.alias = alias
        self.audition = audition
        self.authors = authors
        self.category = category
        self.charge = charge
        self.comm_cate_id = comm_cate_id
        self.cover = cover
        self.description = description
        self.hot_score = hot_score
        self.id = id
        self.item_type = item_type
        self.raw_id = raw_id
        self.source = source
        self.title = title
        self.type = type
        self.valid = valid

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = ListRecommendContentResponseBodyResultAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = ListRecommendContentResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class ListRecommendContentResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListRecommendContentResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListRecommendContentResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListRecommendContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRecommendContentResponseBody = None,
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
            temp_model = ListRecommendContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubHeaders(TeaModel):
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


class ListSubRequestDeviceInfo(TeaModel):
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


class ListSubRequestPage(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSubRequestUserInfo(TeaModel):
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


class ListSubRequest(TeaModel):
    def __init__(
        self,
        device_info: ListSubRequestDeviceInfo = None,
        page: ListSubRequestPage = None,
        user_info: ListSubRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.page = page
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.page:
            self.page.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListSubRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Page') is not None:
            temp_model = ListSubRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('UserInfo') is not None:
            temp_model = ListSubRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListSubShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        page_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.page_shrink = page_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.page_shrink is not None:
            result['Page'] = self.page_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Page') is not None:
            self.page_shrink = m.get('Page')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListSubResponseBodyResultDataListScheduleInfo(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class ListSubResponseBodyResultDataList(TeaModel):
    def __init__(
        self,
        album_id: str = None,
        cover_url: str = None,
        daily_study_cnt: int = None,
        device_id: str = None,
        id: int = None,
        play_mode: str = None,
        schedule_info: ListSubResponseBodyResultDataListScheduleInfo = None,
        title: str = None,
        user_id: int = None,
    ):
        self.album_id = album_id
        self.cover_url = cover_url
        self.daily_study_cnt = daily_study_cnt
        self.device_id = device_id
        self.id = id
        self.play_mode = play_mode
        self.schedule_info = schedule_info
        self.title = title
        self.user_id = user_id

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.daily_study_cnt is not None:
            result['DailyStudyCnt'] = self.daily_study_cnt
        if self.device_id is not None:
            result['DeviceId'] = self.device_id
        if self.id is not None:
            result['Id'] = self.id
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.title is not None:
            result['Title'] = self.title
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('DailyStudyCnt') is not None:
            self.daily_study_cnt = m.get('DailyStudyCnt')
        if m.get('DeviceId') is not None:
            self.device_id = m.get('DeviceId')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('ScheduleInfo') is not None:
            temp_model = ListSubResponseBodyResultDataListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListSubResponseBodyResult(TeaModel):
    def __init__(
        self,
        data_list: List[ListSubResponseBodyResultDataList] = None,
        has_next: bool = None,
        total_count: int = None,
        total_page_count: int = None,
    ):
        self.data_list = data_list
        self.has_next = has_next
        self.total_count = total_count
        self.total_page_count = total_page_count

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListSubResponseBodyResultDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        return self


class ListSubResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListSubResponseBodyResult = None,
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
            temp_model = ListSubResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListSubResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubResponseBody = None,
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
            temp_model = ListSubResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubAlbumHeaders(TeaModel):
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


class ListSubAlbumRequestDeviceInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class ListSubAlbumRequestQuerySubscriptionAlbumRequestPage(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ListSubAlbumRequestQuerySubscriptionAlbumRequest(TeaModel):
    def __init__(
        self,
        album_id: str = None,
        category_id: int = None,
        page: ListSubAlbumRequestQuerySubscriptionAlbumRequestPage = None,
        title: str = None,
    ):
        self.album_id = album_id
        # This parameter is required.
        self.category_id = category_id
        # This parameter is required.
        self.page = page
        self.title = title

    def validate(self):
        if self.page:
            self.page.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.page is not None:
            result['Page'] = self.page.to_map()
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('Page') is not None:
            temp_model = ListSubAlbumRequestQuerySubscriptionAlbumRequestPage()
            self.page = temp_model.from_map(m['Page'])
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class ListSubAlbumRequestUserInfo(TeaModel):
    def __init__(
        self,
        encode_key: str = None,
        encode_type: str = None,
        id: str = None,
        id_type: str = None,
        organization_id: str = None,
    ):
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.id = id
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


class ListSubAlbumRequest(TeaModel):
    def __init__(
        self,
        device_info: ListSubAlbumRequestDeviceInfo = None,
        query_subscription_album_request: ListSubAlbumRequestQuerySubscriptionAlbumRequest = None,
        user_info: ListSubAlbumRequestUserInfo = None,
    ):
        self.device_info = device_info
        # request
        self.query_subscription_album_request = query_subscription_album_request
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.query_subscription_album_request:
            self.query_subscription_album_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.query_subscription_album_request is not None:
            result['QuerySubscriptionAlbumRequest'] = self.query_subscription_album_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ListSubAlbumRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('QuerySubscriptionAlbumRequest') is not None:
            temp_model = ListSubAlbumRequestQuerySubscriptionAlbumRequest()
            self.query_subscription_album_request = temp_model.from_map(m['QuerySubscriptionAlbumRequest'])
        if m.get('UserInfo') is not None:
            temp_model = ListSubAlbumRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListSubAlbumShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        query_subscription_album_request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        self.device_info_shrink = device_info_shrink
        # request
        self.query_subscription_album_request_shrink = query_subscription_album_request_shrink
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.query_subscription_album_request_shrink is not None:
            result['QuerySubscriptionAlbumRequest'] = self.query_subscription_album_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('QuerySubscriptionAlbumRequest') is not None:
            self.query_subscription_album_request_shrink = m.get('QuerySubscriptionAlbumRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ListSubAlbumResponseBodyResultDataListScheduleInfo(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
        schedule_id: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute
        self.schedule_id = schedule_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.schedule_id is not None:
            result['ScheduleId'] = self.schedule_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('ScheduleId') is not None:
            self.schedule_id = m.get('ScheduleId')
        return self


class ListSubAlbumResponseBodyResultDataList(TeaModel):
    def __init__(
        self,
        album_id: str = None,
        category_id: int = None,
        cover_url: str = None,
        id: int = None,
        is_added: bool = None,
        schedule_info: ListSubAlbumResponseBodyResultDataListScheduleInfo = None,
        sequence: int = None,
        title: str = None,
        total_episode: int = None,
    ):
        self.album_id = album_id
        self.category_id = category_id
        self.cover_url = cover_url
        self.id = id
        self.is_added = is_added
        self.schedule_info = schedule_info
        self.sequence = sequence
        self.title = title
        self.total_episode = total_episode

    def validate(self):
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.cover_url is not None:
            result['CoverUrl'] = self.cover_url
        if self.id is not None:
            result['Id'] = self.id
        if self.is_added is not None:
            result['IsAdded'] = self.is_added
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.sequence is not None:
            result['Sequence'] = self.sequence
        if self.title is not None:
            result['Title'] = self.title
        if self.total_episode is not None:
            result['TotalEpisode'] = self.total_episode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CoverUrl') is not None:
            self.cover_url = m.get('CoverUrl')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('IsAdded') is not None:
            self.is_added = m.get('IsAdded')
        if m.get('ScheduleInfo') is not None:
            temp_model = ListSubAlbumResponseBodyResultDataListScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('Sequence') is not None:
            self.sequence = m.get('Sequence')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('TotalEpisode') is not None:
            self.total_episode = m.get('TotalEpisode')
        return self


class ListSubAlbumResponseBodyResult(TeaModel):
    def __init__(
        self,
        data_list: List[ListSubAlbumResponseBodyResultDataList] = None,
        has_next: bool = None,
        total_count: int = None,
        total_page_count: int = None,
    ):
        self.data_list = data_list
        self.has_next = has_next
        self.total_count = total_count
        self.total_page_count = total_page_count

    def validate(self):
        if self.data_list:
            for k in self.data_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['DataList'] = []
        if self.data_list is not None:
            for k in self.data_list:
                result['DataList'].append(k.to_map() if k else None)
        if self.has_next is not None:
            result['HasNext'] = self.has_next
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        if self.total_page_count is not None:
            result['TotalPageCount'] = self.total_page_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data_list = []
        if m.get('DataList') is not None:
            for k in m.get('DataList'):
                temp_model = ListSubAlbumResponseBodyResultDataList()
                self.data_list.append(temp_model.from_map(k))
        if m.get('HasNext') is not None:
            self.has_next = m.get('HasNext')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        if m.get('TotalPageCount') is not None:
            self.total_page_count = m.get('TotalPageCount')
        return self


class ListSubAlbumResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: ListSubAlbumResponseBodyResult = None,
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
            temp_model = ListSubAlbumResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ListSubAlbumResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubAlbumResponseBody = None,
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
            temp_model = ListSubAlbumResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSubscriptionAlbumCategoryHeaders(TeaModel):
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


class ListSubscriptionAlbumCategoryRequest(TeaModel):
    def __init__(
        self,
        category_name: str = None,
    ):
        self.category_name = category_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        return self


class ListSubscriptionAlbumCategoryResponseBodyResult(TeaModel):
    def __init__(
        self,
        category_id: str = None,
        category_name: str = None,
    ):
        self.category_id = category_id
        self.category_name = category_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category_id is not None:
            result['CategoryId'] = self.category_id
        if self.category_name is not None:
            result['CategoryName'] = self.category_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryId') is not None:
            self.category_id = m.get('CategoryId')
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')
        return self


class ListSubscriptionAlbumCategoryResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[ListSubscriptionAlbumCategoryResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListSubscriptionAlbumCategoryResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListSubscriptionAlbumCategoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListSubscriptionAlbumCategoryResponseBody = None,
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
            temp_model = ListSubscriptionAlbumCategoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserMessageHeaders(TeaModel):
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


class ListUserMessageRequestUserInfo(TeaModel):
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


class ListUserMessageRequest(TeaModel):
    def __init__(
        self,
        before_time: str = None,
        user_info: ListUserMessageRequestUserInfo = None,
        limit: int = None,
    ):
        self.before_time = before_time
        # This parameter is required.
        self.user_info = user_info
        self.limit = limit

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('UserInfo') is not None:
            temp_model = ListUserMessageRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class ListUserMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        before_time: str = None,
        user_info_shrink: str = None,
        limit: int = None,
    ):
        self.before_time = before_time
        # This parameter is required.
        self.user_info_shrink = user_info_shrink
        self.limit = limit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.before_time is not None:
            result['BeforeTime'] = self.before_time
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        if self.limit is not None:
            result['limit'] = self.limit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeforeTime') is not None:
            self.before_time = m.get('BeforeTime')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        return self


class ListUserMessageResponseBodyResult(TeaModel):
    def __init__(
        self,
        content: str = None,
        device_name: str = None,
        gmt_create: str = None,
        id: str = None,
        pic: str = None,
        source: str = None,
        source_uuid: str = None,
        status: int = None,
        type: str = None,
        url: str = None,
    ):
        self.content = content
        self.device_name = device_name
        self.gmt_create = gmt_create
        self.id = id
        self.pic = pic
        self.source = source
        self.source_uuid = source_uuid
        self.status = status
        self.type = type
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['Content'] = self.content
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create
        if self.id is not None:
            result['Id'] = self.id
        if self.pic is not None:
            result['Pic'] = self.pic
        if self.source is not None:
            result['Source'] = self.source
        if self.source_uuid is not None:
            result['SourceUuid'] = self.source_uuid
        if self.status is not None:
            result['Status'] = self.status
        if self.type is not None:
            result['Type'] = self.type
        if self.url is not None:
            result['Url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Pic') is not None:
            self.pic = m.get('Pic')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUuid') is not None:
            self.source_uuid = m.get('SourceUuid')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Url') is not None:
            self.url = m.get('Url')
        return self


class ListUserMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        result: List[ListUserMessageResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ListUserMessageResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ListUserMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserMessageResponseBody = None,
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
            temp_model = ListUserMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MobileRecommendHeaders(TeaModel):
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


class MobileRecommendRequestDeviceInfo(TeaModel):
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


class MobileRecommendRequestUserInfo(TeaModel):
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


class MobileRecommendRequest(TeaModel):
    def __init__(
        self,
        bot_id: str = None,
        count: str = None,
        device_info: MobileRecommendRequestDeviceInfo = None,
        style: str = None,
        type: str = None,
        user_info: MobileRecommendRequestUserInfo = None,
    ):
        self.bot_id = bot_id
        self.count = count
        # This parameter is required.
        self.device_info = device_info
        self.style = style
        self.type = type
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bot_id is not None:
            result['BotId'] = self.bot_id
        if self.count is not None:
            result['Count'] = self.count
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.style is not None:
            result['Style'] = self.style
        if self.type is not None:
            result['Type'] = self.type
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DeviceInfo') is not None:
            temp_model = MobileRecommendRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Style') is not None:
            self.style = m.get('Style')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserInfo') is not None:
            temp_model = MobileRecommendRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class MobileRecommendShrinkRequest(TeaModel):
    def __init__(
        self,
        bot_id: str = None,
        count: str = None,
        device_info_shrink: str = None,
        style: str = None,
        type: str = None,
        user_info_shrink: str = None,
    ):
        self.bot_id = bot_id
        self.count = count
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        self.style = style
        self.type = type
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bot_id is not None:
            result['BotId'] = self.bot_id
        if self.count is not None:
            result['Count'] = self.count
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.style is not None:
            result['Style'] = self.style
        if self.type is not None:
            result['Type'] = self.type
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BotId') is not None:
            self.bot_id = m.get('BotId')
        if m.get('Count') is not None:
            self.count = m.get('Count')
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Style') is not None:
            self.style = m.get('Style')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class MobileRecommendResponseBodyResult(TeaModel):
    def __init__(
        self,
        authors: List[str] = None,
        cover: str = None,
        raw_id: str = None,
        source: str = None,
        title: str = None,
    ):
        self.authors = authors
        self.cover = cover
        self.raw_id = raw_id
        self.source = source
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authors is not None:
            result['Authors'] = self.authors
        if self.cover is not None:
            result['Cover'] = self.cover
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authors') is not None:
            self.authors = m.get('Authors')
        if m.get('Cover') is not None:
            self.cover = m.get('Cover')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class MobileRecommendResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        request_id: str = None,
        result: List[MobileRecommendResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = MobileRecommendResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class MobileRecommendResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MobileRecommendResponseBody = None,
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
            temp_model = MobileRecommendResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PlayAndPauseControlHeaders(TeaModel):
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


class PlayAndPauseControlRequestDeviceInfo(TeaModel):
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


class PlayAndPauseControlRequestOpenPlayAndPauseControlParam(TeaModel):
    def __init__(
        self,
        open_play_and_pause_command: str = None,
    ):
        # This parameter is required.
        self.open_play_and_pause_command = open_play_and_pause_command

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_play_and_pause_command is not None:
            result['OpenPlayAndPauseCommand'] = self.open_play_and_pause_command
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenPlayAndPauseCommand') is not None:
            self.open_play_and_pause_command = m.get('OpenPlayAndPauseCommand')
        return self


class PlayAndPauseControlRequestUserInfo(TeaModel):
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


class PlayAndPauseControlRequest(TeaModel):
    def __init__(
        self,
        device_info: PlayAndPauseControlRequestDeviceInfo = None,
        open_play_and_pause_control_param: PlayAndPauseControlRequestOpenPlayAndPauseControlParam = None,
        user_info: PlayAndPauseControlRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.open_play_and_pause_control_param = open_play_and_pause_control_param
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_play_and_pause_control_param:
            self.open_play_and_pause_control_param.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_play_and_pause_control_param is not None:
            result['OpenPlayAndPauseControlParam'] = self.open_play_and_pause_control_param.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = PlayAndPauseControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenPlayAndPauseControlParam') is not None:
            temp_model = PlayAndPauseControlRequestOpenPlayAndPauseControlParam()
            self.open_play_and_pause_control_param = temp_model.from_map(m['OpenPlayAndPauseControlParam'])
        if m.get('UserInfo') is not None:
            temp_model = PlayAndPauseControlRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class PlayAndPauseControlShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        open_play_and_pause_control_param_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.open_play_and_pause_control_param_shrink = open_play_and_pause_control_param_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_play_and_pause_control_param_shrink is not None:
            result['OpenPlayAndPauseControlParam'] = self.open_play_and_pause_control_param_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenPlayAndPauseControlParam') is not None:
            self.open_play_and_pause_control_param_shrink = m.get('OpenPlayAndPauseControlParam')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class PlayAndPauseControlResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PlayAndPauseControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PlayAndPauseControlResponseBody = None,
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
            temp_model = PlayAndPauseControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PlayModeControlHeaders(TeaModel):
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


class PlayModeControlRequestDeviceInfo(TeaModel):
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


class PlayModeControlRequestOpenPlayModeControlRequest(TeaModel):
    def __init__(
        self,
        open_play_mode: str = None,
    ):
        # This parameter is required.
        self.open_play_mode = open_play_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_play_mode is not None:
            result['OpenPlayMode'] = self.open_play_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenPlayMode') is not None:
            self.open_play_mode = m.get('OpenPlayMode')
        return self


class PlayModeControlRequestUserInfo(TeaModel):
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


class PlayModeControlRequest(TeaModel):
    def __init__(
        self,
        device_info: PlayModeControlRequestDeviceInfo = None,
        open_play_mode_control_request: PlayModeControlRequestOpenPlayModeControlRequest = None,
        user_info: PlayModeControlRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.open_play_mode_control_request = open_play_mode_control_request
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_play_mode_control_request:
            self.open_play_mode_control_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_play_mode_control_request is not None:
            result['OpenPlayModeControlRequest'] = self.open_play_mode_control_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = PlayModeControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenPlayModeControlRequest') is not None:
            temp_model = PlayModeControlRequestOpenPlayModeControlRequest()
            self.open_play_mode_control_request = temp_model.from_map(m['OpenPlayModeControlRequest'])
        if m.get('UserInfo') is not None:
            temp_model = PlayModeControlRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class PlayModeControlShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        open_play_mode_control_request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.open_play_mode_control_request_shrink = open_play_mode_control_request_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_play_mode_control_request_shrink is not None:
            result['OpenPlayModeControlRequest'] = self.open_play_mode_control_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenPlayModeControlRequest') is not None:
            self.open_play_mode_control_request_shrink = m.get('OpenPlayModeControlRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class PlayModeControlResponseBodyResult(TeaModel):
    def __init__(
        self,
        open_play_mode: str = None,
    ):
        self.open_play_mode = open_play_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.open_play_mode is not None:
            result['OpenPlayMode'] = self.open_play_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenPlayMode') is not None:
            self.open_play_mode = m.get('OpenPlayMode')
        return self


class PlayModeControlResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: PlayModeControlResponseBodyResult = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = PlayModeControlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PlayModeControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PlayModeControlResponseBody = None,
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
            temp_model = PlayModeControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class PreviousAndNextControlHeaders(TeaModel):
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


class PreviousAndNextControlRequestDeviceInfo(TeaModel):
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


class PreviousAndNextControlRequestOpenControlPlayingListRequest(TeaModel):
    def __init__(
        self,
        cmd: str = None,
        extend_info: Dict[str, Any] = None,
        is_from_device: bool = None,
    ):
        # This parameter is required.
        self.cmd = cmd
        self.extend_info = extend_info
        self.is_from_device = is_from_device

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cmd is not None:
            result['Cmd'] = self.cmd
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.is_from_device is not None:
            result['IsFromDevice'] = self.is_from_device
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cmd') is not None:
            self.cmd = m.get('Cmd')
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('IsFromDevice') is not None:
            self.is_from_device = m.get('IsFromDevice')
        return self


class PreviousAndNextControlRequestUserInfo(TeaModel):
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


class PreviousAndNextControlRequest(TeaModel):
    def __init__(
        self,
        device_info: PreviousAndNextControlRequestDeviceInfo = None,
        open_control_playing_list_request: PreviousAndNextControlRequestOpenControlPlayingListRequest = None,
        user_info: PreviousAndNextControlRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.open_control_playing_list_request = open_control_playing_list_request
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_control_playing_list_request:
            self.open_control_playing_list_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_control_playing_list_request is not None:
            result['OpenControlPlayingListRequest'] = self.open_control_playing_list_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = PreviousAndNextControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenControlPlayingListRequest') is not None:
            temp_model = PreviousAndNextControlRequestOpenControlPlayingListRequest()
            self.open_control_playing_list_request = temp_model.from_map(m['OpenControlPlayingListRequest'])
        if m.get('UserInfo') is not None:
            temp_model = PreviousAndNextControlRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class PreviousAndNextControlShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        open_control_playing_list_request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.open_control_playing_list_request_shrink = open_control_playing_list_request_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_control_playing_list_request_shrink is not None:
            result['OpenControlPlayingListRequest'] = self.open_control_playing_list_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenControlPlayingListRequest') is not None:
            self.open_control_playing_list_request_shrink = m.get('OpenControlPlayingListRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class PreviousAndNextControlResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.mediam = mediam
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class PreviousAndNextControlResponseBodyResult(TeaModel):
    def __init__(
        self,
        album_name: str = None,
        album_raw_id: str = None,
        audio_length: int = None,
        copyright: int = None,
        cover: PreviousAndNextControlResponseBodyResultCover = None,
        default_play_order: int = None,
        item_url: str = None,
        liked: bool = None,
        lyric_url: str = None,
        play_mode: str = None,
        pos: int = None,
        progress: int = None,
        raw_id: str = None,
        singer: str = None,
        source: str = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        self.album_name = album_name
        self.album_raw_id = album_raw_id
        self.audio_length = audio_length
        self.copyright = copyright
        self.cover = cover
        self.default_play_order = default_play_order
        self.item_url = item_url
        self.liked = liked
        self.lyric_url = lyric_url
        self.play_mode = play_mode
        self.pos = pos
        self.progress = progress
        self.raw_id = raw_id
        self.singer = singer
        self.source = source
        self.title = title
        self.type = type
        self.valid = valid

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_name is not None:
            result['AlbumName'] = self.album_name
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.audio_length is not None:
            result['AudioLength'] = self.audio_length
        if self.copyright is not None:
            result['Copyright'] = self.copyright
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.default_play_order is not None:
            result['DefaultPlayOrder'] = self.default_play_order
        if self.item_url is not None:
            result['ItemUrl'] = self.item_url
        if self.liked is not None:
            result['Liked'] = self.liked
        if self.lyric_url is not None:
            result['LyricUrl'] = self.lyric_url
        if self.play_mode is not None:
            result['PlayMode'] = self.play_mode
        if self.pos is not None:
            result['Pos'] = self.pos
        if self.progress is not None:
            result['Progress'] = self.progress
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singer is not None:
            result['Singer'] = self.singer
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumName') is not None:
            self.album_name = m.get('AlbumName')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AudioLength') is not None:
            self.audio_length = m.get('AudioLength')
        if m.get('Copyright') is not None:
            self.copyright = m.get('Copyright')
        if m.get('Cover') is not None:
            temp_model = PreviousAndNextControlResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('DefaultPlayOrder') is not None:
            self.default_play_order = m.get('DefaultPlayOrder')
        if m.get('ItemUrl') is not None:
            self.item_url = m.get('ItemUrl')
        if m.get('Liked') is not None:
            self.liked = m.get('Liked')
        if m.get('LyricUrl') is not None:
            self.lyric_url = m.get('LyricUrl')
        if m.get('PlayMode') is not None:
            self.play_mode = m.get('PlayMode')
        if m.get('Pos') is not None:
            self.pos = m.get('Pos')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singer') is not None:
            self.singer = m.get('Singer')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class PreviousAndNextControlResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: PreviousAndNextControlResponseBodyResult = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = PreviousAndNextControlResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class PreviousAndNextControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: PreviousAndNextControlResponseBody = None,
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
            temp_model = PreviousAndNextControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ProgressControlHeaders(TeaModel):
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


class ProgressControlRequestDeviceInfo(TeaModel):
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


class ProgressControlRequestOpenProgressControlRequest(TeaModel):
    def __init__(
        self,
        extend_info: Dict[str, Any] = None,
        progress: int = None,
    ):
        self.extend_info = extend_info
        # This parameter is required.
        self.progress = progress

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extend_info is not None:
            result['ExtendInfo'] = self.extend_info
        if self.progress is not None:
            result['Progress'] = self.progress
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExtendInfo') is not None:
            self.extend_info = m.get('ExtendInfo')
        if m.get('Progress') is not None:
            self.progress = m.get('Progress')
        return self


class ProgressControlRequestUserInfo(TeaModel):
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


class ProgressControlRequest(TeaModel):
    def __init__(
        self,
        device_info: ProgressControlRequestDeviceInfo = None,
        open_progress_control_request: ProgressControlRequestOpenProgressControlRequest = None,
        user_info: ProgressControlRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.open_progress_control_request = open_progress_control_request
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.open_progress_control_request:
            self.open_progress_control_request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.open_progress_control_request is not None:
            result['OpenProgressControlRequest'] = self.open_progress_control_request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = ProgressControlRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('OpenProgressControlRequest') is not None:
            temp_model = ProgressControlRequestOpenProgressControlRequest()
            self.open_progress_control_request = temp_model.from_map(m['OpenProgressControlRequest'])
        if m.get('UserInfo') is not None:
            temp_model = ProgressControlRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ProgressControlShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        open_progress_control_request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.open_progress_control_request_shrink = open_progress_control_request_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.open_progress_control_request_shrink is not None:
            result['OpenProgressControlRequest'] = self.open_progress_control_request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('OpenProgressControlRequest') is not None:
            self.open_progress_control_request_shrink = m.get('OpenProgressControlRequest')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ProgressControlResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
        success: str = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result
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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ProgressControlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ProgressControlResponseBody = None,
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
            temp_model = ProgressControlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryMusicTypeHeaders(TeaModel):
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


class QueryMusicTypeRequestDeviceInfo(TeaModel):
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


class QueryMusicTypeRequestPayload(TeaModel):
    def __init__(self):
        pass

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        return self


class QueryMusicTypeRequestUserInfo(TeaModel):
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


class QueryMusicTypeRequest(TeaModel):
    def __init__(
        self,
        device_info: QueryMusicTypeRequestDeviceInfo = None,
        payload: QueryMusicTypeRequestPayload = None,
        user_info: QueryMusicTypeRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = QueryMusicTypeRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = QueryMusicTypeRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = QueryMusicTypeRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class QueryMusicTypeShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class QueryMusicTypeResponseBodyResult(TeaModel):
    def __init__(
        self,
        music_type: int = None,
        music_type_name: str = None,
    ):
        self.music_type = music_type
        self.music_type_name = music_type_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        return self


class QueryMusicTypeResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[QueryMusicTypeResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = QueryMusicTypeResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class QueryMusicTypeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryMusicTypeResponseBody = None,
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
            temp_model = QueryMusicTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryUserDeviceListByTmeUserIdHeaders(TeaModel):
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


class QueryUserDeviceListByTmeUserIdRequest(TeaModel):
    def __init__(
        self,
        sp: str = None,
        tme_user_id: str = None,
    ):
        # This parameter is required.
        self.sp = sp
        # This parameter is required.
        self.tme_user_id = tme_user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sp is not None:
            result['Sp'] = self.sp
        if self.tme_user_id is not None:
            result['TmeUserId'] = self.tme_user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Sp') is not None:
            self.sp = m.get('Sp')
        if m.get('TmeUserId') is not None:
            self.tme_user_id = m.get('TmeUserId')
        return self


class QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoListAuthorizedDeviceList(TeaModel):
    def __init__(
        self,
        device_name: str = None,
        online: bool = None,
        open_device_id: str = None,
        tme_device_id: str = None,
        tme_product_id: str = None,
    ):
        self.device_name = device_name
        self.online = online
        self.open_device_id = open_device_id
        self.tme_device_id = tme_device_id
        self.tme_product_id = tme_product_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_name is not None:
            result['DeviceName'] = self.device_name
        if self.online is not None:
            result['Online'] = self.online
        if self.open_device_id is not None:
            result['OpenDeviceId'] = self.open_device_id
        if self.tme_device_id is not None:
            result['TmeDeviceId'] = self.tme_device_id
        if self.tme_product_id is not None:
            result['TmeProductId'] = self.tme_product_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceName') is not None:
            self.device_name = m.get('DeviceName')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('OpenDeviceId') is not None:
            self.open_device_id = m.get('OpenDeviceId')
        if m.get('TmeDeviceId') is not None:
            self.tme_device_id = m.get('TmeDeviceId')
        if m.get('TmeProductId') is not None:
            self.tme_product_id = m.get('TmeProductId')
        return self


class QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoList(TeaModel):
    def __init__(
        self,
        authorized_device_list: List[QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoListAuthorizedDeviceList] = None,
        open_user_id: str = None,
        user_nickname: str = None,
    ):
        self.authorized_device_list = authorized_device_list
        self.open_user_id = open_user_id
        self.user_nickname = user_nickname

    def validate(self):
        if self.authorized_device_list:
            for k in self.authorized_device_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AuthorizedDeviceList'] = []
        if self.authorized_device_list is not None:
            for k in self.authorized_device_list:
                result['AuthorizedDeviceList'].append(k.to_map() if k else None)
        if self.open_user_id is not None:
            result['OpenUserId'] = self.open_user_id
        if self.user_nickname is not None:
            result['UserNickname'] = self.user_nickname
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.authorized_device_list = []
        if m.get('AuthorizedDeviceList') is not None:
            for k in m.get('AuthorizedDeviceList'):
                temp_model = QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoListAuthorizedDeviceList()
                self.authorized_device_list.append(temp_model.from_map(k))
        if m.get('OpenUserId') is not None:
            self.open_user_id = m.get('OpenUserId')
        if m.get('UserNickname') is not None:
            self.user_nickname = m.get('UserNickname')
        return self


class QueryUserDeviceListByTmeUserIdResponseBodyResult(TeaModel):
    def __init__(
        self,
        aligenie_user_info_list: List[QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoList] = None,
        encode_key: str = None,
        encode_type: str = None,
        sp: str = None,
    ):
        self.aligenie_user_info_list = aligenie_user_info_list
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.sp = sp

    def validate(self):
        if self.aligenie_user_info_list:
            for k in self.aligenie_user_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AligenieUserInfoList'] = []
        if self.aligenie_user_info_list is not None:
            for k in self.aligenie_user_info_list:
                result['AligenieUserInfoList'].append(k.to_map() if k else None)
        if self.encode_key is not None:
            result['EncodeKey'] = self.encode_key
        if self.encode_type is not None:
            result['EncodeType'] = self.encode_type
        if self.sp is not None:
            result['Sp'] = self.sp
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aligenie_user_info_list = []
        if m.get('AligenieUserInfoList') is not None:
            for k in m.get('AligenieUserInfoList'):
                temp_model = QueryUserDeviceListByTmeUserIdResponseBodyResultAligenieUserInfoList()
                self.aligenie_user_info_list.append(temp_model.from_map(k))
        if m.get('EncodeKey') is not None:
            self.encode_key = m.get('EncodeKey')
        if m.get('EncodeType') is not None:
            self.encode_type = m.get('EncodeType')
        if m.get('Sp') is not None:
            self.sp = m.get('Sp')
        return self


class QueryUserDeviceListByTmeUserIdResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: QueryUserDeviceListByTmeUserIdResponseBodyResult = None,
        success: bool = None,
    ):
        self.code = code
        self.message = message
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
            temp_model = QueryUserDeviceListByTmeUserIdResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class QueryUserDeviceListByTmeUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryUserDeviceListByTmeUserIdResponseBody = None,
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
            temp_model = QueryUserDeviceListByTmeUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ReadMessageHeaders(TeaModel):
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


class ReadMessageRequestUserInfo(TeaModel):
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


class ReadMessageRequest(TeaModel):
    def __init__(
        self,
        message_id: int = None,
        user_info: ReadMessageRequestUserInfo = None,
    ):
        self.message_id = message_id
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('UserInfo') is not None:
            temp_model = ReadMessageRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ReadMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        message_id: int = None,
        user_info_shrink: str = None,
    ):
        self.message_id = message_id
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.message_id is not None:
            result['MessageId'] = self.message_id
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MessageId') is not None:
            self.message_id = m.get('MessageId')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ReadMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            self.result = m.get('Result')
        return self


class ReadMessageResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ReadMessageResponseBody = None,
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
            temp_model = ReadMessageResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScanCodeBindHeaders(TeaModel):
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


class ScanCodeBindRequestBindReq(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        code: str = None,
        ext_info: str = None,
    ):
        # This parameter is required.
        self.client_id = client_id
        # authCode
        # 
        # This parameter is required.
        self.code = code
        self.ext_info = ext_info

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['ClientId'] = self.client_id
        if self.code is not None:
            result['Code'] = self.code
        if self.ext_info is not None:
            result['ExtInfo'] = self.ext_info
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('ExtInfo') is not None:
            self.ext_info = m.get('ExtInfo')
        return self


class ScanCodeBindRequestUserInfo(TeaModel):
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


class ScanCodeBindRequest(TeaModel):
    def __init__(
        self,
        bind_req: ScanCodeBindRequestBindReq = None,
        user_info: ScanCodeBindRequestUserInfo = None,
    ):
        # This parameter is required.
        self.bind_req = bind_req
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.bind_req:
            self.bind_req.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_req is not None:
            result['BindReq'] = self.bind_req.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindReq') is not None:
            temp_model = ScanCodeBindRequestBindReq()
            self.bind_req = temp_model.from_map(m['BindReq'])
        if m.get('UserInfo') is not None:
            temp_model = ScanCodeBindRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ScanCodeBindShrinkRequest(TeaModel):
    def __init__(
        self,
        bind_req_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.bind_req_shrink = bind_req_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bind_req_shrink is not None:
            result['BindReq'] = self.bind_req_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindReq') is not None:
            self.bind_req_shrink = m.get('BindReq')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class ScanCodeBindResponseBodyResult(TeaModel):
    def __init__(
        self,
        biz_group: str = None,
        biz_type: str = None,
        device_open_id: str = None,
        user_open_id: str = None,
    ):
        self.biz_group = biz_group
        self.biz_type = biz_type
        # A963*0158
        self.device_open_id = device_open_id
        # DAFE****ce3ej=\
        self.user_open_id = user_open_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_group is not None:
            result['BizGroup'] = self.biz_group
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.device_open_id is not None:
            result['DeviceOpenId'] = self.device_open_id
        if self.user_open_id is not None:
            result['UserOpenId'] = self.user_open_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizGroup') is not None:
            self.biz_group = m.get('BizGroup')
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('DeviceOpenId') is not None:
            self.device_open_id = m.get('DeviceOpenId')
        if m.get('UserOpenId') is not None:
            self.user_open_id = m.get('UserOpenId')
        return self


class ScanCodeBindResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: ScanCodeBindResponseBodyResult = None,
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
            temp_model = ScanCodeBindResponseBodyResult()
            self.result = temp_model.from_map(m['Result'])
        return self


class ScanCodeBindResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScanCodeBindResponseBody = None,
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
            temp_model = ScanCodeBindResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ScgSearchHeaders(TeaModel):
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


class ScgSearchRequestScgFilterOffSetParam(TeaModel):
    def __init__(
        self,
        limit: int = None,
        offset: int = None,
    ):
        self.limit = limit
        self.offset = offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['Limit'] = self.limit
        if self.offset is not None:
            result['Offset'] = self.offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Limit') is not None:
            self.limit = m.get('Limit')
        if m.get('Offset') is not None:
            self.offset = m.get('Offset')
        return self


class ScgSearchRequestScgFilterPageParam(TeaModel):
    def __init__(
        self,
        page_num: int = None,
        page_size: int = None,
    ):
        self.page_num = page_num
        self.page_size = page_size

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        return self


class ScgSearchRequestScgFilterSortParam(TeaModel):
    def __init__(
        self,
        sort_key: str = None,
        sort_order: str = None,
        sort_text: str = None,
    ):
        self.sort_key = sort_key
        self.sort_order = sort_order
        self.sort_text = sort_text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.sort_key is not None:
            result['SortKey'] = self.sort_key
        if self.sort_order is not None:
            result['SortOrder'] = self.sort_order
        if self.sort_text is not None:
            result['SortText'] = self.sort_text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SortKey') is not None:
            self.sort_key = m.get('SortKey')
        if m.get('SortOrder') is not None:
            self.sort_order = m.get('SortOrder')
        if m.get('SortText') is not None:
            self.sort_text = m.get('SortText')
        return self


class ScgSearchRequestScgFilter(TeaModel):
    def __init__(
        self,
        off_set_param: ScgSearchRequestScgFilterOffSetParam = None,
        page_param: ScgSearchRequestScgFilterPageParam = None,
        sort_param: ScgSearchRequestScgFilterSortParam = None,
        use_off_set: bool = None,
    ):
        self.off_set_param = off_set_param
        self.page_param = page_param
        # This parameter is required.
        self.sort_param = sort_param
        # This parameter is required.
        self.use_off_set = use_off_set

    def validate(self):
        if self.off_set_param:
            self.off_set_param.validate()
        if self.page_param:
            self.page_param.validate()
        if self.sort_param:
            self.sort_param.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.off_set_param is not None:
            result['OffSetParam'] = self.off_set_param.to_map()
        if self.page_param is not None:
            result['PageParam'] = self.page_param.to_map()
        if self.sort_param is not None:
            result['SortParam'] = self.sort_param.to_map()
        if self.use_off_set is not None:
            result['UseOffSet'] = self.use_off_set
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OffSetParam') is not None:
            temp_model = ScgSearchRequestScgFilterOffSetParam()
            self.off_set_param = temp_model.from_map(m['OffSetParam'])
        if m.get('PageParam') is not None:
            temp_model = ScgSearchRequestScgFilterPageParam()
            self.page_param = temp_model.from_map(m['PageParam'])
        if m.get('SortParam') is not None:
            temp_model = ScgSearchRequestScgFilterSortParam()
            self.sort_param = temp_model.from_map(m['SortParam'])
        if m.get('UseOffSet') is not None:
            self.use_off_set = m.get('UseOffSet')
        return self


class ScgSearchRequest(TeaModel):
    def __init__(
        self,
        scg_filter: ScgSearchRequestScgFilter = None,
        topic_id: str = None,
    ):
        # This parameter is required.
        self.scg_filter = scg_filter
        # This parameter is required.
        self.topic_id = topic_id

    def validate(self):
        if self.scg_filter:
            self.scg_filter.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scg_filter is not None:
            result['ScgFilter'] = self.scg_filter.to_map()
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScgFilter') is not None:
            temp_model = ScgSearchRequestScgFilter()
            self.scg_filter = temp_model.from_map(m['ScgFilter'])
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        return self


class ScgSearchShrinkRequest(TeaModel):
    def __init__(
        self,
        scg_filter_shrink: str = None,
        topic_id: str = None,
    ):
        # This parameter is required.
        self.scg_filter_shrink = scg_filter_shrink
        # This parameter is required.
        self.topic_id = topic_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.scg_filter_shrink is not None:
            result['ScgFilter'] = self.scg_filter_shrink
        if self.topic_id is not None:
            result['TopicId'] = self.topic_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ScgFilter') is not None:
            self.scg_filter_shrink = m.get('ScgFilter')
        if m.get('TopicId') is not None:
            self.topic_id = m.get('TopicId')
        return self


class ScgSearchResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        img: str = None,
        large: str = None,
        medium: str = None,
        small: str = None,
        can_resize: bool = None,
    ):
        self.img = img
        self.large = large
        self.medium = medium
        self.small = small
        self.can_resize = can_resize

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        if self.can_resize is not None:
            result['canResize'] = self.can_resize
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        if m.get('canResize') is not None:
            self.can_resize = m.get('canResize')
        return self


class ScgSearchResponseBodyResult(TeaModel):
    def __init__(
        self,
        album: bool = None,
        album_raw_id: str = None,
        album_type: int = None,
        alias: List[str] = None,
        author_ids: List[int] = None,
        author_names: List[str] = None,
        category: str = None,
        content_type: str = None,
        cover: ScgSearchResponseBodyResultCover = None,
        is_audition: bool = None,
        is_charge: str = None,
        need_charge: bool = None,
        raw_id: str = None,
        singers: str = None,
        source: str = None,
        support_audition: bool = None,
        title: str = None,
        type: str = None,
    ):
        self.album = album
        self.album_raw_id = album_raw_id
        self.album_type = album_type
        self.alias = alias
        self.author_ids = author_ids
        self.author_names = author_names
        self.category = category
        self.content_type = content_type
        self.cover = cover
        self.is_audition = is_audition
        self.is_charge = is_charge
        self.need_charge = need_charge
        self.raw_id = raw_id
        self.singers = singers
        self.source = source
        self.support_audition = support_audition
        self.title = title
        self.type = type

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album is not None:
            result['Album'] = self.album
        if self.album_raw_id is not None:
            result['AlbumRawId'] = self.album_raw_id
        if self.album_type is not None:
            result['AlbumType'] = self.album_type
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.author_ids is not None:
            result['AuthorIds'] = self.author_ids
        if self.author_names is not None:
            result['AuthorNames'] = self.author_names
        if self.category is not None:
            result['Category'] = self.category
        if self.content_type is not None:
            result['ContentType'] = self.content_type
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.is_audition is not None:
            result['IsAudition'] = self.is_audition
        if self.is_charge is not None:
            result['IsCharge'] = self.is_charge
        if self.need_charge is not None:
            result['NeedCharge'] = self.need_charge
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.singers is not None:
            result['Singers'] = self.singers
        if self.source is not None:
            result['Source'] = self.source
        if self.support_audition is not None:
            result['SupportAudition'] = self.support_audition
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Album') is not None:
            self.album = m.get('Album')
        if m.get('AlbumRawId') is not None:
            self.album_raw_id = m.get('AlbumRawId')
        if m.get('AlbumType') is not None:
            self.album_type = m.get('AlbumType')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('AuthorIds') is not None:
            self.author_ids = m.get('AuthorIds')
        if m.get('AuthorNames') is not None:
            self.author_names = m.get('AuthorNames')
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('ContentType') is not None:
            self.content_type = m.get('ContentType')
        if m.get('Cover') is not None:
            temp_model = ScgSearchResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('IsAudition') is not None:
            self.is_audition = m.get('IsAudition')
        if m.get('IsCharge') is not None:
            self.is_charge = m.get('IsCharge')
        if m.get('NeedCharge') is not None:
            self.need_charge = m.get('NeedCharge')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Singers') is not None:
            self.singers = m.get('Singers')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SupportAudition') is not None:
            self.support_audition = m.get('SupportAudition')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        return self


class ScgSearchResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        page_num: int = None,
        page_size: int = None,
        request_id: str = None,
        result: List[ScgSearchResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        self.page_num = page_num
        self.page_size = page_size
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = ScgSearchResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class ScgSearchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScgSearchResponseBody = None,
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
            temp_model = ScgSearchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchContentHeaders(TeaModel):
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


class SearchContentRequestDeviceInfo(TeaModel):
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


class SearchContentRequestRequest(TeaModel):
    def __init__(
        self,
        cate: str = None,
        page_num: int = None,
        page_size: int = None,
        query: str = None,
        query_album: bool = None,
        sub_cate: str = None,
    ):
        self.cate = cate
        self.page_num = page_num
        self.page_size = page_size
        self.query = query
        self.query_album = query_album
        self.sub_cate = sub_cate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cate is not None:
            result['Cate'] = self.cate
        if self.page_num is not None:
            result['PageNum'] = self.page_num
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.query is not None:
            result['Query'] = self.query
        if self.query_album is not None:
            result['QueryAlbum'] = self.query_album
        if self.sub_cate is not None:
            result['SubCate'] = self.sub_cate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cate') is not None:
            self.cate = m.get('Cate')
        if m.get('PageNum') is not None:
            self.page_num = m.get('PageNum')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('Query') is not None:
            self.query = m.get('Query')
        if m.get('QueryAlbum') is not None:
            self.query_album = m.get('QueryAlbum')
        if m.get('SubCate') is not None:
            self.sub_cate = m.get('SubCate')
        return self


class SearchContentRequestUserInfo(TeaModel):
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


class SearchContentRequest(TeaModel):
    def __init__(
        self,
        device_info: SearchContentRequestDeviceInfo = None,
        request: SearchContentRequestRequest = None,
        user_info: SearchContentRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.request = request
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.request:
            self.request.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.request is not None:
            result['Request'] = self.request.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = SearchContentRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Request') is not None:
            temp_model = SearchContentRequestRequest()
            self.request = temp_model.from_map(m['Request'])
        if m.get('UserInfo') is not None:
            temp_model = SearchContentRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class SearchContentShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        request_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.request_shrink = request_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.request_shrink is not None:
            result['Request'] = self.request_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Request') is not None:
            self.request_shrink = m.get('Request')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class SearchContentResponseBodyResultAuthorsCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class SearchContentResponseBodyResultAuthors(TeaModel):
    def __init__(
        self,
        author_types: List[str] = None,
        cover: SearchContentResponseBodyResultAuthorsCover = None,
        description: str = None,
        gender: str = None,
        id: int = None,
        online: bool = None,
        raw_id: str = None,
        source: str = None,
        title: str = None,
    ):
        self.author_types = author_types
        self.cover = cover
        self.description = description
        self.gender = gender
        self.id = id
        self.online = online
        self.raw_id = raw_id
        self.source = source
        self.title = title

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.author_types is not None:
            result['AuthorTypes'] = self.author_types
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.gender is not None:
            result['Gender'] = self.gender
        if self.id is not None:
            result['Id'] = self.id
        if self.online is not None:
            result['Online'] = self.online
        if self.raw_id is not None:
            result['RawId'] = self.raw_id
        if self.source is not None:
            result['Source'] = self.source
        if self.title is not None:
            result['Title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthorTypes') is not None:
            self.author_types = m.get('AuthorTypes')
        if m.get('Cover') is not None:
            temp_model = SearchContentResponseBodyResultAuthorsCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Gender') is not None:
            self.gender = m.get('Gender')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Online') is not None:
            self.online = m.get('Online')
        if m.get('RawId') is not None:
            self.raw_id = m.get('RawId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        return self


class SearchContentResponseBodyResultCover(TeaModel):
    def __init__(
        self,
        can_resize: bool = None,
        img: str = None,
        large: str = None,
        mediam: str = None,
        medium: str = None,
        small: str = None,
    ):
        self.can_resize = can_resize
        self.img = img
        self.large = large
        self.mediam = mediam
        self.medium = medium
        self.small = small

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_resize is not None:
            result['CanResize'] = self.can_resize
        if self.img is not None:
            result['Img'] = self.img
        if self.large is not None:
            result['Large'] = self.large
        if self.mediam is not None:
            result['Mediam'] = self.mediam
        if self.medium is not None:
            result['Medium'] = self.medium
        if self.small is not None:
            result['Small'] = self.small
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanResize') is not None:
            self.can_resize = m.get('CanResize')
        if m.get('Img') is not None:
            self.img = m.get('Img')
        if m.get('Large') is not None:
            self.large = m.get('Large')
        if m.get('Mediam') is not None:
            self.mediam = m.get('Mediam')
        if m.get('Medium') is not None:
            self.medium = m.get('Medium')
        if m.get('Small') is not None:
            self.small = m.get('Small')
        return self


class SearchContentResponseBodyResult(TeaModel):
    def __init__(
        self,
        album_id: str = None,
        alias: List[str] = None,
        audition: bool = None,
        authors: List[SearchContentResponseBodyResultAuthors] = None,
        category: str = None,
        charge: bool = None,
        comm_cate_id: int = None,
        cover: SearchContentResponseBodyResultCover = None,
        description: str = None,
        duration: int = None,
        hot_score: float = None,
        id: int = None,
        item_type: str = None,
        lyric: str = None,
        order_index: str = None,
        source: str = None,
        styles: List[str] = None,
        title: str = None,
        type: str = None,
        valid: str = None,
    ):
        self.album_id = album_id
        self.alias = alias
        self.audition = audition
        self.authors = authors
        self.category = category
        self.charge = charge
        self.comm_cate_id = comm_cate_id
        self.cover = cover
        self.description = description
        self.duration = duration
        self.hot_score = hot_score
        self.id = id
        self.item_type = item_type
        self.lyric = lyric
        self.order_index = order_index
        self.source = source
        self.styles = styles
        self.title = title
        self.type = type
        self.valid = valid

    def validate(self):
        if self.authors:
            for k in self.authors:
                if k:
                    k.validate()
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['AlbumId'] = self.album_id
        if self.alias is not None:
            result['Alias'] = self.alias
        if self.audition is not None:
            result['Audition'] = self.audition
        result['Authors'] = []
        if self.authors is not None:
            for k in self.authors:
                result['Authors'].append(k.to_map() if k else None)
        if self.category is not None:
            result['Category'] = self.category
        if self.charge is not None:
            result['Charge'] = self.charge
        if self.comm_cate_id is not None:
            result['CommCateId'] = self.comm_cate_id
        if self.cover is not None:
            result['Cover'] = self.cover.to_map()
        if self.description is not None:
            result['Description'] = self.description
        if self.duration is not None:
            result['Duration'] = self.duration
        if self.hot_score is not None:
            result['HotScore'] = self.hot_score
        if self.id is not None:
            result['Id'] = self.id
        if self.item_type is not None:
            result['ItemType'] = self.item_type
        if self.lyric is not None:
            result['Lyric'] = self.lyric
        if self.order_index is not None:
            result['OrderIndex'] = self.order_index
        if self.source is not None:
            result['Source'] = self.source
        if self.styles is not None:
            result['Styles'] = self.styles
        if self.title is not None:
            result['Title'] = self.title
        if self.type is not None:
            result['Type'] = self.type
        if self.valid is not None:
            result['Valid'] = self.valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlbumId') is not None:
            self.album_id = m.get('AlbumId')
        if m.get('Alias') is not None:
            self.alias = m.get('Alias')
        if m.get('Audition') is not None:
            self.audition = m.get('Audition')
        self.authors = []
        if m.get('Authors') is not None:
            for k in m.get('Authors'):
                temp_model = SearchContentResponseBodyResultAuthors()
                self.authors.append(temp_model.from_map(k))
        if m.get('Category') is not None:
            self.category = m.get('Category')
        if m.get('Charge') is not None:
            self.charge = m.get('Charge')
        if m.get('CommCateId') is not None:
            self.comm_cate_id = m.get('CommCateId')
        if m.get('Cover') is not None:
            temp_model = SearchContentResponseBodyResultCover()
            self.cover = temp_model.from_map(m['Cover'])
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('Duration') is not None:
            self.duration = m.get('Duration')
        if m.get('HotScore') is not None:
            self.hot_score = m.get('HotScore')
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')
        if m.get('Lyric') is not None:
            self.lyric = m.get('Lyric')
        if m.get('OrderIndex') is not None:
            self.order_index = m.get('OrderIndex')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('Styles') is not None:
            self.styles = m.get('Styles')
        if m.get('Title') is not None:
            self.title = m.get('Title')
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Valid') is not None:
            self.valid = m.get('Valid')
        return self


class SearchContentResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: List[SearchContentResponseBodyResult] = None,
    ):
        self.code = code
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.result = result

    def validate(self):
        if self.result:
            for k in self.result:
                if k:
                    k.validate()

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
        result['Result'] = []
        if self.result is not None:
            for k in self.result:
                result['Result'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.result = []
        if m.get('Result') is not None:
            for k in m.get('Result'):
                temp_model = SearchContentResponseBodyResult()
                self.result.append(temp_model.from_map(k))
        return self


class SearchContentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchContentResponseBody = None,
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
            temp_model = SearchContentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SendMessageHeaders(TeaModel):
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


class SendMessageRequestUserInfo(TeaModel):
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


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        user_info: SendMessageRequestUserInfo = None,
    ):
        self.url = url
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserInfo') is not None:
            temp_model = SendMessageRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class SendMessageShrinkRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        user_info_shrink: str = None,
    ):
        self.url = url
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.url is not None:
            result['Url'] = self.url
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Url') is not None:
            self.url = m.get('Url')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class SendMessageResponseBody(TeaModel):
    def __init__(
        self,
        code: str = None,
        message: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('Result') is not None:
            self.result = m.get('Result')
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


class SetDeviceSettingHeaders(TeaModel):
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


class SetDeviceSettingRequestDeviceInfo(TeaModel):
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


class SetDeviceSettingRequest(TeaModel):
    def __init__(
        self,
        device_info: SetDeviceSettingRequestDeviceInfo = None,
        key: str = None,
        value: Any = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.key = key
        self.value = value

    def validate(self):
        if self.device_info:
            self.device_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = SetDeviceSettingRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SetDeviceSettingShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        key: str = None,
        value: Any = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class SetDeviceSettingResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class SetDeviceSettingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SetDeviceSettingResponseBody = None,
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
            temp_model = SetDeviceSettingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ThirdImmediateMsgPushHeaders(TeaModel):
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


class ThirdImmediateMsgPushRequest(TeaModel):
    def __init__(
        self,
        biz_type: str = None,
        change_detail: str = None,
        order_id: str = None,
        psg_ids: str = None,
        source: str = None,
        traffic_change_type: str = None,
        traffic_change_type_desc: str = None,
        traffic_journey_ids: str = None,
        traffic_sub_order_ids: str = None,
        user_id: str = None,
    ):
        self.biz_type = biz_type
        self.change_detail = change_detail
        self.order_id = order_id
        self.psg_ids = psg_ids
        self.source = source
        self.traffic_change_type = traffic_change_type
        self.traffic_change_type_desc = traffic_change_type_desc
        self.traffic_journey_ids = traffic_journey_ids
        self.traffic_sub_order_ids = traffic_sub_order_ids
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.biz_type is not None:
            result['BizType'] = self.biz_type
        if self.change_detail is not None:
            result['ChangeDetail'] = self.change_detail
        if self.order_id is not None:
            result['OrderId'] = self.order_id
        if self.psg_ids is not None:
            result['PsgIds'] = self.psg_ids
        if self.source is not None:
            result['Source'] = self.source
        if self.traffic_change_type is not None:
            result['TrafficChangeType'] = self.traffic_change_type
        if self.traffic_change_type_desc is not None:
            result['TrafficChangeTypeDesc'] = self.traffic_change_type_desc
        if self.traffic_journey_ids is not None:
            result['TrafficJourneyIds'] = self.traffic_journey_ids
        if self.traffic_sub_order_ids is not None:
            result['TrafficSubOrderIds'] = self.traffic_sub_order_ids
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')
        if m.get('ChangeDetail') is not None:
            self.change_detail = m.get('ChangeDetail')
        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')
        if m.get('PsgIds') is not None:
            self.psg_ids = m.get('PsgIds')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('TrafficChangeType') is not None:
            self.traffic_change_type = m.get('TrafficChangeType')
        if m.get('TrafficChangeTypeDesc') is not None:
            self.traffic_change_type_desc = m.get('TrafficChangeTypeDesc')
        if m.get('TrafficJourneyIds') is not None:
            self.traffic_journey_ids = m.get('TrafficJourneyIds')
        if m.get('TrafficSubOrderIds') is not None:
            self.traffic_sub_order_ids = m.get('TrafficSubOrderIds')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ThirdImmediateMsgPushResponseBodyModel(TeaModel):
    def __init__(
        self,
        request_id: str = None,
        success: bool = None,
    ):
        self.request_id = request_id
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ThirdImmediateMsgPushResponseBody(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_msg: str = None,
        model: ThirdImmediateMsgPushResponseBodyModel = None,
        success: bool = None,
    ):
        self.error_code = error_code
        self.error_msg = error_msg
        self.model = model
        self.success = success

    def validate(self):
        if self.model:
            self.model.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code
        if self.error_msg is not None:
            result['ErrorMsg'] = self.error_msg
        if self.model is not None:
            result['Model'] = self.model.to_map()
        if self.success is not None:
            result['Success'] = self.success
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')
        if m.get('ErrorMsg') is not None:
            self.error_msg = m.get('ErrorMsg')
        if m.get('Model') is not None:
            temp_model = ThirdImmediateMsgPushResponseBodyModel()
            self.model = temp_model.from_map(m['Model'])
        if m.get('Success') is not None:
            self.success = m.get('Success')
        return self


class ThirdImmediateMsgPushResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ThirdImmediateMsgPushResponseBody = None,
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
            temp_model = ThirdImmediateMsgPushResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindAligenieUserHeaders(TeaModel):
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


class UnbindAligenieUserRequest(TeaModel):
    def __init__(
        self,
        login_state_access_token: str = None,
    ):
        # This parameter is required.
        self.login_state_access_token = login_state_access_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.login_state_access_token is not None:
            result['LoginStateAccessToken'] = self.login_state_access_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginStateAccessToken') is not None:
            self.login_state_access_token = m.get('LoginStateAccessToken')
        return self


class UnbindAligenieUserResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
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


class UnbindAligenieUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindAligenieUserResponseBody = None,
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
            temp_model = UnbindAligenieUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnbindDeviceHeaders(TeaModel):
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


class UnbindDeviceRequestDeviceInfo(TeaModel):
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


class UnbindDeviceRequestUserInfo(TeaModel):
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


class UnbindDeviceRequest(TeaModel):
    def __init__(
        self,
        device_info: UnbindDeviceRequestDeviceInfo = None,
        user_info: UnbindDeviceRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = UnbindDeviceRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('UserInfo') is not None:
            temp_model = UnbindDeviceRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class UnbindDeviceShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class UnbindDeviceResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class UnbindDeviceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UnbindDeviceResponseBody = None,
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
            temp_model = UnbindDeviceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateAlarmHeaders(TeaModel):
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


class UpdateAlarmRequestDeviceInfo(TeaModel):
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


class UpdateAlarmRequestPayloadMusicInfo(TeaModel):
    def __init__(
        self,
        music_id: int = None,
        music_name: str = None,
        music_type: int = None,
        music_type_name: str = None,
        music_url: str = None,
    ):
        # This parameter is required.
        self.music_id = music_id
        # This parameter is required.
        self.music_name = music_name
        # This parameter is required.
        self.music_type = music_type
        # This parameter is required.
        self.music_type_name = music_type_name
        self.music_url = music_url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.music_id is not None:
            result['MusicId'] = self.music_id
        if self.music_name is not None:
            result['MusicName'] = self.music_name
        if self.music_type is not None:
            result['MusicType'] = self.music_type
        if self.music_type_name is not None:
            result['MusicTypeName'] = self.music_type_name
        if self.music_url is not None:
            result['MusicUrl'] = self.music_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MusicId') is not None:
            self.music_id = m.get('MusicId')
        if m.get('MusicName') is not None:
            self.music_name = m.get('MusicName')
        if m.get('MusicType') is not None:
            self.music_type = m.get('MusicType')
        if m.get('MusicTypeName') is not None:
            self.music_type_name = m.get('MusicTypeName')
        if m.get('MusicUrl') is not None:
            self.music_url = m.get('MusicUrl')
        return self


class UpdateAlarmRequestPayloadScheduleInfoOnce(TeaModel):
    def __init__(
        self,
        day: int = None,
        hour: int = None,
        minute: int = None,
        month: int = None,
        year: int = None,
    ):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.month = month
        self.year = year

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.day is not None:
            result['Day'] = self.day
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        if self.month is not None:
            result['Month'] = self.month
        if self.year is not None:
            result['Year'] = self.year
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Day') is not None:
            self.day = m.get('Day')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        if m.get('Month') is not None:
            self.month = m.get('Month')
        if m.get('Year') is not None:
            self.year = m.get('Year')
        return self


class UpdateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay(TeaModel):
    def __init__(
        self,
        hour: int = None,
        minute: int = None,
    ):
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class UpdateAlarmRequestPayloadScheduleInfoWeekly(TeaModel):
    def __init__(
        self,
        days_of_week: List[int] = None,
        hour: int = None,
        minute: int = None,
    ):
        self.days_of_week = days_of_week
        self.hour = hour
        self.minute = minute

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.days_of_week is not None:
            result['DaysOfWeek'] = self.days_of_week
        if self.hour is not None:
            result['Hour'] = self.hour
        if self.minute is not None:
            result['Minute'] = self.minute
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysOfWeek') is not None:
            self.days_of_week = m.get('DaysOfWeek')
        if m.get('Hour') is not None:
            self.hour = m.get('Hour')
        if m.get('Minute') is not None:
            self.minute = m.get('Minute')
        return self


class UpdateAlarmRequestPayloadScheduleInfo(TeaModel):
    def __init__(
        self,
        once: UpdateAlarmRequestPayloadScheduleInfoOnce = None,
        statutory_working_day: UpdateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay = None,
        type: str = None,
        weekly: UpdateAlarmRequestPayloadScheduleInfoWeekly = None,
    ):
        self.once = once
        self.statutory_working_day = statutory_working_day
        # This parameter is required.
        self.type = type
        self.weekly = weekly

    def validate(self):
        if self.once:
            self.once.validate()
        if self.statutory_working_day:
            self.statutory_working_day.validate()
        if self.weekly:
            self.weekly.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.once is not None:
            result['Once'] = self.once.to_map()
        if self.statutory_working_day is not None:
            result['StatutoryWorkingDay'] = self.statutory_working_day.to_map()
        if self.type is not None:
            result['Type'] = self.type
        if self.weekly is not None:
            result['Weekly'] = self.weekly.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Once') is not None:
            temp_model = UpdateAlarmRequestPayloadScheduleInfoOnce()
            self.once = temp_model.from_map(m['Once'])
        if m.get('StatutoryWorkingDay') is not None:
            temp_model = UpdateAlarmRequestPayloadScheduleInfoStatutoryWorkingDay()
            self.statutory_working_day = temp_model.from_map(m['StatutoryWorkingDay'])
        if m.get('Type') is not None:
            self.type = m.get('Type')
        if m.get('Weekly') is not None:
            temp_model = UpdateAlarmRequestPayloadScheduleInfoWeekly()
            self.weekly = temp_model.from_map(m['Weekly'])
        return self


class UpdateAlarmRequestPayload(TeaModel):
    def __init__(
        self,
        alarm_id: int = None,
        music_info: UpdateAlarmRequestPayloadMusicInfo = None,
        schedule_info: UpdateAlarmRequestPayloadScheduleInfo = None,
        volume: int = None,
    ):
        # This parameter is required.
        self.alarm_id = alarm_id
        # This parameter is required.
        self.music_info = music_info
        # This parameter is required.
        self.schedule_info = schedule_info
        self.volume = volume

    def validate(self):
        if self.music_info:
            self.music_info.validate()
        if self.schedule_info:
            self.schedule_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.alarm_id is not None:
            result['AlarmId'] = self.alarm_id
        if self.music_info is not None:
            result['MusicInfo'] = self.music_info.to_map()
        if self.schedule_info is not None:
            result['ScheduleInfo'] = self.schedule_info.to_map()
        if self.volume is not None:
            result['Volume'] = self.volume
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlarmId') is not None:
            self.alarm_id = m.get('AlarmId')
        if m.get('MusicInfo') is not None:
            temp_model = UpdateAlarmRequestPayloadMusicInfo()
            self.music_info = temp_model.from_map(m['MusicInfo'])
        if m.get('ScheduleInfo') is not None:
            temp_model = UpdateAlarmRequestPayloadScheduleInfo()
            self.schedule_info = temp_model.from_map(m['ScheduleInfo'])
        if m.get('Volume') is not None:
            self.volume = m.get('Volume')
        return self


class UpdateAlarmRequestUserInfo(TeaModel):
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


class UpdateAlarmRequest(TeaModel):
    def __init__(
        self,
        device_info: UpdateAlarmRequestDeviceInfo = None,
        payload: UpdateAlarmRequestPayload = None,
        user_info: UpdateAlarmRequestUserInfo = None,
    ):
        # This parameter is required.
        self.device_info = device_info
        # This parameter is required.
        self.payload = payload
        # This parameter is required.
        self.user_info = user_info

    def validate(self):
        if self.device_info:
            self.device_info.validate()
        if self.payload:
            self.payload.validate()
        if self.user_info:
            self.user_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info is not None:
            result['DeviceInfo'] = self.device_info.to_map()
        if self.payload is not None:
            result['Payload'] = self.payload.to_map()
        if self.user_info is not None:
            result['UserInfo'] = self.user_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            temp_model = UpdateAlarmRequestDeviceInfo()
            self.device_info = temp_model.from_map(m['DeviceInfo'])
        if m.get('Payload') is not None:
            temp_model = UpdateAlarmRequestPayload()
            self.payload = temp_model.from_map(m['Payload'])
        if m.get('UserInfo') is not None:
            temp_model = UpdateAlarmRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class UpdateAlarmShrinkRequest(TeaModel):
    def __init__(
        self,
        device_info_shrink: str = None,
        payload_shrink: str = None,
        user_info_shrink: str = None,
    ):
        # This parameter is required.
        self.device_info_shrink = device_info_shrink
        # This parameter is required.
        self.payload_shrink = payload_shrink
        # This parameter is required.
        self.user_info_shrink = user_info_shrink

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.device_info_shrink is not None:
            result['DeviceInfo'] = self.device_info_shrink
        if self.payload_shrink is not None:
            result['Payload'] = self.payload_shrink
        if self.user_info_shrink is not None:
            result['UserInfo'] = self.user_info_shrink
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DeviceInfo') is not None:
            self.device_info_shrink = m.get('DeviceInfo')
        if m.get('Payload') is not None:
            self.payload_shrink = m.get('Payload')
        if m.get('UserInfo') is not None:
            self.user_info_shrink = m.get('UserInfo')
        return self


class UpdateAlarmResponseBody(TeaModel):
    def __init__(
        self,
        code: int = None,
        message: str = None,
        request_id: str = None,
        result: bool = None,
    ):
        self.code = code
        self.message = message
        self.request_id = request_id
        self.result = result

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
        if self.result is not None:
            result['Result'] = self.result
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
            self.result = m.get('Result')
        return self


class UpdateAlarmResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateAlarmResponseBody = None,
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
            temp_model = UpdateAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



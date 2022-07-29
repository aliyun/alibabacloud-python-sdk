# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import Dict, Any, List


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


class AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequestOpenSourceRawIdPair(TeaModel):
    def __init__(
        self,
        extend_info: Dict[str, Any] = None,
        raw_id: str = None,
        source: str = None,
    ):
        self.extend_info = extend_info
        self.raw_id = raw_id
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
        self.favorite_cmd = favorite_cmd
        self.open_source_raw_id_pair = open_source_raw_id_pair
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


class AddAndRemoveFavoriteContentRequest(TeaModel):
    def __init__(
        self,
        device_info: AddAndRemoveFavoriteContentRequestDeviceInfo = None,
        open_add_and_remove_favorite_content_request: AddAndRemoveFavoriteContentRequestOpenAddAndRemoveFavoriteContentRequest = None,
        user_info: AddAndRemoveFavoriteContentRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.open_add_and_remove_favorite_content_request = open_add_and_remove_favorite_content_request
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
        self.device_info_shrink = device_info_shrink
        self.open_add_and_remove_favorite_content_request_shrink = open_add_and_remove_favorite_content_request_shrink
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
            temp_model = AddSubResponseBody()
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


class CheckAuthCodeBindForExtRequest(TeaModel):
    def __init__(
        self,
        auth_code: str = None,
        encode_key: str = None,
        encode_type: str = None,
        user_info: CheckAuthCodeBindForExtRequestUserInfo = None,
    ):
        self.auth_code = auth_code
        self.encode_key = encode_key
        self.encode_type = encode_type
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
        self.auth_code = auth_code
        self.encode_key = encode_key
        self.encode_type = encode_type
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
            temp_model = CheckAuthCodeBindForExtResponseBody()
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


class CreateAlarmRequestPayloadMusicInfo(TeaModel):
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
        self.music_info = music_info
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


class CreateAlarmRequest(TeaModel):
    def __init__(
        self,
        device_info: CreateAlarmRequestDeviceInfo = None,
        payload: CreateAlarmRequestPayload = None,
        user_info: CreateAlarmRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
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
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
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


class CreatePlayingListRequestOpenCreatePlayingListRequestContentList(TeaModel):
    def __init__(
        self,
        raw_id: str = None,
        source: str = None,
    ):
        self.raw_id = raw_id
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
        self.content_list = content_list
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


class CreatePlayingListRequest(TeaModel):
    def __init__(
        self,
        device_info: CreatePlayingListRequestDeviceInfo = None,
        open_create_playing_list_request: CreatePlayingListRequestOpenCreatePlayingListRequest = None,
        user_info: CreatePlayingListRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.open_create_playing_list_request = open_create_playing_list_request
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
        self.device_info_shrink = device_info_shrink
        self.open_create_playing_list_request_shrink = open_create_playing_list_request_shrink
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
            temp_model = CreatePlayingListResponseBody()
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
        self.schedule_end_time = schedule_end_time
        self.schedule_start_time = schedule_start_time
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
        invoker: str = None,
        schedule_dto: CreateScheduleTaskRequestPayloadScheduleDTO = None,
    ):
        self.action_dtos = action_dtos
        self.idempotent_id = idempotent_id
        self.invoker = invoker
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
        if self.invoker is not None:
            result['Invoker'] = self.invoker
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
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
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
        self.device_info = device_info
        self.payload = payload
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
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
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


class DeleteAlarmsRequestPayload(TeaModel):
    def __init__(
        self,
        alarm_ids: List[int] = None,
    ):
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


class DeleteAlarmsRequest(TeaModel):
    def __init__(
        self,
        device_info: DeleteAlarmsRequestDeviceInfo = None,
        payload: DeleteAlarmsRequestPayload = None,
        user_info: DeleteAlarmsRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
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
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
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
        invoker: str = None,
    ):
        self.id = id
        self.invoker = invoker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
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
        self.device_info = device_info
        self.payload = payload
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
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
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


class DeviceControlRequest(TeaModel):
    def __init__(
        self,
        control_request: DeviceControlRequestControlRequest = None,
        device_info: DeviceControlRequestDeviceInfo = None,
    ):
        self.control_request = control_request
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
            temp_model = DeviceControlResponseBody()
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


class GetAlarmRequestPayload(TeaModel):
    def __init__(
        self,
        alarm_id: int = None,
    ):
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


class GetAlarmRequest(TeaModel):
    def __init__(
        self,
        device_info: GetAlarmRequestDeviceInfo = None,
        payload: GetAlarmRequestPayload = None,
        user_info: GetAlarmRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
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
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
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
        user_id: int = None,
        uuid: str = None,
        volume: int = None,
    ):
        self.alarm_id = alarm_id
        self.music_info = music_info
        self.schedule_info = schedule_info
        self.schedule_type_desc = schedule_type_desc
        self.status = status
        self.trigger_date_desc = trigger_date_desc
        self.trigger_time_desc = trigger_time_desc
        self.user_id = user_id
        self.uuid = uuid
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
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
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
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
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
        self.id = id
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
            temp_model = GetAlbumDetailByIdResponseBody()
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


class GetCodeEnhanceRequest(TeaModel):
    def __init__(
        self,
        channel_info: GetCodeEnhanceRequestChannelInfo = None,
        user_info: GetCodeEnhanceRequestUserInfo = None,
    ):
        self.channel_info = channel_info
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
        self.channel_info_shrink = channel_info_shrink
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
        self.id = id
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


class GetCurrentPlayingItemRequestUserInfo(TeaModel):
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


class GetCurrentPlayingItemRequest(TeaModel):
    def __init__(
        self,
        device_info: GetCurrentPlayingItemRequestDeviceInfo = None,
        user_info: GetCurrentPlayingItemRequestUserInfo = None,
    ):
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
        self.device_info_shrink = device_info_shrink
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


class GetCurrentPlayingListRequestOpenQueryPlayListRequest(TeaModel):
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


class GetCurrentPlayingListRequestUserInfo(TeaModel):
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


class GetCurrentPlayingListRequest(TeaModel):
    def __init__(
        self,
        device_info: GetCurrentPlayingListRequestDeviceInfo = None,
        open_query_play_list_request: GetCurrentPlayingListRequestOpenQueryPlayListRequest = None,
        user_info: GetCurrentPlayingListRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.open_query_play_list_request = open_query_play_list_request
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
        self.device_info_shrink = device_info_shrink
        self.open_query_play_list_request_shrink = open_query_play_list_request_shrink
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


class GetDeviceBasicInfoRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceBasicInfoRequestDeviceInfo = None,
    ):
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
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.identity_id = identity_id
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


class GetDeviceSettingRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceSettingRequestDeviceInfo = None,
        keys: List[str] = None,
    ):
        self.device_info = device_info
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


class GetDeviceStatusDetailRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceStatusDetailRequestDeviceInfo = None,
        keys: List[str] = None,
    ):
        self.device_info = device_info
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
        self.device_info_shrink = device_info_shrink
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


class GetDeviceStatusInfoRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceStatusInfoRequestDeviceInfo = None,
    ):
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


class GetDeviceTagRequest(TeaModel):
    def __init__(
        self,
        device_info: GetDeviceTagRequestDeviceInfo = None,
    ):
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
            temp_model = GetDeviceTagResponseBody()
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
        invoker: str = None,
    ):
        self.id = id
        self.invoker = invoker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.id is not None:
            result['Id'] = self.id
        if self.invoker is not None:
            result['Invoker'] = self.invoker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')
        if m.get('Invoker') is not None:
            self.invoker = m.get('Invoker')
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
        self.device_info = device_info
        self.payload = payload
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
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
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
        user_id: int = None,
        uuid: str = None,
    ):
        self.action_topic_list = action_topic_list
        self.cron = cron
        self.schedule_end_time = schedule_end_time
        self.schedule_id = schedule_id
        self.schedule_start_time = schedule_start_time
        self.schedule_type = schedule_type
        self.user_id = user_id
        self.uuid = uuid

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
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
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
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
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


class GetUserByDeviceIdRequest(TeaModel):
    def __init__(
        self,
        device_info: GetUserByDeviceIdRequestDeviceInfo = None,
    ):
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
            temp_model = GetUserByDeviceIdResponseBody()
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


class IndexControlPlayingListRequestOpenIndexControlRequest(TeaModel):
    def __init__(
        self,
        extend_info: Dict[str, Any] = None,
        index: int = None,
        need_content_continued: bool = None,
    ):
        self.extend_info = extend_info
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


class IndexControlPlayingListRequest(TeaModel):
    def __init__(
        self,
        device_info: IndexControlPlayingListRequestDeviceInfo = None,
        open_index_control_request: IndexControlPlayingListRequestOpenIndexControlRequest = None,
        user_info: IndexControlPlayingListRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.open_index_control_request = open_index_control_request
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
        self.device_info_shrink = device_info_shrink
        self.open_index_control_request_shrink = open_index_control_request_shrink
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
            temp_model = IndexControlPlayingListResponseBody()
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


class ListAlarmsRequest(TeaModel):
    def __init__(
        self,
        device_info: ListAlarmsRequestDeviceInfo = None,
        payload: ListAlarmsRequestPayload = None,
        user_info: ListAlarmsRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
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
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
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
        user_id: int = None,
        uuid: str = None,
        volume: int = None,
    ):
        self.alarm_id = alarm_id
        self.music_info = music_info
        self.schedule_info = schedule_info
        self.schedule_type_desc = schedule_type_desc
        self.status = status
        self.trigger_date_desc = trigger_date_desc
        self.trigger_time_desc = trigger_time_desc
        self.user_id = user_id
        self.uuid = uuid
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
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.uuid is not None:
            result['Uuid'] = self.uuid
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
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')
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
        self.id = id
        self.page_num = page_num
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
        self.cate_id = cate_id
        self.is_album = is_album
        self.page_num = page_num
        self.page_size = page_size
        self.sort_by = sort_by
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


class ListCateContentRequest(TeaModel):
    def __init__(
        self,
        device_info: ListCateContentRequestDeviceInfo = None,
        request: ListCateContentRequestRequest = None,
        user_info: ListCateContentRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.request = request
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
        self.device_info_shrink = device_info_shrink
        self.request_shrink = request_shrink
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
        self.encode_key = encode_key
        self.encode_type = encode_type
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


class ListDeviceByUserIdRequest(TeaModel):
    def __init__(
        self,
        user_info: ListDeviceByUserIdRequestUserInfo = None,
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
            temp_model = ListDeviceByUserIdRequestUserInfo()
            self.user_info = temp_model.from_map(m['UserInfo'])
        return self


class ListDeviceByUserIdShrinkRequest(TeaModel):
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


class ListDeviceByUserIdAndChanelRequest(TeaModel):
    def __init__(
        self,
        channel_info: ListDeviceByUserIdAndChanelRequestChannelInfo = None,
        user_info: ListDeviceByUserIdAndChanelRequestUserInfo = None,
    ):
        self.channel_info = channel_info
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
        self.channel_info_shrink = channel_info_shrink
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
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.identity_ids = identity_ids
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
        self.encode_key = encode_key
        self.encode_type = encode_type
        self.identity_ids_shrink = identity_ids_shrink
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
        self.music_type = music_type
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


class ListMusicRequest(TeaModel):
    def __init__(
        self,
        device_info: ListMusicRequestDeviceInfo = None,
        payload: ListMusicRequestPayload = None,
        user_info: ListMusicRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
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
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
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


class ListPlayHistoryRequest(TeaModel):
    def __init__(
        self,
        device_info: ListPlayHistoryRequestDeviceInfo = None,
        request: ListPlayHistoryRequestRequest = None,
        user_info: ListPlayHistoryRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.request = request
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
        self.device_info_shrink = device_info_shrink
        self.request_shrink = request_shrink
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
        self.device_info = device_info
        self.request = request
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
        self.device_info_shrink = device_info_shrink
        self.request_shrink = request_shrink
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


class ListSubRequest(TeaModel):
    def __init__(
        self,
        device_info: ListSubRequestDeviceInfo = None,
        page: ListSubRequestPage = None,
        user_info: ListSubRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.page = page
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
        self.device_info_shrink = device_info_shrink
        self.page_shrink = page_shrink
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
        self.category_id = category_id
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


class ListUserMessageRequest(TeaModel):
    def __init__(
        self,
        before_time: str = None,
        user_info: ListUserMessageRequestUserInfo = None,
        limit: int = None,
    ):
        self.before_time = before_time
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
            temp_model = ListUserMessageResponseBody()
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


class PlayAndPauseControlRequestOpenPlayAndPauseControlParam(TeaModel):
    def __init__(
        self,
        open_play_and_pause_command: str = None,
    ):
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


class PlayAndPauseControlRequest(TeaModel):
    def __init__(
        self,
        device_info: PlayAndPauseControlRequestDeviceInfo = None,
        open_play_and_pause_control_param: PlayAndPauseControlRequestOpenPlayAndPauseControlParam = None,
        user_info: PlayAndPauseControlRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.open_play_and_pause_control_param = open_play_and_pause_control_param
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
        self.device_info_shrink = device_info_shrink
        self.open_play_and_pause_control_param_shrink = open_play_and_pause_control_param_shrink
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


class PlayModeControlRequestOpenPlayModeControlRequest(TeaModel):
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


class PlayModeControlRequestUserInfo(TeaModel):
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


class PlayModeControlRequest(TeaModel):
    def __init__(
        self,
        device_info: PlayModeControlRequestDeviceInfo = None,
        open_play_mode_control_request: PlayModeControlRequestOpenPlayModeControlRequest = None,
        user_info: PlayModeControlRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.open_play_mode_control_request = open_play_mode_control_request
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
        self.device_info_shrink = device_info_shrink
        self.open_play_mode_control_request_shrink = open_play_mode_control_request_shrink
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


class PreviousAndNextControlRequestOpenControlPlayingListRequest(TeaModel):
    def __init__(
        self,
        cmd: str = None,
        extend_info: Dict[str, Any] = None,
        is_from_device: bool = None,
    ):
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


class PreviousAndNextControlRequest(TeaModel):
    def __init__(
        self,
        device_info: PreviousAndNextControlRequestDeviceInfo = None,
        open_control_playing_list_request: PreviousAndNextControlRequestOpenControlPlayingListRequest = None,
        user_info: PreviousAndNextControlRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.open_control_playing_list_request = open_control_playing_list_request
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
        self.device_info_shrink = device_info_shrink
        self.open_control_playing_list_request_shrink = open_control_playing_list_request_shrink
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


class ProgressControlRequestOpenProgressControlRequest(TeaModel):
    def __init__(
        self,
        extend_info: Dict[str, Any] = None,
        progress: int = None,
    ):
        self.extend_info = extend_info
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


class ProgressControlRequest(TeaModel):
    def __init__(
        self,
        device_info: ProgressControlRequestDeviceInfo = None,
        open_progress_control_request: ProgressControlRequestOpenProgressControlRequest = None,
        user_info: ProgressControlRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.open_progress_control_request = open_progress_control_request
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
        self.device_info_shrink = device_info_shrink
        self.open_progress_control_request_shrink = open_progress_control_request_shrink
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


class QueryMusicTypeRequest(TeaModel):
    def __init__(
        self,
        device_info: QueryMusicTypeRequestDeviceInfo = None,
        payload: QueryMusicTypeRequestPayload = None,
        user_info: QueryMusicTypeRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
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
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
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
            temp_model = QueryMusicTypeResponseBody()
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


class ReadMessageRequest(TeaModel):
    def __init__(
        self,
        message_id: int = None,
        user_info: ReadMessageRequestUserInfo = None,
    ):
        self.message_id = message_id
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
            temp_model = ReadMessageResponseBody()
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


class SearchContentRequest(TeaModel):
    def __init__(
        self,
        device_info: SearchContentRequestDeviceInfo = None,
        request: SearchContentRequestRequest = None,
        user_info: SearchContentRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.request = request
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
        self.device_info_shrink = device_info_shrink
        self.request_shrink = request_shrink
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


class SendMessageRequest(TeaModel):
    def __init__(
        self,
        url: str = None,
        user_info: SendMessageRequestUserInfo = None,
    ):
        self.url = url
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


class SetDeviceSettingRequest(TeaModel):
    def __init__(
        self,
        device_info: SetDeviceSettingRequestDeviceInfo = None,
        key: str = None,
        value: Any = None,
    ):
        self.device_info = device_info
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
        self.device_info_shrink = device_info_shrink
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
            temp_model = SetDeviceSettingResponseBody()
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


class UnbindDeviceRequestUserInfo(TeaModel):
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


class UnbindDeviceRequest(TeaModel):
    def __init__(
        self,
        device_info: UnbindDeviceRequestDeviceInfo = None,
        user_info: UnbindDeviceRequestUserInfo = None,
    ):
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
        self.device_info_shrink = device_info_shrink
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


class UpdateAlarmRequestPayloadMusicInfo(TeaModel):
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
        self.alarm_id = alarm_id
        self.music_info = music_info
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


class UpdateAlarmRequest(TeaModel):
    def __init__(
        self,
        device_info: UpdateAlarmRequestDeviceInfo = None,
        payload: UpdateAlarmRequestPayload = None,
        user_info: UpdateAlarmRequestUserInfo = None,
    ):
        self.device_info = device_info
        self.payload = payload
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
        self.device_info_shrink = device_info_shrink
        self.payload_shrink = payload_shrink
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
            temp_model = UpdateAlarmResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self



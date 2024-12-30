# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class LinkInfo(TeaModel):
    def __init__(
        self,
        extra: str = None,
        identity: str = None,
        type: str = None,
    ):
        self.extra = extra
        self.identity = identity
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class AccountAccessTokenResponse(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        avatar: str = None,
        default_drive_id: str = None,
        default_sbox_drive_id: str = None,
        device_id: str = None,
        device_name: str = None,
        domain_id: str = None,
        exist_link: List[LinkInfo] = None,
        expire_time: str = None,
        expires_in: int = None,
        is_first_login: bool = None,
        need_link: bool = None,
        need_rp_verify: bool = None,
        nick_name: str = None,
        path_status: str = None,
        pin_setup: bool = None,
        refresh_token: str = None,
        role: str = None,
        state: str = None,
        status: str = None,
        token_type: str = None,
        user_data: Dict[str, str] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.access_token = access_token
        self.avatar = avatar
        self.default_drive_id = default_drive_id
        self.default_sbox_drive_id = default_sbox_drive_id
        self.device_id = device_id
        self.device_name = device_name
        self.domain_id = domain_id
        self.exist_link = exist_link
        self.expire_time = expire_time
        self.expires_in = expires_in
        self.is_first_login = is_first_login
        self.need_link = need_link
        self.need_rp_verify = need_rp_verify
        self.nick_name = nick_name
        self.path_status = path_status
        self.pin_setup = pin_setup
        self.refresh_token = refresh_token
        self.role = role
        self.state = state
        self.status = status
        self.token_type = token_type
        self.user_data = user_data
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.exist_link:
            for k in self.exist_link:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.default_sbox_drive_id is not None:
            result['default_sbox_drive_id'] = self.default_sbox_drive_id
        if self.device_id is not None:
            result['device_id'] = self.device_id
        if self.device_name is not None:
            result['device_name'] = self.device_name
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        result['exist_link'] = []
        if self.exist_link is not None:
            for k in self.exist_link:
                result['exist_link'].append(k.to_map() if k else None)
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.is_first_login is not None:
            result['is_first_login'] = self.is_first_login
        if self.need_link is not None:
            result['need_link'] = self.need_link
        if self.need_rp_verify is not None:
            result['need_rp_verify'] = self.need_rp_verify
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.path_status is not None:
            result['path_status'] = self.path_status
        if self.pin_setup is not None:
            result['pin_setup'] = self.pin_setup
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        if self.role is not None:
            result['role'] = self.role
        if self.state is not None:
            result['state'] = self.state
        if self.status is not None:
            result['status'] = self.status
        if self.token_type is not None:
            result['token_type'] = self.token_type
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('default_sbox_drive_id') is not None:
            self.default_sbox_drive_id = m.get('default_sbox_drive_id')
        if m.get('device_id') is not None:
            self.device_id = m.get('device_id')
        if m.get('device_name') is not None:
            self.device_name = m.get('device_name')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        self.exist_link = []
        if m.get('exist_link') is not None:
            for k in m.get('exist_link'):
                temp_model = LinkInfo()
                self.exist_link.append(temp_model.from_map(k))
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('is_first_login') is not None:
            self.is_first_login = m.get('is_first_login')
        if m.get('need_link') is not None:
            self.need_link = m.get('need_link')
        if m.get('need_rp_verify') is not None:
            self.need_rp_verify = m.get('need_rp_verify')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('path_status') is not None:
            self.path_status = m.get('path_status')
        if m.get('pin_setup') is not None:
            self.pin_setup = m.get('pin_setup')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('token_type') is not None:
            self.token_type = m.get('token_type')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class AccountLinkInfo(TeaModel):
    def __init__(
        self,
        authentication_type: str = None,
        created_at: int = None,
        display_name: str = None,
        domain_id: str = None,
        extra: str = None,
        identity: str = None,
        last_login_time: int = None,
        status: str = None,
        user_id: str = None,
    ):
        self.authentication_type = authentication_type
        self.created_at = created_at
        self.display_name = display_name
        self.domain_id = domain_id
        self.extra = extra
        self.identity = identity
        self.last_login_time = last_login_time
        self.status = status
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_type is not None:
            result['authentication_type'] = self.authentication_type
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.display_name is not None:
            result['display_name'] = self.display_name
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.last_login_time is not None:
            result['last_login_time'] = self.last_login_time
        if self.status is not None:
            result['status'] = self.status
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authentication_type') is not None:
            self.authentication_type = m.get('authentication_type')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('display_name') is not None:
            self.display_name = m.get('display_name')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('last_login_time') is not None:
            self.last_login_time = m.get('last_login_time')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class Activity(TeaModel):
    def __init__(
        self,
        activity_id: str = None,
        device: str = None,
        drive_id: str = None,
        event_type: int = None,
        latest_event_time: str = None,
        resource_category: int = None,
        resource_list: List[Dict[str, Any]] = None,
        total_resource_count: int = None,
        user_id: str = None,
    ):
        self.activity_id = activity_id
        self.device = device
        self.drive_id = drive_id
        self.event_type = event_type
        self.latest_event_time = latest_event_time
        self.resource_category = resource_category
        self.resource_list = resource_list
        self.total_resource_count = total_resource_count
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['activity_id'] = self.activity_id
        if self.device is not None:
            result['device'] = self.device
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.event_type is not None:
            result['event_type'] = self.event_type
        if self.latest_event_time is not None:
            result['latest_event_time'] = self.latest_event_time
        if self.resource_category is not None:
            result['resource_category'] = self.resource_category
        if self.resource_list is not None:
            result['resource_list'] = self.resource_list
        if self.total_resource_count is not None:
            result['total_resource_count'] = self.total_resource_count
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activity_id') is not None:
            self.activity_id = m.get('activity_id')
        if m.get('device') is not None:
            self.device = m.get('device')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('event_type') is not None:
            self.event_type = m.get('event_type')
        if m.get('latest_event_time') is not None:
            self.latest_event_time = m.get('latest_event_time')
        if m.get('resource_category') is not None:
            self.resource_category = m.get('resource_category')
        if m.get('resource_list') is not None:
            self.resource_list = m.get('resource_list')
        if m.get('total_resource_count') is not None:
            self.total_resource_count = m.get('total_resource_count')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class AddStoryFile(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        file_id: str = None,
        revision_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.file_id = file_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_message is not None:
            result['error_message'] = self.error_message
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class Address(TeaModel):
    def __init__(
        self,
        city: str = None,
        country: str = None,
        district: str = None,
        province: str = None,
        township: str = None,
    ):
        self.city = city
        self.country = country
        self.district = district
        self.province = province
        self.township = township

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.city is not None:
            result['city'] = self.city
        if self.country is not None:
            result['country'] = self.country
        if self.district is not None:
            result['district'] = self.district
        if self.province is not None:
            result['province'] = self.province
        if self.township is not None:
            result['township'] = self.township
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('district') is not None:
            self.district = m.get('district')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('township') is not None:
            self.township = m.get('township')
        return self


class AddressGroup(TeaModel):
    def __init__(
        self,
        address_detail: Address = None,
        count: int = None,
        cover_file_id: str = None,
        cover_url: str = None,
        location: str = None,
        name: str = None,
    ):
        self.address_detail = address_detail
        self.count = count
        self.cover_file_id = cover_file_id
        self.cover_url = cover_url
        self.location = location
        self.name = name

    def validate(self):
        if self.address_detail:
            self.address_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_detail is not None:
            result['address_detail'] = self.address_detail.to_map()
        if self.count is not None:
            result['count'] = self.count
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id
        if self.cover_url is not None:
            result['cover_url'] = self.cover_url
        if self.location is not None:
            result['location'] = self.location
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address_detail') is not None:
            temp_model = Address()
            self.address_detail = temp_model.from_map(m['address_detail'])
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')
        if m.get('cover_url') is not None:
            self.cover_url = m.get('cover_url')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class AggregationsGroup(TeaModel):
    def __init__(
        self,
        count: int = None,
        value: bytes = None,
    ):
        self.count = count
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class Aggregation(TeaModel):
    def __init__(
        self,
        field: bytes = None,
        groups: List[AggregationsGroup] = None,
        operation: bytes = None,
        value: float = None,
    ):
        self.field = field
        self.groups = groups
        self.operation = operation
        self.value = value

    def validate(self):
        if self.groups:
            for k in self.groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['field'] = self.field
        result['groups'] = []
        if self.groups is not None:
            for k in self.groups:
                result['groups'].append(k.to_map() if k else None)
        if self.operation is not None:
            result['operation'] = self.operation
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')
        self.groups = []
        if m.get('groups') is not None:
            for k in m.get('groups'):
                temp_model = AggregationsGroup()
                self.groups.append(temp_model.from_map(k))
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class FaceThumbnail(TeaModel):
    def __init__(
        self,
        face_group_id: str = None,
        face_id: str = None,
        face_thumbnail: str = None,
    ):
        self.face_group_id = face_group_id
        self.face_id = face_id
        self.face_thumbnail = face_thumbnail

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.face_group_id is not None:
            result['face_group_id'] = self.face_group_id
        if self.face_id is not None:
            result['face_id'] = self.face_id
        if self.face_thumbnail is not None:
            result['face_thumbnail'] = self.face_thumbnail
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('face_group_id') is not None:
            self.face_group_id = m.get('face_group_id')
        if m.get('face_id') is not None:
            self.face_id = m.get('face_id')
        if m.get('face_thumbnail') is not None:
            self.face_thumbnail = m.get('face_thumbnail')
        return self


class ImageQuality(TeaModel):
    def __init__(
        self,
        overall_score: float = None,
    ):
        self.overall_score = overall_score

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.overall_score is not None:
            result['overall_score'] = self.overall_score
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('overall_score') is not None:
            self.overall_score = m.get('overall_score')
        return self


class SystemTag(TeaModel):
    def __init__(
        self,
        centric_score: float = None,
        confidence: float = None,
        name: str = None,
        parent_name: str = None,
        tag_level: int = None,
    ):
        self.centric_score = centric_score
        self.confidence = confidence
        self.name = name
        self.parent_name = parent_name
        self.tag_level = tag_level

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.centric_score is not None:
            result['centric_score'] = self.centric_score
        if self.confidence is not None:
            result['confidence'] = self.confidence
        if self.name is not None:
            result['name'] = self.name
        if self.parent_name is not None:
            result['parent_name'] = self.parent_name
        if self.tag_level is not None:
            result['tag_level'] = self.tag_level
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('centric_score') is not None:
            self.centric_score = m.get('centric_score')
        if m.get('confidence') is not None:
            self.confidence = m.get('confidence')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_name') is not None:
            self.parent_name = m.get('parent_name')
        if m.get('tag_level') is not None:
            self.tag_level = m.get('tag_level')
        return self


class ImageMediaMetadata(TeaModel):
    def __init__(
        self,
        address_line: str = None,
        city: str = None,
        country: str = None,
        district: str = None,
        exif: str = None,
        faces_thumbnail: List[FaceThumbnail] = None,
        height: int = None,
        image_quality: ImageQuality = None,
        image_tags: List[SystemTag] = None,
        location: str = None,
        province: str = None,
        time: str = None,
        township: str = None,
        width: int = None,
    ):
        self.address_line = address_line
        self.city = city
        self.country = country
        self.district = district
        self.exif = exif
        self.faces_thumbnail = faces_thumbnail
        self.height = height
        self.image_quality = image_quality
        self.image_tags = image_tags
        self.location = location
        self.province = province
        self.time = time
        self.township = township
        self.width = width

    def validate(self):
        if self.faces_thumbnail:
            for k in self.faces_thumbnail:
                if k:
                    k.validate()
        if self.image_quality:
            self.image_quality.validate()
        if self.image_tags:
            for k in self.image_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_line is not None:
            result['address_line'] = self.address_line
        if self.city is not None:
            result['city'] = self.city
        if self.country is not None:
            result['country'] = self.country
        if self.district is not None:
            result['district'] = self.district
        if self.exif is not None:
            result['exif'] = self.exif
        result['faces_thumbnail'] = []
        if self.faces_thumbnail is not None:
            for k in self.faces_thumbnail:
                result['faces_thumbnail'].append(k.to_map() if k else None)
        if self.height is not None:
            result['height'] = self.height
        if self.image_quality is not None:
            result['image_quality'] = self.image_quality.to_map()
        result['image_tags'] = []
        if self.image_tags is not None:
            for k in self.image_tags:
                result['image_tags'].append(k.to_map() if k else None)
        if self.location is not None:
            result['location'] = self.location
        if self.province is not None:
            result['province'] = self.province
        if self.time is not None:
            result['time'] = self.time
        if self.township is not None:
            result['township'] = self.township
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address_line') is not None:
            self.address_line = m.get('address_line')
        if m.get('city') is not None:
            self.city = m.get('city')
        if m.get('country') is not None:
            self.country = m.get('country')
        if m.get('district') is not None:
            self.district = m.get('district')
        if m.get('exif') is not None:
            self.exif = m.get('exif')
        self.faces_thumbnail = []
        if m.get('faces_thumbnail') is not None:
            for k in m.get('faces_thumbnail'):
                temp_model = FaceThumbnail()
                self.faces_thumbnail.append(temp_model.from_map(k))
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('image_quality') is not None:
            temp_model = ImageQuality()
            self.image_quality = temp_model.from_map(m['image_quality'])
        self.image_tags = []
        if m.get('image_tags') is not None:
            for k in m.get('image_tags'):
                temp_model = SystemTag()
                self.image_tags.append(temp_model.from_map(k))
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('province') is not None:
            self.province = m.get('province')
        if m.get('time') is not None:
            self.time = m.get('time')
        if m.get('township') is not None:
            self.township = m.get('township')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class VideoMediaAudioStream(TeaModel):
    def __init__(
        self,
        bit_rate: str = None,
        code_name: str = None,
        duration: str = None,
    ):
        self.bit_rate = bit_rate
        self.code_name = code_name
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bit_rate is not None:
            result['bit_rate'] = self.bit_rate
        if self.code_name is not None:
            result['code_name'] = self.code_name
        if self.duration is not None:
            result['duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bit_rate') is not None:
            self.bit_rate = m.get('bit_rate')
        if m.get('code_name') is not None:
            self.code_name = m.get('code_name')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        return self


class VideoMediaVideoStream(TeaModel):
    def __init__(
        self,
        bitrate: str = None,
        code_name: str = None,
        duration: str = None,
        frame_count: str = None,
    ):
        self.bitrate = bitrate
        self.code_name = code_name
        self.duration = duration
        self.frame_count = frame_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bitrate is not None:
            result['bitrate'] = self.bitrate
        if self.code_name is not None:
            result['code_name'] = self.code_name
        if self.duration is not None:
            result['duration'] = self.duration
        if self.frame_count is not None:
            result['frame_count'] = self.frame_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bitrate') is not None:
            self.bitrate = m.get('bitrate')
        if m.get('code_name') is not None:
            self.code_name = m.get('code_name')
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('frame_count') is not None:
            self.frame_count = m.get('frame_count')
        return self


class VideoMediaMetadata(TeaModel):
    def __init__(
        self,
        height: int = None,
        video_media_audio_stream: List[VideoMediaAudioStream] = None,
        video_media_video_stream: List[VideoMediaVideoStream] = None,
        width: int = None,
    ):
        self.height = height
        self.video_media_audio_stream = video_media_audio_stream
        self.video_media_video_stream = video_media_video_stream
        self.width = width

    def validate(self):
        if self.video_media_audio_stream:
            for k in self.video_media_audio_stream:
                if k:
                    k.validate()
        if self.video_media_video_stream:
            for k in self.video_media_video_stream:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['height'] = self.height
        result['video_media_audio_stream'] = []
        if self.video_media_audio_stream is not None:
            for k in self.video_media_audio_stream:
                result['video_media_audio_stream'].append(k.to_map() if k else None)
        result['video_media_video_stream'] = []
        if self.video_media_video_stream is not None:
            for k in self.video_media_video_stream:
                result['video_media_video_stream'].append(k.to_map() if k else None)
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        self.video_media_audio_stream = []
        if m.get('video_media_audio_stream') is not None:
            for k in m.get('video_media_audio_stream'):
                temp_model = VideoMediaAudioStream()
                self.video_media_audio_stream.append(temp_model.from_map(k))
        self.video_media_video_stream = []
        if m.get('video_media_video_stream') is not None:
            for k in m.get('video_media_video_stream'):
                temp_model = VideoMediaVideoStream()
                self.video_media_video_stream.append(temp_model.from_map(k))
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class File(TeaModel):
    def __init__(
        self,
        action_list: List[str] = None,
        category: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        file_extension: str = None,
        file_id: str = None,
        hidden: bool = None,
        id_path: str = None,
        image_media_metadata: ImageMediaMetadata = None,
        labels: List[str] = None,
        local_created_at: str = None,
        local_modified_at: str = None,
        name: str = None,
        name_path: str = None,
        parent_file_id: str = None,
        revision_id: str = None,
        size: int = None,
        starred: bool = None,
        status: str = None,
        thumbnail: str = None,
        thumbnail_urls: Dict[str, str] = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        user_tags: Dict[str, str] = None,
        video_media_metadata: VideoMediaMetadata = None,
    ):
        self.action_list = action_list
        self.category = category
        self.content_hash = content_hash
        self.content_hash_name = content_hash_name
        self.content_type = content_type
        self.crc_64hash = crc_64hash
        self.created_at = created_at
        self.description = description
        self.domain_id = domain_id
        self.download_url = download_url
        self.drive_id = drive_id
        self.file_extension = file_extension
        self.file_id = file_id
        self.hidden = hidden
        self.id_path = id_path
        self.image_media_metadata = image_media_metadata
        self.labels = labels
        self.local_created_at = local_created_at
        self.local_modified_at = local_modified_at
        self.name = name
        self.name_path = name_path
        self.parent_file_id = parent_file_id
        self.revision_id = revision_id
        self.size = size
        self.starred = starred
        self.status = status
        self.thumbnail = thumbnail
        self.thumbnail_urls = thumbnail_urls
        self.trashed_at = trashed_at
        self.type = type
        self.updated_at = updated_at
        self.upload_id = upload_id
        self.user_tags = user_tags
        self.video_media_metadata = video_media_metadata

    def validate(self):
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_list is not None:
            result['action_list'] = self.action_list
        if self.category is not None:
            result['category'] = self.category
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.id_path is not None:
            result['id_path'] = self.id_path
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        if self.labels is not None:
            result['labels'] = self.labels
        if self.local_created_at is not None:
            result['local_created_at'] = self.local_created_at
        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at
        if self.name is not None:
            result['name'] = self.name
        if self.name_path is not None:
            result['name_path'] = self.name_path
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        if self.size is not None:
            result['size'] = self.size
        if self.starred is not None:
            result['starred'] = self.starred
        if self.status is not None:
            result['status'] = self.status
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.thumbnail_urls is not None:
            result['thumbnail_urls'] = self.thumbnail_urls
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.user_tags is not None:
            result['user_tags'] = self.user_tags
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_list') is not None:
            self.action_list = m.get('action_list')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('id_path') is not None:
            self.id_path = m.get('id_path')
        if m.get('image_media_metadata') is not None:
            temp_model = ImageMediaMetadata()
            self.image_media_metadata = temp_model.from_map(m['image_media_metadata'])
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('local_created_at') is not None:
            self.local_created_at = m.get('local_created_at')
        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('name_path') is not None:
            self.name_path = m.get('name_path')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('thumbnail_urls') is not None:
            self.thumbnail_urls = m.get('thumbnail_urls')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('user_tags') is not None:
            self.user_tags = m.get('user_tags')
        if m.get('video_media_metadata') is not None:
            temp_model = VideoMediaMetadata()
            self.video_media_metadata = temp_model.from_map(m['video_media_metadata'])
        return self


class Album(TeaModel):
    def __init__(
        self,
        album_id: str = None,
        base_face_file: File = None,
        base_face_group_id: str = None,
        cover_file: File = None,
        created_at: str = None,
        description: str = None,
        file_count: int = None,
        name: str = None,
        owner: str = None,
        updated_at: str = None,
        user_tags: Dict[str, str] = None,
    ):
        self.album_id = album_id
        self.base_face_file = base_face_file
        self.base_face_group_id = base_face_group_id
        self.cover_file = cover_file
        self.created_at = created_at
        self.description = description
        self.file_count = file_count
        self.name = name
        self.owner = owner
        self.updated_at = updated_at
        self.user_tags = user_tags

    def validate(self):
        if self.base_face_file:
            self.base_face_file.validate()
        if self.cover_file:
            self.cover_file.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['album_id'] = self.album_id
        if self.base_face_file is not None:
            result['base_face_file'] = self.base_face_file.to_map()
        if self.base_face_group_id is not None:
            result['base_face_group_id'] = self.base_face_group_id
        if self.cover_file is not None:
            result['cover_file'] = self.cover_file.to_map()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.file_count is not None:
            result['file_count'] = self.file_count
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_tags is not None:
            result['user_tags'] = self.user_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('album_id') is not None:
            self.album_id = m.get('album_id')
        if m.get('base_face_file') is not None:
            temp_model = File()
            self.base_face_file = temp_model.from_map(m['base_face_file'])
        if m.get('base_face_group_id') is not None:
            self.base_face_group_id = m.get('base_face_group_id')
        if m.get('cover_file') is not None:
            temp_model = File()
            self.cover_file = temp_model.from_map(m['cover_file'])
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('file_count') is not None:
            self.file_count = m.get('file_count')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_tags') is not None:
            self.user_tags = m.get('user_tags')
        return self


class InvestigationInfoVideoDetailBlockFrames(TeaModel):
    def __init__(
        self,
        label: str = None,
        offset: int = None,
        rate: float = None,
    ):
        self.label = label
        self.offset = offset
        self.rate = rate

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.label is not None:
            result['label'] = self.label
        if self.offset is not None:
            result['offset'] = self.offset
        if self.rate is not None:
            result['rate'] = self.rate
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('label') is not None:
            self.label = m.get('label')
        if m.get('offset') is not None:
            self.offset = m.get('offset')
        if m.get('rate') is not None:
            self.rate = m.get('rate')
        return self


class InvestigationInfoVideoDetail(TeaModel):
    def __init__(
        self,
        block_frames: List[InvestigationInfoVideoDetailBlockFrames] = None,
    ):
        self.block_frames = block_frames

    def validate(self):
        if self.block_frames:
            for k in self.block_frames:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['block_frames'] = []
        if self.block_frames is not None:
            for k in self.block_frames:
                result['block_frames'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.block_frames = []
        if m.get('block_frames') is not None:
            for k in m.get('block_frames'):
                temp_model = InvestigationInfoVideoDetailBlockFrames()
                self.block_frames.append(temp_model.from_map(k))
        return self


class InvestigationInfo(TeaModel):
    def __init__(
        self,
        status: int = None,
        suggestion: str = None,
        video_detail: InvestigationInfoVideoDetail = None,
    ):
        self.status = status
        self.suggestion = suggestion
        self.video_detail = video_detail

    def validate(self):
        if self.video_detail:
            self.video_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.suggestion is not None:
            result['suggestion'] = self.suggestion
        if self.video_detail is not None:
            result['video_detail'] = self.video_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('suggestion') is not None:
            self.suggestion = m.get('suggestion')
        if m.get('video_detail') is not None:
            temp_model = InvestigationInfoVideoDetail()
            self.video_detail = temp_model.from_map(m['video_detail'])
        return self


class AlbumFile(TeaModel):
    def __init__(
        self,
        album_id: str = None,
        category: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        ex_fields_info: Dict[str, Any] = None,
        file_extension: str = None,
        file_id: str = None,
        hidden: bool = None,
        image_media_metadata: ImageMediaMetadata = None,
        investigation_info: InvestigationInfo = None,
        joined_at: int = None,
        labels: List[str] = None,
        local_created_at: str = None,
        local_modified_at: str = None,
        mime_type: str = None,
        name: str = None,
        object_uri: str = None,
        parent_file_id: str = None,
        revision_id: str = None,
        size: int = None,
        starred: bool = None,
        status: str = None,
        thumbnail: str = None,
        thumbnail_urls: Dict[str, str] = None,
        transhed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        user_meta: str = None,
    ):
        self.album_id = album_id
        self.category = category
        self.content_hash = content_hash
        self.content_hash_name = content_hash_name
        self.content_type = content_type
        self.crc_64hash = crc_64hash
        self.created_at = created_at
        self.description = description
        self.domain_id = domain_id
        self.download_url = download_url
        self.drive_id = drive_id
        self.ex_fields_info = ex_fields_info
        self.file_extension = file_extension
        self.file_id = file_id
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        self.investigation_info = investigation_info
        self.joined_at = joined_at
        self.labels = labels
        self.local_created_at = local_created_at
        self.local_modified_at = local_modified_at
        self.mime_type = mime_type
        self.name = name
        self.object_uri = object_uri
        self.parent_file_id = parent_file_id
        self.revision_id = revision_id
        self.size = size
        self.starred = starred
        self.status = status
        self.thumbnail = thumbnail
        self.thumbnail_urls = thumbnail_urls
        self.transhed_at = transhed_at
        self.type = type
        self.updated_at = updated_at
        self.upload_id = upload_id
        self.user_meta = user_meta

    def validate(self):
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        if self.investigation_info:
            self.investigation_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.album_id is not None:
            result['album_id'] = self.album_id
        if self.category is not None:
            result['category'] = self.category
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.ex_fields_info is not None:
            result['ex_fields_info'] = self.ex_fields_info
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        if self.investigation_info is not None:
            result['investigation_info'] = self.investigation_info.to_map()
        if self.joined_at is not None:
            result['joined_at'] = self.joined_at
        if self.labels is not None:
            result['labels'] = self.labels
        if self.local_created_at is not None:
            result['local_created_at'] = self.local_created_at
        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at
        if self.mime_type is not None:
            result['mime_type'] = self.mime_type
        if self.name is not None:
            result['name'] = self.name
        if self.object_uri is not None:
            result['object_uri'] = self.object_uri
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        if self.size is not None:
            result['size'] = self.size
        if self.starred is not None:
            result['starred'] = self.starred
        if self.status is not None:
            result['status'] = self.status
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.thumbnail_urls is not None:
            result['thumbnail_urls'] = self.thumbnail_urls
        if self.transhed_at is not None:
            result['transhed_at'] = self.transhed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.user_meta is not None:
            result['user_meta'] = self.user_meta
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('album_id') is not None:
            self.album_id = m.get('album_id')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('ex_fields_info') is not None:
            self.ex_fields_info = m.get('ex_fields_info')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('image_media_metadata') is not None:
            temp_model = ImageMediaMetadata()
            self.image_media_metadata = temp_model.from_map(m['image_media_metadata'])
        if m.get('investigation_info') is not None:
            temp_model = InvestigationInfo()
            self.investigation_info = temp_model.from_map(m['investigation_info'])
        if m.get('joined_at') is not None:
            self.joined_at = m.get('joined_at')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('local_created_at') is not None:
            self.local_created_at = m.get('local_created_at')
        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')
        if m.get('mime_type') is not None:
            self.mime_type = m.get('mime_type')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('object_uri') is not None:
            self.object_uri = m.get('object_uri')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('thumbnail_urls') is not None:
            self.thumbnail_urls = m.get('thumbnail_urls')
        if m.get('transhed_at') is not None:
            self.transhed_at = m.get('transhed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('user_meta') is not None:
            self.user_meta = m.get('user_meta')
        return self


class App(TeaModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        app_secret: str = None,
        created_at: str = None,
        description: str = None,
        logo: str = None,
        provider: str = None,
        redirect_uri: str = None,
        scope: List[str] = None,
        stage: str = None,
        type: str = None,
        updated_at: str = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.app_secret = app_secret
        self.created_at = created_at
        self.description = description
        self.logo = logo
        self.provider = provider
        self.redirect_uri = redirect_uri
        self.scope = scope
        self.stage = stage
        self.type = type
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.app_id is not None:
            result['app_id'] = self.app_id
        if self.app_name is not None:
            result['app_name'] = self.app_name
        if self.app_secret is not None:
            result['app_secret'] = self.app_secret
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.logo is not None:
            result['logo'] = self.logo
        if self.provider is not None:
            result['provider'] = self.provider
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        if self.scope is not None:
            result['scope'] = self.scope
        if self.stage is not None:
            result['stage'] = self.stage
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('app_id') is not None:
            self.app_id = m.get('app_id')
        if m.get('app_name') is not None:
            self.app_name = m.get('app_name')
        if m.get('app_secret') is not None:
            self.app_secret = m.get('app_secret')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('logo') is not None:
            self.logo = m.get('logo')
        if m.get('provider') is not None:
            self.provider = m.get('provider')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('stage') is not None:
            self.stage = m.get('stage')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class AppAccessStrategy(TeaModel):
    def __init__(
        self,
        effect: str = None,
        except_app_id_list: List[str] = None,
    ):
        self.effect = effect
        self.except_app_id_list = except_app_id_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect is not None:
            result['effect'] = self.effect
        if self.except_app_id_list is not None:
            result['except_app_id_list'] = self.except_app_id_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('except_app_id_list') is not None:
            self.except_app_id_list = m.get('except_app_id_list')
        return self


class ArchiveFilesConfigResponse(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        version: str = None,
    ):
        self.enabled = enabled
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class DriveLogDetailUpdateTo(TeaModel):
    def __init__(
        self,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        owner_type: str = None,
        total_size: int = None,
    ):
        self.name = name
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.name is not None:
            result['name'] = self.name
        if self.owner_id is not None:
            result['owner_id'] = self.owner_id
        if self.owner_name is not None:
            result['owner_name'] = self.owner_name
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.total_size is not None:
            result['total_size'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner_id') is not None:
            self.owner_id = m.get('owner_id')
        if m.get('owner_name') is not None:
            self.owner_name = m.get('owner_name')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        return self


class DriveLogDetail(TeaModel):
    def __init__(
        self,
        force_delete: bool = None,
        handover_owner_name: str = None,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        owner_type: str = None,
        total_size: int = None,
        update_to: DriveLogDetailUpdateTo = None,
    ):
        self.force_delete = force_delete
        self.handover_owner_name = handover_owner_name
        self.name = name
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.total_size = total_size
        self.update_to = update_to

    def validate(self):
        if self.update_to:
            self.update_to.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.force_delete is not None:
            result['force_delete'] = self.force_delete
        if self.handover_owner_name is not None:
            result['handover_owner_name'] = self.handover_owner_name
        if self.name is not None:
            result['name'] = self.name
        if self.owner_id is not None:
            result['owner_id'] = self.owner_id
        if self.owner_name is not None:
            result['owner_name'] = self.owner_name
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.update_to is not None:
            result['update_to'] = self.update_to.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('force_delete') is not None:
            self.force_delete = m.get('force_delete')
        if m.get('handover_owner_name') is not None:
            self.handover_owner_name = m.get('handover_owner_name')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner_id') is not None:
            self.owner_id = m.get('owner_id')
        if m.get('owner_name') is not None:
            self.owner_name = m.get('owner_name')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('update_to') is not None:
            temp_model = DriveLogDetailUpdateTo()
            self.update_to = temp_model.from_map(m['update_to'])
        return self


class FileLogDetail(TeaModel):
    def __init__(
        self,
        decompress_file_list: List[str] = None,
        new_name: str = None,
        parent_path: str = None,
        rev_version: int = None,
        revision_id: str = None,
        size: int = None,
        to_parent_path: str = None,
        to_parent_path_type: str = None,
        type: str = None,
    ):
        self.decompress_file_list = decompress_file_list
        self.new_name = new_name
        self.parent_path = parent_path
        self.rev_version = rev_version
        self.revision_id = revision_id
        self.size = size
        self.to_parent_path = to_parent_path
        self.to_parent_path_type = to_parent_path_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.decompress_file_list is not None:
            result['decompress_file_list'] = self.decompress_file_list
        if self.new_name is not None:
            result['new_name'] = self.new_name
        if self.parent_path is not None:
            result['parent_path'] = self.parent_path
        if self.rev_version is not None:
            result['rev_version'] = self.rev_version
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        if self.size is not None:
            result['size'] = self.size
        if self.to_parent_path is not None:
            result['to_parent_path'] = self.to_parent_path
        if self.to_parent_path_type is not None:
            result['to_parent_path_type'] = self.to_parent_path_type
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('decompress_file_list') is not None:
            self.decompress_file_list = m.get('decompress_file_list')
        if m.get('new_name') is not None:
            self.new_name = m.get('new_name')
        if m.get('parent_path') is not None:
            self.parent_path = m.get('parent_path')
        if m.get('rev_version') is not None:
            self.rev_version = m.get('rev_version')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('to_parent_path') is not None:
            self.to_parent_path = m.get('to_parent_path')
        if m.get('to_parent_path_type') is not None:
            self.to_parent_path_type = m.get('to_parent_path_type')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class UserLogDetailUpdateTo(TeaModel):
    def __init__(
        self,
        email: str = None,
        expired_at: int = None,
        name: str = None,
        phone: str = None,
        role_id: str = None,
    ):
        self.email = email
        self.expired_at = expired_at
        self.name = name
        self.phone = phone
        self.role_id = role_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.expired_at is not None:
            result['expired_at'] = self.expired_at
        if self.name is not None:
            result['name'] = self.name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role_id is not None:
            result['role_id'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('expired_at') is not None:
            self.expired_at = m.get('expired_at')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        return self


class UserLogDetail(TeaModel):
    def __init__(
        self,
        email: str = None,
        expired_at: int = None,
        name: str = None,
        phone: str = None,
        role_id: str = None,
        update_to: UserLogDetailUpdateTo = None,
    ):
        self.email = email
        self.expired_at = expired_at
        self.name = name
        self.phone = phone
        self.role_id = role_id
        self.update_to = update_to

    def validate(self):
        if self.update_to:
            self.update_to.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.expired_at is not None:
            result['expired_at'] = self.expired_at
        if self.name is not None:
            result['name'] = self.name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role_id is not None:
            result['role_id'] = self.role_id
        if self.update_to is not None:
            result['update_to'] = self.update_to.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('expired_at') is not None:
            self.expired_at = m.get('expired_at')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        if m.get('update_to') is not None:
            temp_model = UserLogDetailUpdateTo()
            self.update_to = temp_model.from_map(m['update_to'])
        return self


class AuditLogDetail(TeaModel):
    def __init__(
        self,
        drive_log_detail: DriveLogDetail = None,
        file_log_detail: FileLogDetail = None,
        user_log_detail: UserLogDetail = None,
    ):
        self.drive_log_detail = drive_log_detail
        self.file_log_detail = file_log_detail
        self.user_log_detail = user_log_detail

    def validate(self):
        if self.drive_log_detail:
            self.drive_log_detail.validate()
        if self.file_log_detail:
            self.file_log_detail.validate()
        if self.user_log_detail:
            self.user_log_detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_log_detail is not None:
            result['drive_log_detail'] = self.drive_log_detail.to_map()
        if self.file_log_detail is not None:
            result['file_log_detail'] = self.file_log_detail.to_map()
        if self.user_log_detail is not None:
            result['user_log_detail'] = self.user_log_detail.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_log_detail') is not None:
            temp_model = DriveLogDetail()
            self.drive_log_detail = temp_model.from_map(m['drive_log_detail'])
        if m.get('file_log_detail') is not None:
            temp_model = FileLogDetail()
            self.file_log_detail = temp_model.from_map(m['file_log_detail'])
        if m.get('user_log_detail') is not None:
            temp_model = UserLogDetail()
            self.user_log_detail = temp_model.from_map(m['user_log_detail'])
        return self


class AuditLog(TeaModel):
    def __init__(
        self,
        acted_at: str = None,
        action_category: str = None,
        action_type: str = None,
        actor_id: str = None,
        actor_name: str = None,
        actor_type: str = None,
        client_device: str = None,
        client_ip: str = None,
        client_type: str = None,
        client_version: str = None,
        detail: AuditLogDetail = None,
        file_path_type: str = None,
        log_id: str = None,
        object_id: str = None,
        object_name: str = None,
    ):
        self.acted_at = acted_at
        self.action_category = action_category
        self.action_type = action_type
        self.actor_id = actor_id
        self.actor_name = actor_name
        self.actor_type = actor_type
        self.client_device = client_device
        self.client_ip = client_ip
        self.client_type = client_type
        self.client_version = client_version
        self.detail = detail
        self.file_path_type = file_path_type
        self.log_id = log_id
        self.object_id = object_id
        self.object_name = object_name

    def validate(self):
        if self.detail:
            self.detail.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.acted_at is not None:
            result['acted_at'] = self.acted_at
        if self.action_category is not None:
            result['action_category'] = self.action_category
        if self.action_type is not None:
            result['action_type'] = self.action_type
        if self.actor_id is not None:
            result['actor_id'] = self.actor_id
        if self.actor_name is not None:
            result['actor_name'] = self.actor_name
        if self.actor_type is not None:
            result['actor_type'] = self.actor_type
        if self.client_device is not None:
            result['client_device'] = self.client_device
        if self.client_ip is not None:
            result['client_ip'] = self.client_ip
        if self.client_type is not None:
            result['client_type'] = self.client_type
        if self.client_version is not None:
            result['client_version'] = self.client_version
        if self.detail is not None:
            result['detail'] = self.detail.to_map()
        if self.file_path_type is not None:
            result['file_path_type'] = self.file_path_type
        if self.log_id is not None:
            result['log_id'] = self.log_id
        if self.object_id is not None:
            result['object_id'] = self.object_id
        if self.object_name is not None:
            result['object_name'] = self.object_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acted_at') is not None:
            self.acted_at = m.get('acted_at')
        if m.get('action_category') is not None:
            self.action_category = m.get('action_category')
        if m.get('action_type') is not None:
            self.action_type = m.get('action_type')
        if m.get('actor_id') is not None:
            self.actor_id = m.get('actor_id')
        if m.get('actor_name') is not None:
            self.actor_name = m.get('actor_name')
        if m.get('actor_type') is not None:
            self.actor_type = m.get('actor_type')
        if m.get('client_device') is not None:
            self.client_device = m.get('client_device')
        if m.get('client_ip') is not None:
            self.client_ip = m.get('client_ip')
        if m.get('client_type') is not None:
            self.client_type = m.get('client_type')
        if m.get('client_version') is not None:
            self.client_version = m.get('client_version')
        if m.get('detail') is not None:
            temp_model = AuditLogDetail()
            self.detail = temp_model.from_map(m['detail'])
        if m.get('file_path_type') is not None:
            self.file_path_type = m.get('file_path_type')
        if m.get('log_id') is not None:
            self.log_id = m.get('log_id')
        if m.get('object_id') is not None:
            self.object_id = m.get('object_id')
        if m.get('object_name') is not None:
            self.object_name = m.get('object_name')
        return self


class CommonFileItem(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        revision_id: str = None,
    ):
        self.drive_id = drive_id
        self.file_id = file_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class BaseAlbumFileOperationResult(TeaModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        file: CommonFileItem = None,
        is_succeed: bool = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.file = file
        self.is_succeed = is_succeed

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_message is not None:
            result['error_message'] = self.error_message
        if self.file is not None:
            result['file'] = self.file.to_map()
        if self.is_succeed is not None:
            result['is_succeed'] = self.is_succeed
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')
        if m.get('file') is not None:
            temp_model = CommonFileItem()
            self.file = temp_model.from_map(m['file'])
        if m.get('is_succeed') is not None:
            self.is_succeed = m.get('is_succeed')
        return self


class Identity(TeaModel):
    def __init__(
        self,
        identity_id: str = None,
        identity_type: str = None,
    ):
        self.identity_id = identity_id
        self.identity_type = identity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_id is not None:
            result['identity_id'] = self.identity_id
        if self.identity_type is not None:
            result['identity_type'] = self.identity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')
        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')
        return self


class BaseAssignmentResponse(TeaModel):
    def __init__(
        self,
        associated_role_tag_id: str = None,
        created_at: str = None,
        creator: str = None,
        disinherit_sub_group: bool = None,
        domain_id: str = None,
        identity: Identity = None,
        manage_resource_id: str = None,
        manage_resource_type: str = None,
        role_id: str = None,
        updated_at: str = None,
    ):
        self.associated_role_tag_id = associated_role_tag_id
        self.created_at = created_at
        self.creator = creator
        self.disinherit_sub_group = disinherit_sub_group
        self.domain_id = domain_id
        self.identity = identity
        self.manage_resource_id = manage_resource_id
        self.manage_resource_type = manage_resource_type
        self.role_id = role_id
        self.updated_at = updated_at

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.associated_role_tag_id is not None:
            result['associated_role_tag_id'] = self.associated_role_tag_id
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.disinherit_sub_group is not None:
            result['disinherit_sub_group'] = self.disinherit_sub_group
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.identity is not None:
            result['identity'] = self.identity.to_map()
        if self.manage_resource_id is not None:
            result['manage_resource_id'] = self.manage_resource_id
        if self.manage_resource_type is not None:
            result['manage_resource_type'] = self.manage_resource_type
        if self.role_id is not None:
            result['role_id'] = self.role_id
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('associated_role_tag_id') is not None:
            self.associated_role_tag_id = m.get('associated_role_tag_id')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('disinherit_sub_group') is not None:
            self.disinherit_sub_group = m.get('disinherit_sub_group')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('identity') is not None:
            temp_model = Identity()
            self.identity = temp_model.from_map(m['identity'])
        if m.get('manage_resource_id') is not None:
            self.manage_resource_id = m.get('manage_resource_id')
        if m.get('manage_resource_type') is not None:
            self.manage_resource_type = m.get('manage_resource_type')
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class BaseDomainResponse(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        domain_name: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        parent_domain_id: str = None,
        published_app_access_strategy: AppAccessStrategy = None,
        share_link_enabled: bool = None,
        size_quota: int = None,
        size_quota_used: int = None,
        status: int = None,
        updated_at: str = None,
        used_size: int = None,
    ):
        self.created_at = created_at
        self.description = description
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.init_drive_enable = init_drive_enable
        self.init_drive_size = init_drive_size
        self.parent_domain_id = parent_domain_id
        self.published_app_access_strategy = published_app_access_strategy
        self.share_link_enabled = share_link_enabled
        self.size_quota = size_quota
        self.size_quota_used = size_quota_used
        self.status = status
        self.updated_at = updated_at
        self.used_size = used_size

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.domain_name is not None:
            result['domain_name'] = self.domain_name
        if self.init_drive_enable is not None:
            result['init_drive_enable'] = self.init_drive_enable
        if self.init_drive_size is not None:
            result['init_drive_size'] = self.init_drive_size
        if self.parent_domain_id is not None:
            result['parent_domain_id'] = self.parent_domain_id
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        if self.share_link_enabled is not None:
            result['share_link_enabled'] = self.share_link_enabled
        if self.size_quota is not None:
            result['size_quota'] = self.size_quota
        if self.size_quota_used is not None:
            result['size_quota_used'] = self.size_quota_used
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.used_size is not None:
            result['used_size'] = self.used_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')
        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')
        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')
        if m.get('parent_domain_id') is not None:
            self.parent_domain_id = m.get('parent_domain_id')
        if m.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(m['published_app_access_strategy'])
        if m.get('share_link_enabled') is not None:
            self.share_link_enabled = m.get('share_link_enabled')
        if m.get('size_quota') is not None:
            self.size_quota = m.get('size_quota')
        if m.get('size_quota_used') is not None:
            self.size_quota_used = m.get('size_quota_used')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')
        return self


class PermissionConditionIpEquals(TeaModel):
    def __init__(
        self,
        client_ip: List[str] = None,
    ):
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['client_ip'] = self.client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_ip') is not None:
            self.client_ip = m.get('client_ip')
        return self


class PermissionConditionIpNotEquals(TeaModel):
    def __init__(
        self,
        client_ip: List[str] = None,
    ):
        self.client_ip = client_ip

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_ip is not None:
            result['client_ip'] = self.client_ip
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_ip') is not None:
            self.client_ip = m.get('client_ip')
        return self


class PermissionConditionStringLike(TeaModel):
    def __init__(
        self,
        vpc_id: List[str] = None,
    ):
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')
        return self


class PermissionConditionStringNotLike(TeaModel):
    def __init__(
        self,
        vpc_id: List[str] = None,
    ):
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.vpc_id is not None:
            result['vpc_id'] = self.vpc_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('vpc_id') is not None:
            self.vpc_id = m.get('vpc_id')
        return self


class PermissionCondition(TeaModel):
    def __init__(
        self,
        ip_equals: PermissionConditionIpEquals = None,
        ip_not_equals: PermissionConditionIpNotEquals = None,
        string_like: PermissionConditionStringLike = None,
        string_not_like: PermissionConditionStringNotLike = None,
    ):
        self.ip_equals = ip_equals
        self.ip_not_equals = ip_not_equals
        self.string_like = string_like
        self.string_not_like = string_not_like

    def validate(self):
        if self.ip_equals:
            self.ip_equals.validate()
        if self.ip_not_equals:
            self.ip_not_equals.validate()
        if self.string_like:
            self.string_like.validate()
        if self.string_not_like:
            self.string_not_like.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ip_equals is not None:
            result['ip_equals'] = self.ip_equals.to_map()
        if self.ip_not_equals is not None:
            result['ip_not_equals'] = self.ip_not_equals.to_map()
        if self.string_like is not None:
            result['string_like'] = self.string_like.to_map()
        if self.string_not_like is not None:
            result['string_not_like'] = self.string_not_like.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ip_equals') is not None:
            temp_model = PermissionConditionIpEquals()
            self.ip_equals = temp_model.from_map(m['ip_equals'])
        if m.get('ip_not_equals') is not None:
            temp_model = PermissionConditionIpNotEquals()
            self.ip_not_equals = temp_model.from_map(m['ip_not_equals'])
        if m.get('string_like') is not None:
            temp_model = PermissionConditionStringLike()
            self.string_like = temp_model.from_map(m['string_like'])
        if m.get('string_not_like') is not None:
            temp_model = PermissionConditionStringNotLike()
            self.string_not_like = temp_model.from_map(m['string_not_like'])
        return self


class PermissionActionList(TeaModel):
    def __init__(
        self,
        action: str = None,
    ):
        self.action = action

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action is not None:
            result['action'] = self.action
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action') is not None:
            self.action = m.get('action')
        return self


class Permission(TeaModel):
    def __init__(
        self,
        action_list: List[PermissionActionList] = None,
        collection: str = None,
        condition: PermissionCondition = None,
        created_at: int = None,
        effect: str = None,
        identity_id: str = None,
        identity_type: str = None,
        resource: str = None,
        resource_type: str = None,
        updated_at: int = None,
        user_tags: List[str] = None,
    ):
        self.action_list = action_list
        self.collection = collection
        self.condition = condition
        self.created_at = created_at
        self.effect = effect
        self.identity_id = identity_id
        self.identity_type = identity_type
        self.resource = resource
        self.resource_type = resource_type
        self.updated_at = updated_at
        self.user_tags = user_tags

    def validate(self):
        if self.action_list:
            for k in self.action_list:
                if k:
                    k.validate()
        if self.condition:
            self.condition.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['action_list'] = []
        if self.action_list is not None:
            for k in self.action_list:
                result['action_list'].append(k.to_map() if k else None)
        if self.collection is not None:
            result['collection'] = self.collection
        if self.condition is not None:
            result['condition'] = self.condition.to_map()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.effect is not None:
            result['effect'] = self.effect
        if self.identity_id is not None:
            result['identity_id'] = self.identity_id
        if self.identity_type is not None:
            result['identity_type'] = self.identity_type
        if self.resource is not None:
            result['resource'] = self.resource
        if self.resource_type is not None:
            result['resource_type'] = self.resource_type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_tags is not None:
            result['user_tags'] = self.user_tags
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.action_list = []
        if m.get('action_list') is not None:
            for k in m.get('action_list'):
                temp_model = PermissionActionList()
                self.action_list.append(temp_model.from_map(k))
        if m.get('collection') is not None:
            self.collection = m.get('collection')
        if m.get('condition') is not None:
            temp_model = PermissionCondition()
            self.condition = temp_model.from_map(m['condition'])
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('effect') is not None:
            self.effect = m.get('effect')
        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')
        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        if m.get('resource_type') is not None:
            self.resource_type = m.get('resource_type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_tags') is not None:
            self.user_tags = m.get('user_tags')
        return self


class IDPermission(TeaModel):
    def __init__(
        self,
        disinherit_sub_group: bool = None,
        expire_time: int = None,
        permission: Permission = None,
        roles: List[str] = None,
    ):
        self.disinherit_sub_group = disinherit_sub_group
        self.expire_time = expire_time
        self.permission = permission
        self.roles = roles

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.disinherit_sub_group is not None:
            result['disinherit_sub_group'] = self.disinherit_sub_group
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.permission is not None:
            result['permission'] = self.permission.to_map()
        if self.roles is not None:
            result['roles'] = self.roles
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('disinherit_sub_group') is not None:
            self.disinherit_sub_group = m.get('disinherit_sub_group')
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('permission') is not None:
            temp_model = Permission()
            self.permission = temp_model.from_map(m['permission'])
        if m.get('roles') is not None:
            self.roles = m.get('roles')
        return self


class BaseDriveResponse(TeaModel):
    def __init__(
        self,
        action_list: List[str] = None,
        category: str = None,
        created_at: str = None,
        creator: str = None,
        delta_enabled: bool = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        drive_name: str = None,
        drive_type: str = None,
        encrypt_data_access: bool = None,
        encrypt_mode: str = None,
        is_handover: bool = None,
        owner: str = None,
        owner_type: str = None,
        path_status: str = None,
        permission: Dict[str, IDPermission] = None,
        relative_path: str = None,
        status: str = None,
        store_id: str = None,
        total_size: int = None,
        updated_at: str = None,
        used_size: int = None,
    ):
        self.action_list = action_list
        self.category = category
        self.created_at = created_at
        self.creator = creator
        self.delta_enabled = delta_enabled
        self.description = description
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.drive_name = drive_name
        self.drive_type = drive_type
        self.encrypt_data_access = encrypt_data_access
        self.encrypt_mode = encrypt_mode
        self.is_handover = is_handover
        self.owner = owner
        self.owner_type = owner_type
        self.path_status = path_status
        self.permission = permission
        self.relative_path = relative_path
        self.status = status
        self.store_id = store_id
        self.total_size = total_size
        self.updated_at = updated_at
        self.used_size = used_size

    def validate(self):
        if self.permission:
            for v in self.permission.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_list is not None:
            result['action_list'] = self.action_list
        if self.category is not None:
            result['category'] = self.category
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.delta_enabled is not None:
            result['delta_enabled'] = self.delta_enabled
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.drive_type is not None:
            result['drive_type'] = self.drive_type
        if self.encrypt_data_access is not None:
            result['encrypt_data_access'] = self.encrypt_data_access
        if self.encrypt_mode is not None:
            result['encrypt_mode'] = self.encrypt_mode
        if self.is_handover is not None:
            result['is_handover'] = self.is_handover
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.path_status is not None:
            result['path_status'] = self.path_status
        result['permission'] = {}
        if self.permission is not None:
            for k, v in self.permission.items():
                result['permission'][k] = v.to_map()
        if self.relative_path is not None:
            result['relative_path'] = self.relative_path
        if self.status is not None:
            result['status'] = self.status
        if self.store_id is not None:
            result['store_id'] = self.store_id
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.used_size is not None:
            result['used_size'] = self.used_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_list') is not None:
            self.action_list = m.get('action_list')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('delta_enabled') is not None:
            self.delta_enabled = m.get('delta_enabled')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')
        if m.get('encrypt_data_access') is not None:
            self.encrypt_data_access = m.get('encrypt_data_access')
        if m.get('encrypt_mode') is not None:
            self.encrypt_mode = m.get('encrypt_mode')
        if m.get('is_handover') is not None:
            self.is_handover = m.get('is_handover')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('path_status') is not None:
            self.path_status = m.get('path_status')
        self.permission = {}
        if m.get('permission') is not None:
            for k, v in m.get('permission').items():
                temp_model = IDPermission()
                self.permission[k] = temp_model.from_map(v)
        if m.get('relative_path') is not None:
            self.relative_path = m.get('relative_path')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')
        return self


class FilePermissionMember(TeaModel):
    def __init__(
        self,
        action_list: List[str] = None,
        disinherit_sub_group: bool = None,
        expire_time: int = None,
        identity: Identity = None,
        role_id: str = None,
    ):
        self.action_list = action_list
        self.disinherit_sub_group = disinherit_sub_group
        self.expire_time = expire_time
        self.identity = identity
        self.role_id = role_id

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_list is not None:
            result['action_list'] = self.action_list
        if self.disinherit_sub_group is not None:
            result['disinherit_sub_group'] = self.disinherit_sub_group
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.identity is not None:
            result['identity'] = self.identity.to_map()
        if self.role_id is not None:
            result['role_id'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_list') is not None:
            self.action_list = m.get('action_list')
        if m.get('disinherit_sub_group') is not None:
            self.disinherit_sub_group = m.get('disinherit_sub_group')
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('identity') is not None:
            temp_model = Identity()
            self.identity = temp_model.from_map(m['identity'])
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        return self


class BaseFileListInheritPermissionResponse(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        member: FilePermissionMember = None,
    ):
        self.file_id = file_id
        self.member = member

    def validate(self):
        if self.member:
            self.member.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.member is not None:
            result['member'] = self.member.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('member') is not None:
            temp_model = FilePermissionMember()
            self.member = temp_model.from_map(m['member'])
        return self


class BaseFileUserPermissionResponse(TeaModel):
    def __init__(
        self,
        can_access: bool = None,
        created_at: int = None,
        creator: str = None,
        disinherit_sub_group: bool = None,
        domain_id: str = None,
        drive_id: str = None,
        expire_time: int = None,
        file_full_path: str = None,
        file_id: str = None,
        identity: Identity = None,
        role_id: str = None,
    ):
        self.can_access = can_access
        self.created_at = created_at
        self.creator = creator
        self.disinherit_sub_group = disinherit_sub_group
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.expire_time = expire_time
        self.file_full_path = file_full_path
        self.file_id = file_id
        self.identity = identity
        self.role_id = role_id

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.can_access is not None:
            result['can_access'] = self.can_access
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.disinherit_sub_group is not None:
            result['disinherit_sub_group'] = self.disinherit_sub_group
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.file_full_path is not None:
            result['file_full_path'] = self.file_full_path
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.identity is not None:
            result['identity'] = self.identity.to_map()
        if self.role_id is not None:
            result['role_id'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('can_access') is not None:
            self.can_access = m.get('can_access')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('disinherit_sub_group') is not None:
            self.disinherit_sub_group = m.get('disinherit_sub_group')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('file_full_path') is not None:
            self.file_full_path = m.get('file_full_path')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('identity') is not None:
            temp_model = Identity()
            self.identity = temp_model.from_map(m['identity'])
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        return self


class BaseGroupResponse(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        group_name: str = None,
        is_sync: bool = None,
        permission: Dict[str, IDPermission] = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.description = description
        self.domain_id = domain_id
        self.group_id = group_id
        self.group_name = group_name
        self.is_sync = is_sync
        self.permission = permission
        self.updated_at = updated_at

    def validate(self):
        if self.permission:
            for v in self.permission.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.is_sync is not None:
            result['is_sync'] = self.is_sync
        result['permission'] = {}
        if self.permission is not None:
            for k, v in self.permission.items():
                result['permission'][k] = v.to_map()
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('is_sync') is not None:
            self.is_sync = m.get('is_sync')
        self.permission = {}
        if m.get('permission') is not None:
            for k, v in m.get('permission').items():
                temp_model = IDPermission()
                self.permission[k] = temp_model.from_map(v)
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class BaseRoleMemberResponse(TeaModel):
    def __init__(
        self,
        assignment_list: List[BaseAssignmentResponse] = None,
        created_at: str = None,
        creator: str = None,
        domain_id: str = None,
        identity: Identity = None,
        identity_name: str = None,
        is_admin: bool = None,
        subdomain_id: str = None,
    ):
        self.assignment_list = assignment_list
        self.created_at = created_at
        self.creator = creator
        self.domain_id = domain_id
        self.identity = identity
        self.identity_name = identity_name
        self.is_admin = is_admin
        self.subdomain_id = subdomain_id

    def validate(self):
        if self.assignment_list:
            for k in self.assignment_list:
                if k:
                    k.validate()
        if self.identity:
            self.identity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['assignment_list'] = []
        if self.assignment_list is not None:
            for k in self.assignment_list:
                result['assignment_list'].append(k.to_map() if k else None)
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.identity is not None:
            result['identity'] = self.identity.to_map()
        if self.identity_name is not None:
            result['identity_name'] = self.identity_name
        if self.is_admin is not None:
            result['is_admin'] = self.is_admin
        if self.subdomain_id is not None:
            result['subdomain_id'] = self.subdomain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assignment_list = []
        if m.get('assignment_list') is not None:
            for k in m.get('assignment_list'):
                temp_model = BaseAssignmentResponse()
                self.assignment_list.append(temp_model.from_map(k))
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('identity') is not None:
            temp_model = Identity()
            self.identity = temp_model.from_map(m['identity'])
        if m.get('identity_name') is not None:
            self.identity_name = m.get('identity_name')
        if m.get('is_admin') is not None:
            self.is_admin = m.get('is_admin')
        if m.get('subdomain_id') is not None:
            self.subdomain_id = m.get('subdomain_id')
        return self


class BaseUserResponse(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        created_at: str = None,
        creator: str = None,
        default_drive_id: str = None,
        default_location: str = None,
        deny_change_password_by_self: bool = None,
        description: str = None,
        domain_id: str = None,
        email: str = None,
        expired_at: int = None,
        is_sync: bool = None,
        last_login_time: int = None,
        need_change_password_next_login: bool = None,
        nick_name: str = None,
        path_status: str = None,
        permission: Dict[str, IDPermission] = None,
        phone: str = None,
        phone_region: str = None,
        role: str = None,
        status: str = None,
        updated_at: str = None,
        user_data: Dict[str, Any] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.avatar = avatar
        self.created_at = created_at
        self.creator = creator
        self.default_drive_id = default_drive_id
        self.default_location = default_location
        self.deny_change_password_by_self = deny_change_password_by_self
        self.description = description
        self.domain_id = domain_id
        self.email = email
        self.expired_at = expired_at
        self.is_sync = is_sync
        self.last_login_time = last_login_time
        self.need_change_password_next_login = need_change_password_next_login
        self.nick_name = nick_name
        self.path_status = path_status
        self.permission = permission
        self.phone = phone
        self.phone_region = phone_region
        self.role = role
        self.status = status
        self.updated_at = updated_at
        self.user_data = user_data
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.permission:
            for v in self.permission.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.default_location is not None:
            result['default_location'] = self.default_location
        if self.deny_change_password_by_self is not None:
            result['deny_change_password_by_self'] = self.deny_change_password_by_self
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.email is not None:
            result['email'] = self.email
        if self.expired_at is not None:
            result['expired_at'] = self.expired_at
        if self.is_sync is not None:
            result['is_sync'] = self.is_sync
        if self.last_login_time is not None:
            result['last_login_time'] = self.last_login_time
        if self.need_change_password_next_login is not None:
            result['need_change_password_next_login'] = self.need_change_password_next_login
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.path_status is not None:
            result['path_status'] = self.path_status
        result['permission'] = {}
        if self.permission is not None:
            for k, v in self.permission.items():
                result['permission'][k] = v.to_map()
        if self.phone is not None:
            result['phone'] = self.phone
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('default_location') is not None:
            self.default_location = m.get('default_location')
        if m.get('deny_change_password_by_self') is not None:
            self.deny_change_password_by_self = m.get('deny_change_password_by_self')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('expired_at') is not None:
            self.expired_at = m.get('expired_at')
        if m.get('is_sync') is not None:
            self.is_sync = m.get('is_sync')
        if m.get('last_login_time') is not None:
            self.last_login_time = m.get('last_login_time')
        if m.get('need_change_password_next_login') is not None:
            self.need_change_password_next_login = m.get('need_change_password_next_login')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('path_status') is not None:
            self.path_status = m.get('path_status')
        self.permission = {}
        if m.get('permission') is not None:
            for k, v in m.get('permission').items():
                temp_model = IDPermission()
                self.permission[k] = temp_model.from_map(v)
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('phone_region') is not None:
            self.phone_region = m.get('phone_region')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class BenefitPkgDeliveryInfo(TeaModel):
    def __init__(
        self,
        amount: int = None,
        created_at: str = None,
        expire_time: str = None,
        is_permanent: bool = None,
    ):
        self.amount = amount
        self.created_at = created_at
        self.expire_time = expire_time
        self.is_permanent = is_permanent

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.is_permanent is not None:
            result['is_permanent'] = self.is_permanent
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('is_permanent') is not None:
            self.is_permanent = m.get('is_permanent')
        return self


class CNameStatus(TeaModel):
    def __init__(
        self,
        bingding_state: str = None,
        legal_state: str = None,
        remark: str = None,
    ):
        self.bingding_state = bingding_state
        self.legal_state = legal_state
        self.remark = remark

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bingding_state is not None:
            result['bingding_state'] = self.bingding_state
        if self.legal_state is not None:
            result['legal_state'] = self.legal_state
        if self.remark is not None:
            result['remark'] = self.remark
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bingding_state') is not None:
            self.bingding_state = m.get('bingding_state')
        if m.get('legal_state') is not None:
            self.legal_state = m.get('legal_state')
        if m.get('remark') is not None:
            self.remark = m.get('remark')
        return self


class CdnFileDownloadCallbackInfo(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        domain_id: str = None,
        drive_id: str = None,
        expire: int = None,
        file_id: str = None,
        object: str = None,
        token: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.bucket = bucket
        # This parameter is required.
        self.domain_id = domain_id
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.expire = expire
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.object = object
        # This parameter is required.
        self.token = token
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire is not None:
            result['expire'] = self.expire
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.object is not None:
            result['object'] = self.object
        if self.token is not None:
            result['token'] = self.token
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expire') is not None:
            self.expire = m.get('expire')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('object') is not None:
            self.object = m.get('object')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CertInfo(TeaModel):
    def __init__(
        self,
        cert_body: str = None,
        cert_name: str = None,
        cert_privatekey: str = None,
    ):
        self.cert_body = cert_body
        self.cert_name = cert_name
        self.cert_privatekey = cert_privatekey

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_body is not None:
            result['cert_body'] = self.cert_body
        if self.cert_name is not None:
            result['cert_name'] = self.cert_name
        if self.cert_privatekey is not None:
            result['cert_privatekey'] = self.cert_privatekey
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_body') is not None:
            self.cert_body = m.get('cert_body')
        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')
        if m.get('cert_privatekey') is not None:
            self.cert_privatekey = m.get('cert_privatekey')
        return self


class ClearRecycleBinItem(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        task_id: str = None,
    ):
        self.async_task_id = async_task_id
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class CssInstanceProperty(TeaModel):
    def __init__(
        self,
        code: str = None,
        global_key: str = None,
        name: str = None,
        unit: str = None,
        value: str = None,
    ):
        self.code = code
        self.global_key = global_key
        self.name = name
        self.unit = unit
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.global_key is not None:
            result['globalKey'] = self.global_key
        if self.name is not None:
            result['name'] = self.name
        if self.unit is not None:
            result['unit'] = self.unit
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('globalKey') is not None:
            self.global_key = m.get('globalKey')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('unit') is not None:
            self.unit = m.get('unit')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class CssInstanceComponent(TeaModel):
    def __init__(
        self,
        component_code: str = None,
        component_name: str = None,
        global_key: str = None,
        instance_property: List[CssInstanceProperty] = None,
        module_attr_status: int = None,
        tag: str = None,
    ):
        self.component_code = component_code
        self.component_name = component_name
        self.global_key = global_key
        self.instance_property = instance_property
        self.module_attr_status = module_attr_status
        self.tag = tag

    def validate(self):
        if self.instance_property:
            for k in self.instance_property:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.component_code is not None:
            result['componentCode'] = self.component_code
        if self.component_name is not None:
            result['componentName'] = self.component_name
        if self.global_key is not None:
            result['globalKey'] = self.global_key
        result['instanceProperty'] = []
        if self.instance_property is not None:
            for k in self.instance_property:
                result['instanceProperty'].append(k.to_map() if k else None)
        if self.module_attr_status is not None:
            result['moduleAttrStatus'] = self.module_attr_status
        if self.tag is not None:
            result['tag'] = self.tag
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentCode') is not None:
            self.component_code = m.get('componentCode')
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')
        if m.get('globalKey') is not None:
            self.global_key = m.get('globalKey')
        self.instance_property = []
        if m.get('instanceProperty') is not None:
            for k in m.get('instanceProperty'):
                temp_model = CssInstanceProperty()
                self.instance_property.append(temp_model.from_map(k))
        if m.get('moduleAttrStatus') is not None:
            self.module_attr_status = m.get('moduleAttrStatus')
        if m.get('tag') is not None:
            self.tag = m.get('tag')
        return self


class CssInstanceCommodity(TeaModel):
    def __init__(
        self,
        activity_id: int = None,
        aliyun_produce_code: str = None,
        charge_type: str = None,
        commodity_code: str = None,
        components: List[CssInstanceComponent] = None,
        duration: int = None,
        instance_id: str = None,
        is_free: bool = None,
        is_pre_pay_post_charge: bool = None,
        is_renew_change: bool = None,
        is_sync_to_subscription: bool = None,
        order_params: Dict[str, str] = None,
        order_type: str = None,
        plan_item_id: int = None,
        pricing_cycle: str = None,
        quantity: int = None,
        redeem_no_list: List[str] = None,
        redeem_order_type: str = None,
        refund_spec_code: str = None,
        spec_code: str = None,
        spec_upgrade_origin_spec_codes: List[str] = None,
        specify_start_date: int = None,
        upgrade_inquire_financial_value: bool = None,
    ):
        self.activity_id = activity_id
        self.aliyun_produce_code = aliyun_produce_code
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.components = components
        self.duration = duration
        self.instance_id = instance_id
        self.is_free = is_free
        self.is_pre_pay_post_charge = is_pre_pay_post_charge
        self.is_renew_change = is_renew_change
        self.is_sync_to_subscription = is_sync_to_subscription
        self.order_params = order_params
        self.order_type = order_type
        self.plan_item_id = plan_item_id
        self.pricing_cycle = pricing_cycle
        self.quantity = quantity
        self.redeem_no_list = redeem_no_list
        self.redeem_order_type = redeem_order_type
        self.refund_spec_code = refund_spec_code
        self.spec_code = spec_code
        self.spec_upgrade_origin_spec_codes = spec_upgrade_origin_spec_codes
        self.specify_start_date = specify_start_date
        self.upgrade_inquire_financial_value = upgrade_inquire_financial_value

    def validate(self):
        if self.components:
            for k in self.components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.activity_id is not None:
            result['activityId'] = self.activity_id
        if self.aliyun_produce_code is not None:
            result['aliyunProduceCode'] = self.aliyun_produce_code
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        result['components'] = []
        if self.components is not None:
            for k in self.components:
                result['components'].append(k.to_map() if k else None)
        if self.duration is not None:
            result['duration'] = self.duration
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.is_free is not None:
            result['isFree'] = self.is_free
        if self.is_pre_pay_post_charge is not None:
            result['isPrePayPostCharge'] = self.is_pre_pay_post_charge
        if self.is_renew_change is not None:
            result['isRenewChange'] = self.is_renew_change
        if self.is_sync_to_subscription is not None:
            result['isSyncToSubscription'] = self.is_sync_to_subscription
        if self.order_params is not None:
            result['orderParams'] = self.order_params
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.plan_item_id is not None:
            result['planItemId'] = self.plan_item_id
        if self.pricing_cycle is not None:
            result['pricingCycle'] = self.pricing_cycle
        if self.quantity is not None:
            result['quantity'] = self.quantity
        if self.redeem_no_list is not None:
            result['redeemNoList'] = self.redeem_no_list
        if self.redeem_order_type is not None:
            result['redeemOrderType'] = self.redeem_order_type
        if self.refund_spec_code is not None:
            result['refundSpecCode'] = self.refund_spec_code
        if self.spec_code is not None:
            result['specCode'] = self.spec_code
        if self.spec_upgrade_origin_spec_codes is not None:
            result['specUpgradeOriginSpecCodes'] = self.spec_upgrade_origin_spec_codes
        if self.specify_start_date is not None:
            result['specifyStartDate'] = self.specify_start_date
        if self.upgrade_inquire_financial_value is not None:
            result['upgradeInquireFinancialValue'] = self.upgrade_inquire_financial_value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('activityId') is not None:
            self.activity_id = m.get('activityId')
        if m.get('aliyunProduceCode') is not None:
            self.aliyun_produce_code = m.get('aliyunProduceCode')
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        self.components = []
        if m.get('components') is not None:
            for k in m.get('components'):
                temp_model = CssInstanceComponent()
                self.components.append(temp_model.from_map(k))
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('isFree') is not None:
            self.is_free = m.get('isFree')
        if m.get('isPrePayPostCharge') is not None:
            self.is_pre_pay_post_charge = m.get('isPrePayPostCharge')
        if m.get('isRenewChange') is not None:
            self.is_renew_change = m.get('isRenewChange')
        if m.get('isSyncToSubscription') is not None:
            self.is_sync_to_subscription = m.get('isSyncToSubscription')
        if m.get('orderParams') is not None:
            self.order_params = m.get('orderParams')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('planItemId') is not None:
            self.plan_item_id = m.get('planItemId')
        if m.get('pricingCycle') is not None:
            self.pricing_cycle = m.get('pricingCycle')
        if m.get('quantity') is not None:
            self.quantity = m.get('quantity')
        if m.get('redeemNoList') is not None:
            self.redeem_no_list = m.get('redeemNoList')
        if m.get('redeemOrderType') is not None:
            self.redeem_order_type = m.get('redeemOrderType')
        if m.get('refundSpecCode') is not None:
            self.refund_spec_code = m.get('refundSpecCode')
        if m.get('specCode') is not None:
            self.spec_code = m.get('specCode')
        if m.get('specUpgradeOriginSpecCodes') is not None:
            self.spec_upgrade_origin_spec_codes = m.get('specUpgradeOriginSpecCodes')
        if m.get('specifyStartDate') is not None:
            self.specify_start_date = m.get('specifyStartDate')
        if m.get('upgradeInquireFinancialValue') is not None:
            self.upgrade_inquire_financial_value = m.get('upgradeInquireFinancialValue')
        return self


class CssCreateOrderParam(TeaModel):
    def __init__(
        self,
        agent_id: str = None,
        auto_pay: bool = None,
        auto_use_coupon: bool = None,
        bid: str = None,
        buyer_id: int = None,
        certificate: str = None,
        child_id: int = None,
        cilent_ip: str = None,
        commodities: List[CssInstanceCommodity] = None,
        creater_nick: str = None,
        css_auth_request_param: Any = None,
        from_app: str = None,
        language: str = None,
        market_type: int = None,
        memo: str = None,
        order_origin: str = None,
        order_params: Dict[str, str] = None,
        payer_id: int = None,
        plan_group_id: int = None,
        plan_id: int = None,
        plan_instance_id: str = None,
        promotion_code: str = None,
        promotion_input_param: Any = None,
        request_id: str = None,
        skip_channel: bool = None,
        token: str = None,
        transient_access: Any = None,
        umid_token: str = None,
        user_id: int = None,
    ):
        self.agent_id = agent_id
        self.auto_pay = auto_pay
        self.auto_use_coupon = auto_use_coupon
        self.bid = bid
        self.buyer_id = buyer_id
        self.certificate = certificate
        self.child_id = child_id
        self.cilent_ip = cilent_ip
        self.commodities = commodities
        self.creater_nick = creater_nick
        self.css_auth_request_param = css_auth_request_param
        self.from_app = from_app
        self.language = language
        self.market_type = market_type
        self.memo = memo
        self.order_origin = order_origin
        self.order_params = order_params
        self.payer_id = payer_id
        self.plan_group_id = plan_group_id
        self.plan_id = plan_id
        self.plan_instance_id = plan_instance_id
        self.promotion_code = promotion_code
        self.promotion_input_param = promotion_input_param
        self.request_id = request_id
        self.skip_channel = skip_channel
        self.token = token
        self.transient_access = transient_access
        self.umid_token = umid_token
        self.user_id = user_id

    def validate(self):
        if self.commodities:
            for k in self.commodities:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['agentId'] = self.agent_id
        if self.auto_pay is not None:
            result['autoPay'] = self.auto_pay
        if self.auto_use_coupon is not None:
            result['autoUseCoupon'] = self.auto_use_coupon
        if self.bid is not None:
            result['bid'] = self.bid
        if self.buyer_id is not None:
            result['buyerId'] = self.buyer_id
        if self.certificate is not None:
            result['certificate'] = self.certificate
        if self.child_id is not None:
            result['childId'] = self.child_id
        if self.cilent_ip is not None:
            result['cilentIp'] = self.cilent_ip
        result['commodities'] = []
        if self.commodities is not None:
            for k in self.commodities:
                result['commodities'].append(k.to_map() if k else None)
        if self.creater_nick is not None:
            result['createrNick'] = self.creater_nick
        if self.css_auth_request_param is not None:
            result['cssAuthRequestParam'] = self.css_auth_request_param
        if self.from_app is not None:
            result['fromApp'] = self.from_app
        if self.language is not None:
            result['language'] = self.language
        if self.market_type is not None:
            result['marketType'] = self.market_type
        if self.memo is not None:
            result['memo'] = self.memo
        if self.order_origin is not None:
            result['orderOrigin'] = self.order_origin
        if self.order_params is not None:
            result['orderParams'] = self.order_params
        if self.payer_id is not None:
            result['payerId'] = self.payer_id
        if self.plan_group_id is not None:
            result['planGroupId'] = self.plan_group_id
        if self.plan_id is not None:
            result['planId'] = self.plan_id
        if self.plan_instance_id is not None:
            result['planInstanceId'] = self.plan_instance_id
        if self.promotion_code is not None:
            result['promotionCode'] = self.promotion_code
        if self.promotion_input_param is not None:
            result['promotionInputParam'] = self.promotion_input_param
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.skip_channel is not None:
            result['skipChannel'] = self.skip_channel
        if self.token is not None:
            result['token'] = self.token
        if self.transient_access is not None:
            result['transientAccess'] = self.transient_access
        if self.umid_token is not None:
            result['umidToken'] = self.umid_token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('agentId') is not None:
            self.agent_id = m.get('agentId')
        if m.get('autoPay') is not None:
            self.auto_pay = m.get('autoPay')
        if m.get('autoUseCoupon') is not None:
            self.auto_use_coupon = m.get('autoUseCoupon')
        if m.get('bid') is not None:
            self.bid = m.get('bid')
        if m.get('buyerId') is not None:
            self.buyer_id = m.get('buyerId')
        if m.get('certificate') is not None:
            self.certificate = m.get('certificate')
        if m.get('childId') is not None:
            self.child_id = m.get('childId')
        if m.get('cilentIp') is not None:
            self.cilent_ip = m.get('cilentIp')
        self.commodities = []
        if m.get('commodities') is not None:
            for k in m.get('commodities'):
                temp_model = CssInstanceCommodity()
                self.commodities.append(temp_model.from_map(k))
        if m.get('createrNick') is not None:
            self.creater_nick = m.get('createrNick')
        if m.get('cssAuthRequestParam') is not None:
            self.css_auth_request_param = m.get('cssAuthRequestParam')
        if m.get('fromApp') is not None:
            self.from_app = m.get('fromApp')
        if m.get('language') is not None:
            self.language = m.get('language')
        if m.get('marketType') is not None:
            self.market_type = m.get('marketType')
        if m.get('memo') is not None:
            self.memo = m.get('memo')
        if m.get('orderOrigin') is not None:
            self.order_origin = m.get('orderOrigin')
        if m.get('orderParams') is not None:
            self.order_params = m.get('orderParams')
        if m.get('payerId') is not None:
            self.payer_id = m.get('payerId')
        if m.get('planGroupId') is not None:
            self.plan_group_id = m.get('planGroupId')
        if m.get('planId') is not None:
            self.plan_id = m.get('planId')
        if m.get('planInstanceId') is not None:
            self.plan_instance_id = m.get('planInstanceId')
        if m.get('promotionCode') is not None:
            self.promotion_code = m.get('promotionCode')
        if m.get('promotionInputParam') is not None:
            self.promotion_input_param = m.get('promotionInputParam')
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('skipChannel') is not None:
            self.skip_channel = m.get('skipChannel')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('transientAccess') is not None:
            self.transient_access = m.get('transientAccess')
        if m.get('umidToken') is not None:
            self.umid_token = m.get('umidToken')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CssPurchase(TeaModel):
    def __init__(
        self,
        charge_type: str = None,
        commodity_code: str = None,
        end_date: int = None,
        gmt_create: int = None,
        instance_components: List[CssInstanceComponent] = None,
        instance_id: str = None,
        order_type: str = None,
        purchase_params: Dict[str, str] = None,
        start_date: int = None,
    ):
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.end_date = end_date
        self.gmt_create = gmt_create
        self.instance_components = instance_components
        self.instance_id = instance_id
        self.order_type = order_type
        self.purchase_params = purchase_params
        self.start_date = start_date

    def validate(self):
        if self.instance_components:
            for k in self.instance_components:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.charge_type is not None:
            result['chargeType'] = self.charge_type
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.end_date is not None:
            result['endDate'] = self.end_date
        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create
        result['instanceComponents'] = []
        if self.instance_components is not None:
            for k in self.instance_components:
                result['instanceComponents'].append(k.to_map() if k else None)
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.order_type is not None:
            result['orderType'] = self.order_type
        if self.purchase_params is not None:
            result['purchaseParams'] = self.purchase_params
        if self.start_date is not None:
            result['startDate'] = self.start_date
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chargeType') is not None:
            self.charge_type = m.get('chargeType')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('endDate') is not None:
            self.end_date = m.get('endDate')
        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')
        self.instance_components = []
        if m.get('instanceComponents') is not None:
            for k in m.get('instanceComponents'):
                temp_model = CssInstanceComponent()
                self.instance_components.append(temp_model.from_map(k))
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('orderType') is not None:
            self.order_type = m.get('orderType')
        if m.get('purchaseParams') is not None:
            self.purchase_params = m.get('purchaseParams')
        if m.get('startDate') is not None:
            self.start_date = m.get('startDate')
        return self


class CssProduce(TeaModel):
    def __init__(
        self,
        bid: str = None,
        buyer_id: int = None,
        child_id: int = None,
        from_app: str = None,
        order_id: int = None,
        payer_id: int = None,
        purchases: List[CssPurchase] = None,
        request_id: str = None,
        skip_channel: bool = None,
        token: str = None,
        user_id: int = None,
    ):
        self.bid = bid
        self.buyer_id = buyer_id
        self.child_id = child_id
        self.from_app = from_app
        self.order_id = order_id
        self.payer_id = payer_id
        self.purchases = purchases
        self.request_id = request_id
        self.skip_channel = skip_channel
        self.token = token
        self.user_id = user_id

    def validate(self):
        if self.purchases:
            for k in self.purchases:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bid is not None:
            result['bid'] = self.bid
        if self.buyer_id is not None:
            result['buyerId'] = self.buyer_id
        if self.child_id is not None:
            result['childId'] = self.child_id
        if self.from_app is not None:
            result['fromApp'] = self.from_app
        if self.order_id is not None:
            result['orderId'] = self.order_id
        if self.payer_id is not None:
            result['payerId'] = self.payer_id
        result['purchases'] = []
        if self.purchases is not None:
            for k in self.purchases:
                result['purchases'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['requestId'] = self.request_id
        if self.skip_channel is not None:
            result['skipChannel'] = self.skip_channel
        if self.token is not None:
            result['token'] = self.token
        if self.user_id is not None:
            result['userId'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bid') is not None:
            self.bid = m.get('bid')
        if m.get('buyerId') is not None:
            self.buyer_id = m.get('buyerId')
        if m.get('childId') is not None:
            self.child_id = m.get('childId')
        if m.get('fromApp') is not None:
            self.from_app = m.get('fromApp')
        if m.get('orderId') is not None:
            self.order_id = m.get('orderId')
        if m.get('payerId') is not None:
            self.payer_id = m.get('payerId')
        self.purchases = []
        if m.get('purchases') is not None:
            for k in m.get('purchases'):
                temp_model = CssPurchase()
                self.purchases.append(temp_model.from_map(k))
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')
        if m.get('skipChannel') is not None:
            self.skip_channel = m.get('skipChannel')
        if m.get('token') is not None:
            self.token = m.get('token')
        if m.get('userId') is not None:
            self.user_id = m.get('userId')
        return self


class CustomSideLinkConfig(TeaModel):
    def __init__(
        self,
        icon: str = None,
        link: str = None,
        text: str = None,
    ):
        self.icon = icon
        self.link = link
        self.text = text

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.icon is not None:
            result['icon'] = self.icon
        if self.link is not None:
            result['link'] = self.link
        if self.text is not None:
            result['text'] = self.text
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('link') is not None:
            self.link = m.get('link')
        if m.get('text') is not None:
            self.text = m.get('text')
        return self


class DataBoxPrivileges(TeaModel):
    def __init__(
        self,
        feature_attr_id: str = None,
        feature_id: str = None,
        quota: int = None,
    ):
        self.feature_attr_id = feature_attr_id
        self.feature_id = feature_id
        self.quota = quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.feature_attr_id is not None:
            result['feature_attr_id'] = self.feature_attr_id
        if self.feature_id is not None:
            result['feature_id'] = self.feature_id
        if self.quota is not None:
            result['quota'] = self.quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('feature_attr_id') is not None:
            self.feature_attr_id = m.get('feature_attr_id')
        if m.get('feature_id') is not None:
            self.feature_id = m.get('feature_id')
        if m.get('quota') is not None:
            self.quota = m.get('quota')
        return self


class DataCName(TeaModel):
    def __init__(
        self,
        cert_expire_time: int = None,
        cert_name: str = None,
        cname: str = None,
        cname_type: str = None,
        location: str = None,
        store_id: str = None,
    ):
        self.cert_expire_time = cert_expire_time
        self.cert_name = cert_name
        self.cname = cname
        self.cname_type = cname_type
        self.location = location
        self.store_id = store_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cert_expire_time is not None:
            result['cert_expire_time'] = self.cert_expire_time
        if self.cert_name is not None:
            result['cert_name'] = self.cert_name
        if self.cname is not None:
            result['cname'] = self.cname
        if self.cname_type is not None:
            result['cname_type'] = self.cname_type
        if self.location is not None:
            result['location'] = self.location
        if self.store_id is not None:
            result['store_id'] = self.store_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cert_expire_time') is not None:
            self.cert_expire_time = m.get('cert_expire_time')
        if m.get('cert_name') is not None:
            self.cert_name = m.get('cert_name')
        if m.get('cname') is not None:
            self.cname = m.get('cname')
        if m.get('cname_type') is not None:
            self.cname_type = m.get('cname_type')
        if m.get('location') is not None:
            self.location = m.get('location')
        if m.get('store_id') is not None:
            self.store_id = m.get('store_id')
        return self


class Domain(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        data_hash_name: str = None,
        description: str = None,
        domain_id: str = None,
        domain_name: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        parent_domain_id: str = None,
        published_app_access_strategy: AppAccessStrategy = None,
        sharable: bool = None,
        size_quota: int = None,
        size_quota_used: int = None,
        status: int = None,
        updated_at: str = None,
        used_size: int = None,
        user_count_quota: int = None,
    ):
        self.created_at = created_at
        self.data_hash_name = data_hash_name
        self.description = description
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.init_drive_enable = init_drive_enable
        self.init_drive_size = init_drive_size
        self.parent_domain_id = parent_domain_id
        self.published_app_access_strategy = published_app_access_strategy
        self.sharable = sharable
        self.size_quota = size_quota
        self.size_quota_used = size_quota_used
        self.status = status
        self.updated_at = updated_at
        self.used_size = used_size
        self.user_count_quota = user_count_quota

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.data_hash_name is not None:
            result['data_hash_name'] = self.data_hash_name
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.domain_name is not None:
            result['domain_name'] = self.domain_name
        if self.init_drive_enable is not None:
            result['init_drive_enable'] = self.init_drive_enable
        if self.init_drive_size is not None:
            result['init_drive_size'] = self.init_drive_size
        if self.parent_domain_id is not None:
            result['parent_domain_id'] = self.parent_domain_id
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        if self.sharable is not None:
            result['sharable'] = self.sharable
        if self.size_quota is not None:
            result['size_quota'] = self.size_quota
        if self.size_quota_used is not None:
            result['size_quota_used'] = self.size_quota_used
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.used_size is not None:
            result['used_size'] = self.used_size
        if self.user_count_quota is not None:
            result['user_count_quota'] = self.user_count_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('data_hash_name') is not None:
            self.data_hash_name = m.get('data_hash_name')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')
        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')
        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')
        if m.get('parent_domain_id') is not None:
            self.parent_domain_id = m.get('parent_domain_id')
        if m.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(m['published_app_access_strategy'])
        if m.get('sharable') is not None:
            self.sharable = m.get('sharable')
        if m.get('size_quota') is not None:
            self.size_quota = m.get('size_quota')
        if m.get('size_quota_used') is not None:
            self.size_quota_used = m.get('size_quota_used')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')
        if m.get('user_count_quota') is not None:
            self.user_count_quota = m.get('user_count_quota')
        return self


class DomainAppConfig(TeaModel):
    def __init__(
        self,
        allow_upload_custom_file_ext_list: List[str] = None,
        allow_upload_file_category_list: List[str] = None,
        same_name_file_upload_mode: str = None,
        single_file_upload_size_limit: int = None,
        web_client_download_mode: str = None,
    ):
        self.allow_upload_custom_file_ext_list = allow_upload_custom_file_ext_list
        self.allow_upload_file_category_list = allow_upload_file_category_list
        self.same_name_file_upload_mode = same_name_file_upload_mode
        self.single_file_upload_size_limit = single_file_upload_size_limit
        self.web_client_download_mode = web_client_download_mode

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_upload_custom_file_ext_list is not None:
            result['allow_upload_custom_file_ext_list'] = self.allow_upload_custom_file_ext_list
        if self.allow_upload_file_category_list is not None:
            result['allow_upload_file_category_list'] = self.allow_upload_file_category_list
        if self.same_name_file_upload_mode is not None:
            result['same_name_file_upload_mode'] = self.same_name_file_upload_mode
        if self.single_file_upload_size_limit is not None:
            result['single_file_upload_size_limit'] = self.single_file_upload_size_limit
        if self.web_client_download_mode is not None:
            result['web_client_download_mode'] = self.web_client_download_mode
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allow_upload_custom_file_ext_list') is not None:
            self.allow_upload_custom_file_ext_list = m.get('allow_upload_custom_file_ext_list')
        if m.get('allow_upload_file_category_list') is not None:
            self.allow_upload_file_category_list = m.get('allow_upload_file_category_list')
        if m.get('same_name_file_upload_mode') is not None:
            self.same_name_file_upload_mode = m.get('same_name_file_upload_mode')
        if m.get('single_file_upload_size_limit') is not None:
            self.single_file_upload_size_limit = m.get('single_file_upload_size_limit')
        if m.get('web_client_download_mode') is not None:
            self.web_client_download_mode = m.get('web_client_download_mode')
        return self


class DomainBuildClientConfig(TeaModel):
    def __init__(
        self,
        copyright: str = None,
        name: str = None,
    ):
        self.copyright = copyright
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copyright is not None:
            result['copyright'] = self.copyright
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('copyright') is not None:
            self.copyright = m.get('copyright')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class DomainEndpoints(TeaModel):
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


class WxTrustedDomainConfig(TeaModel):
    def __init__(
        self,
        content: str = None,
        name: str = None,
        show: bool = None,
    ):
        self.content = content
        self.name = name
        self.show = show

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content is not None:
            result['content'] = self.content
        if self.name is not None:
            result['name'] = self.name
        if self.show is not None:
            result['show'] = self.show
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content') is not None:
            self.content = m.get('content')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('show') is not None:
            self.show = m.get('show')
        return self


class DomainSeniorConfig(TeaModel):
    def __init__(
        self,
        client_download_enable: bool = None,
        csp_frame_ancestors: str = None,
        custom_login_appid: str = None,
        custom_login_url: str = None,
        custom_logout_url: str = None,
        custom_side_link_list: List[CustomSideLinkConfig] = None,
        home_page_bg_image_url: str = None,
        home_page_footer: str = None,
        home_page_footer_2: str = None,
        home_page_slogan: str = None,
        referer_enable: bool = None,
        wx_txt_list: WxTrustedDomainConfig = None,
    ):
        self.client_download_enable = client_download_enable
        self.csp_frame_ancestors = csp_frame_ancestors
        self.custom_login_appid = custom_login_appid
        self.custom_login_url = custom_login_url
        self.custom_logout_url = custom_logout_url
        self.custom_side_link_list = custom_side_link_list
        self.home_page_bg_image_url = home_page_bg_image_url
        self.home_page_footer = home_page_footer
        self.home_page_footer_2 = home_page_footer_2
        self.home_page_slogan = home_page_slogan
        self.referer_enable = referer_enable
        self.wx_txt_list = wx_txt_list

    def validate(self):
        if self.custom_side_link_list:
            for k in self.custom_side_link_list:
                if k:
                    k.validate()
        if self.wx_txt_list:
            self.wx_txt_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_download_enable is not None:
            result['client_download_enable'] = self.client_download_enable
        if self.csp_frame_ancestors is not None:
            result['csp_frame_ancestors'] = self.csp_frame_ancestors
        if self.custom_login_appid is not None:
            result['custom_login_appid'] = self.custom_login_appid
        if self.custom_login_url is not None:
            result['custom_login_url'] = self.custom_login_url
        if self.custom_logout_url is not None:
            result['custom_logout_url'] = self.custom_logout_url
        result['custom_side_link_list'] = []
        if self.custom_side_link_list is not None:
            for k in self.custom_side_link_list:
                result['custom_side_link_list'].append(k.to_map() if k else None)
        if self.home_page_bg_image_url is not None:
            result['home_page_bg_image_url'] = self.home_page_bg_image_url
        if self.home_page_footer is not None:
            result['home_page_footer'] = self.home_page_footer
        if self.home_page_footer_2 is not None:
            result['home_page_footer2'] = self.home_page_footer_2
        if self.home_page_slogan is not None:
            result['home_page_slogan'] = self.home_page_slogan
        if self.referer_enable is not None:
            result['referer_enable'] = self.referer_enable
        if self.wx_txt_list is not None:
            result['wx_txt_list'] = self.wx_txt_list.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_download_enable') is not None:
            self.client_download_enable = m.get('client_download_enable')
        if m.get('csp_frame_ancestors') is not None:
            self.csp_frame_ancestors = m.get('csp_frame_ancestors')
        if m.get('custom_login_appid') is not None:
            self.custom_login_appid = m.get('custom_login_appid')
        if m.get('custom_login_url') is not None:
            self.custom_login_url = m.get('custom_login_url')
        if m.get('custom_logout_url') is not None:
            self.custom_logout_url = m.get('custom_logout_url')
        self.custom_side_link_list = []
        if m.get('custom_side_link_list') is not None:
            for k in m.get('custom_side_link_list'):
                temp_model = CustomSideLinkConfig()
                self.custom_side_link_list.append(temp_model.from_map(k))
        if m.get('home_page_bg_image_url') is not None:
            self.home_page_bg_image_url = m.get('home_page_bg_image_url')
        if m.get('home_page_footer') is not None:
            self.home_page_footer = m.get('home_page_footer')
        if m.get('home_page_footer2') is not None:
            self.home_page_footer_2 = m.get('home_page_footer2')
        if m.get('home_page_slogan') is not None:
            self.home_page_slogan = m.get('home_page_slogan')
        if m.get('referer_enable') is not None:
            self.referer_enable = m.get('referer_enable')
        if m.get('wx_txt_list') is not None:
            temp_model = WxTrustedDomainConfig()
            self.wx_txt_list = temp_model.from_map(m['wx_txt_list'])
        return self


class Drive(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        drive_name: str = None,
        drive_type: str = None,
        owner: str = None,
        owner_type: str = None,
        status: str = None,
        total_size: int = None,
        used_size: int = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.description = description
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.drive_name = drive_name
        self.drive_type = drive_type
        self.owner = owner
        self.owner_type = owner_type
        self.status = status
        self.total_size = total_size
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.drive_type is not None:
            result['drive_type'] = self.drive_type
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.status is not None:
            result['status'] = self.status
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.used_size is not None:
            result['used_size'] = self.used_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')
        return self


class ExternalMultiFileRevisionConfig(TeaModel):
    def __init__(
        self,
        revision_count: int = None,
        revision_merge_enabled: bool = None,
        revision_recycle_period: int = None,
    ):
        self.revision_count = revision_count
        self.revision_merge_enabled = revision_merge_enabled
        self.revision_recycle_period = revision_recycle_period

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.revision_count is not None:
            result['revision_count'] = self.revision_count
        if self.revision_merge_enabled is not None:
            result['revision_merge_enabled'] = self.revision_merge_enabled
        if self.revision_recycle_period is not None:
            result['revision_recycle_period'] = self.revision_recycle_period
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('revision_count') is not None:
            self.revision_count = m.get('revision_count')
        if m.get('revision_merge_enabled') is not None:
            self.revision_merge_enabled = m.get('revision_merge_enabled')
        if m.get('revision_recycle_period') is not None:
            self.revision_recycle_period = m.get('revision_recycle_period')
        return self


class FaceGroupGroupCoverFaceBoundary(TeaModel):
    def __init__(
        self,
        height: int = None,
        left: int = None,
        top: int = None,
        width: int = None,
    ):
        self.height = height
        self.left = left
        self.top = top
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.height is not None:
            result['Height'] = self.height
        if self.left is not None:
            result['Left'] = self.left
        if self.top is not None:
            result['Top'] = self.top
        if self.width is not None:
            result['Width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Height') is not None:
            self.height = m.get('Height')
        if m.get('Left') is not None:
            self.left = m.get('Left')
        if m.get('Top') is not None:
            self.top = m.get('Top')
        if m.get('Width') is not None:
            self.width = m.get('Width')
        return self


class FaceGroup(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        group_cover_face_boundary: FaceGroupGroupCoverFaceBoundary = None,
        group_cover_file_id: str = None,
        group_cover_height: int = None,
        group_cover_url: str = None,
        group_cover_width: int = None,
        group_id: str = None,
        group_name: str = None,
        image_count: int = None,
        remarks: str = None,
        updated_at: str = None,
    ):
        self.created_at = created_at
        self.group_cover_face_boundary = group_cover_face_boundary
        self.group_cover_file_id = group_cover_file_id
        self.group_cover_height = group_cover_height
        self.group_cover_url = group_cover_url
        self.group_cover_width = group_cover_width
        self.group_id = group_id
        self.group_name = group_name
        self.image_count = image_count
        self.remarks = remarks
        self.updated_at = updated_at

    def validate(self):
        if self.group_cover_face_boundary:
            self.group_cover_face_boundary.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.group_cover_face_boundary is not None:
            result['group_cover_face_boundary'] = self.group_cover_face_boundary.to_map()
        if self.group_cover_file_id is not None:
            result['group_cover_file_id'] = self.group_cover_file_id
        if self.group_cover_height is not None:
            result['group_cover_height'] = self.group_cover_height
        if self.group_cover_url is not None:
            result['group_cover_url'] = self.group_cover_url
        if self.group_cover_width is not None:
            result['group_cover_width'] = self.group_cover_width
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.image_count is not None:
            result['image_count'] = self.image_count
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('group_cover_face_boundary') is not None:
            temp_model = FaceGroupGroupCoverFaceBoundary()
            self.group_cover_face_boundary = temp_model.from_map(m['group_cover_face_boundary'])
        if m.get('group_cover_file_id') is not None:
            self.group_cover_file_id = m.get('group_cover_file_id')
        if m.get('group_cover_height') is not None:
            self.group_cover_height = m.get('group_cover_height')
        if m.get('group_cover_url') is not None:
            self.group_cover_url = m.get('group_cover_url')
        if m.get('group_cover_width') is not None:
            self.group_cover_width = m.get('group_cover_width')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('image_count') is not None:
            self.image_count = m.get('image_count')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class FileDownloadCallbackInfo(TeaModel):
    def __init__(
        self,
        bucket: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
        object: str = None,
        user_id: str = None,
    ):
        # This parameter is required.
        self.bucket = bucket
        # This parameter is required.
        self.domain_id = domain_id
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.file_id = file_id
        # This parameter is required.
        self.object = object
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket is not None:
            result['bucket'] = self.bucket
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.object is not None:
            result['object'] = self.object
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket') is not None:
            self.bucket = m.get('bucket')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('object') is not None:
            self.object = m.get('object')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class UploadPartInfoParallelSha1Ctx(TeaModel):
    def __init__(
        self,
        h: List[int] = None,
        part_offset: int = None,
    ):
        self.h = h
        self.part_offset = part_offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['h'] = self.h
        if self.part_offset is not None:
            result['part_offset'] = self.part_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('h') is not None:
            self.h = m.get('h')
        if m.get('part_offset') is not None:
            self.part_offset = m.get('part_offset')
        return self


class UploadPartInfoParallelSha256Ctx(TeaModel):
    def __init__(
        self,
        h: List[int] = None,
        part_offset: int = None,
    ):
        self.h = h
        self.part_offset = part_offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['h'] = self.h
        if self.part_offset is not None:
            result['part_offset'] = self.part_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('h') is not None:
            self.h = m.get('h')
        if m.get('part_offset') is not None:
            self.part_offset = m.get('part_offset')
        return self


class UploadPartInfo(TeaModel):
    def __init__(
        self,
        etag: str = None,
        internal_upload_url: str = None,
        parallel_sha_1ctx: UploadPartInfoParallelSha1Ctx = None,
        parallel_sha_256ctx: UploadPartInfoParallelSha256Ctx = None,
        part_number: int = None,
        part_size: int = None,
        upload_url: str = None,
    ):
        self.etag = etag
        self.internal_upload_url = internal_upload_url
        self.parallel_sha_1ctx = parallel_sha_1ctx
        self.parallel_sha_256ctx = parallel_sha_256ctx
        # This parameter is required.
        self.part_number = part_number
        self.part_size = part_size
        # This parameter is required.
        self.upload_url = upload_url

    def validate(self):
        if self.parallel_sha_1ctx:
            self.parallel_sha_1ctx.validate()
        if self.parallel_sha_256ctx:
            self.parallel_sha_256ctx.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.etag is not None:
            result['etag'] = self.etag
        if self.internal_upload_url is not None:
            result['internal_upload_url'] = self.internal_upload_url
        if self.parallel_sha_1ctx is not None:
            result['parallel_sha1_ctx'] = self.parallel_sha_1ctx.to_map()
        if self.parallel_sha_256ctx is not None:
            result['parallel_sha256_ctx'] = self.parallel_sha_256ctx.to_map()
        if self.part_number is not None:
            result['part_number'] = self.part_number
        if self.part_size is not None:
            result['part_size'] = self.part_size
        if self.upload_url is not None:
            result['upload_url'] = self.upload_url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('etag') is not None:
            self.etag = m.get('etag')
        if m.get('internal_upload_url') is not None:
            self.internal_upload_url = m.get('internal_upload_url')
        if m.get('parallel_sha1_ctx') is not None:
            temp_model = UploadPartInfoParallelSha1Ctx()
            self.parallel_sha_1ctx = temp_model.from_map(m['parallel_sha1_ctx'])
        if m.get('parallel_sha256_ctx') is not None:
            temp_model = UploadPartInfoParallelSha256Ctx()
            self.parallel_sha_256ctx = temp_model.from_map(m['parallel_sha256_ctx'])
        if m.get('part_number') is not None:
            self.part_number = m.get('part_number')
        if m.get('part_size') is not None:
            self.part_size = m.get('part_size')
        if m.get('upload_url') is not None:
            self.upload_url = m.get('upload_url')
        return self


class FileStreamInfo(TeaModel):
    def __init__(
        self,
        content_hash: str = None,
        content_hash_name: str = None,
        content_md_5: str = None,
        part_info_list: UploadPartInfo = None,
        pre_hash: str = None,
        proof_code: str = None,
        proof_version: str = None,
        size: int = None,
    ):
        self.content_hash = content_hash
        self.content_hash_name = content_hash_name
        self.content_md_5 = content_md_5
        self.part_info_list = part_info_list
        self.pre_hash = pre_hash
        self.proof_code = proof_code
        self.proof_version = proof_version
        self.size = size

    def validate(self):
        if self.part_info_list:
            self.part_info_list.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.part_info_list is not None:
            result['part_info_list'] = self.part_info_list.to_map()
        if self.pre_hash is not None:
            result['pre_hash'] = self.pre_hash
        if self.proof_code is not None:
            result['proof_code'] = self.proof_code
        if self.proof_version is not None:
            result['proof_version'] = self.proof_version
        if self.size is not None:
            result['size'] = self.size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('part_info_list') is not None:
            temp_model = UploadPartInfo()
            self.part_info_list = temp_model.from_map(m['part_info_list'])
        if m.get('pre_hash') is not None:
            self.pre_hash = m.get('pre_hash')
        if m.get('proof_code') is not None:
            self.proof_code = m.get('proof_code')
        if m.get('proof_version') is not None:
            self.proof_version = m.get('proof_version')
        if m.get('size') is not None:
            self.size = m.get('size')
        return self


class GetOfficeEditUrlOption(TeaModel):
    def __init__(
        self,
        copy: bool = None,
        print: bool = None,
        readonly: bool = None,
    ):
        self.copy = copy
        self.print = print
        self.readonly = readonly

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copy is not None:
            result['copy'] = self.copy
        if self.print is not None:
            result['print'] = self.print
        if self.readonly is not None:
            result['readonly'] = self.readonly
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('copy') is not None:
            self.copy = m.get('copy')
        if m.get('print') is not None:
            self.print = m.get('print')
        if m.get('readonly') is not None:
            self.readonly = m.get('readonly')
        return self


class GetOfficeEditUrlWatermark(TeaModel):
    def __init__(
        self,
        fillstyle: str = None,
        font: str = None,
        horizontal: int = None,
        rotate: float = None,
        type: int = None,
        value: str = None,
        vertical: int = None,
    ):
        self.fillstyle = fillstyle
        self.font = font
        self.horizontal = horizontal
        self.rotate = rotate
        self.type = type
        self.value = value
        self.vertical = vertical

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.fillstyle is not None:
            result['fillstyle'] = self.fillstyle
        if self.font is not None:
            result['font'] = self.font
        if self.horizontal is not None:
            result['horizontal'] = self.horizontal
        if self.rotate is not None:
            result['rotate'] = self.rotate
        if self.type is not None:
            result['type'] = self.type
        if self.value is not None:
            result['value'] = self.value
        if self.vertical is not None:
            result['vertical'] = self.vertical
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('fillstyle') is not None:
            self.fillstyle = m.get('fillstyle')
        if m.get('font') is not None:
            self.font = m.get('font')
        if m.get('horizontal') is not None:
            self.horizontal = m.get('horizontal')
        if m.get('rotate') is not None:
            self.rotate = m.get('rotate')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('value') is not None:
            self.value = m.get('value')
        if m.get('vertical') is not None:
            self.vertical = m.get('vertical')
        return self


class GetOfficePreviewUrlOption(TeaModel):
    def __init__(
        self,
        copy: bool = None,
        print: bool = None,
    ):
        self.copy = copy
        self.print = print

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.copy is not None:
            result['copy'] = self.copy
        if self.print is not None:
            result['print'] = self.print
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('copy') is not None:
            self.copy = m.get('copy')
        if m.get('print') is not None:
            self.print = m.get('print')
        return self


class Group(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        group_name: str = None,
        updated_at: int = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.description = description
        self.domain_id = domain_id
        self.group_id = group_id
        self.group_name = group_name
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class HotDriveFile(TeaModel):
    def __init__(
        self,
        action_count: int = None,
        action_list: List[str] = None,
        category: str = None,
        count_at: int = None,
        drive_id: str = None,
        file_id: str = None,
        name: str = None,
        revision_id: str = None,
    ):
        self.action_count = action_count
        self.action_list = action_list
        self.category = category
        self.count_at = count_at
        self.drive_id = drive_id
        self.file_id = file_id
        self.name = name
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_count is not None:
            result['action_count'] = self.action_count
        if self.action_list is not None:
            result['action_list'] = self.action_list
        if self.category is not None:
            result['category'] = self.category
        if self.count_at is not None:
            result['count_at'] = self.count_at
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.name is not None:
            result['name'] = self.name
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_count') is not None:
            self.action_count = m.get('action_count')
        if m.get('action_list') is not None:
            self.action_list = m.get('action_list')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('count_at') is not None:
            self.count_at = m.get('count_at')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class HotKnowledgeBaseFile(TeaModel):
    def __init__(
        self,
        action_count: int = None,
        action_list: List[str] = None,
        category: str = None,
        count_at: int = None,
        drive_id: str = None,
        file_id: str = None,
        knowledge_base_id: str = None,
        name: str = None,
        revision_id: str = None,
    ):
        self.action_count = action_count
        self.action_list = action_list
        self.category = category
        self.count_at = count_at
        self.drive_id = drive_id
        self.file_id = file_id
        self.knowledge_base_id = knowledge_base_id
        self.name = name
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.action_count is not None:
            result['action_count'] = self.action_count
        if self.action_list is not None:
            result['action_list'] = self.action_list
        if self.category is not None:
            result['category'] = self.category
        if self.count_at is not None:
            result['count_at'] = self.count_at
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.knowledge_base_id is not None:
            result['knowledge_base_id'] = self.knowledge_base_id
        if self.name is not None:
            result['name'] = self.name
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('action_count') is not None:
            self.action_count = m.get('action_count')
        if m.get('action_list') is not None:
            self.action_list = m.get('action_list')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('count_at') is not None:
            self.count_at = m.get('count_at')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('knowledge_base_id') is not None:
            self.knowledge_base_id = m.get('knowledge_base_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class IdentityToBenefitPkgMapping(TeaModel):
    def __init__(
        self,
        benefit_pkg_computation_rule: str = None,
        benefit_pkg_id: str = None,
        benefit_pkg_name: str = None,
        benefit_pkg_owner_id: str = None,
        benefit_pkg_priority: int = None,
        benefit_pkg_type: str = None,
        created_at: str = None,
        delivery_info_list: List[BenefitPkgDeliveryInfo] = None,
        identity_id: str = None,
        identity_type: str = None,
        updated_at: str = None,
    ):
        self.benefit_pkg_computation_rule = benefit_pkg_computation_rule
        self.benefit_pkg_id = benefit_pkg_id
        self.benefit_pkg_name = benefit_pkg_name
        self.benefit_pkg_owner_id = benefit_pkg_owner_id
        self.benefit_pkg_priority = benefit_pkg_priority
        self.benefit_pkg_type = benefit_pkg_type
        self.created_at = created_at
        self.delivery_info_list = delivery_info_list
        self.identity_id = identity_id
        self.identity_type = identity_type
        self.updated_at = updated_at

    def validate(self):
        if self.delivery_info_list:
            for k in self.delivery_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.benefit_pkg_computation_rule is not None:
            result['benefit_pkg_computation_rule'] = self.benefit_pkg_computation_rule
        if self.benefit_pkg_id is not None:
            result['benefit_pkg_id'] = self.benefit_pkg_id
        if self.benefit_pkg_name is not None:
            result['benefit_pkg_name'] = self.benefit_pkg_name
        if self.benefit_pkg_owner_id is not None:
            result['benefit_pkg_owner_id'] = self.benefit_pkg_owner_id
        if self.benefit_pkg_priority is not None:
            result['benefit_pkg_priority'] = self.benefit_pkg_priority
        if self.benefit_pkg_type is not None:
            result['benefit_pkg_type'] = self.benefit_pkg_type
        if self.created_at is not None:
            result['created_at'] = self.created_at
        result['delivery_info_list'] = []
        if self.delivery_info_list is not None:
            for k in self.delivery_info_list:
                result['delivery_info_list'].append(k.to_map() if k else None)
        if self.identity_id is not None:
            result['identity_id'] = self.identity_id
        if self.identity_type is not None:
            result['identity_type'] = self.identity_type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('benefit_pkg_computation_rule') is not None:
            self.benefit_pkg_computation_rule = m.get('benefit_pkg_computation_rule')
        if m.get('benefit_pkg_id') is not None:
            self.benefit_pkg_id = m.get('benefit_pkg_id')
        if m.get('benefit_pkg_name') is not None:
            self.benefit_pkg_name = m.get('benefit_pkg_name')
        if m.get('benefit_pkg_owner_id') is not None:
            self.benefit_pkg_owner_id = m.get('benefit_pkg_owner_id')
        if m.get('benefit_pkg_priority') is not None:
            self.benefit_pkg_priority = m.get('benefit_pkg_priority')
        if m.get('benefit_pkg_type') is not None:
            self.benefit_pkg_type = m.get('benefit_pkg_type')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        self.delivery_info_list = []
        if m.get('delivery_info_list') is not None:
            for k in m.get('delivery_info_list'):
                temp_model = BenefitPkgDeliveryInfo()
                self.delivery_info_list.append(temp_model.from_map(k))
        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')
        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class ImageProcess(TeaModel):
    def __init__(
        self,
        image_thumbnail_process: str = None,
        office_thumbnail_process: str = None,
        video_thumbnail_process: str = None,
    ):
        self.image_thumbnail_process = image_thumbnail_process
        self.office_thumbnail_process = office_thumbnail_process
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.office_thumbnail_process is not None:
            result['office_thumbnail_process'] = self.office_thumbnail_process
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('office_thumbnail_process') is not None:
            self.office_thumbnail_process = m.get('office_thumbnail_process')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class ImageTag(TeaModel):
    def __init__(
        self,
        count: int = None,
        cover_file_category: str = None,
        cover_file_id: str = None,
        cover_overall_score: float = None,
        cover_tag_confidence: float = None,
        cover_url: str = None,
        name: str = None,
    ):
        self.count = count
        self.cover_file_category = cover_file_category
        self.cover_file_id = cover_file_id
        self.cover_overall_score = cover_overall_score
        self.cover_tag_confidence = cover_tag_confidence
        self.cover_url = cover_url
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.count is not None:
            result['count'] = self.count
        if self.cover_file_category is not None:
            result['cover_file_category'] = self.cover_file_category
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id
        if self.cover_overall_score is not None:
            result['cover_overall_score'] = self.cover_overall_score
        if self.cover_tag_confidence is not None:
            result['cover_tag_confidence'] = self.cover_tag_confidence
        if self.cover_url is not None:
            result['cover_url'] = self.cover_url
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('count') is not None:
            self.count = m.get('count')
        if m.get('cover_file_category') is not None:
            self.cover_file_category = m.get('cover_file_category')
        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')
        if m.get('cover_overall_score') is not None:
            self.cover_overall_score = m.get('cover_overall_score')
        if m.get('cover_tag_confidence') is not None:
            self.cover_tag_confidence = m.get('cover_tag_confidence')
        if m.get('cover_url') is not None:
            self.cover_url = m.get('cover_url')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class Int64Range(TeaModel):
    def __init__(
        self,
        from_: int = None,
        to: int = None,
    ):
        self.from_ = from_
        self.to = to

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.from_ is not None:
            result['from'] = self.from_
        if self.to is not None:
            result['to'] = self.to
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('from') is not None:
            self.from_ = m.get('from')
        if m.get('to') is not None:
            self.to = m.get('to')
        return self


class JWTPayload(TeaModel):
    def __init__(
        self,
        aud: str = None,
        auto_create: bool = None,
        exp: int = None,
        iat: int = None,
        iss: str = None,
        jti: str = None,
        nbf: int = None,
        sub: str = None,
        sub_type: str = None,
    ):
        self.aud = aud
        self.auto_create = auto_create
        self.exp = exp
        self.iat = iat
        self.iss = iss
        self.jti = jti
        self.nbf = nbf
        self.sub = sub
        self.sub_type = sub_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aud is not None:
            result['aud'] = self.aud
        if self.auto_create is not None:
            result['auto_create'] = self.auto_create
        if self.exp is not None:
            result['exp'] = self.exp
        if self.iat is not None:
            result['iat'] = self.iat
        if self.iss is not None:
            result['iss'] = self.iss
        if self.jti is not None:
            result['jti'] = self.jti
        if self.nbf is not None:
            result['nbf'] = self.nbf
        if self.sub is not None:
            result['sub'] = self.sub
        if self.sub_type is not None:
            result['sub_type'] = self.sub_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aud') is not None:
            self.aud = m.get('aud')
        if m.get('auto_create') is not None:
            self.auto_create = m.get('auto_create')
        if m.get('exp') is not None:
            self.exp = m.get('exp')
        if m.get('iat') is not None:
            self.iat = m.get('iat')
        if m.get('iss') is not None:
            self.iss = m.get('iss')
        if m.get('jti') is not None:
            self.jti = m.get('jti')
        if m.get('nbf') is not None:
            self.nbf = m.get('nbf')
        if m.get('sub') is not None:
            self.sub = m.get('sub')
        if m.get('sub_type') is not None:
            self.sub_type = m.get('sub_type')
        return self


class LinkRule(TeaModel):
    def __init__(
        self,
        link_type: str = None,
        src_drive_id: str = None,
        src_drive_name: str = None,
        src_file_id: str = None,
        src_file_name: str = None,
        src_valid: bool = None,
    ):
        self.link_type = link_type
        self.src_drive_id = src_drive_id
        self.src_drive_name = src_drive_name
        self.src_file_id = src_file_id
        self.src_file_name = src_file_name
        self.src_valid = src_valid

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.link_type is not None:
            result['link_type'] = self.link_type
        if self.src_drive_id is not None:
            result['src_drive_id'] = self.src_drive_id
        if self.src_drive_name is not None:
            result['src_drive_name'] = self.src_drive_name
        if self.src_file_id is not None:
            result['src_file_id'] = self.src_file_id
        if self.src_file_name is not None:
            result['src_file_name'] = self.src_file_name
        if self.src_valid is not None:
            result['src_valid'] = self.src_valid
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('link_type') is not None:
            self.link_type = m.get('link_type')
        if m.get('src_drive_id') is not None:
            self.src_drive_id = m.get('src_drive_id')
        if m.get('src_drive_name') is not None:
            self.src_drive_name = m.get('src_drive_name')
        if m.get('src_file_id') is not None:
            self.src_file_id = m.get('src_file_id')
        if m.get('src_file_name') is not None:
            self.src_file_name = m.get('src_file_name')
        if m.get('src_valid') is not None:
            self.src_valid = m.get('src_valid')
        return self


class KnowledgeBase(TeaModel):
    def __init__(
        self,
        cover_uri: str = None,
        created_at: int = None,
        description: str = None,
        file_filter: str = None,
        knowledge_base_id: str = None,
        link_rule_list: List[LinkRule] = None,
        name: str = None,
        owner_id: str = None,
        owner_name: str = None,
        owner_type: str = None,
        updated_at: int = None,
    ):
        self.cover_uri = cover_uri
        self.created_at = created_at
        self.description = description
        self.file_filter = file_filter
        self.knowledge_base_id = knowledge_base_id
        self.link_rule_list = link_rule_list
        self.name = name
        self.owner_id = owner_id
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.updated_at = updated_at

    def validate(self):
        if self.link_rule_list:
            for k in self.link_rule_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_uri is not None:
            result['cover_uri'] = self.cover_uri
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.file_filter is not None:
            result['file_filter'] = self.file_filter
        if self.knowledge_base_id is not None:
            result['knowledge_base_id'] = self.knowledge_base_id
        result['link_rule_list'] = []
        if self.link_rule_list is not None:
            for k in self.link_rule_list:
                result['link_rule_list'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.owner_id is not None:
            result['owner_id'] = self.owner_id
        if self.owner_name is not None:
            result['owner_name'] = self.owner_name
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover_uri') is not None:
            self.cover_uri = m.get('cover_uri')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('file_filter') is not None:
            self.file_filter = m.get('file_filter')
        if m.get('knowledge_base_id') is not None:
            self.knowledge_base_id = m.get('knowledge_base_id')
        self.link_rule_list = []
        if m.get('link_rule_list') is not None:
            for k in m.get('link_rule_list'):
                temp_model = LinkRule()
                self.link_rule_list.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner_id') is not None:
            self.owner_id = m.get('owner_id')
        if m.get('owner_name') is not None:
            self.owner_name = m.get('owner_name')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class KnowledgeCategory(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        description: str = None,
        keywords: List[str] = None,
        knowledge_base_id: str = None,
        knowledge_base_name: str = None,
        knowledge_category_id: str = None,
        name: str = None,
        owner: str = None,
        owner_type: str = None,
        parent_knowledge_category_id: str = None,
        status: str = None,
        updated_at: int = None,
    ):
        self.created_at = created_at
        self.description = description
        self.keywords = keywords
        self.knowledge_base_id = knowledge_base_id
        self.knowledge_base_name = knowledge_base_name
        self.knowledge_category_id = knowledge_category_id
        self.name = name
        self.owner = owner
        self.owner_type = owner_type
        self.parent_knowledge_category_id = parent_knowledge_category_id
        self.status = status
        self.updated_at = updated_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.keywords is not None:
            result['keywords'] = self.keywords
        if self.knowledge_base_id is not None:
            result['knowledge_base_id'] = self.knowledge_base_id
        if self.knowledge_base_name is not None:
            result['knowledge_base_name'] = self.knowledge_base_name
        if self.knowledge_category_id is not None:
            result['knowledge_category_id'] = self.knowledge_category_id
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.parent_knowledge_category_id is not None:
            result['parent_knowledge_category_id'] = self.parent_knowledge_category_id
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('keywords') is not None:
            self.keywords = m.get('keywords')
        if m.get('knowledge_base_id') is not None:
            self.knowledge_base_id = m.get('knowledge_base_id')
        if m.get('knowledge_base_name') is not None:
            self.knowledge_base_name = m.get('knowledge_base_name')
        if m.get('knowledge_category_id') is not None:
            self.knowledge_category_id = m.get('knowledge_category_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('parent_knowledge_category_id') is not None:
            self.parent_knowledge_category_id = m.get('parent_knowledge_category_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class KnowledgeFile(TeaModel):
    def __init__(
        self,
        creator_id: str = None,
        drive_id: str = None,
        drive_name: str = None,
        file_category: str = None,
        file_created_at: int = None,
        file_creator_id: str = None,
        file_id: str = None,
        file_image_time: int = None,
        file_last_modifier_id: str = None,
        file_last_modifier_type: str = None,
        file_name: str = None,
        file_name_path: str = None,
        file_size: int = None,
        file_updated_at: int = None,
        joined_at: int = None,
        knowledge_base_id: str = None,
        knowledge_category_id: str = None,
        revision_id: str = None,
    ):
        self.creator_id = creator_id
        self.drive_id = drive_id
        self.drive_name = drive_name
        self.file_category = file_category
        self.file_created_at = file_created_at
        self.file_creator_id = file_creator_id
        self.file_id = file_id
        self.file_image_time = file_image_time
        self.file_last_modifier_id = file_last_modifier_id
        self.file_last_modifier_type = file_last_modifier_type
        self.file_name = file_name
        self.file_name_path = file_name_path
        self.file_size = file_size
        self.file_updated_at = file_updated_at
        self.joined_at = joined_at
        self.knowledge_base_id = knowledge_base_id
        self.knowledge_category_id = knowledge_category_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator_id is not None:
            result['creator_id'] = self.creator_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.file_category is not None:
            result['file_category'] = self.file_category
        if self.file_created_at is not None:
            result['file_created_at'] = self.file_created_at
        if self.file_creator_id is not None:
            result['file_creator_id'] = self.file_creator_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_image_time is not None:
            result['file_image_time'] = self.file_image_time
        if self.file_last_modifier_id is not None:
            result['file_last_modifier_id'] = self.file_last_modifier_id
        if self.file_last_modifier_type is not None:
            result['file_last_modifier_type'] = self.file_last_modifier_type
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.file_name_path is not None:
            result['file_name_path'] = self.file_name_path
        if self.file_size is not None:
            result['file_size'] = self.file_size
        if self.file_updated_at is not None:
            result['file_updated_at'] = self.file_updated_at
        if self.joined_at is not None:
            result['joined_at'] = self.joined_at
        if self.knowledge_base_id is not None:
            result['knowledge_base_id'] = self.knowledge_base_id
        if self.knowledge_category_id is not None:
            result['knowledge_category_id'] = self.knowledge_category_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator_id') is not None:
            self.creator_id = m.get('creator_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('file_category') is not None:
            self.file_category = m.get('file_category')
        if m.get('file_created_at') is not None:
            self.file_created_at = m.get('file_created_at')
        if m.get('file_creator_id') is not None:
            self.file_creator_id = m.get('file_creator_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_image_time') is not None:
            self.file_image_time = m.get('file_image_time')
        if m.get('file_last_modifier_id') is not None:
            self.file_last_modifier_id = m.get('file_last_modifier_id')
        if m.get('file_last_modifier_type') is not None:
            self.file_last_modifier_type = m.get('file_last_modifier_type')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('file_name_path') is not None:
            self.file_name_path = m.get('file_name_path')
        if m.get('file_size') is not None:
            self.file_size = m.get('file_size')
        if m.get('file_updated_at') is not None:
            self.file_updated_at = m.get('file_updated_at')
        if m.get('joined_at') is not None:
            self.joined_at = m.get('joined_at')
        if m.get('knowledge_base_id') is not None:
            self.knowledge_base_id = m.get('knowledge_base_id')
        if m.get('knowledge_category_id') is not None:
            self.knowledge_category_id = m.get('knowledge_category_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class KnowledgeFileItem(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class LocationDateCluster(TeaModel):
    def __init__(
        self,
        address: Address = None,
        cluster_id: str = None,
        created_at: str = None,
        custom_labels: Dict[str, str] = None,
        drive_id: str = None,
        end_time: str = None,
        level: str = None,
        start_time: str = None,
        title: str = None,
        updated_at: str = None,
    ):
        self.address = address
        self.cluster_id = cluster_id
        self.created_at = created_at
        self.custom_labels = custom_labels
        self.drive_id = drive_id
        self.end_time = end_time
        self.level = level
        self.start_time = start_time
        self.title = title
        self.updated_at = updated_at

    def validate(self):
        if self.address:
            self.address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address.to_map()
        if self.cluster_id is not None:
            result['cluster_id'] = self.cluster_id
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.end_time is not None:
            result['end_time'] = self.end_time
        if self.level is not None:
            result['level'] = self.level
        if self.start_time is not None:
            result['start_time'] = self.start_time
        if self.title is not None:
            result['title'] = self.title
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            temp_model = Address()
            self.address = temp_model.from_map(m['address'])
        if m.get('cluster_id') is not None:
            self.cluster_id = m.get('cluster_id')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('end_time') is not None:
            self.end_time = m.get('end_time')
        if m.get('level') is not None:
            self.level = m.get('level')
        if m.get('start_time') is not None:
            self.start_time = m.get('start_time')
        if m.get('title') is not None:
            self.title = m.get('title')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class Membership(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        group_id: str = None,
        member_role: str = None,
        member_type: str = None,
        sub_group_id: str = None,
        updated_at: int = None,
        user_id: str = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.description = description
        self.domain_id = domain_id
        self.group_id = group_id
        self.member_role = member_role
        self.member_type = member_type
        self.sub_group_id = sub_group_id
        self.updated_at = updated_at
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_role is not None:
            result['member_role'] = self.member_role
        if self.member_type is not None:
            result['member_type'] = self.member_type
        if self.sub_group_id is not None:
            result['sub_group_id'] = self.sub_group_id
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_role') is not None:
            self.member_role = m.get('member_role')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        if m.get('sub_group_id') is not None:
            self.sub_group_id = m.get('sub_group_id')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class NameCheckResult(TeaModel):
    def __init__(
        self,
        exist_file_id: str = None,
        exist_file_type: str = None,
    ):
        self.exist_file_id = exist_file_id
        self.exist_file_type = exist_file_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.exist_file_id is not None:
            result['exist_file_id'] = self.exist_file_id
        if self.exist_file_type is not None:
            result['exist_file_type'] = self.exist_file_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exist_file_id') is not None:
            self.exist_file_id = m.get('exist_file_id')
        if m.get('exist_file_type') is not None:
            self.exist_file_type = m.get('exist_file_type')
        return self


class OfficeEditConfig(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class OfficePreviewConfig(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
    ):
        self.enabled = enabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        return self


class PersonalRightsInfoResponse(TeaModel):
    def __init__(
        self,
        expires_time: str = None,
        history_latest_rights: 'PersonalRightsInfoResponse' = None,
        icon: str = None,
        is_expires: bool = None,
        name: str = None,
        other_rights: 'PersonalRightsInfoResponse' = None,
        privileges: List[DataBoxPrivileges] = None,
        spu_id: str = None,
        title: str = None,
    ):
        self.expires_time = expires_time
        self.history_latest_rights = history_latest_rights
        self.icon = icon
        self.is_expires = is_expires
        self.name = name
        self.other_rights = other_rights
        self.privileges = privileges
        self.spu_id = spu_id
        self.title = title

    def validate(self):
        if self.history_latest_rights:
            self.history_latest_rights.validate()
        if self.other_rights:
            self.other_rights.validate()
        if self.privileges:
            for k in self.privileges:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expires_time is not None:
            result['expires_time'] = self.expires_time
        if self.history_latest_rights is not None:
            result['history_latest_rights'] = self.history_latest_rights.to_map()
        if self.icon is not None:
            result['icon'] = self.icon
        if self.is_expires is not None:
            result['is_expires'] = self.is_expires
        if self.name is not None:
            result['name'] = self.name
        if self.other_rights is not None:
            result['other_rights'] = self.other_rights.to_map()
        result['privileges'] = []
        if self.privileges is not None:
            for k in self.privileges:
                result['privileges'].append(k.to_map() if k else None)
        if self.spu_id is not None:
            result['spu_id'] = self.spu_id
        if self.title is not None:
            result['title'] = self.title
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expires_time') is not None:
            self.expires_time = m.get('expires_time')
        if m.get('history_latest_rights') is not None:
            temp_model = PersonalRightsInfoResponse()
            self.history_latest_rights = temp_model.from_map(m['history_latest_rights'])
        if m.get('icon') is not None:
            self.icon = m.get('icon')
        if m.get('is_expires') is not None:
            self.is_expires = m.get('is_expires')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('other_rights') is not None:
            temp_model = PersonalRightsInfoResponse()
            self.other_rights = temp_model.from_map(m['other_rights'])
        self.privileges = []
        if m.get('privileges') is not None:
            for k in m.get('privileges'):
                temp_model = DataBoxPrivileges()
                self.privileges.append(temp_model.from_map(k))
        if m.get('spu_id') is not None:
            self.spu_id = m.get('spu_id')
        if m.get('title') is not None:
            self.title = m.get('title')
        return self


class PersonalSpaceInfo(TeaModel):
    def __init__(
        self,
        total_size: int = None,
        used_size: int = None,
    ):
        self.total_size = total_size
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.used_size is not None:
            result['used_size'] = self.used_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')
        return self


class RecycleBinConfig(TeaModel):
    def __init__(
        self,
        auto_delete_enabled: bool = None,
        auto_delete_keep_second: int = None,
        delete_trash_normal_file_disabled: bool = None,
    ):
        self.auto_delete_enabled = auto_delete_enabled
        self.auto_delete_keep_second = auto_delete_keep_second
        self.delete_trash_normal_file_disabled = delete_trash_normal_file_disabled

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_delete_enabled is not None:
            result['auto_delete_enabled'] = self.auto_delete_enabled
        if self.auto_delete_keep_second is not None:
            result['auto_delete_keep_second'] = self.auto_delete_keep_second
        if self.delete_trash_normal_file_disabled is not None:
            result['delete_trash_normal_file_disabled'] = self.delete_trash_normal_file_disabled
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_delete_enabled') is not None:
            self.auto_delete_enabled = m.get('auto_delete_enabled')
        if m.get('auto_delete_keep_second') is not None:
            self.auto_delete_keep_second = m.get('auto_delete_keep_second')
        if m.get('delete_trash_normal_file_disabled') is not None:
            self.delete_trash_normal_file_disabled = m.get('delete_trash_normal_file_disabled')
        return self


class RefundNoticeParam(TeaModel):
    def __init__(
        self,
        aliuid: int = None,
        aliyun_produce_code: str = None,
        commodity_code: str = None,
        instance_id: str = None,
        new_expire_time: Any = None,
        order_ids: List[int] = None,
        refund_param_map: Dict[str, str] = None,
        refund_type: str = None,
    ):
        self.aliuid = aliuid
        self.aliyun_produce_code = aliyun_produce_code
        self.commodity_code = commodity_code
        self.instance_id = instance_id
        self.new_expire_time = new_expire_time
        self.order_ids = order_ids
        self.refund_param_map = refund_param_map
        self.refund_type = refund_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.aliuid is not None:
            result['aliuid'] = self.aliuid
        if self.aliyun_produce_code is not None:
            result['aliyunProduceCode'] = self.aliyun_produce_code
        if self.commodity_code is not None:
            result['commodityCode'] = self.commodity_code
        if self.instance_id is not None:
            result['instanceId'] = self.instance_id
        if self.new_expire_time is not None:
            result['newExpireTime'] = self.new_expire_time
        if self.order_ids is not None:
            result['orderIds'] = self.order_ids
        if self.refund_param_map is not None:
            result['refundParamMap'] = self.refund_param_map
        if self.refund_type is not None:
            result['refundType'] = self.refund_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('aliuid') is not None:
            self.aliuid = m.get('aliuid')
        if m.get('aliyunProduceCode') is not None:
            self.aliyun_produce_code = m.get('aliyunProduceCode')
        if m.get('commodityCode') is not None:
            self.commodity_code = m.get('commodityCode')
        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')
        if m.get('newExpireTime') is not None:
            self.new_expire_time = m.get('newExpireTime')
        if m.get('orderIds') is not None:
            self.order_ids = m.get('orderIds')
        if m.get('refundParamMap') is not None:
            self.refund_param_map = m.get('refundParamMap')
        if m.get('refundType') is not None:
            self.refund_type = m.get('refundType')
        return self


class Revision(TeaModel):
    def __init__(
        self,
        content_hash: str = None,
        content_hash_name: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        creator_id: str = None,
        creator_name: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        file_extension: str = None,
        file_id: str = None,
        is_latest_version: bool = None,
        keep_forever: bool = None,
        revision_description: str = None,
        revision_id: str = None,
        revision_name: str = None,
        revision_version: int = None,
        size: int = None,
        thumbnail: str = None,
        updated_at: str = None,
        url: str = None,
    ):
        self.content_hash = content_hash
        self.content_hash_name = content_hash_name
        self.crc_64hash = crc_64hash
        self.created_at = created_at
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.domain_id = domain_id
        self.download_url = download_url
        self.drive_id = drive_id
        self.file_extension = file_extension
        self.file_id = file_id
        self.is_latest_version = is_latest_version
        self.keep_forever = keep_forever
        self.revision_description = revision_description
        self.revision_id = revision_id
        self.revision_name = revision_name
        self.revision_version = revision_version
        self.size = size
        self.thumbnail = thumbnail
        self.updated_at = updated_at
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator_id is not None:
            result['creator_id'] = self.creator_id
        if self.creator_name is not None:
            result['creator_name'] = self.creator_name
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.is_latest_version is not None:
            result['is_latest_version'] = self.is_latest_version
        if self.keep_forever is not None:
            result['keep_forever'] = self.keep_forever
        if self.revision_description is not None:
            result['revision_description'] = self.revision_description
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        if self.revision_name is not None:
            result['revision_name'] = self.revision_name
        if self.revision_version is not None:
            result['revision_version'] = self.revision_version
        if self.size is not None:
            result['size'] = self.size
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator_id') is not None:
            self.creator_id = m.get('creator_id')
        if m.get('creator_name') is not None:
            self.creator_name = m.get('creator_name')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('is_latest_version') is not None:
            self.is_latest_version = m.get('is_latest_version')
        if m.get('keep_forever') is not None:
            self.keep_forever = m.get('keep_forever')
        if m.get('revision_description') is not None:
            self.revision_description = m.get('revision_description')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        if m.get('revision_name') is not None:
            self.revision_name = m.get('revision_name')
        if m.get('revision_version') is not None:
            self.revision_version = m.get('revision_version')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class Role(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        creator: str = None,
        description: str = None,
        manage_resource_type: str = None,
        name: str = None,
        permissions: List[Permission] = None,
        role_id: str = None,
        status: str = None,
        updated_at: int = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.description = description
        self.manage_resource_type = manage_resource_type
        self.name = name
        self.permissions = permissions
        self.role_id = role_id
        self.status = status
        self.updated_at = updated_at

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.manage_resource_type is not None:
            result['manage_resource_type'] = self.manage_resource_type
        if self.name is not None:
            result['name'] = self.name
        result['permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['permissions'].append(k.to_map() if k else None)
        if self.role_id is not None:
            result['role_id'] = self.role_id
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('manage_resource_type') is not None:
            self.manage_resource_type = m.get('manage_resource_type')
        if m.get('name') is not None:
            self.name = m.get('name')
        self.permissions = []
        if m.get('permissions') is not None:
            for k in m.get('permissions'):
                temp_model = Permission()
                self.permissions.append(temp_model.from_map(k))
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class SearchFromThirdPartyItem(TeaModel):
    def __init__(
        self,
        authentication_type: str = None,
        extra: str = None,
        identity: str = None,
        others: Dict[str, Any] = None,
    ):
        self.authentication_type = authentication_type
        self.extra = extra
        self.identity = identity
        self.others = others

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_type is not None:
            result['authentication_type'] = self.authentication_type
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.others is not None:
            result['others'] = self.others
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authentication_type') is not None:
            self.authentication_type = m.get('authentication_type')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('others') is not None:
            self.others = m.get('others')
        return self


class ShareLink(TeaModel):
    def __init__(
        self,
        access_count: int = None,
        created_at: str = None,
        creator: str = None,
        description: str = None,
        disable_download: bool = None,
        disable_preview: bool = None,
        disable_save: bool = None,
        download_count: int = None,
        download_limit: int = None,
        drive_id: str = None,
        expiration: str = None,
        expired: bool = None,
        file_id_list: List[str] = None,
        office_editable: bool = None,
        preview_count: int = None,
        preview_limit: int = None,
        report_count: int = None,
        save_count: int = None,
        save_download_limit: int = None,
        save_limit: int = None,
        share_all_files: bool = None,
        share_id: str = None,
        share_name: str = None,
        share_pwd: str = None,
        status: str = None,
        updated_at: str = None,
        video_preview_count: int = None,
    ):
        self.access_count = access_count
        self.created_at = created_at
        self.creator = creator
        self.description = description
        self.disable_download = disable_download
        self.disable_preview = disable_preview
        self.disable_save = disable_save
        self.download_count = download_count
        self.download_limit = download_limit
        self.drive_id = drive_id
        self.expiration = expiration
        self.expired = expired
        self.file_id_list = file_id_list
        self.office_editable = office_editable
        self.preview_count = preview_count
        self.preview_limit = preview_limit
        self.report_count = report_count
        self.save_count = save_count
        self.save_download_limit = save_download_limit
        self.save_limit = save_limit
        self.share_all_files = share_all_files
        self.share_id = share_id
        self.share_name = share_name
        self.share_pwd = share_pwd
        self.status = status
        self.updated_at = updated_at
        self.video_preview_count = video_preview_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_count is not None:
            result['access_count'] = self.access_count
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.disable_download is not None:
            result['disable_download'] = self.disable_download
        if self.disable_preview is not None:
            result['disable_preview'] = self.disable_preview
        if self.disable_save is not None:
            result['disable_save'] = self.disable_save
        if self.download_count is not None:
            result['download_count'] = self.download_count
        if self.download_limit is not None:
            result['download_limit'] = self.download_limit
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.expired is not None:
            result['expired'] = self.expired
        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list
        if self.office_editable is not None:
            result['office_editable'] = self.office_editable
        if self.preview_count is not None:
            result['preview_count'] = self.preview_count
        if self.preview_limit is not None:
            result['preview_limit'] = self.preview_limit
        if self.report_count is not None:
            result['report_count'] = self.report_count
        if self.save_count is not None:
            result['save_count'] = self.save_count
        if self.save_download_limit is not None:
            result['save_download_limit'] = self.save_download_limit
        if self.save_limit is not None:
            result['save_limit'] = self.save_limit
        if self.share_all_files is not None:
            result['share_all_files'] = self.share_all_files
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.video_preview_count is not None:
            result['video_preview_count'] = self.video_preview_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_count') is not None:
            self.access_count = m.get('access_count')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('disable_download') is not None:
            self.disable_download = m.get('disable_download')
        if m.get('disable_preview') is not None:
            self.disable_preview = m.get('disable_preview')
        if m.get('disable_save') is not None:
            self.disable_save = m.get('disable_save')
        if m.get('download_count') is not None:
            self.download_count = m.get('download_count')
        if m.get('download_limit') is not None:
            self.download_limit = m.get('download_limit')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('expired') is not None:
            self.expired = m.get('expired')
        if m.get('file_id_list') is not None:
            self.file_id_list = m.get('file_id_list')
        if m.get('office_editable') is not None:
            self.office_editable = m.get('office_editable')
        if m.get('preview_count') is not None:
            self.preview_count = m.get('preview_count')
        if m.get('preview_limit') is not None:
            self.preview_limit = m.get('preview_limit')
        if m.get('report_count') is not None:
            self.report_count = m.get('report_count')
        if m.get('save_count') is not None:
            self.save_count = m.get('save_count')
        if m.get('save_download_limit') is not None:
            self.save_download_limit = m.get('save_download_limit')
        if m.get('save_limit') is not None:
            self.save_limit = m.get('save_limit')
        if m.get('share_all_files') is not None:
            self.share_all_files = m.get('share_all_files')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('video_preview_count') is not None:
            self.video_preview_count = m.get('video_preview_count')
        return self


class ShareLinkConfig(TeaModel):
    def __init__(
        self,
        enable_share_link_office_edit: bool = None,
    ):
        self.enable_share_link_office_edit = enable_share_link_office_edit

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_share_link_office_edit is not None:
            result['enable_share_link_office_edit'] = self.enable_share_link_office_edit
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable_share_link_office_edit') is not None:
            self.enable_share_link_office_edit = m.get('enable_share_link_office_edit')
        return self


class ShareLinkDetail(TeaModel):
    def __init__(
        self,
        enable_office_editable: bool = None,
    ):
        self.enable_office_editable = enable_office_editable

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_office_editable is not None:
            result['enable_office_editable'] = self.enable_office_editable
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enable_office_editable') is not None:
            self.enable_office_editable = m.get('enable_office_editable')
        return self


class SimpleQuery(TeaModel):
    def __init__(
        self,
        field: bytes = None,
        operation: bytes = None,
        sub_queries: List['SimpleQuery'] = None,
        value: bytes = None,
    ):
        self.field = field
        self.operation = operation
        self.sub_queries = sub_queries
        self.value = value

    def validate(self):
        if self.sub_queries:
            for k in self.sub_queries:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.field is not None:
            result['field'] = self.field
        if self.operation is not None:
            result['operation'] = self.operation
        result['sub_queries'] = []
        if self.sub_queries is not None:
            for k in self.sub_queries:
                result['sub_queries'].append(k.to_map() if k else None)
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('field') is not None:
            self.field = m.get('field')
        if m.get('operation') is not None:
            self.operation = m.get('operation')
        self.sub_queries = []
        if m.get('sub_queries') is not None:
            for k in m.get('sub_queries'):
                temp_model = SimpleQuery()
                self.sub_queries.append(temp_model.from_map(k))
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class SimpleStreamInfo(TeaModel):
    def __init__(
        self,
        content_hash: str = None,
        content_hash_name: str = None,
        crc_64hash: str = None,
        download_url: str = None,
        size: int = None,
        thumbnail: str = None,
        url: str = None,
    ):
        self.content_hash = content_hash
        self.content_hash_name = content_hash_name
        self.crc_64hash = crc_64hash
        self.download_url = download_url
        self.size = size
        self.thumbnail = thumbnail
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.size is not None:
            result['size'] = self.size
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class Story(TeaModel):
    def __init__(
        self,
        cover_file_id: str = None,
        cover_file_thumbnail_url: str = None,
        created_at: str = None,
        custom_labels: Dict[str, Any] = None,
        face_group_ids: List[str] = None,
        story_end_time: str = None,
        story_file_list: List[File] = None,
        story_id: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
        updated_at: str = None,
    ):
        self.cover_file_id = cover_file_id
        self.cover_file_thumbnail_url = cover_file_thumbnail_url
        self.created_at = created_at
        self.custom_labels = custom_labels
        self.face_group_ids = face_group_ids
        self.story_end_time = story_end_time
        self.story_file_list = story_file_list
        self.story_id = story_id
        self.story_name = story_name
        self.story_start_time = story_start_time
        self.story_sub_type = story_sub_type
        self.story_type = story_type
        self.updated_at = updated_at

    def validate(self):
        if self.story_file_list:
            for k in self.story_file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_file_id is not None:
            result['cover_file_id'] = self.cover_file_id
        if self.cover_file_thumbnail_url is not None:
            result['cover_file_thumbnail_url'] = self.cover_file_thumbnail_url
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels
        if self.face_group_ids is not None:
            result['face_group_ids'] = self.face_group_ids
        if self.story_end_time is not None:
            result['story_end_time'] = self.story_end_time
        result['story_file_list'] = []
        if self.story_file_list is not None:
            for k in self.story_file_list:
                result['story_file_list'].append(k.to_map() if k else None)
        if self.story_id is not None:
            result['story_id'] = self.story_id
        if self.story_name is not None:
            result['story_name'] = self.story_name
        if self.story_start_time is not None:
            result['story_start_time'] = self.story_start_time
        if self.story_sub_type is not None:
            result['story_sub_type'] = self.story_sub_type
        if self.story_type is not None:
            result['story_type'] = self.story_type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover_file_id') is not None:
            self.cover_file_id = m.get('cover_file_id')
        if m.get('cover_file_thumbnail_url') is not None:
            self.cover_file_thumbnail_url = m.get('cover_file_thumbnail_url')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')
        if m.get('face_group_ids') is not None:
            self.face_group_ids = m.get('face_group_ids')
        if m.get('story_end_time') is not None:
            self.story_end_time = m.get('story_end_time')
        self.story_file_list = []
        if m.get('story_file_list') is not None:
            for k in m.get('story_file_list'):
                temp_model = File()
                self.story_file_list.append(temp_model.from_map(k))
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        if m.get('story_name') is not None:
            self.story_name = m.get('story_name')
        if m.get('story_start_time') is not None:
            self.story_start_time = m.get('story_start_time')
        if m.get('story_sub_type') is not None:
            self.story_sub_type = m.get('story_sub_type')
        if m.get('story_type') is not None:
            self.story_type = m.get('story_type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class TimeRange(TeaModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class Token(TeaModel):
    def __init__(
        self,
        access_token: str = None,
        avatar: str = None,
        default_drive_id: str = None,
        default_sbox_drive_id: str = None,
        device_id: str = None,
        device_name: str = None,
        domain_id: str = None,
        exist_link: List[LinkInfo] = None,
        expire_time: str = None,
        expires_in: int = None,
        is_first_login: bool = None,
        need_link: bool = None,
        need_rp_verify: bool = None,
        nick_name: str = None,
        pin_setup: bool = None,
        refresh_token: str = None,
        role: str = None,
        state: str = None,
        status: str = None,
        token_type: str = None,
        user_data: Dict[str, str] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.access_token = access_token
        self.avatar = avatar
        self.default_drive_id = default_drive_id
        self.default_sbox_drive_id = default_sbox_drive_id
        self.device_id = device_id
        self.device_name = device_name
        self.domain_id = domain_id
        self.exist_link = exist_link
        self.expire_time = expire_time
        self.expires_in = expires_in
        self.is_first_login = is_first_login
        self.need_link = need_link
        self.need_rp_verify = need_rp_verify
        self.nick_name = nick_name
        self.pin_setup = pin_setup
        self.refresh_token = refresh_token
        self.role = role
        self.state = state
        self.status = status
        self.token_type = token_type
        self.user_data = user_data
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.exist_link:
            for k in self.exist_link:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_token is not None:
            result['access_token'] = self.access_token
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.default_sbox_drive_id is not None:
            result['default_sbox_drive_id'] = self.default_sbox_drive_id
        if self.device_id is not None:
            result['device_id'] = self.device_id
        if self.device_name is not None:
            result['device_name'] = self.device_name
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        result['exist_link'] = []
        if self.exist_link is not None:
            for k in self.exist_link:
                result['exist_link'].append(k.to_map() if k else None)
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.is_first_login is not None:
            result['is_first_login'] = self.is_first_login
        if self.need_link is not None:
            result['need_link'] = self.need_link
        if self.need_rp_verify is not None:
            result['need_rp_verify'] = self.need_rp_verify
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.pin_setup is not None:
            result['pin_setup'] = self.pin_setup
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        if self.role is not None:
            result['role'] = self.role
        if self.state is not None:
            result['state'] = self.state
        if self.status is not None:
            result['status'] = self.status
        if self.token_type is not None:
            result['token_type'] = self.token_type
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_token') is not None:
            self.access_token = m.get('access_token')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('default_sbox_drive_id') is not None:
            self.default_sbox_drive_id = m.get('default_sbox_drive_id')
        if m.get('device_id') is not None:
            self.device_id = m.get('device_id')
        if m.get('device_name') is not None:
            self.device_name = m.get('device_name')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        self.exist_link = []
        if m.get('exist_link') is not None:
            for k in m.get('exist_link'):
                temp_model = LinkInfo()
                self.exist_link.append(temp_model.from_map(k))
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('is_first_login') is not None:
            self.is_first_login = m.get('is_first_login')
        if m.get('need_link') is not None:
            self.need_link = m.get('need_link')
        if m.get('need_rp_verify') is not None:
            self.need_rp_verify = m.get('need_rp_verify')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('pin_setup') is not None:
            self.pin_setup = m.get('pin_setup')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('token_type') is not None:
            self.token_type = m.get('token_type')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class UncompressConfigResponse(TeaModel):
    def __init__(
        self,
        enabled: bool = None,
        version: str = None,
    ):
        self.enabled = enabled
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enabled is not None:
            result['enabled'] = self.enabled
        if self.version is not None:
            result['version'] = self.version
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enabled') is not None:
            self.enabled = m.get('enabled')
        if m.get('version') is not None:
            self.version = m.get('version')
        return self


class UncompressedFileInfo(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        is_folder: bool = None,
        items: List['UncompressedFileInfo'] = None,
        name: str = None,
        size: int = None,
        updated_at: int = None,
    ):
        self.drive_id = drive_id
        self.file_id = file_id
        self.is_folder = is_folder
        self.items = items
        self.name = name
        self.size = size
        self.updated_at = updated_at

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.is_folder is not None:
            result['is_folder'] = self.is_folder
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.name is not None:
            result['name'] = self.name
        if self.size is not None:
            result['size'] = self.size
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('is_folder') is not None:
            self.is_folder = m.get('is_folder')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = UncompressedFileInfo()
                self.items.append(temp_model.from_map(k))
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        return self


class UploadFormInfo(TeaModel):
    def __init__(
        self,
        bucket_name: str = None,
        endpoint: str = None,
        form_data: Dict[str, str] = None,
        object_key: str = None,
        oss_access_key_id: str = None,
        oss_end_point: str = None,
        oss_security_token: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.bucket_name = bucket_name
        self.endpoint = endpoint
        self.form_data = form_data
        self.object_key = object_key
        self.oss_access_key_id = oss_access_key_id
        self.oss_end_point = oss_end_point
        self.oss_security_token = oss_security_token
        self.policy = policy
        self.signature = signature

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.bucket_name is not None:
            result['bucket_name'] = self.bucket_name
        if self.endpoint is not None:
            result['endpoint'] = self.endpoint
        if self.form_data is not None:
            result['form_data'] = self.form_data
        if self.object_key is not None:
            result['object_key'] = self.object_key
        if self.oss_access_key_id is not None:
            result['oss_access_key_id'] = self.oss_access_key_id
        if self.oss_end_point is not None:
            result['oss_end_point'] = self.oss_end_point
        if self.oss_security_token is not None:
            result['oss_security_token'] = self.oss_security_token
        if self.policy is not None:
            result['policy'] = self.policy
        if self.signature is not None:
            result['signature'] = self.signature
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('bucket_name') is not None:
            self.bucket_name = m.get('bucket_name')
        if m.get('endpoint') is not None:
            self.endpoint = m.get('endpoint')
        if m.get('form_data') is not None:
            self.form_data = m.get('form_data')
        if m.get('object_key') is not None:
            self.object_key = m.get('object_key')
        if m.get('oss_access_key_id') is not None:
            self.oss_access_key_id = m.get('oss_access_key_id')
        if m.get('oss_end_point') is not None:
            self.oss_end_point = m.get('oss_end_point')
        if m.get('oss_security_token') is not None:
            self.oss_security_token = m.get('oss_security_token')
        if m.get('policy') is not None:
            self.policy = m.get('policy')
        if m.get('signature') is not None:
            self.signature = m.get('signature')
        return self


class User(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        created_at: int = None,
        creator: str = None,
        default_drive_id: str = None,
        description: str = None,
        domain_id: str = None,
        email: str = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        updated_at: int = None,
        user_data: Dict[str, str] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.avatar = avatar
        self.created_at = created_at
        self.creator = creator
        self.default_drive_id = default_drive_id
        self.description = description
        self.domain_id = domain_id
        self.email = email
        self.nick_name = nick_name
        self.phone = phone
        self.role = role
        self.status = status
        self.updated_at = updated_at
        self.user_data = user_data
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.email is not None:
            result['email'] = self.email
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class UserExtraItem(TeaModel):
    def __init__(
        self,
        account: List[AccountLinkInfo] = None,
        avatar: str = None,
        created_at: str = None,
        creator: str = None,
        default_drive: BaseDriveResponse = None,
        default_drive_id: str = None,
        default_location: str = None,
        deny_change_password_by_self: bool = None,
        description: str = None,
        domain_id: str = None,
        email: str = None,
        expired_at: int = None,
        is_sync: bool = None,
        last_login_time: int = None,
        need_change_password_next_login: bool = None,
        nick_name: str = None,
        parent_group: List[BaseDriveResponse] = None,
        path_status: str = None,
        permission: Dict[str, IDPermission] = None,
        phone: str = None,
        phone_region: str = None,
        role: str = None,
        status: str = None,
        updated_at: str = None,
        user_data: Dict[str, Any] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.account = account
        self.avatar = avatar
        self.created_at = created_at
        self.creator = creator
        self.default_drive = default_drive
        self.default_drive_id = default_drive_id
        self.default_location = default_location
        self.deny_change_password_by_self = deny_change_password_by_self
        self.description = description
        self.domain_id = domain_id
        self.email = email
        self.expired_at = expired_at
        self.is_sync = is_sync
        self.last_login_time = last_login_time
        self.need_change_password_next_login = need_change_password_next_login
        self.nick_name = nick_name
        self.parent_group = parent_group
        self.path_status = path_status
        self.permission = permission
        self.phone = phone
        self.phone_region = phone_region
        self.role = role
        self.status = status
        self.updated_at = updated_at
        self.user_data = user_data
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        if self.account:
            for k in self.account:
                if k:
                    k.validate()
        if self.default_drive:
            self.default_drive.validate()
        if self.parent_group:
            for k in self.parent_group:
                if k:
                    k.validate()
        if self.permission:
            for v in self.permission.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['account'] = []
        if self.account is not None:
            for k in self.account:
                result['account'].append(k.to_map() if k else None)
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.default_drive is not None:
            result['default_drive'] = self.default_drive.to_map()
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.default_location is not None:
            result['default_location'] = self.default_location
        if self.deny_change_password_by_self is not None:
            result['deny_change_password_by_self'] = self.deny_change_password_by_self
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.email is not None:
            result['email'] = self.email
        if self.expired_at is not None:
            result['expired_at'] = self.expired_at
        if self.is_sync is not None:
            result['is_sync'] = self.is_sync
        if self.last_login_time is not None:
            result['last_login_time'] = self.last_login_time
        if self.need_change_password_next_login is not None:
            result['need_change_password_next_login'] = self.need_change_password_next_login
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        result['parent_group'] = []
        if self.parent_group is not None:
            for k in self.parent_group:
                result['parent_group'].append(k.to_map() if k else None)
        if self.path_status is not None:
            result['path_status'] = self.path_status
        result['permission'] = {}
        if self.permission is not None:
            for k, v in self.permission.items():
                result['permission'][k] = v.to_map()
        if self.phone is not None:
            result['phone'] = self.phone
        if self.phone_region is not None:
            result['phone_region'] = self.phone_region
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.account = []
        if m.get('account') is not None:
            for k in m.get('account'):
                temp_model = AccountLinkInfo()
                self.account.append(temp_model.from_map(k))
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('default_drive') is not None:
            temp_model = BaseDriveResponse()
            self.default_drive = temp_model.from_map(m['default_drive'])
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('default_location') is not None:
            self.default_location = m.get('default_location')
        if m.get('deny_change_password_by_self') is not None:
            self.deny_change_password_by_self = m.get('deny_change_password_by_self')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('expired_at') is not None:
            self.expired_at = m.get('expired_at')
        if m.get('is_sync') is not None:
            self.is_sync = m.get('is_sync')
        if m.get('last_login_time') is not None:
            self.last_login_time = m.get('last_login_time')
        if m.get('need_change_password_next_login') is not None:
            self.need_change_password_next_login = m.get('need_change_password_next_login')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        self.parent_group = []
        if m.get('parent_group') is not None:
            for k in m.get('parent_group'):
                temp_model = BaseDriveResponse()
                self.parent_group.append(temp_model.from_map(k))
        if m.get('path_status') is not None:
            self.path_status = m.get('path_status')
        self.permission = {}
        if m.get('permission') is not None:
            for k, v in m.get('permission').items():
                temp_model = IDPermission()
                self.permission[k] = temp_model.from_map(v)
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('phone_region') is not None:
            self.phone_region = m.get('phone_region')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class UserTag(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # This parameter is required.
        self.key = key
        # This parameter is required.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class VideoPreviewPlayInfoLiveTranscodingTaskList(TeaModel):
    def __init__(
        self,
        keep_original_resolution: bool = None,
        status: str = None,
        template_id: str = None,
        url: str = None,
    ):
        self.keep_original_resolution = keep_original_resolution
        self.status = status
        self.template_id = template_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_original_resolution is not None:
            result['keep_original_resolution'] = self.keep_original_resolution
        if self.status is not None:
            result['status'] = self.status
        if self.template_id is not None:
            result['template_id'] = self.template_id
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keep_original_resolution') is not None:
            self.keep_original_resolution = m.get('keep_original_resolution')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class VideoPreviewPlayInfoMeta(TeaModel):
    def __init__(
        self,
        duration: float = None,
        height: int = None,
        width: int = None,
    ):
        self.duration = duration
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class VideoPreviewPlayInfoOfflineVideoTranscodingList(TeaModel):
    def __init__(
        self,
        keep_original_resolution: bool = None,
        status: str = None,
        template_id: str = None,
        url: str = None,
    ):
        self.keep_original_resolution = keep_original_resolution
        self.status = status
        self.template_id = template_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_original_resolution is not None:
            result['keep_original_resolution'] = self.keep_original_resolution
        if self.status is not None:
            result['status'] = self.status
        if self.template_id is not None:
            result['template_id'] = self.template_id
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keep_original_resolution') is not None:
            self.keep_original_resolution = m.get('keep_original_resolution')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class VideoPreviewPlayInfo(TeaModel):
    def __init__(
        self,
        category: str = None,
        live_transcoding_task_list: List[VideoPreviewPlayInfoLiveTranscodingTaskList] = None,
        master_url: str = None,
        meta: VideoPreviewPlayInfoMeta = None,
        offline_video_transcoding_list: List[VideoPreviewPlayInfoOfflineVideoTranscodingList] = None,
    ):
        self.category = category
        self.live_transcoding_task_list = live_transcoding_task_list
        self.master_url = master_url
        self.meta = meta
        self.offline_video_transcoding_list = offline_video_transcoding_list

    def validate(self):
        if self.live_transcoding_task_list:
            for k in self.live_transcoding_task_list:
                if k:
                    k.validate()
        if self.meta:
            self.meta.validate()
        if self.offline_video_transcoding_list:
            for k in self.offline_video_transcoding_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['live_transcoding_task_list'] = []
        if self.live_transcoding_task_list is not None:
            for k in self.live_transcoding_task_list:
                result['live_transcoding_task_list'].append(k.to_map() if k else None)
        if self.master_url is not None:
            result['master_url'] = self.master_url
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        result['offline_video_transcoding_list'] = []
        if self.offline_video_transcoding_list is not None:
            for k in self.offline_video_transcoding_list:
                result['offline_video_transcoding_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.live_transcoding_task_list = []
        if m.get('live_transcoding_task_list') is not None:
            for k in m.get('live_transcoding_task_list'):
                temp_model = VideoPreviewPlayInfoLiveTranscodingTaskList()
                self.live_transcoding_task_list.append(temp_model.from_map(k))
        if m.get('master_url') is not None:
            self.master_url = m.get('master_url')
        if m.get('meta') is not None:
            temp_model = VideoPreviewPlayInfoMeta()
            self.meta = temp_model.from_map(m['meta'])
        self.offline_video_transcoding_list = []
        if m.get('offline_video_transcoding_list') is not None:
            for k in m.get('offline_video_transcoding_list'):
                temp_model = VideoPreviewPlayInfoOfflineVideoTranscodingList()
                self.offline_video_transcoding_list.append(temp_model.from_map(k))
        return self


class VideoPreviewPlayMetaLiveTranscodingTaskList(TeaModel):
    def __init__(
        self,
        keep_original_resolution: bool = None,
        status: str = None,
        template_id: str = None,
    ):
        self.keep_original_resolution = keep_original_resolution
        self.status = status
        self.template_id = template_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.keep_original_resolution is not None:
            result['keep_original_resolution'] = self.keep_original_resolution
        if self.status is not None:
            result['status'] = self.status
        if self.template_id is not None:
            result['template_id'] = self.template_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('keep_original_resolution') is not None:
            self.keep_original_resolution = m.get('keep_original_resolution')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        return self


class VideoPreviewPlayMetaMeta(TeaModel):
    def __init__(
        self,
        duration: float = None,
        height: int = None,
        width: int = None,
    ):
        self.duration = duration
        self.height = height
        self.width = width

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.height is not None:
            result['height'] = self.height
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('width') is not None:
            self.width = m.get('width')
        return self


class VideoPreviewPlayMeta(TeaModel):
    def __init__(
        self,
        category: str = None,
        live_transcoding_task_list: List[VideoPreviewPlayMetaLiveTranscodingTaskList] = None,
        meta: VideoPreviewPlayMetaMeta = None,
    ):
        self.category = category
        self.live_transcoding_task_list = live_transcoding_task_list
        self.meta = meta

    def validate(self):
        if self.live_transcoding_task_list:
            for k in self.live_transcoding_task_list:
                if k:
                    k.validate()
        if self.meta:
            self.meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        result['live_transcoding_task_list'] = []
        if self.live_transcoding_task_list is not None:
            for k in self.live_transcoding_task_list:
                result['live_transcoding_task_list'].append(k.to_map() if k else None)
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        self.live_transcoding_task_list = []
        if m.get('live_transcoding_task_list') is not None:
            for k in m.get('live_transcoding_task_list'):
                temp_model = VideoPreviewPlayMetaLiveTranscodingTaskList()
                self.live_transcoding_task_list.append(temp_model.from_map(k))
        if m.get('meta') is not None:
            temp_model = VideoPreviewPlayMetaMeta()
            self.meta = temp_model.from_map(m['meta'])
        return self


class View(TeaModel):
    def __init__(
        self,
        category: str = None,
        created_at: str = None,
        description: str = None,
        ex_fields_info: Dict[str, Any] = None,
        file_count: int = None,
        name: str = None,
        owner: str = None,
        updated_at: str = None,
        view_id: str = None,
    ):
        self.category = category
        self.created_at = created_at
        self.description = description
        self.ex_fields_info = ex_fields_info
        self.file_count = file_count
        self.name = name
        self.owner = owner
        self.updated_at = updated_at
        self.view_id = view_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.ex_fields_info is not None:
            result['ex_fields_info'] = self.ex_fields_info
        if self.file_count is not None:
            result['file_count'] = self.file_count
        if self.name is not None:
            result['name'] = self.name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.view_id is not None:
            result['view_id'] = self.view_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('ex_fields_info') is not None:
            self.ex_fields_info = m.get('ex_fields_info')
        if m.get('file_count') is not None:
            self.file_count = m.get('file_count')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('view_id') is not None:
            self.view_id = m.get('view_id')
        return self


class ViewFileInvestigationInfo(TeaModel):
    def __init__(
        self,
        status: int = None,
        suggestion: str = None,
    ):
        self.status = status
        self.suggestion = suggestion

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        if self.suggestion is not None:
            result['suggestion'] = self.suggestion
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('suggestion') is not None:
            self.suggestion = m.get('suggestion')
        return self


class ViewFile(TeaModel):
    def __init__(
        self,
        category: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        crc_64hash: str = None,
        created_at: str = None,
        description: str = None,
        domain_id: str = None,
        download_url: str = None,
        drive_id: str = None,
        fields: Dict[str, Any] = None,
        file_extension: str = None,
        file_id: str = None,
        file_revision_id: str = None,
        hidden: bool = None,
        investigation_info: ViewFileInvestigationInfo = None,
        joined_at: int = None,
        labels: List[str] = None,
        local_created_at: str = None,
        local_modified_at: str = None,
        name: str = None,
        parent_file_id: str = None,
        revision_id: str = None,
        size: int = None,
        starred: bool = None,
        status: str = None,
        thumbnail: str = None,
        thumbnail_urls: Dict[str, str] = None,
        trashed_at: str = None,
        type: str = None,
        updated_at: str = None,
        upload_id: str = None,
        view_id: str = None,
    ):
        self.category = category
        self.content_hash = content_hash
        self.content_hash_name = content_hash_name
        self.content_type = content_type
        self.crc_64hash = crc_64hash
        self.created_at = created_at
        self.description = description
        self.domain_id = domain_id
        self.download_url = download_url
        self.drive_id = drive_id
        self.fields = fields
        self.file_extension = file_extension
        self.file_id = file_id
        self.file_revision_id = file_revision_id
        self.hidden = hidden
        self.investigation_info = investigation_info
        self.joined_at = joined_at
        self.labels = labels
        self.local_created_at = local_created_at
        self.local_modified_at = local_modified_at
        self.name = name
        self.parent_file_id = parent_file_id
        self.revision_id = revision_id
        self.size = size
        self.starred = starred
        self.status = status
        self.thumbnail = thumbnail
        self.thumbnail_urls = thumbnail_urls
        self.trashed_at = trashed_at
        self.type = type
        self.updated_at = updated_at
        self.upload_id = upload_id
        self.view_id = view_id

    def validate(self):
        if self.investigation_info:
            self.investigation_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.download_url is not None:
            result['download_url'] = self.download_url
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_revision_id is not None:
            result['file_revision_id'] = self.file_revision_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.investigation_info is not None:
            result['investigation_info'] = self.investigation_info.to_map()
        if self.joined_at is not None:
            result['joined_at'] = self.joined_at
        if self.labels is not None:
            result['labels'] = self.labels
        if self.local_created_at is not None:
            result['local_created_at'] = self.local_created_at
        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at
        if self.name is not None:
            result['name'] = self.name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        if self.size is not None:
            result['size'] = self.size
        if self.starred is not None:
            result['starred'] = self.starred
        if self.status is not None:
            result['status'] = self.status
        if self.thumbnail is not None:
            result['thumbnail'] = self.thumbnail
        if self.thumbnail_urls is not None:
            result['thumbnail_urls'] = self.thumbnail_urls
        if self.trashed_at is not None:
            result['trashed_at'] = self.trashed_at
        if self.type is not None:
            result['type'] = self.type
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        if self.view_id is not None:
            result['view_id'] = self.view_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('download_url') is not None:
            self.download_url = m.get('download_url')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_revision_id') is not None:
            self.file_revision_id = m.get('file_revision_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('investigation_info') is not None:
            temp_model = ViewFileInvestigationInfo()
            self.investigation_info = temp_model.from_map(m['investigation_info'])
        if m.get('joined_at') is not None:
            self.joined_at = m.get('joined_at')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('local_created_at') is not None:
            self.local_created_at = m.get('local_created_at')
        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('thumbnail') is not None:
            self.thumbnail = m.get('thumbnail')
        if m.get('thumbnail_urls') is not None:
            self.thumbnail_urls = m.get('thumbnail_urls')
        if m.get('trashed_at') is not None:
            self.trashed_at = m.get('trashed_at')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        if m.get('view_id') is not None:
            self.view_id = m.get('view_id')
        return self


class WatermarkEnableConfig(TeaModel):
    def __init__(
        self,
        display_access_user_name: bool = None,
        display_custom_text: str = None,
        display_share_link_creator_name: bool = None,
        enable_doc_preview: bool = None,
    ):
        self.display_access_user_name = display_access_user_name
        self.display_custom_text = display_custom_text
        self.display_share_link_creator_name = display_share_link_creator_name
        self.enable_doc_preview = enable_doc_preview

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_access_user_name is not None:
            result['display_access_user_name'] = self.display_access_user_name
        if self.display_custom_text is not None:
            result['display_custom_text'] = self.display_custom_text
        if self.display_share_link_creator_name is not None:
            result['display_shareLink_creator_name'] = self.display_share_link_creator_name
        if self.enable_doc_preview is not None:
            result['enable_doc_preview'] = self.enable_doc_preview
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('display_access_user_name') is not None:
            self.display_access_user_name = m.get('display_access_user_name')
        if m.get('display_custom_text') is not None:
            self.display_custom_text = m.get('display_custom_text')
        if m.get('display_shareLink_creator_name') is not None:
            self.display_share_link_creator_name = m.get('display_shareLink_creator_name')
        if m.get('enable_doc_preview') is not None:
            self.enable_doc_preview = m.get('enable_doc_preview')
        return self


class AddGroupMemberRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        member_id: str = None,
        member_type: str = None,
    ):
        # The ID of the destination group to which the member is added.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The member ID. If member_type is set to user, set this parameter to a user ID.
        # 
        # This parameter is required.
        self.member_id = member_id
        # The type of the member. Set the value to user. When you create a group, you can directly add the group to a parent group.
        # 
        # * user
        # 
        # Note: A group can be added to only one group. A user can be added to multiple groups.
        # 
        # This parameter is required.
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_id is not None:
            result['member_id'] = self.member_id
        if self.member_type is not None:
            result['member_type'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_id') is not None:
            self.member_id = m.get('member_id')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        return self


class AddGroupMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class AddStoryFilesRequestFiles(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        revision_id: str = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class AddStoryFilesRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        files: List[AddStoryFilesRequestFiles] = None,
        story_id: str = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id
        self.files = files
        # This parameter is required.
        self.story_id = story_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.story_id is not None:
            result['story_id'] = self.story_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = AddStoryFilesRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        return self


class AddStoryFilesResponseBody(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        files: List[AddStoryFile] = None,
        request_id: str = None,
        story_id: str = None,
    ):
        self.drive_id = drive_id
        self.files = files
        self.request_id = request_id
        self.story_id = story_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['request_id'] = self.request_id
        if self.story_id is not None:
            result['story_id'] = self.story_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = AddStoryFile()
                self.files.append(temp_model.from_map(k))
        if m.get('request_id') is not None:
            self.request_id = m.get('request_id')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        return self


class AddStoryFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AddStoryFilesResponseBody = None,
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
            temp_model = AddStoryFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssignRoleRequest(TeaModel):
    def __init__(
        self,
        identity: Identity = None,
        manage_resource_id: str = None,
        manage_resource_type: str = None,
        role_id: str = None,
    ):
        # The unique identifier of a user. The group administrator role can only be assigned to a user.
        # 
        # This parameter is required.
        self.identity = identity
        # The ID of the resource that the role can manage. You can only set this parameter to the ID of a group.
        # 
        # This parameter is required.
        self.manage_resource_id = manage_resource_id
        # The type of the resource that the role can manage. Valid value: RT_Group.
        # 
        # This parameter is required.
        self.manage_resource_type = manage_resource_type
        # The ID of the role that is assigned to a user. Valid value: SystemGroupAdmin.
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity is not None:
            result['identity'] = self.identity.to_map()
        if self.manage_resource_id is not None:
            result['manage_resource_id'] = self.manage_resource_id
        if self.manage_resource_type is not None:
            result['manage_resource_type'] = self.manage_resource_type
        if self.role_id is not None:
            result['role_id'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identity') is not None:
            temp_model = Identity()
            self.identity = temp_model.from_map(m['identity'])
        if m.get('manage_resource_id') is not None:
            self.manage_resource_id = m.get('manage_resource_id')
        if m.get('manage_resource_type') is not None:
            self.manage_resource_type = m.get('manage_resource_type')
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        return self


class AssignRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class AuthorizeRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        hide_consent: bool = None,
        login_type: str = None,
        redirect_uri: str = None,
        response_type: str = None,
        scope: List[str] = None,
        state: str = None,
    ):
        # The application ID returned when the application was created.
        # 
        # This parameter is required.
        self.client_id = client_id
        # Specifies whether to hide the consent page.
        self.hide_consent = hide_consent
        # The authentication method. Valid values:
        # 
        # *   default: all logon methods that are integrated on the default logon page provided by Drive and Photo Service.
        # *   ding: logs on by scanning a DingTalk QR code.
        # *   ding_sns: logs on by entering a DingTalk account and its password.
        # *   ram: logs on as an Alibaba Cloud Resource Access Management (RAM) user.
        # *   wechat: logs on by scanning a WeCom QR code.
        # *   wechat_app: logs on without authentication in WeCom.
        # 
        # This parameter is required.
        self.login_type = login_type
        # The callback URL specified when the application was created.
        # 
        # This parameter is required.
        self.redirect_uri = redirect_uri
        # The format in which to return the response. Set the value to code.
        # 
        # This parameter is required.
        self.response_type = response_type
        # The requested permissions. By default, all permissions are requested.
        self.scope = scope
        # The user-defined parameter to return in the callback URL after the requested permissions are granted.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.hide_consent is not None:
            result['hide_consent'] = self.hide_consent
        if self.login_type is not None:
            result['login_type'] = self.login_type
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        if self.response_type is not None:
            result['response_type'] = self.response_type
        if self.scope is not None:
            result['scope'] = self.scope
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('hide_consent') is not None:
            self.hide_consent = m.get('hide_consent')
        if m.get('login_type') is not None:
            self.login_type = m.get('login_type')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        if m.get('response_type') is not None:
            self.response_type = m.get('response_type')
        if m.get('scope') is not None:
            self.scope = m.get('scope')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class AuthorizeShrinkRequest(TeaModel):
    def __init__(
        self,
        client_id: str = None,
        hide_consent: bool = None,
        login_type: str = None,
        redirect_uri: str = None,
        response_type: str = None,
        scope_shrink: str = None,
        state: str = None,
    ):
        # The application ID returned when the application was created.
        # 
        # This parameter is required.
        self.client_id = client_id
        # Specifies whether to hide the consent page.
        self.hide_consent = hide_consent
        # The authentication method. Valid values:
        # 
        # *   default: all logon methods that are integrated on the default logon page provided by Drive and Photo Service.
        # *   ding: logs on by scanning a DingTalk QR code.
        # *   ding_sns: logs on by entering a DingTalk account and its password.
        # *   ram: logs on as an Alibaba Cloud Resource Access Management (RAM) user.
        # *   wechat: logs on by scanning a WeCom QR code.
        # *   wechat_app: logs on without authentication in WeCom.
        # 
        # This parameter is required.
        self.login_type = login_type
        # The callback URL specified when the application was created.
        # 
        # This parameter is required.
        self.redirect_uri = redirect_uri
        # The format in which to return the response. Set the value to code.
        # 
        # This parameter is required.
        self.response_type = response_type
        # The requested permissions. By default, all permissions are requested.
        self.scope_shrink = scope_shrink
        # The user-defined parameter to return in the callback URL after the requested permissions are granted.
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.hide_consent is not None:
            result['hide_consent'] = self.hide_consent
        if self.login_type is not None:
            result['login_type'] = self.login_type
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        if self.response_type is not None:
            result['response_type'] = self.response_type
        if self.scope_shrink is not None:
            result['scope'] = self.scope_shrink
        if self.state is not None:
            result['state'] = self.state
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('hide_consent') is not None:
            self.hide_consent = m.get('hide_consent')
        if m.get('login_type') is not None:
            self.login_type = m.get('login_type')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        if m.get('response_type') is not None:
            self.response_type = m.get('response_type')
        if m.get('scope') is not None:
            self.scope_shrink = m.get('scope')
        if m.get('state') is not None:
            self.state = m.get('state')
        return self


class AuthorizeResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class BatchRequestRequests(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
        headers: Dict[str, str] = None,
        id: str = None,
        method: str = None,
        url: str = None,
    ):
        # The request parameters of a child request. The parameter value must be a JSON string. For more information, see the topic of the corresponding child request.
        # 
        # Before you specify the request body, you must specify a header by using Content-Type. Content-Type can only be set to application/json.
        self.body = body
        # The header of a child request, which indicates the type of the data specified in the request body.
        self.headers = headers
        # The ID of the child request. The ID is used to associate a child request with a response. The ID of a child request must be unique.
        # 
        # This parameter is required.
        self.id = id
        # The method of a child request. Valid values:
        # 
        # *   POST
        # *   GET
        # *   PUT
        # *   DELETE
        # *   HEAD
        # 
        # This parameter is required.
        self.method = method
        # The API path of a child request. Valid values:
        # 
        # *   /file/get: queries the information about a file.
        # *   /file/update: modifies the information about a file.
        # *   /file/search: searches for a file.
        # *   /file/copy: copies a file or folder.
        # *   /file/move: moves a file or folder.
        # *   /file/delete: deletes a file or folder.
        # *   /file/get_download_url: queries the download URL of a file.
        # *   /file/get_share_link_download_url: queries the download URL of a file in a share.
        # *   /recyclebin/trash: moves a file or folder to the recycle bin.
        # *   /recyclebin/restore: restores a file or folder.
        # *   /file/put_usertags: adds tags to a user.
        # *   /file/delete_usertags: removes tags from a user.
        # *   /drive/get: queries the information about a drive.
        # *   /user/get: queries the information about a user.
        # *   /group/get: queries the information about a group.
        # *   /share_link/create: creates a share.
        # *   /share_link/update: modifies a share.
        # *   /share_link/cancel: cancels a share.
        # *   /share_link/list: queries shares.
        # *   /share_link/get: queries the information about a share.
        # *   /share_link/get_share_token: queries an access token of a share.
        # *   /async_task/get: queries the information about an asynchronous task.
        # 
        # This parameter is required.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.headers is not None:
            result['headers'] = self.headers
        if self.id is not None:
            result['id'] = self.id
        if self.method is not None:
            result['method'] = self.method
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('method') is not None:
            self.method = m.get('method')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class BatchRequest(TeaModel):
    def __init__(
        self,
        requests: List[BatchRequestRequests] = None,
        resource: str = None,
    ):
        # The child requests.
        # 
        # The number of child requests. Valid value: 1 to 100.
        # 
        # This parameter is required.
        self.requests = requests
        # The type of the resource that you want to manage. Valid values:
        # 
        # *   file: a file.
        # *   drive: an individual drive or a team drive.
        # *   user: a user.
        # *   group: a group.
        # *   membership: a group member.
        # *   share_link: a share.
        # *   async_task: an asynchronous task.
        # 
        # This parameter is required.
        self.resource = resource

    def validate(self):
        if self.requests:
            for k in self.requests:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['requests'] = []
        if self.requests is not None:
            for k in self.requests:
                result['requests'].append(k.to_map() if k else None)
        if self.resource is not None:
            result['resource'] = self.resource
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.requests = []
        if m.get('requests') is not None:
            for k in m.get('requests'):
                temp_model = BatchRequestRequests()
                self.requests.append(temp_model.from_map(k))
        if m.get('resource') is not None:
            self.resource = m.get('resource')
        return self


class BatchResponseBodyResponses(TeaModel):
    def __init__(
        self,
        body: Dict[str, Any] = None,
        id: str = None,
        status: int = None,
    ):
        # The response parameters of a child request. For more information, see the topic of the corresponding child request.
        self.body = body
        # The ID of the child request. The ID is used to associate a child request with a response.
        self.id = id
        # The returned HTTP status code of a child request. For more information, see the topic of the corresponding child request.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.body is not None:
            result['body'] = self.body
        if self.id is not None:
            result['id'] = self.id
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('body') is not None:
            self.body = m.get('body')
        if m.get('id') is not None:
            self.id = m.get('id')
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class BatchResponseBody(TeaModel):
    def __init__(
        self,
        responses: List[BatchResponseBodyResponses] = None,
    ):
        # All responses of the child requests.
        self.responses = responses

    def validate(self):
        if self.responses:
            for k in self.responses:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['responses'] = []
        if self.responses is not None:
            for k in self.responses:
                result['responses'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.responses = []
        if m.get('responses') is not None:
            for k in m.get('responses'):
                temp_model = BatchResponseBodyResponses()
                self.responses.append(temp_model.from_map(k))
        return self


class BatchResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BatchResponseBody = None,
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
            temp_model = BatchResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CancelAssignRoleRequest(TeaModel):
    def __init__(
        self,
        identity: Identity = None,
        manage_resource_id: str = None,
        manage_resource_type: str = None,
        role_id: str = None,
    ):
        # The unique identifier. You can cancel only the role assigned to a user.
        # 
        # This parameter is required.
        self.identity = identity
        # The ID of the resource that the role manages. Set the value to a group ID.
        # 
        # This parameter is required.
        self.manage_resource_id = manage_resource_id
        # The type of the resource that the role manages. Set the value to RT_Group, which specifies group.
        # 
        # This parameter is required.
        self.manage_resource_type = manage_resource_type
        # The ID of the role to be canceled. Set the value to SystemGroupAdmin, which is the ID of the group administrator role.
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity is not None:
            result['identity'] = self.identity.to_map()
        if self.manage_resource_id is not None:
            result['manage_resource_id'] = self.manage_resource_id
        if self.manage_resource_type is not None:
            result['manage_resource_type'] = self.manage_resource_type
        if self.role_id is not None:
            result['role_id'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identity') is not None:
            temp_model = Identity()
            self.identity = temp_model.from_map(m['identity'])
        if m.get('manage_resource_id') is not None:
            self.manage_resource_id = m.get('manage_resource_id')
        if m.get('manage_resource_type') is not None:
            self.manage_resource_type = m.get('manage_resource_type')
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        return self


class CancelAssignRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CancelShareLinkRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
    ):
        # The share ID.
        # 
        # This parameter is required.
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class CancelShareLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ClearRecyclebinRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class ClearRecyclebinResponseBody(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
    ):
        # The ID of the asynchronous task.
        # 
        # You can call the GetAsyncTask operation to query the information about the asynchronous task based on the task ID.
        self.async_task_id = async_task_id
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class ClearRecyclebinResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ClearRecyclebinResponseBody = None,
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
            temp_model = ClearRecyclebinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CompleteFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        upload_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The upload ID.
        # 
        # This parameter is required.
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class CompleteFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: File = None,
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
            temp_model = File()
            self.body = temp_model.from_map(m['body'])
        return self


class CopyFileRequest(TeaModel):
    def __init__(
        self,
        auto_rename: bool = None,
        drive_id: str = None,
        file_id: str = None,
        share_id: str = None,
        to_drive_id: str = None,
        to_parent_file_id: str = None,
    ):
        # Specifies whether to automatically rename the file if the file name already exists in the destination folder. Default value: false.
        self.auto_rename = auto_rename
        # The drive ID.
        self.drive_id = drive_id
        # The file ID or folder ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The share ID. If you want to manage a file by using a share link, carry the `x-share-token` header for authentication in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify one of `share_id` and `drive_id`.
        self.share_id = share_id
        # The ID of the drive to which you want to copy the file or folder. Default value: the value of drive_id.
        self.to_drive_id = to_drive_id
        # The ID of the destination parent folder. If you want to copy the file or folder to a root directory, set this parameter to root.
        # 
        # This parameter is required.
        self.to_parent_file_id = to_parent_file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_rename is not None:
            result['auto_rename'] = self.auto_rename
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.to_drive_id is not None:
            result['to_drive_id'] = self.to_drive_id
        if self.to_parent_file_id is not None:
            result['to_parent_file_id'] = self.to_parent_file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_rename') is not None:
            self.auto_rename = m.get('auto_rename')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('to_drive_id') is not None:
            self.to_drive_id = m.get('to_drive_id')
        if m.get('to_parent_file_id') is not None:
            self.to_parent_file_id = m.get('to_parent_file_id')
        return self


class CopyFileResponseBody(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
    ):
        # The ID of the asynchronous task.
        # 
        # If a file is copied, this parameter is not returned. If a folder is copied, the folder is asynchronously copied in the background and this parameter is returned. You can call the GetAsyncTask operation to query the information about the asynchronous task based on the task ID.
        self.async_task_id = async_task_id
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # The ID of the copied file or folder.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class CopyFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CopyFileResponseBody = None,
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
            temp_model = CopyFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomizedStoryRequestStoryCover(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        revision_id: str = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class CreateCustomizedStoryRequestStoryFiles(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        revision_id: str = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class CreateCustomizedStoryRequest(TeaModel):
    def __init__(
        self,
        custom_labels: Dict[str, str] = None,
        drive_id: str = None,
        story_cover: CreateCustomizedStoryRequestStoryCover = None,
        story_files: List[CreateCustomizedStoryRequestStoryFiles] = None,
        story_name: str = None,
        story_sub_type: str = None,
        story_type: str = None,
    ):
        self.custom_labels = custom_labels
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.story_cover = story_cover
        # This parameter is required.
        self.story_files = story_files
        # This parameter is required.
        self.story_name = story_name
        # This parameter is required.
        self.story_sub_type = story_sub_type
        # This parameter is required.
        self.story_type = story_type

    def validate(self):
        if self.story_cover:
            self.story_cover.validate()
        if self.story_files:
            for k in self.story_files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.story_cover is not None:
            result['story_cover'] = self.story_cover.to_map()
        result['story_files'] = []
        if self.story_files is not None:
            for k in self.story_files:
                result['story_files'].append(k.to_map() if k else None)
        if self.story_name is not None:
            result['story_name'] = self.story_name
        if self.story_sub_type is not None:
            result['story_sub_type'] = self.story_sub_type
        if self.story_type is not None:
            result['story_type'] = self.story_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('story_cover') is not None:
            temp_model = CreateCustomizedStoryRequestStoryCover()
            self.story_cover = temp_model.from_map(m['story_cover'])
        self.story_files = []
        if m.get('story_files') is not None:
            for k in m.get('story_files'):
                temp_model = CreateCustomizedStoryRequestStoryFiles()
                self.story_files.append(temp_model.from_map(k))
        if m.get('story_name') is not None:
            self.story_name = m.get('story_name')
        if m.get('story_sub_type') is not None:
            self.story_sub_type = m.get('story_sub_type')
        if m.get('story_type') is not None:
            self.story_type = m.get('story_type')
        return self


class CreateCustomizedStoryResponseBody(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        story_id: str = None,
    ):
        self.drive_id = drive_id
        self.story_id = story_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.story_id is not None:
            result['story_id'] = self.story_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        return self


class CreateCustomizedStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateCustomizedStoryResponseBody = None,
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
            temp_model = CreateCustomizedStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDomainRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        domain_name: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        parent_domain_id: str = None,
        size_quota: int = None,
        user_count_quota: int = None,
    ):
        # domain 描述
        self.description = description
        # If you want to perform secondary operations based on Drive and Photo Service and perform fine-grained control on your tenants, you can use the parent-child domain feature of Drive and Photo Service. For more information, join the DingTalk group whose ID is 23146118.
        # 
        # This parameter is required.
        self.domain_name = domain_name
        # https
        self.init_drive_enable = init_drive_enable
        # http
        self.init_drive_size = init_drive_size
        # Create domain.
        self.parent_domain_id = parent_domain_id
        # The ID of the parent domain. If you want to create a child domain, specify parent_domain_id. In most cases, you do not need to create a child domain. If you want to perform secondary operations based on Drive and Photo Service, contact the customer service.
        self.size_quota = size_quota
        # The information about the domain.
        self.user_count_quota = user_count_quota

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.domain_name is not None:
            result['domain_name'] = self.domain_name
        if self.init_drive_enable is not None:
            result['init_drive_enable'] = self.init_drive_enable
        if self.init_drive_size is not None:
            result['init_drive_size'] = self.init_drive_size
        if self.parent_domain_id is not None:
            result['parent_domain_id'] = self.parent_domain_id
        if self.size_quota is not None:
            result['size_quota'] = self.size_quota
        if self.user_count_quota is not None:
            result['user_count_quota'] = self.user_count_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')
        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')
        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')
        if m.get('parent_domain_id') is not None:
            self.parent_domain_id = m.get('parent_domain_id')
        if m.get('size_quota') is not None:
            self.size_quota = m.get('size_quota')
        if m.get('user_count_quota') is not None:
            self.user_count_quota = m.get('user_count_quota')
        return self


class CreateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Domain = None,
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
            temp_model = Domain()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateDriveRequest(TeaModel):
    def __init__(
        self,
        default: bool = None,
        description: str = None,
        drive_name: str = None,
        drive_type: str = None,
        owner: str = None,
        owner_type: str = None,
        status: str = None,
        total_size: int = None,
    ):
        # Specifies whether the drive is the default drive. Default value: false.
        self.default = default
        # The description of the drive. The description can be up to 1,024 characters in length.
        self.description = description
        # The name of the drive. The name can be up to 128 characters in length.
        # 
        # This parameter is required.
        self.drive_name = drive_name
        # The type of the drive. Set the value to normal.
        self.drive_type = drive_type
        # The owner of the drive.
        # 
        # This parameter is required.
        self.owner = owner
        # The type of the owner. Valid values:
        # 
        # user and group.
        # 
        # This parameter is required.
        self.owner_type = owner_type
        # The state of the drive. Valid values:
        # 
        # enabled and disabled.
        # 
        # Default value: enabled.
        self.status = status
        # The total size of the drive. Unit: bytes. By default, the size is unlimited.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.default is not None:
            result['default'] = self.default
        if self.description is not None:
            result['description'] = self.description
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.drive_type is not None:
            result['drive_type'] = self.drive_type
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.status is not None:
            result['status'] = self.status
        if self.total_size is not None:
            result['total_size'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('default') is not None:
            self.default = m.get('default')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        return self


class CreateDriveResponseBody(TeaModel):
    def __init__(
        self,
        created_at: str = None,
        creator: str = None,
        description: str = None,
        domain_id: str = None,
        drive_id: str = None,
        drive_name: str = None,
        drive_type: str = None,
        owner: str = None,
        owner_type: str = None,
        status: str = None,
        total_size: int = None,
        used_size: int = None,
    ):
        self.created_at = created_at
        self.creator = creator
        self.description = description
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        self.drive_name = drive_name
        self.drive_type = drive_type
        self.owner = owner
        self.owner_type = owner_type
        self.status = status
        self.total_size = total_size
        self.used_size = used_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.drive_type is not None:
            result['drive_type'] = self.drive_type
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        if self.status is not None:
            result['status'] = self.status
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.used_size is not None:
            result['used_size'] = self.used_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('drive_type') is not None:
            self.drive_type = m.get('drive_type')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('used_size') is not None:
            self.used_size = m.get('used_size')
        return self


class CreateDriveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateDriveResponseBody = None,
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
            temp_model = CreateDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileRequestPartInfoListParallelSha1Ctx(TeaModel):
    def __init__(
        self,
        h: List[int] = None,
        part_offset: int = None,
    ):
        # The first to fifth 32-bit variables of the SHA-1 hash value of the file content before the file part. This parameter takes effect only if the parallel upload feature is enabled.
        self.h = h
        # The size of the file content before the file part. Unit: bytes. The value must be a multiple of 64. This parameter takes effect only if the parallel upload feature is enabled.
        self.part_offset = part_offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['h'] = self.h
        if self.part_offset is not None:
            result['part_offset'] = self.part_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('h') is not None:
            self.h = m.get('h')
        if m.get('part_offset') is not None:
            self.part_offset = m.get('part_offset')
        return self


class CreateFileRequestPartInfoList(TeaModel):
    def __init__(
        self,
        content_md_5: str = None,
        parallel_sha_1ctx: CreateFileRequestPartInfoListParallelSha1Ctx = None,
        part_number: int = None,
    ):
        # The MD5 hash value of the file part. This parameter is required when the MD5 hash value of the file part needs to be verified during part upload.
        self.content_md_5 = content_md_5
        # The SHA-1 hash value of the file content before the file part. This parameter takes effect only if the parallel upload feature is enabled.
        self.parallel_sha_1ctx = parallel_sha_1ctx
        # The serial number of a file part. The number starts from 1.
        self.part_number = part_number

    def validate(self):
        if self.parallel_sha_1ctx:
            self.parallel_sha_1ctx.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.parallel_sha_1ctx is not None:
            result['parallel_sha1_ctx'] = self.parallel_sha_1ctx.to_map()
        if self.part_number is not None:
            result['part_number'] = self.part_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('parallel_sha1_ctx') is not None:
            temp_model = CreateFileRequestPartInfoListParallelSha1Ctx()
            self.parallel_sha_1ctx = temp_model.from_map(m['parallel_sha1_ctx'])
        if m.get('part_number') is not None:
            self.part_number = m.get('part_number')
        return self


class CreateFileRequest(TeaModel):
    def __init__(
        self,
        check_name_mode: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        content_type: str = None,
        description: str = None,
        drive_id: str = None,
        file_id: str = None,
        hidden: bool = None,
        image_media_metadata: ImageMediaMetadata = None,
        local_created_at: str = None,
        local_modified_at: str = None,
        name: str = None,
        parallel_upload: bool = None,
        parent_file_id: str = None,
        part_info_list: List[CreateFileRequestPartInfoList] = None,
        pre_hash: str = None,
        share_id: str = None,
        size: int = None,
        type: str = None,
        user_tags: List[UserTag] = None,
        video_media_metadata: VideoMediaMetadata = None,
    ):
        # The processing method that is used if the file that you want to create has the same name as an existing file in the cloud. Valid values:
        # 
        # ignore: allows you to create the file by using the same name as an existing file in the cloud.
        # 
        # auto_rename: automatically renames the file that you want to create. By default, the current point in time is added to the end of the file name. Example: xxx_20060102_150405.
        # 
        # refuse: does not create the file that you want to create but returns the information about the file that has the same name in the cloud.
        # 
        # Default value: ignore.
        self.check_name_mode = check_name_mode
        # The hash value of the file content. The value is calculated based on the algorithm specified by content_hash_name.
        self.content_hash = content_hash
        # The name of the algorithm that is used to calculate the hash value of the file content. Only SHA1 is supported.
        self.content_hash_name = content_hash_name
        # The type of the file content. Default value: application/oct-stream.
        self.content_type = content_type
        # The description of the file. The description can be up to 1,024 characters in length. By default, this parameter is left empty.
        self.description = description
        # The drive ID. This parameter is required if the file is not uploaded by using the share URL of the file.
        self.drive_id = drive_id
        # The file ID. This parameter is required if check_name_mode is set to ignore.
        self.file_id = file_id
        # Specifies whether to hide the file or folder. By default, the file or folder is not hidden.
        self.hidden = hidden
        # The information about the image specified by the client.
        self.image_media_metadata = image_media_metadata
        # The time when the local file was created. By default, this parameter is left empty. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format based on the UTC+0 time zone.
        self.local_created_at = local_created_at
        # The time when the local file was modified. By default, this parameter is left empty. Specify the time in the yyyy-MM-ddTHH:mm:ssZ format based on the UTC+0 time zone.
        self.local_modified_at = local_modified_at
        # The name of the file. The name can be up to 1,024 bytes in length based on the UTF-8 encoding rule and cannot end with a forward slash (/).
        # 
        # This parameter is required.
        self.name = name
        # Specifies whether to enable the parallel upload feature.
        self.parallel_upload = parallel_upload
        # The ID of the parent directory. If you want to create a file or folder in the root directory, set this parameter to root.
        # 
        # This parameter is required.
        self.parent_file_id = parent_file_id
        # The information about the file parts. You can specify up to 10,000 parts. By default, if you do not specify this parameter, only one part is returned.
        self.part_info_list = part_info_list
        # The SHA-1 hash value of the first 1 KB data of the file. This parameter is required if you perform instant file upload by using the pre-hashing feature. If the SHA-1 hash value is not matched on the cloud, the client does not need to calculate the SHA-1 hash value of the entire file.
        self.pre_hash = pre_hash
        # The share ID. This parameter is required if the file is uploaded by using the share URL of the file.
        self.share_id = share_id
        # The size of the file. Unit: bytes.
        self.size = size
        # The type of the file. Valid values:
        # 
        # file folder
        # 
        # This parameter is required.
        self.type = type
        # The custom tags. You can specify up to 1,000 tags.
        self.user_tags = user_tags
        # The information about the video specified by the client.
        self.video_media_metadata = video_media_metadata

    def validate(self):
        if self.image_media_metadata:
            self.image_media_metadata.validate()
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()
        if self.user_tags:
            for k in self.user_tags:
                if k:
                    k.validate()
        if self.video_media_metadata:
            self.video_media_metadata.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name_mode is not None:
            result['check_name_mode'] = self.check_name_mode
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.image_media_metadata is not None:
            result['image_media_metadata'] = self.image_media_metadata.to_map()
        if self.local_created_at is not None:
            result['local_created_at'] = self.local_created_at
        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at
        if self.name is not None:
            result['name'] = self.name
        if self.parallel_upload is not None:
            result['parallel_upload'] = self.parallel_upload
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.pre_hash is not None:
            result['pre_hash'] = self.pre_hash
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.size is not None:
            result['size'] = self.size
        if self.type is not None:
            result['type'] = self.type
        result['user_tags'] = []
        if self.user_tags is not None:
            for k in self.user_tags:
                result['user_tags'].append(k.to_map() if k else None)
        if self.video_media_metadata is not None:
            result['video_media_metadata'] = self.video_media_metadata.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_name_mode') is not None:
            self.check_name_mode = m.get('check_name_mode')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('image_media_metadata') is not None:
            temp_model = ImageMediaMetadata()
            self.image_media_metadata = temp_model.from_map(m['image_media_metadata'])
        if m.get('local_created_at') is not None:
            self.local_created_at = m.get('local_created_at')
        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('parallel_upload') is not None:
            self.parallel_upload = m.get('parallel_upload')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = CreateFileRequestPartInfoList()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('pre_hash') is not None:
            self.pre_hash = m.get('pre_hash')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('type') is not None:
            self.type = m.get('type')
        self.user_tags = []
        if m.get('user_tags') is not None:
            for k in m.get('user_tags'):
                temp_model = UserTag()
                self.user_tags.append(temp_model.from_map(k))
        if m.get('video_media_metadata') is not None:
            temp_model = VideoMediaMetadata()
            self.video_media_metadata = temp_model.from_map(m['video_media_metadata'])
        return self


class CreateFileResponseBody(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        drive_id: str = None,
        exist: bool = None,
        file_id: str = None,
        file_name: str = None,
        parent_file_id: str = None,
        part_info_list: List[UploadPartInfo] = None,
        rapid_upload: bool = None,
        status: str = None,
        type: str = None,
        upload_id: str = None,
    ):
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # Indicates whether the file exists.
        self.exist = exist
        # The file ID.
        self.file_id = file_id
        # The file name.
        self.file_name = file_name
        # The ID of the parent directory.
        self.parent_file_id = parent_file_id
        # The information about the file parts.
        self.part_info_list = part_info_list
        # Indicates whether the file is instantly uploaded.
        self.rapid_upload = rapid_upload
        # The state of the file.
        self.status = status
        # The type of the file.
        self.type = type
        # The ID of the upload task.
        self.upload_id = upload_id

    def validate(self):
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.exist is not None:
            result['exist'] = self.exist
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.rapid_upload is not None:
            result['rapid_upload'] = self.rapid_upload
        if self.status is not None:
            result['status'] = self.status
        if self.type is not None:
            result['type'] = self.type
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('exist') is not None:
            self.exist = m.get('exist')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('rapid_upload') is not None:
            self.rapid_upload = m.get('rapid_upload')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class CreateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateFileResponseBody = None,
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
            temp_model = CreateFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateGroupRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_name: str = None,
        is_root: bool = None,
        parent_group_id: str = None,
    ):
        # The description of the group. The description can be up to 1,024 characters in length.
        self.description = description
        # The name of the group. The name must be 1 to 128 characters in length.
        # 
        # This parameter is required.
        self.group_name = group_name
        # Specifies whether the group is a root group. A root group cannot be added to any other group. In most cases, a root group is the top-level organization in the organizational structure.
        self.is_root = is_root
        # The ID of the parent group to which the group is added. If this parameter is specified, the system automatically adds the group to the specified parent group after the group is created.
        self.parent_group_id = parent_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.is_root is not None:
            result['is_root'] = self.is_root
        if self.parent_group_id is not None:
            result['parent_group_id'] = self.parent_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('is_root') is not None:
            self.is_root = m.get('is_root')
        if m.get('parent_group_id') is not None:
            self.parent_group_id = m.get('parent_group_id')
        return self


class CreateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Group = None,
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
            temp_model = Group()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateIdentityToBenefitPkgMappingRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        benefit_pkg_id: str = None,
        expire_time: int = None,
        identity_id: str = None,
        identity_type: str = None,
    ):
        # The number of benefit packages.
        # 
        # This parameter takes effect only for the benefit packages of the resource type. Default value: 1.
        self.amount = amount
        # The unique identifier of the benefit package.
        # 
        # This parameter is required.
        self.benefit_pkg_id = benefit_pkg_id
        # The time when the benefit package expires. Set the value to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # By default, the benefit package never expires.
        self.expire_time = expire_time
        # The unique identifier of the entity.
        # 
        # If you want to manage the benefits of a user, set this parameter to a user ID.
        # 
        # This parameter is required.
        self.identity_id = identity_id
        # The type of the entity.
        # 
        # If you want to manage the benefits of a user, set this parameter to user.
        # 
        # This parameter is required.
        self.identity_type = identity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.benefit_pkg_id is not None:
            result['benefit_pkg_id'] = self.benefit_pkg_id
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.identity_id is not None:
            result['identity_id'] = self.identity_id
        if self.identity_type is not None:
            result['identity_type'] = self.identity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('benefit_pkg_id') is not None:
            self.benefit_pkg_id = m.get('benefit_pkg_id')
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')
        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')
        return self


class CreateIdentityToBenefitPkgMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class CreateOrderRequest(TeaModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        code: str = None,
        instance_id: str = None,
        order_type: str = None,
        package: str = None,
        period: int = None,
        period_unit: str = None,
        total_size: int = None,
        user_count: int = None,
    ):
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        # This parameter is required.
        self.code = code
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.order_type = order_type
        # This parameter is required.
        self.package = package
        # This parameter is required.
        self.period = period
        # This parameter is required.
        self.period_unit = period_unit
        # This parameter is required.
        self.total_size = total_size
        # This parameter is required.
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.auto_pay is not None:
            result['auto_pay'] = self.auto_pay
        if self.auto_renew is not None:
            result['auto_renew'] = self.auto_renew
        if self.code is not None:
            result['code'] = self.code
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.order_type is not None:
            result['order_type'] = self.order_type
        if self.package is not None:
            result['package'] = self.package
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['period_unit'] = self.period_unit
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.user_count is not None:
            result['user_count'] = self.user_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('auto_pay') is not None:
            self.auto_pay = m.get('auto_pay')
        if m.get('auto_renew') is not None:
            self.auto_renew = m.get('auto_renew')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')
        if m.get('package') is not None:
            self.package = m.get('package')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('period_unit') is not None:
            self.period_unit = m.get('period_unit')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('user_count') is not None:
            self.user_count = m.get('user_count')
        return self


class CreateOrderResponseBody(TeaModel):
    def __init__(
        self,
        instance_id: str = None,
        order_id: str = None,
    ):
        self.instance_id = instance_id
        self.order_id = order_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.order_id is not None:
            result['order_id'] = self.order_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('order_id') is not None:
            self.order_id = m.get('order_id')
        return self


class CreateOrderResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateOrderResponseBody = None,
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
            temp_model = CreateOrderResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateShareLinkRequest(TeaModel):
    def __init__(
        self,
        creatable: bool = None,
        creatable_file_id_list: List[str] = None,
        description: str = None,
        disable_download: bool = None,
        disable_preview: bool = None,
        disable_save: bool = None,
        download_limit: int = None,
        drive_id: str = None,
        expiration: str = None,
        file_id_list: List[str] = None,
        office_editable: bool = None,
        preview_limit: int = None,
        require_login: bool = None,
        save_limit: int = None,
        share_all_files: bool = None,
        share_name: str = None,
        share_pwd: str = None,
        user_id: str = None,
    ):
        self.creatable = creatable
        self.creatable_file_id_list = creatable_file_id_list
        # The description of the share. The description must be 0 to 1,024 characters in length.
        self.description = description
        # Specifies whether to disable the download feature.
        self.disable_download = disable_download
        # Specifies whether to disable the preview feature.
        self.disable_preview = disable_preview
        # Specifies whether to disable the dump feature.
        self.disable_save = disable_save
        # The limit on the number of times that the shared files can be downloaded. The value of this parameter must be equal to or greater than 0. A value of 0 indicates no limit.
        self.download_limit = download_limit
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The time when the share URL expires. The value of this parameter follows the RFC 3339 standard. Example: "2020-06-28T11:33:00.000+08:00". If expiration is set to "", the share URL never expires.
        self.expiration = expiration
        # The IDs of the files to share in the parent path. The number of files in the parent path ranges from 1 to 100. If share_all_files is set to true, this parameter does not take effect. Otherwise, you must specify this parameter.``
        self.file_id_list = file_id_list
        self.office_editable = office_editable
        # The limit on the number of times that the shared files can be previewed. The value of this parameter must be equal to or greater than 0. A value of 0 indicates no limit.
        self.preview_limit = preview_limit
        self.require_login = require_login
        # The limit on the number of times that the shared files can be dumped. The value of this parameter must be equal to or greater than 0. A value of 0 indicates no limit.
        self.save_limit = save_limit
        # Specifies whether to share all files in the drive.
        self.share_all_files = share_all_files
        # The name of the share. If you leave this parameter empty, the file name that corresponds to the first ID in the file ID list is used. The name must be 0 to 128 characters in length.
        self.share_name = share_name
        # The access code. An access code must be 0 to 64 bytes in length. If you do not specify this parameter or leave this parameter empty, the files can be accessed without an access code. In this case, you do not need to specify the share_pwd parameter when you call an operation to query the share URL. The access code can contain only visible ASCII characters.
        self.share_pwd = share_pwd
        # The user ID.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creatable is not None:
            result['creatable'] = self.creatable
        if self.creatable_file_id_list is not None:
            result['creatable_file_id_list'] = self.creatable_file_id_list
        if self.description is not None:
            result['description'] = self.description
        if self.disable_download is not None:
            result['disable_download'] = self.disable_download
        if self.disable_preview is not None:
            result['disable_preview'] = self.disable_preview
        if self.disable_save is not None:
            result['disable_save'] = self.disable_save
        if self.download_limit is not None:
            result['download_limit'] = self.download_limit
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.file_id_list is not None:
            result['file_id_list'] = self.file_id_list
        if self.office_editable is not None:
            result['office_editable'] = self.office_editable
        if self.preview_limit is not None:
            result['preview_limit'] = self.preview_limit
        if self.require_login is not None:
            result['require_login'] = self.require_login
        if self.save_limit is not None:
            result['save_limit'] = self.save_limit
        if self.share_all_files is not None:
            result['share_all_files'] = self.share_all_files
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creatable') is not None:
            self.creatable = m.get('creatable')
        if m.get('creatable_file_id_list') is not None:
            self.creatable_file_id_list = m.get('creatable_file_id_list')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('disable_download') is not None:
            self.disable_download = m.get('disable_download')
        if m.get('disable_preview') is not None:
            self.disable_preview = m.get('disable_preview')
        if m.get('disable_save') is not None:
            self.disable_save = m.get('disable_save')
        if m.get('download_limit') is not None:
            self.download_limit = m.get('download_limit')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('file_id_list') is not None:
            self.file_id_list = m.get('file_id_list')
        if m.get('office_editable') is not None:
            self.office_editable = m.get('office_editable')
        if m.get('preview_limit') is not None:
            self.preview_limit = m.get('preview_limit')
        if m.get('require_login') is not None:
            self.require_login = m.get('require_login')
        if m.get('save_limit') is not None:
            self.save_limit = m.get('save_limit')
        if m.get('share_all_files') is not None:
            self.share_all_files = m.get('share_all_files')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class CreateShareLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ShareLink = None,
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
            temp_model = ShareLink()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSimilarImageClusterTaskRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class CreateSimilarImageClusterTaskResponseBody(TeaModel):
    def __init__(
        self,
        task_id: str = None,
    ):
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class CreateSimilarImageClusterTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateSimilarImageClusterTaskResponseBody = None,
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
            temp_model = CreateSimilarImageClusterTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateStoryRequest(TeaModel):
    def __init__(
        self,
        address: Address = None,
        custom_labels: Dict[str, str] = None,
        drive_id: str = None,
        max_image_count: int = None,
        min_image_count: int = None,
        story_end_time: str = None,
        story_id: str = None,
        story_name: str = None,
        story_start_time: str = None,
        story_sub_type: str = None,
        story_type: str = None,
    ):
        self.address = address
        self.custom_labels = custom_labels
        # This parameter is required.
        self.drive_id = drive_id
        self.max_image_count = max_image_count
        self.min_image_count = min_image_count
        self.story_end_time = story_end_time
        self.story_id = story_id
        self.story_name = story_name
        self.story_start_time = story_start_time
        self.story_sub_type = story_sub_type
        # This parameter is required.
        self.story_type = story_type

    def validate(self):
        if self.address:
            self.address.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address is not None:
            result['address'] = self.address.to_map()
        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.max_image_count is not None:
            result['max_image_count'] = self.max_image_count
        if self.min_image_count is not None:
            result['min_image_count'] = self.min_image_count
        if self.story_end_time is not None:
            result['story_end_time'] = self.story_end_time
        if self.story_id is not None:
            result['story_id'] = self.story_id
        if self.story_name is not None:
            result['story_name'] = self.story_name
        if self.story_start_time is not None:
            result['story_start_time'] = self.story_start_time
        if self.story_sub_type is not None:
            result['story_sub_type'] = self.story_sub_type
        if self.story_type is not None:
            result['story_type'] = self.story_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address') is not None:
            temp_model = Address()
            self.address = temp_model.from_map(m['address'])
        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('max_image_count') is not None:
            self.max_image_count = m.get('max_image_count')
        if m.get('min_image_count') is not None:
            self.min_image_count = m.get('min_image_count')
        if m.get('story_end_time') is not None:
            self.story_end_time = m.get('story_end_time')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        if m.get('story_name') is not None:
            self.story_name = m.get('story_name')
        if m.get('story_start_time') is not None:
            self.story_start_time = m.get('story_start_time')
        if m.get('story_sub_type') is not None:
            self.story_sub_type = m.get('story_sub_type')
        if m.get('story_type') is not None:
            self.story_type = m.get('story_type')
        return self


class CreateStoryResponseBody(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
    ):
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class CreateStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateStoryResponseBody = None,
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
            temp_model = CreateStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequestGroupInfoList(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        # The group ID.
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self


class CreateUserRequest(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        description: str = None,
        email: str = None,
        group_info_list: List[CreateUserRequestGroupInfoList] = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        user_data: Dict[str, Any] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The URL of the profile picture.
        # 
        # If you specify the parameter in the HTTP URL format, the URL must start with http:// or https:// and can be up to 4 KB in size.
        # 
        # If you specify the parameter in the data URL format, the URL must start with data:// and be encoded in Base64. The URL can be up to 300 KB in size.
        self.avatar = avatar
        # The description of the user. The description can be up to 1,024 characters in length.
        self.description = description
        # The email address.
        self.email = email
        # The information about the group.
        self.group_info_list = group_info_list
        # The nickname of the user. The nickname can be up to 128 characters in length.
        self.nick_name = nick_name
        # The phone number.
        self.phone = phone
        # The role of the user. Default value: user. Valid values:
        # 
        # *   superadmin
        # *   admin
        # *   user
        # 
        # If the domain can be divided into subdomains, the subdomain_super_admin and subdomain_admin roles are also supported.
        # 
        # Valid values:
        # 
        # *   subdomain_super_admin
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   subdomain_admin
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   superadmin
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   admin
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   user
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.role = role
        # The state of the user. Default value: enabled. Valid values:
        # 
        # *   enabled: The user is in a normal state.
        # *   disabled: The user is prohibited from logon.
        self.status = status
        # The custom data. The data can be up to 1,024 characters in length.
        self.user_data = user_data
        # The user ID. The ID can be up to 64 characters in length and cannot contain number signs (#).
        # 
        # This parameter is required.
        self.user_id = user_id
        # The username. The username can be up to 128 characters in length.
        self.user_name = user_name

    def validate(self):
        if self.group_info_list:
            for k in self.group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.description is not None:
            result['description'] = self.description
        if self.email is not None:
            result['email'] = self.email
        result['group_info_list'] = []
        if self.group_info_list is not None:
            for k in self.group_info_list:
                result['group_info_list'].append(k.to_map() if k else None)
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('email') is not None:
            self.email = m.get('email')
        self.group_info_list = []
        if m.get('group_info_list') is not None:
            for k in m.get('group_info_list'):
                temp_model = CreateUserRequestGroupInfoList()
                self.group_info_list.append(temp_model.from_map(k))
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        created_at: int = None,
        creator: str = None,
        default_drive_id: str = None,
        description: str = None,
        domain_id: str = None,
        email: str = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        updated_at: int = None,
        user_data: Dict[str, Any] = None,
        user_id: str = None,
        user_name: str = None,
    ):
        # The URL of the profile picture.
        self.avatar = avatar
        # The time when the user was created. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.created_at = created_at
        # The user who created the user.
        self.creator = creator
        # The ID of the default drive.
        self.default_drive_id = default_drive_id
        # The description of the user.
        self.description = description
        # The domain ID.
        self.domain_id = domain_id
        # The email address.
        self.email = email
        # The nickname of the user.
        self.nick_name = nick_name
        # The phone number.
        self.phone = phone
        # The role of the user. Valid values:
        # 
        # *   superadmin
        # *   admin
        # *   user
        self.role = role
        # The state of the user. Valid values:
        # 
        # *   disabled: The user is prohibited from logon.
        # *   enabled: The user is in a normal state.
        self.status = status
        # The time when the user was modified. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.updated_at = updated_at
        # The custom data.
        self.user_data = user_data
        # The user ID.
        self.user_id = user_id
        # The username.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.default_drive_id is not None:
            result['default_drive_id'] = self.default_drive_id
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.email is not None:
            result['email'] = self.email
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('default_drive_id') is not None:
            self.default_drive_id = m.get('default_drive_id')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class CreateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CreateUserResponseBody = None,
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
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CsiGetFileInfoRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        url_expire_sec: int = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.file_id = file_id
        self.url_expire_sec = url_expire_sec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        return self


class CsiGetFileInfoResponseBody(TeaModel):
    def __init__(
        self,
        investigation_info: InvestigationInfo = None,
        url: str = None,
    ):
        self.investigation_info = investigation_info
        self.url = url

    def validate(self):
        if self.investigation_info:
            self.investigation_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.investigation_info is not None:
            result['investigation_info'] = self.investigation_info.to_map()
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('investigation_info') is not None:
            temp_model = InvestigationInfo()
            self.investigation_info = temp_model.from_map(m['investigation_info'])
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class CsiGetFileInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: CsiGetFileInfoResponseBody = None,
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
            temp_model = CsiGetFileInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
    ):
        # The domain ID.
        self.domain_id = domain_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        return self


class DeleteDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteDriveRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class DeleteDriveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID or folder ID.
        # 
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class DeleteFileResponseBody(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
    ):
        # The ID of the asynchronous task. This parameter is returned only in asynchronous processing scenarios. You can call the [GetAsyncTask](https://help.aliyun.com/document_detail/440456.html) operation to query the information about the asynchronous task based on the task ID.
        self.async_task_id = async_task_id
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class DeleteFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteFileResponseBody = None,
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
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        # The group ID.
        # 
        # This parameter is required.
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self


class DeleteGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteRevisionRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        revision_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The version ID.
        # 
        # This parameter is required.
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class DeleteRevisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeleteStoryRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        story_id: str = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.story_id = story_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.story_id is not None:
            result['story_id'] = self.story_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        return self


class DeleteStoryResponseBody(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
    ):
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class DeleteStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeleteStoryResponseBody = None,
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
            temp_model = DeleteStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class DeleteUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class DeltaGetLastCursorRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        sync_root_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The ID of the root file of the synced folder.
        self.sync_root_id = sync_root_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.sync_root_id is not None:
            result['sync_root_id'] = self.sync_root_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('sync_root_id') is not None:
            self.sync_root_id = m.get('sync_root_id')
        return self


class DeltaGetLastCursorResponseBody(TeaModel):
    def __init__(
        self,
        cursor: str = None,
    ):
        # The latest cursor of incremental information in the specified drive or synced folder.
        self.cursor = cursor

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        return self


class DeltaGetLastCursorResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: DeltaGetLastCursorResponseBody = None,
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
            temp_model = DeltaGetLastCursorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DownloadFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        image_thumbnail_process: str = None,
        office_thumbnail_process: str = None,
        share_id: str = None,
        video_thumbnail_process: str = None,
    ):
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The method used to generate the thumbnail of an image. If this parameter is specified, you are redirected to the URL of the generated thumbnail.
        self.image_thumbnail_process = image_thumbnail_process
        # The method used to generate the thumbnail of a document. If this parameter is specified, you are redirected to the URL of the generated thumbnail.
        self.office_thumbnail_process = office_thumbnail_process
        # The share ID. If you want to manage a file by using a share link, carry the `x-share-token` header for authentication in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify one of `share_id` and `drive_id`.
        self.share_id = share_id
        # The method used to generate the thumbnail of a video. If this parameter is specified, you are redirected to the URL of the generated thumbnail.
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.office_thumbnail_process is not None:
            result['office_thumbnail_process'] = self.office_thumbnail_process
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('office_thumbnail_process') is not None:
            self.office_thumbnail_process = m.get('office_thumbnail_process')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class DownloadFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class FileAddPermissionRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        member_list: List[FilePermissionMember] = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The ID of the folder. If you want to authorize a user or group to access a team drive, set this parameter to root. If you want to authorize a user or group to access an individual drive, you cannot set this parameter to root.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The members that are authorized to access files.
        # 
        # This parameter is required.
        self.member_list = member_list

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['member_list'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['member_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.member_list = []
        if m.get('member_list') is not None:
            for k in m.get('member_list'):
                temp_model = FilePermissionMember()
                self.member_list.append(temp_model.from_map(k))
        return self


class FileAddPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class FileDeleteUserTagsRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        key_list: List[str] = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The tags that you want to remove from a file. You cannot leave this parameter empty. You can specify up to 1,000 tags.
        # 
        # This parameter is required.
        self.key_list = key_list

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.key_list is not None:
            result['key_list'] = self.key_list
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('key_list') is not None:
            self.key_list = m.get('key_list')
        return self


class FileDeleteUserTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class FileListPermissionRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class FileListPermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[FilePermissionMember] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for k in self.body:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        result['body'] = []
        if self.body is not None:
            for k in self.body:
                result['body'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        self.body = []
        if m.get('body') is not None:
            for k in m.get('body'):
                temp_model = FilePermissionMember()
                self.body.append(temp_model.from_map(k))
        return self


class FilePutUserTagsRequestUserTags(TeaModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The name of the tag. The tag name cannot be empty and cannot contain number signs (#).
        # 
        # This parameter is required.
        self.key = key
        # The value of the tag. The tag value cannot contain number signs (#).
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['key'] = self.key
        if self.value is not None:
            result['value'] = self.value
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')
        if m.get('value') is not None:
            self.value = m.get('value')
        return self


class FilePutUserTagsRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        user_tags: List[FilePutUserTagsRequestUserTags] = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The tags to be added to the file. You cannot leave this parameter empty. You can specify up to 1,000 tags. You cannot specify tags that have the same name.
        # 
        # This parameter is required.
        self.user_tags = user_tags

    def validate(self):
        if self.user_tags:
            for k in self.user_tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['user_tags'] = []
        if self.user_tags is not None:
            for k in self.user_tags:
                result['user_tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.user_tags = []
        if m.get('user_tags') is not None:
            for k in m.get('user_tags'):
                temp_model = FilePutUserTagsRequestUserTags()
                self.user_tags.append(temp_model.from_map(k))
        return self


class FilePutUserTagsResponseBody(TeaModel):
    def __init__(
        self,
        file_id: str = None,
    ):
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class FilePutUserTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: FilePutUserTagsResponseBody = None,
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
            temp_model = FilePutUserTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FileRemovePermissionRequestMemberList(TeaModel):
    def __init__(
        self,
        identity: Identity = None,
        role_id: str = None,
    ):
        # The identity to whom the permissions are granted, which is a user or a group.
        # 
        # This parameter is required.
        self.identity = identity
        # The role ID. You can grant permissions by assigning roles to identities, or you can customize the permissions. To grant permissions by assigning roles to identities, specify role_id. role_id and action_list are mutually exclusive. If both parameters are specified, role_id has a higher priority.
        # 
        # Valid values:
        # 
        # SystemFileOwner: collaborator.
        # 
        # SystemFileDownloader: downloader.
        # 
        # SystemFileEditor: editor.
        # 
        # SystemFileEditorWithoutDelete: editor without permissions to delete the file.
        # 
        # SystemFileEditorWithoutShareLink: editor without permissions to share the file.
        # 
        # SystemFileMetaViewer: viewer of lists.
        # 
        # SystemFileUploader: uploader. SystemFileUploaderAndDownloader: uploader and downloader.
        # 
        # SystemFileDownloaderWithShareLink: downloader and sharer.
        # 
        # SystemFileUploaderAndDownloaderWithShareLink: uploader, downloader, and sharer.
        # 
        # SystemFileUploaderAndViewer: viewer and uploader.
        # 
        # SystemFileUploaderWithShareLink: uploader and sharer.
        # 
        # SystemFileViewer: viewer.
        # 
        # This parameter is required.
        self.role_id = role_id

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity is not None:
            result['identity'] = self.identity.to_map()
        if self.role_id is not None:
            result['role_id'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identity') is not None:
            temp_model = Identity()
            self.identity = temp_model.from_map(m['identity'])
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        return self


class FileRemovePermissionRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        member_list: List[FileRemovePermissionRequestMemberList] = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The identities with whom the file is shared.
        # 
        # This parameter is required.
        self.member_list = member_list

    def validate(self):
        if self.member_list:
            for k in self.member_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['member_list'] = []
        if self.member_list is not None:
            for k in self.member_list:
                result['member_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.member_list = []
        if m.get('member_list') is not None:
            for k in m.get('member_list'):
                temp_model = FileRemovePermissionRequestMemberList()
                self.member_list.append(temp_model.from_map(k))
        return self


class FileRemovePermissionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class GetAsyncTaskRequest(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
    ):
        # The ID of the asynchronous task.
        # 
        # This parameter is required.
        self.async_task_id = async_task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        return self


class GetAsyncTaskResponseBody(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
        category: str = None,
        consumed_process: int = None,
        created_at: str = None,
        err_code: int = None,
        error_code: str = None,
        error_message: str = None,
        failed_process: int = None,
        finished_at: str = None,
        message: str = None,
        skipped_process: int = None,
        started_at: str = None,
        state: str = None,
        status: str = None,
        total_process: int = None,
        uncompress_file_list: List[UncompressedFileInfo] = None,
        url: str = None,
    ):
        # The ID of the asynchronous task.
        self.async_task_id = async_task_id
        # The custom category of the task.
        self.category = category
        # The total amount of work that is done in the asynchronous task, such as the number of files that are packaged for package download on the server.
        self.consumed_process = consumed_process
        # The time when the task was created. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2019-03-28T13:03:29.298Z.
        self.created_at = created_at
        # <warning>This parameter is no longer used. We recommend that you use error_code instead.</warning>
        # 
        # The error code returned if the asynchronous task failed.
        self.err_code = err_code
        # The error code returned if the asynchronous task failed.
        self.error_code = error_code
        # The error message returned if the asynchronous task failed.
        self.error_message = error_message
        self.failed_process = failed_process
        # The time when the task was complete. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2019-03-28T13:03:29.298Z.
        self.finished_at = finished_at
        # <warning>This parameter is no longer used. We recommend that you use error_message instead.</warning>
        # 
        # The error message returned if the asynchronous task failed.
        self.message = message
        self.skipped_process = skipped_process
        # The time when the task was started. The time follows the ISO 8601 standard in the yyyy-MM-ddTHH:mm:ssZ format. Example: 2019-03-28T13:03:29.298Z.
        self.started_at = started_at
        # The state of the task. Valid values:
        # 
        # *   Failed
        # *   Running
        # *   PartialSucceed
        # *   Succeed
        self.state = state
        # <warning>This parameter is no longer used. We recommend that you use state instead.</warning>
        # 
        # The state of the task. Valid values:
        # 
        # *   Failed
        # *   Running
        # *   PartialSucceed
        # *   Succeed
        self.status = status
        # The total amount of work to be done in the asynchronous task, such as the number of files to be packaged for package download on the server.
        self.total_process = total_process
        # The extracted files.
        self.uncompress_file_list = uncompress_file_list
        # The download URL of the data generated by the asynchronous task, such as the download URL of the packaged files generated by the task of package download on the server.
        self.url = url

    def validate(self):
        if self.uncompress_file_list:
            for k in self.uncompress_file_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.category is not None:
            result['category'] = self.category
        if self.consumed_process is not None:
            result['consumed_process'] = self.consumed_process
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.err_code is not None:
            result['err_code'] = self.err_code
        if self.error_code is not None:
            result['error_code'] = self.error_code
        if self.error_message is not None:
            result['error_message'] = self.error_message
        if self.failed_process is not None:
            result['failed_process'] = self.failed_process
        if self.finished_at is not None:
            result['finished_at'] = self.finished_at
        if self.message is not None:
            result['message'] = self.message
        if self.skipped_process is not None:
            result['skipped_process'] = self.skipped_process
        if self.started_at is not None:
            result['started_at'] = self.started_at
        if self.state is not None:
            result['state'] = self.state
        if self.status is not None:
            result['status'] = self.status
        if self.total_process is not None:
            result['total_process'] = self.total_process
        result['uncompress_file_list'] = []
        if self.uncompress_file_list is not None:
            for k in self.uncompress_file_list:
                result['uncompress_file_list'].append(k.to_map() if k else None)
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('consumed_process') is not None:
            self.consumed_process = m.get('consumed_process')
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('err_code') is not None:
            self.err_code = m.get('err_code')
        if m.get('error_code') is not None:
            self.error_code = m.get('error_code')
        if m.get('error_message') is not None:
            self.error_message = m.get('error_message')
        if m.get('failed_process') is not None:
            self.failed_process = m.get('failed_process')
        if m.get('finished_at') is not None:
            self.finished_at = m.get('finished_at')
        if m.get('message') is not None:
            self.message = m.get('message')
        if m.get('skipped_process') is not None:
            self.skipped_process = m.get('skipped_process')
        if m.get('started_at') is not None:
            self.started_at = m.get('started_at')
        if m.get('state') is not None:
            self.state = m.get('state')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_process') is not None:
            self.total_process = m.get('total_process')
        self.uncompress_file_list = []
        if m.get('uncompress_file_list') is not None:
            for k in m.get('uncompress_file_list'):
                temp_model = UncompressedFileInfo()
                self.uncompress_file_list.append(temp_model.from_map(k))
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetAsyncTaskResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetAsyncTaskResponseBody = None,
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
            temp_model = GetAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultDriveRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The user ID. If you use an AccessKey pair for authentication, you must specify this parameter. If you use an access token for authentication, this parameter is optional. By default, the user ID associated with the access token is used.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetDefaultDriveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Drive = None,
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
            temp_model = Drive()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainRequest(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        fields: str = None,
        get_quota_used: bool = None,
    ):
        # The ID of the domain.
        # 
        # This parameter is required.
        self.domain_id = domain_id
        self.fields = fields
        # Specifies whether to return the used quota of the domain. Default value: false. If the quota of the domain is greater than 0 and you set this parameter to true, the used quota of the domain is returned.
        self.get_quota_used = get_quota_used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.get_quota_used is not None:
            result['get_quota_used'] = self.get_quota_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('get_quota_used') is not None:
            self.get_quota_used = m.get('get_quota_used')
        return self


class GetDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Domain = None,
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
            temp_model = Domain()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainQuotaResponseBody(TeaModel):
    def __init__(
        self,
        size_quota: int = None,
        size_used: int = None,
        user_count_quota: int = None,
        user_count_used: int = None,
    ):
        self.size_quota = size_quota
        self.size_used = size_used
        self.user_count_quota = user_count_quota
        self.user_count_used = user_count_used

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.size_quota is not None:
            result['size_quota'] = self.size_quota
        if self.size_used is not None:
            result['size_used'] = self.size_used
        if self.user_count_quota is not None:
            result['user_count_quota'] = self.user_count_quota
        if self.user_count_used is not None:
            result['user_count_used'] = self.user_count_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('size_quota') is not None:
            self.size_quota = m.get('size_quota')
        if m.get('size_used') is not None:
            self.size_used = m.get('size_used')
        if m.get('user_count_quota') is not None:
            self.user_count_quota = m.get('user_count_quota')
        if m.get('user_count_used') is not None:
            self.user_count_used = m.get('user_count_used')
        return self


class GetDomainQuotaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDomainQuotaResponseBody = None,
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
            temp_model = GetDomainQuotaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        expire_sec: int = None,
        file_id: str = None,
        file_name: str = None,
        response_content_type: str = None,
        share_id: str = None,
    ):
        # The drive ID.
        self.drive_id = drive_id
        # The validity period of the download URL. Maximum value: 115200. Default value: 900. Unit: seconds.
        self.expire_sec = expire_sec
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The name of the file. The name can be up to 1,024 characters in length.
        self.file_name = file_name
        self.response_content_type = response_content_type
        # The share ID. If you want to manage a file by using a sharing link, carry the `x-share-token` header in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify at least either `share_id` or `drive_id`.
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.file_name is not None:
            result['file_name'] = self.file_name
        if self.response_content_type is not None:
            result['response_content_type'] = self.response_content_type
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('file_name') is not None:
            self.file_name = m.get('file_name')
        if m.get('response_content_type') is not None:
            self.response_content_type = m.get('response_content_type')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class GetDownloadUrlResponseBody(TeaModel):
    def __init__(
        self,
        cdn_url: str = None,
        content_hash: str = None,
        content_hash_name: str = None,
        crc_64hash: str = None,
        expiration: str = None,
        internal_url: str = None,
        size: int = None,
        url: str = None,
    ):
        # The download URL of a file that is downloaded by using Alibaba Cloud CDN.
        self.cdn_url = cdn_url
        # The hash value of the file content.
        self.content_hash = content_hash
        # The name of the algorithm that is used to calculate the hash value of the file content.
        self.content_hash_name = content_hash_name
        # The hash value calculated by using 64-bit cyclic redundancy check (CRC-64).
        self.crc_64hash = crc_64hash
        # The time when the download URL expires.
        self.expiration = expiration
        # The download URL of a file that is downloaded over a virtual private cloud (VPC).
        self.internal_url = internal_url
        # The size of the file. Unit: bytes.
        self.size = size
        # The download URL of a file that is downloaded over the Internet.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cdn_url is not None:
            result['cdn_url'] = self.cdn_url
        if self.content_hash is not None:
            result['content_hash'] = self.content_hash
        if self.content_hash_name is not None:
            result['content_hash_name'] = self.content_hash_name
        if self.crc_64hash is not None:
            result['crc64_hash'] = self.crc_64hash
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.internal_url is not None:
            result['internal_url'] = self.internal_url
        if self.size is not None:
            result['size'] = self.size
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cdn_url') is not None:
            self.cdn_url = m.get('cdn_url')
        if m.get('content_hash') is not None:
            self.content_hash = m.get('content_hash')
        if m.get('content_hash_name') is not None:
            self.content_hash_name = m.get('content_hash_name')
        if m.get('crc64_hash') is not None:
            self.crc_64hash = m.get('crc64_hash')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('internal_url') is not None:
            self.internal_url = m.get('internal_url')
        if m.get('size') is not None:
            self.size = m.get('size')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class GetDownloadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetDownloadUrlResponseBody = None,
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
            temp_model = GetDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDriveRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        return self


class GetDriveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Drive = None,
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
            temp_model = Drive()
            self.body = temp_model.from_map(m['body'])
        return self


class GetFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        file_id: str = None,
        share_id: str = None,
        thumbnail_processes: Dict[str, ImageProcess] = None,
        url_expire_sec: int = None,
    ):
        # The drive ID.
        self.drive_id = drive_id
        # The fields to return.
        # 
        # 1.  If this parameter is set to \\*, all fields of the file except the fields that must be specified are returned.
        # 2.  If only specific fields are required, you can specify the following fields: url, thumbnail, exif, cropping_suggestion, characteristic_hash, video_metadata, and video_preview_metadata. If multiple fields are required, separate them with commas (,). Example: url,thumbnail.
        # 3.  The investigation_info field is returned only if you specify this field.
        # 
        # By default, all fields except the fields that must be specified are returned.
        self.fields = fields
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The share ID. If you want to manage a file by using a share link, carry the `x-share-token` header for authentication in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify one of `share_id` and `drive_id`.
        self.share_id = share_id
        # 缩略图配置，可一次性返回最多5个缩略图，map的key可以自定义，返回时按key返回对应的缩略图链接
        self.thumbnail_processes = thumbnail_processes
        # The time when the file expires. Unit: seconds. Valid values: 10 to 14400.
        self.url_expire_sec = url_expire_sec

    def validate(self):
        if self.thumbnail_processes:
            for v in self.thumbnail_processes.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        result['thumbnail_processes'] = {}
        if self.thumbnail_processes is not None:
            for k, v in self.thumbnail_processes.items():
                result['thumbnail_processes'][k] = v.to_map()
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        self.thumbnail_processes = {}
        if m.get('thumbnail_processes') is not None:
            for k, v in m.get('thumbnail_processes').items():
                temp_model = ImageProcess()
                self.thumbnail_processes[k] = temp_model.from_map(v)
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        return self


class GetFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: File = None,
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
            temp_model = File()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        # The group ID.
        # 
        # This parameter is required.
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self


class GetGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Group = None,
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
            temp_model = Group()
            self.body = temp_model.from_map(m['body'])
        return self


class GetIdentityToBenefitPkgMappingRequest(TeaModel):
    def __init__(
        self,
        benefit_pkg_id: str = None,
        identity_id: str = None,
        identity_type: str = None,
    ):
        # The unique identifier of the benefit package.
        # 
        # This parameter is required.
        self.benefit_pkg_id = benefit_pkg_id
        # The unique identifier of the entity.
        # 
        # If you want to manage the benefits of a user, set this parameter to a user ID.
        # 
        # This parameter is required.
        self.identity_id = identity_id
        # The type of the entity. If you want to manage the benefits of a user, set this parameter to user.
        # 
        # This parameter is required.
        self.identity_type = identity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.benefit_pkg_id is not None:
            result['benefit_pkg_id'] = self.benefit_pkg_id
        if self.identity_id is not None:
            result['identity_id'] = self.identity_id
        if self.identity_type is not None:
            result['identity_type'] = self.identity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('benefit_pkg_id') is not None:
            self.benefit_pkg_id = m.get('benefit_pkg_id')
        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')
        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')
        return self


class GetIdentityToBenefitPkgMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: IdentityToBenefitPkgMapping = None,
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
            temp_model = IdentityToBenefitPkgMapping()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLinkInfoRequest(TeaModel):
    def __init__(
        self,
        extra: str = None,
        identity: str = None,
        type: str = None,
    ):
        self.extra = extra
        # This parameter is required.
        self.identity = identity
        # This parameter is required.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class GetLinkInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: AccountLinkInfo = None,
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
            temp_model = AccountLinkInfo()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLinkInfoByUserIdRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The user ID.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetLinkInfoByUserIdResponseBody(TeaModel):
    def __init__(
        self,
        items: List[AccountLinkInfo] = None,
    ):
        # The information about the users.
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = AccountLinkInfo()
                self.items.append(temp_model.from_map(k))
        return self


class GetLinkInfoByUserIdResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetLinkInfoByUserIdResponseBody = None,
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
            temp_model = GetLinkInfoByUserIdResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetRevisionRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        file_id: str = None,
        revision_id: str = None,
        url_expire_sec: int = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # Specifies the returned fields.
        # 
        # By default, this parameter is left empty. If you set this parameter to \\*, all fields are returned. If you leave this parameter empty, the creator of the file is not returned.
        self.fields = fields
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The version ID.
        # 
        # This parameter is required.
        self.revision_id = revision_id
        # The validity period of the file download or preview. Valid values: 10 to 86400.
        # 
        # Default value: 900. Unit: seconds.
        self.url_expire_sec = url_expire_sec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        return self


class GetRevisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Revision = None,
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
            temp_model = Revision()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareLinkRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
    ):
        # The share ID.
        # 
        # This parameter is required.
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class GetShareLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ShareLink = None,
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
            temp_model = ShareLink()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareLinkByAnonymousRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
    ):
        # The share ID.
        # 
        # This parameter is required.
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class GetShareLinkByAnonymousResponseBody(TeaModel):
    def __init__(
        self,
        access_count: int = None,
        avatar: str = None,
        creator_id: str = None,
        creator_name: str = None,
        creator_phone: str = None,
        disable_download: bool = None,
        disable_preview: bool = None,
        disable_save: bool = None,
        download_count: int = None,
        download_limit: int = None,
        expiration: str = None,
        preview_count: int = None,
        preview_limit: int = None,
        report_count: int = None,
        save_count: int = None,
        save_download_limit: int = None,
        save_limit: int = None,
        share_name: str = None,
        updated_at: str = None,
        video_preview_count: int = None,
    ):
        # The number of times that the shared files are visited.
        self.access_count = access_count
        # The profile picture of the user who created the share link.
        self.avatar = avatar
        # The ID of the user who created the share link.
        self.creator_id = creator_id
        # The name of the user who created the share link. The value is masked.
        self.creator_name = creator_name
        # The mobile number of the user who created the share link. The value is masked.
        self.creator_phone = creator_phone
        # Indicates whether the downloads of the shared files are prohibited.
        self.disable_download = disable_download
        # Indicates whether the previews of the shared files are prohibited.
        self.disable_preview = disable_preview
        # Indicates whether the saves of the shared files are prohibited.
        self.disable_save = disable_save
        # The number of times that the shared files are downloaded.
        self.download_count = download_count
        # The maximum number of times that the shared files can be downloaded.
        self.download_limit = download_limit
        # The time when the share link expires.
        self.expiration = expiration
        # The number of times that the shared files are previewed.
        self.preview_count = preview_count
        # The maximum number of times that the shared files can be previewed.
        self.preview_limit = preview_limit
        # The number of times that the shared files are reported.
        self.report_count = report_count
        # The number of times that the shared files are saved.
        self.save_count = save_count
        # The maximum number of times that the shared files can be saved and downloaded.
        self.save_download_limit = save_download_limit
        # The maximum number of times that the shared files can be saved.
        self.save_limit = save_limit
        # The name of the share link.
        self.share_name = share_name
        # The time when the share link was last modified.
        self.updated_at = updated_at
        # The number of times that the videos are previewed in the shared files.
        self.video_preview_count = video_preview_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.access_count is not None:
            result['access_count'] = self.access_count
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.creator_id is not None:
            result['creator_id'] = self.creator_id
        if self.creator_name is not None:
            result['creator_name'] = self.creator_name
        if self.creator_phone is not None:
            result['creator_phone'] = self.creator_phone
        if self.disable_download is not None:
            result['disable_download'] = self.disable_download
        if self.disable_preview is not None:
            result['disable_preview'] = self.disable_preview
        if self.disable_save is not None:
            result['disable_save'] = self.disable_save
        if self.download_count is not None:
            result['download_count'] = self.download_count
        if self.download_limit is not None:
            result['download_limit'] = self.download_limit
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.preview_count is not None:
            result['preview_count'] = self.preview_count
        if self.preview_limit is not None:
            result['preview_limit'] = self.preview_limit
        if self.report_count is not None:
            result['report_count'] = self.report_count
        if self.save_count is not None:
            result['save_count'] = self.save_count
        if self.save_download_limit is not None:
            result['save_download_limit'] = self.save_download_limit
        if self.save_limit is not None:
            result['save_limit'] = self.save_limit
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.updated_at is not None:
            result['updated_at'] = self.updated_at
        if self.video_preview_count is not None:
            result['video_preview_count'] = self.video_preview_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('access_count') is not None:
            self.access_count = m.get('access_count')
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('creator_id') is not None:
            self.creator_id = m.get('creator_id')
        if m.get('creator_name') is not None:
            self.creator_name = m.get('creator_name')
        if m.get('creator_phone') is not None:
            self.creator_phone = m.get('creator_phone')
        if m.get('disable_download') is not None:
            self.disable_download = m.get('disable_download')
        if m.get('disable_preview') is not None:
            self.disable_preview = m.get('disable_preview')
        if m.get('disable_save') is not None:
            self.disable_save = m.get('disable_save')
        if m.get('download_count') is not None:
            self.download_count = m.get('download_count')
        if m.get('download_limit') is not None:
            self.download_limit = m.get('download_limit')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('preview_count') is not None:
            self.preview_count = m.get('preview_count')
        if m.get('preview_limit') is not None:
            self.preview_limit = m.get('preview_limit')
        if m.get('report_count') is not None:
            self.report_count = m.get('report_count')
        if m.get('save_count') is not None:
            self.save_count = m.get('save_count')
        if m.get('save_download_limit') is not None:
            self.save_download_limit = m.get('save_download_limit')
        if m.get('save_limit') is not None:
            self.save_limit = m.get('save_limit')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('updated_at') is not None:
            self.updated_at = m.get('updated_at')
        if m.get('video_preview_count') is not None:
            self.video_preview_count = m.get('video_preview_count')
        return self


class GetShareLinkByAnonymousResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetShareLinkByAnonymousResponseBody = None,
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
            temp_model = GetShareLinkByAnonymousResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareLinkTokenRequest(TeaModel):
    def __init__(
        self,
        expire_sec: int = None,
        share_id: str = None,
        share_pwd: str = None,
    ):
        # The validity period of the token. Valid values: (0,7200]. Default value: 7200. Unit: seconds.
        self.expire_sec = expire_sec
        # The share ID.
        # 
        # This parameter is required.
        self.share_id = share_id
        # The access code.
        self.share_pwd = share_pwd

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expire_sec is not None:
            result['expire_sec'] = self.expire_sec
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expire_sec') is not None:
            self.expire_sec = m.get('expire_sec')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        return self


class GetShareLinkTokenResponseBody(TeaModel):
    def __init__(
        self,
        expires_in: int = None,
        share_token: str = None,
    ):
        # The validity period of the token. Unit: seconds. For example, a value of 7200 indicates two hours.
        self.expires_in = expires_in
        # The JSON Web Token (JWT).
        self.share_token = share_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.share_token is not None:
            result['share_token'] = self.share_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('share_token') is not None:
            self.share_token = m.get('share_token')
        return self


class GetShareLinkTokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetShareLinkTokenResponseBody = None,
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
            temp_model = GetShareLinkTokenResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetStoryRequest(TeaModel):
    def __init__(
        self,
        cover_image_thumbnail_process: str = None,
        cover_video_thumbnail_process: str = None,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        image_url_process: str = None,
        story_id: str = None,
        url_expire_sec: int = None,
        video_thumbnail_process: str = None,
    ):
        self.cover_image_thumbnail_process = cover_image_thumbnail_process
        self.cover_video_thumbnail_process = cover_video_thumbnail_process
        # This parameter is required.
        self.drive_id = drive_id
        self.image_thumbnail_process = image_thumbnail_process
        self.image_url_process = image_url_process
        # This parameter is required.
        self.story_id = story_id
        self.url_expire_sec = url_expire_sec
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_image_thumbnail_process is not None:
            result['cover_image_thumbnail_process'] = self.cover_image_thumbnail_process
        if self.cover_video_thumbnail_process is not None:
            result['cover_video_thumbnail_process'] = self.cover_video_thumbnail_process
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.image_url_process is not None:
            result['image_url_process'] = self.image_url_process
        if self.story_id is not None:
            result['story_id'] = self.story_id
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover_image_thumbnail_process') is not None:
            self.cover_image_thumbnail_process = m.get('cover_image_thumbnail_process')
        if m.get('cover_video_thumbnail_process') is not None:
            self.cover_video_thumbnail_process = m.get('cover_video_thumbnail_process')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('image_url_process') is not None:
            self.image_url_process = m.get('image_url_process')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class GetStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Story = None,
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
            temp_model = Story()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatusRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        task_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The ID of the task.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.task_id is not None:
            result['task_id'] = self.task_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('task_id') is not None:
            self.task_id = m.get('task_id')
        return self


class GetTaskStatusResponseBody(TeaModel):
    def __init__(
        self,
        status: str = None,
    ):
        # The state of the task.
        # 
        # Valid values:
        # 
        # *   running
        # 
        #     <!-- -->
        # 
        #     : The task is
        # 
        #     <!-- -->
        # 
        #     running
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   failed
        # 
        #     <!-- -->
        # 
        #     : The task
        # 
        #     <!-- -->
        # 
        #     fails
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   succeeded
        # 
        #     <!-- -->
        # 
        #     : The task is
        # 
        #     <!-- -->
        # 
        #     successful
        # 
        #     <!-- -->
        # 
        #     .
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.status is not None:
            result['status'] = self.status
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        return self


class GetTaskStatusResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetTaskStatusResponseBody = None,
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
            temp_model = GetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadUrlRequestPartInfoListParallelSha1Ctx(TeaModel):
    def __init__(
        self,
        h: List[int] = None,
        part_offset: int = None,
    ):
        # The first to fifth 32-bit variables of the SHA-1 hash value of the file content before the file part. This parameter takes effect only if the parallel upload feature is enabled.
        self.h = h
        # The size of the file part. Unit: bytes. The value must be a multiple of 64. This parameter takes effect only if the parallel upload feature is enabled.
        self.part_offset = part_offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['h'] = self.h
        if self.part_offset is not None:
            result['part_offset'] = self.part_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('h') is not None:
            self.h = m.get('h')
        if m.get('part_offset') is not None:
            self.part_offset = m.get('part_offset')
        return self


class GetUploadUrlRequestPartInfoListParallelSha256Ctx(TeaModel):
    def __init__(
        self,
        h: List[int] = None,
        part_offset: int = None,
    ):
        self.h = h
        self.part_offset = part_offset

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.h is not None:
            result['h'] = self.h
        if self.part_offset is not None:
            result['part_offset'] = self.part_offset
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('h') is not None:
            self.h = m.get('h')
        if m.get('part_offset') is not None:
            self.part_offset = m.get('part_offset')
        return self


class GetUploadUrlRequestPartInfoList(TeaModel):
    def __init__(
        self,
        content_md_5: str = None,
        content_type: str = None,
        parallel_sha_1ctx: GetUploadUrlRequestPartInfoListParallelSha1Ctx = None,
        parallel_sha_256ctx: GetUploadUrlRequestPartInfoListParallelSha256Ctx = None,
        part_number: int = None,
    ):
        self.content_md_5 = content_md_5
        self.content_type = content_type
        # The SHA-1 hash value of the file content before the file part. This parameter takes effect only if the parallel upload feature is enabled.
        self.parallel_sha_1ctx = parallel_sha_1ctx
        self.parallel_sha_256ctx = parallel_sha_256ctx
        # The serial number of a part.
        self.part_number = part_number

    def validate(self):
        if self.parallel_sha_1ctx:
            self.parallel_sha_1ctx.validate()
        if self.parallel_sha_256ctx:
            self.parallel_sha_256ctx.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.parallel_sha_1ctx is not None:
            result['parallel_sha1_ctx'] = self.parallel_sha_1ctx.to_map()
        if self.parallel_sha_256ctx is not None:
            result['parallel_sha256_ctx'] = self.parallel_sha_256ctx.to_map()
        if self.part_number is not None:
            result['part_number'] = self.part_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
        if m.get('content_type') is not None:
            self.content_type = m.get('content_type')
        if m.get('parallel_sha1_ctx') is not None:
            temp_model = GetUploadUrlRequestPartInfoListParallelSha1Ctx()
            self.parallel_sha_1ctx = temp_model.from_map(m['parallel_sha1_ctx'])
        if m.get('parallel_sha256_ctx') is not None:
            temp_model = GetUploadUrlRequestPartInfoListParallelSha256Ctx()
            self.parallel_sha_256ctx = temp_model.from_map(m['parallel_sha256_ctx'])
        if m.get('part_number') is not None:
            self.part_number = m.get('part_number')
        return self


class GetUploadUrlRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        part_info_list: List[GetUploadUrlRequestPartInfoList] = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The information about the file parts.
        # 
        # This parameter is required.
        self.part_info_list = part_info_list
        # The share ID.
        self.share_id = share_id
        # The ID of the upload task.
        # 
        # This parameter is required.
        self.upload_id = upload_id

    def validate(self):
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = GetUploadUrlRequestPartInfoList()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class GetUploadUrlResponseBody(TeaModel):
    def __init__(
        self,
        create_at: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
        part_info_list: List[UploadPartInfo] = None,
        upload_id: str = None,
    ):
        # The time when the upload task was created.
        self.create_at = create_at
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        self.file_id = file_id
        # The information about the file parts.
        self.part_info_list = part_info_list
        # The ID of the upload task.
        self.upload_id = upload_id

    def validate(self):
        if self.part_info_list:
            for k in self.part_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_at is not None:
            result['create_at'] = self.create_at
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('create_at') is not None:
            self.create_at = m.get('create_at')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class GetUploadUrlResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetUploadUrlResponseBody = None,
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
            temp_model = GetUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
        # The user ID. If you use an AccessKey pair to access Drive and Photo Service, you must specify this parameter. If you use an access token to access Drive and Photo Service, you do not need to specify this parameter, and Drive and Photo Service automatically finds the user ID contained in the access token.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class GetUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: User = None,
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
            temp_model = User()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoPreviewPlayInfoRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        drive_id: str = None,
        file_id: str = None,
        get_master_url: bool = None,
        get_without_url: bool = None,
        re_transcode: bool = None,
        share_id: str = None,
        template_id: str = None,
        url_expire_sec: int = None,
    ):
        # The preview type. You must enable the corresponding video transcoding feature. Valid values:
        # 
        # *   live_transcoding: previews a live stream while transcoding is in progress.
        # *   quick_video: previews a video while transcoding is in progress.
        # *   offline_audio: previews a piece of audio after the audio is transcoded offline.
        # *   offline_video: previews a video after the video is transcoded offline.
        # 
        # This parameter is required.
        self.category = category
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        self.get_master_url = get_master_url
        # Specifies whether not to query the playback URL. If you set this parameter to true, only transcoding metadata is returned. The video is not transcoded in the TS format, and the playback URL is not returned. If you set this parameter to false, the playback URL is returned. If the video has not been transcoded by using the template specified by template_id, the transcoding process is triggered. You are charged for the value-added service fees generated for transcoding.
        self.get_without_url = get_without_url
        self.re_transcode = re_transcode
        # The share ID. If you want to manage a file by using a sharing link, carry the `x-share-token` header in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify at least either `share_id` or `drive_id`.
        self.share_id = share_id
        # The ID of the definition template. If you leave this parameter empty, all definition templates are available.
        self.template_id = template_id
        # The validity period of the video preview. Unit: seconds. Default value: 900. Maximum value: 14400.
        self.url_expire_sec = url_expire_sec

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.get_master_url is not None:
            result['get_master_url'] = self.get_master_url
        if self.get_without_url is not None:
            result['get_without_url'] = self.get_without_url
        if self.re_transcode is not None:
            result['re_transcode'] = self.re_transcode
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.template_id is not None:
            result['template_id'] = self.template_id
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('get_master_url') is not None:
            self.get_master_url = m.get('get_master_url')
        if m.get('get_without_url') is not None:
            self.get_without_url = m.get('get_without_url')
        if m.get('re_transcode') is not None:
            self.re_transcode = m.get('re_transcode')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        return self


class GetVideoPreviewPlayInfoResponseBody(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
        share_id: str = None,
        video_preview_play_info: VideoPreviewPlayInfo = None,
    ):
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        self.file_id = file_id
        # The share ID.
        self.share_id = share_id
        # The information about video playback.
        self.video_preview_play_info = video_preview_play_info

    def validate(self):
        if self.video_preview_play_info:
            self.video_preview_play_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.video_preview_play_info is not None:
            result['video_preview_play_info'] = self.video_preview_play_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('video_preview_play_info') is not None:
            temp_model = VideoPreviewPlayInfo()
            self.video_preview_play_info = temp_model.from_map(m['video_preview_play_info'])
        return self


class GetVideoPreviewPlayInfoResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVideoPreviewPlayInfoResponseBody = None,
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
            temp_model = GetVideoPreviewPlayInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoPreviewPlayMetaRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        drive_id: str = None,
        file_id: str = None,
        share_id: str = None,
    ):
        # The preview type. You must enable the corresponding video transcoding feature. Valid values:
        # 
        # *   live_transcoding: previews a live stream while transcoding is in progress.
        # *   quick_video: previews a video while transcoding is in progress.
        # *   offline_audio: previews a piece of audio after the audio is transcoded offline.
        # *   offline_video: previews a video after the video is transcoded offline.
        # 
        # This parameter is required.
        self.category = category
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The share ID. If you want to manage a file by using a sharing link, carry the `x-share-token` header in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify at least either `share_id` or `drive_id`.
        self.share_id = share_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        return self


class GetVideoPreviewPlayMetaResponseBody(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
        share_id: str = None,
        video_preview_play_meta: VideoPreviewPlayMeta = None,
    ):
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # The file ID.
        self.file_id = file_id
        # The share ID.
        self.share_id = share_id
        # The preview metadata of the video.
        self.video_preview_play_meta = video_preview_play_meta

    def validate(self):
        if self.video_preview_play_meta:
            self.video_preview_play_meta.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.video_preview_play_meta is not None:
            result['video_preview_play_meta'] = self.video_preview_play_meta.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('video_preview_play_meta') is not None:
            temp_model = VideoPreviewPlayMeta()
            self.video_preview_play_meta = temp_model.from_map(m['video_preview_play_meta'])
        return self


class GetVideoPreviewPlayMetaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: GetVideoPreviewPlayMetaResponseBody = None,
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
            temp_model = GetVideoPreviewPlayMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GroupUpdateNameRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        name: str = None,
    ):
        # This parameter is required.
        self.group_id = group_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.name is not None:
            result['name'] = self.name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('name') is not None:
            self.name = m.get('name')
        return self


class GroupUpdateNameResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class ImportUserRequest(TeaModel):
    def __init__(
        self,
        authentication_display_name: str = None,
        authentication_type: str = None,
        auto_create_drive: bool = None,
        drive_total_size: int = None,
        extra: str = None,
        identity: str = None,
        nick_name: str = None,
        parent_group_id: str = None,
    ):
        # The display name of the authentication type.
        self.authentication_display_name = authentication_display_name
        # The authentication type. Valid values:
        # 
        # *   mobile: mobile number.
        # *   email: email address.
        # *   ding: DingTalk account.
        # *   ram: Alibaba Cloud Resource Access Management (RAM) user.
        # *   wechat: WeCom account.
        # *   ldap: Lightweight Directory Access Protocol (LDAP) account.
        # *   custom: custom account.
        # 
        # This parameter is required.
        self.authentication_type = authentication_type
        # Specifies whether to automatically create a drive.
        self.auto_create_drive = auto_create_drive
        # The size of the drive. The value cannot be smaller than -1. A value of -1 specifies that the size is unlimited.
        self.drive_total_size = drive_total_size
        # The additional information.
        # 
        # If authentication_type is set to mobile, set this parameter to a country code. If you do not specify this parameter, 86 is used by default.
        self.extra = extra
        # The unique identifier.
        # 
        # This parameter is required.
        self.identity = identity
        # The nickname of the user.
        # 
        # This parameter is required.
        self.nick_name = nick_name
        # The ID of the group to which the user is added.
        self.parent_group_id = parent_group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authentication_display_name is not None:
            result['authentication_display_name'] = self.authentication_display_name
        if self.authentication_type is not None:
            result['authentication_type'] = self.authentication_type
        if self.auto_create_drive is not None:
            result['auto_create_drive'] = self.auto_create_drive
        if self.drive_total_size is not None:
            result['drive_total_size'] = self.drive_total_size
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.parent_group_id is not None:
            result['parent_group_id'] = self.parent_group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('authentication_display_name') is not None:
            self.authentication_display_name = m.get('authentication_display_name')
        if m.get('authentication_type') is not None:
            self.authentication_type = m.get('authentication_type')
        if m.get('auto_create_drive') is not None:
            self.auto_create_drive = m.get('auto_create_drive')
        if m.get('drive_total_size') is not None:
            self.drive_total_size = m.get('drive_total_size')
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('parent_group_id') is not None:
            self.parent_group_id = m.get('parent_group_id')
        return self


class ImportUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: User = None,
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
            temp_model = User()
            self.body = temp_model.from_map(m['body'])
        return self


class InvestigateFileRequestDriveFileIds(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class InvestigateFileRequest(TeaModel):
    def __init__(
        self,
        drive_file_ids: List[InvestigateFileRequestDriveFileIds] = None,
    ):
        # This parameter is required.
        self.drive_file_ids = drive_file_ids

    def validate(self):
        if self.drive_file_ids:
            for k in self.drive_file_ids:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['drive_file_ids'] = []
        if self.drive_file_ids is not None:
            for k in self.drive_file_ids:
                result['drive_file_ids'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.drive_file_ids = []
        if m.get('drive_file_ids') is not None:
            for k in m.get('drive_file_ids'):
                temp_model = InvestigateFileRequestDriveFileIds()
                self.drive_file_ids.append(temp_model.from_map(k))
        return self


class InvestigateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class LinkAccountRequest(TeaModel):
    def __init__(
        self,
        extra: str = None,
        identity: str = None,
        type: str = None,
        user_id: str = None,
    ):
        # The additional information about the unique identifier of the account. For example, if type is set to mobile, set the value of extra to a country code. For example, a value of 86 specifies a mobile number in the Chinese mainland. If you do not specify this parameter, 86 is used by default.
        self.extra = extra
        # The unique identifier of the account, such as a mobile number.
        # 
        # This parameter is required.
        self.identity = identity
        # The account type. Valid values:
        # 
        # *   mobile: a mobile number.
        # *   email: an email address.
        # *   ding: a DingTalk account.
        # *   ram: an Alibaba Cloud Resource Access Management (RAM) user.
        # *   wechat: a WeCom account.
        # *   ldap: a Lightweight Directory Access Protocol (LDAP) account.
        # *   custom: a custom account.
        # 
        # This parameter is required.
        self.type = type
        # The ID of the user with which you want to associate an account.
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class LinkAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Token = None,
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
            temp_model = Token()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAddressGroupsRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        limit: int = None,
        marker: str = None,
        video_thumbnail_process: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The method that is used to generate a thumbnail of an image.
        self.image_thumbnail_process = image_thumbnail_process
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is left empty.
        self.marker = marker
        # The method that is used to generate a thumbnail of a video.
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class ListAddressGroupsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[AddressGroup] = None,
        next_marker: str = None,
    ):
        # The information about the location-based groups.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = AddressGroup()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListAddressGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAddressGroupsResponseBody = None,
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
            temp_model = ListAddressGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListAssignmentRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        manage_resource_id: str = None,
        manage_resource_type: str = None,
        marker: str = None,
    ):
        # The maximum number of results to return. Valid values: 1 to 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The ID of the managed resource, such as a group ID.
        # 
        # This parameter is required.
        self.manage_resource_id = manage_resource_id
        # The type of the managed resource. Set the value to RT_Group, which specifies that the administrators of a group are queried.
        # 
        # This parameter is required.
        self.manage_resource_type = manage_resource_type
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.manage_resource_id is not None:
            result['manage_resource_id'] = self.manage_resource_id
        if self.manage_resource_type is not None:
            result['manage_resource_type'] = self.manage_resource_type
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('manage_resource_id') is not None:
            self.manage_resource_id = m.get('manage_resource_id')
        if m.get('manage_resource_type') is not None:
            self.manage_resource_type = m.get('manage_resource_type')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListAssignmentResponseBodyAssignmentList(TeaModel):
    def __init__(
        self,
        created_at: int = None,
        creator: str = None,
        domain_id: str = None,
        identity: Identity = None,
        manage_resource_id: str = None,
        manage_resource_type: str = None,
        role_id: str = None,
    ):
        # The time when the role was assigned. This value is a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        self.created_at = created_at
        # The ID of the user who assigned the role.
        self.creator = creator
        # The domain ID.
        self.domain_id = domain_id
        # The identity to whom the role is assigned, which is a user or a group.
        self.identity = identity
        # The ID of the managed resource, such as a group ID.
        self.manage_resource_id = manage_resource_id
        # The type of the managed resource. For example, a value of RT_Group indicates group.
        self.manage_resource_type = manage_resource_type
        # The ID of the role assigned to the identity.
        self.role_id = role_id

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.created_at is not None:
            result['created_at'] = self.created_at
        if self.creator is not None:
            result['creator'] = self.creator
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.identity is not None:
            result['identity'] = self.identity.to_map()
        if self.manage_resource_id is not None:
            result['manage_resource_id'] = self.manage_resource_id
        if self.manage_resource_type is not None:
            result['manage_resource_type'] = self.manage_resource_type
        if self.role_id is not None:
            result['role_id'] = self.role_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created_at') is not None:
            self.created_at = m.get('created_at')
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('identity') is not None:
            temp_model = Identity()
            self.identity = temp_model.from_map(m['identity'])
        if m.get('manage_resource_id') is not None:
            self.manage_resource_id = m.get('manage_resource_id')
        if m.get('manage_resource_type') is not None:
            self.manage_resource_type = m.get('manage_resource_type')
        if m.get('role_id') is not None:
            self.role_id = m.get('role_id')
        return self


class ListAssignmentResponseBody(TeaModel):
    def __init__(
        self,
        assignment_list: List[ListAssignmentResponseBodyAssignmentList] = None,
        next_marker: str = None,
    ):
        # The assigned roles.
        self.assignment_list = assignment_list
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.assignment_list:
            for k in self.assignment_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['assignment_list'] = []
        if self.assignment_list is not None:
            for k in self.assignment_list:
                result['assignment_list'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assignment_list = []
        if m.get('assignment_list') is not None:
            for k in m.get('assignment_list'):
                temp_model = ListAssignmentResponseBodyAssignmentList()
                self.assignment_list.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListAssignmentResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListAssignmentResponseBody = None,
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
            temp_model = ListAssignmentResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDeltaRequest(TeaModel):
    def __init__(
        self,
        cursor: str = None,
        drive_id: str = None,
        limit: int = None,
        sync_root_id: str = None,
    ):
        # The cursor of the incremental information.
        self.cursor = cursor
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The maximum number of results to return. Valid values: 0 to 100. Default value: 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The ID of the root file of the synced folder.
        self.sync_root_id = sync_root_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.sync_root_id is not None:
            result['sync_root_id'] = self.sync_root_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('sync_root_id') is not None:
            self.sync_root_id = m.get('sync_root_id')
        return self


class ListDeltaResponseBodyItems(TeaModel):
    def __init__(
        self,
        file: File = None,
        file_id: str = None,
        op: str = None,
    ):
        # The information about the file.
        self.file = file
        # The file ID.
        self.file_id = file_id
        # The operation that is performed. Valid values: Valid values:
        # 
        # *   create
        # *   overwrite
        # *   delete
        # *   update
        # *   move
        # *   trash
        # *   restore
        # *   rename
        self.op = op

    def validate(self):
        if self.file:
            self.file.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file is not None:
            result['file'] = self.file.to_map()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.op is not None:
            result['op'] = self.op
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file') is not None:
            temp_model = File()
            self.file = temp_model.from_map(m['file'])
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('op') is not None:
            self.op = m.get('op')
        return self


class ListDeltaResponseBody(TeaModel):
    def __init__(
        self,
        cursor: str = None,
        has_more: bool = None,
        items: List[ListDeltaResponseBodyItems] = None,
    ):
        # The cursor of the incremental information.
        self.cursor = cursor
        # Indicates whether more information is returned.
        self.has_more = has_more
        # The incremental information returned.
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cursor is not None:
            result['cursor'] = self.cursor
        if self.has_more is not None:
            result['has_more'] = self.has_more
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cursor') is not None:
            self.cursor = m.get('cursor')
        if m.get('has_more') is not None:
            self.has_more = m.get('has_more')
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ListDeltaResponseBodyItems()
                self.items.append(temp_model.from_map(k))
        return self


class ListDeltaResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDeltaResponseBody = None,
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
            temp_model = ListDeltaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
        parent_domain_id: str = None,
        service_code: str = None,
    ):
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 50.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.
        self.marker = marker
        # The ID of the parent domain.
        self.parent_domain_id = parent_domain_id
        self.service_code = service_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.parent_domain_id is not None:
            result['parent_domain_id'] = self.parent_domain_id
        if self.service_code is not None:
            result['service_code'] = self.service_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('parent_domain_id') is not None:
            self.parent_domain_id = m.get('parent_domain_id')
        if m.get('service_code') is not None:
            self.service_code = m.get('service_code')
        return self


class ListDomainsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[Domain] = None,
        next_marker: str = None,
    ):
        # The information about the domains.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Domain()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDomainsResponseBody = None,
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
            temp_model = ListDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDriveRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
        owner: str = None,
        owner_type: str = None,
    ):
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is empty.
        self.marker = marker
        # The owner of the drive. If this parameter is not specified, all drives are returned.
        self.owner = owner
        # The type of the owner. Valid values:
        # 
        # user and group.
        # 
        # By default, drives of all owner types are returned.
        self.owner_type = owner_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        return self


class ListDriveResponseBody(TeaModel):
    def __init__(
        self,
        items: List[Drive] = None,
        next_marker: str = None,
    ):
        # The queried drives.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Drive()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListDriveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListDriveResponseBody = None,
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
            temp_model = ListDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFacegroupsRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        limit: int = None,
        marker: str = None,
        remarks: str = None,
        return_total_count: bool = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is left empty.
        self.marker = marker
        # The filter condition that is used to query groups. The value can be up to 128 characters in length. An exact match is used.
        self.remarks = remarks
        self.return_total_count = return_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.remarks is not None:
            result['remarks'] = self.remarks
        if self.return_total_count is not None:
            result['return_total_count'] = self.return_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        if m.get('return_total_count') is not None:
            self.return_total_count = m.get('return_total_count')
        return self


class ListFacegroupsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[FaceGroup] = None,
        next_marker: str = None,
        total_count: int = None,
    ):
        # The information about the face-based groups.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = FaceGroup()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class ListFacegroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFacegroupsResponseBody = None,
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
            temp_model = ListFacegroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListFileRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        drive_id: str = None,
        fields: str = None,
        limit: int = None,
        marker: str = None,
        order_by: str = None,
        order_direction: str = None,
        parent_file_id: str = None,
        share_id: str = None,
        status: str = None,
        thumbnail_processes: Dict[str, ImageProcess] = None,
        type: str = None,
    ):
        # The category of the file. Valid values:
        # 
        # app: installation package. zip: compressed package. image: image. doc: document. video: video. audio: audio. others: other files.
        # 
        # By default, files of all categories are returned.
        self.category = category
        # The drive ID.
        self.drive_id = drive_id
        # The fields to return.
        # 
        # 1.  If this parameter is set to \\*, all fields of the file except the fields that must be specified are returned.
        # 2.  If only specific fields are required, you can specify the following fields: url, exif, cropping_suggestion, characteristic_hash, video_metadata, and video_preview_metadata. If multiple fields are required, separate them with commas (,). Example: url,exif.
        # 3.  The investigation_info field is returned only if you specify this field.
        # 
        # By default, all fields except the fields that must be specified are returned.
        self.fields = fields
        # The maximum number of results to return. Valid values: 1 to 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is empty.
        self.marker = marker
        # The sorting field.
        # 
        # Default value: created_at.
        # 
        # Valid values:
        # 
        # *   updated_at
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     sorts the results based on the time when the file was last modified
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   size
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     sorts the results based on the size of the file
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   name
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     sorts the results based on the name of the file
        # 
        #     <!-- -->
        # 
        #     .
        # 
        # *   created_at
        # 
        #     <!-- -->
        # 
        #     :
        # 
        #     <!-- -->
        # 
        #     sorts the results based on the time when the file was created
        # 
        #     <!-- -->
        # 
        #     .
        self.order_by = order_by
        # The sorting direction. Valid values:
        # 
        # ASC: ascending order. DESC: descending order.
        # 
        # Default value: ASC.
        self.order_direction = order_direction
        # The ID of the parent folder. If the parent folder is a root directory, set this parameter to root.
        # 
        # This parameter is required.
        self.parent_file_id = parent_file_id
        # The share ID. If you want to manage a file by using a share link, carry the `x-share-token` header for authentication in the request and specify share_id. In this case, `drive_id` is invalid. Otherwise, use an `AccessKey pair` or `access token` for authentication and specify `drive_id`. You must specify one of `share_id` and `drive_id`.
        self.share_id = share_id
        # The state of the file. Valid values:
        # 
        # available: Only normal files are returned. uploading: Only files that are being uploaded are returned.
        # 
        # By default, only files in the available state are returned.
        self.status = status
        # The thumbnail configurations. Up to five thumbnails can be returned at a time. The value contains key-value pairs. You can customize the keys. The URL of a thumbnail is returned based on the key.
        self.thumbnail_processes = thumbnail_processes
        # The type of the file. Valid values:
        # 
        # file: Only files are returned. folder: Only folders are returned.
        # 
        # By default, files of all types are returned.
        self.type = type

    def validate(self):
        if self.thumbnail_processes:
            for v in self.thumbnail_processes.values():
                if v:
                    v.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.category is not None:
            result['category'] = self.category
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.order_direction is not None:
            result['order_direction'] = self.order_direction
        if self.parent_file_id is not None:
            result['parent_file_id'] = self.parent_file_id
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.status is not None:
            result['status'] = self.status
        result['thumbnail_processes'] = {}
        if self.thumbnail_processes is not None:
            for k, v in self.thumbnail_processes.items():
                result['thumbnail_processes'][k] = v.to_map()
        if self.type is not None:
            result['type'] = self.type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('category') is not None:
            self.category = m.get('category')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')
        if m.get('parent_file_id') is not None:
            self.parent_file_id = m.get('parent_file_id')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('status') is not None:
            self.status = m.get('status')
        self.thumbnail_processes = {}
        if m.get('thumbnail_processes') is not None:
            for k, v in m.get('thumbnail_processes').items():
                temp_model = ImageProcess()
                self.thumbnail_processes[k] = temp_model.from_map(v)
        if m.get('type') is not None:
            self.type = m.get('type')
        return self


class ListFileResponseBody(TeaModel):
    def __init__(
        self,
        items: List[File] = None,
        next_marker: str = None,
    ):
        # The queried files.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = File()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListFileResponseBody = None,
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
            temp_model = ListFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is left empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListGroupResponseBody(TeaModel):
    def __init__(
        self,
        items: List[Group] = None,
        next_marker: str = None,
    ):
        # The information about the groups.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Group()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupResponseBody = None,
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
            temp_model = ListGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupMemberRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        limit: int = None,
        marker: str = None,
        member_type: str = None,
    ):
        # The ID of the group of which you want to query members.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The member type. If you do not specify this parameter, both types of members are returned. Valid values:
        # 
        # *   user
        # *   group
        # 
        # Note: A group can be a member of only one group. It cannot be a member of multiple groups. A user can be a member of multiple groups.
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.member_type is not None:
            result['member_type'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        return self


class ListGroupMemberResponseBody(TeaModel):
    def __init__(
        self,
        group_items: List[Group] = None,
        next_marker: str = None,
        user_items: List[User] = None,
    ):
        # The information about the groups.
        self.group_items = group_items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker
        # The information about the users.
        self.user_items = user_items

    def validate(self):
        if self.group_items:
            for k in self.group_items:
                if k:
                    k.validate()
        if self.user_items:
            for k in self.user_items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['group_items'] = []
        if self.group_items is not None:
            for k in self.group_items:
                result['group_items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        result['user_items'] = []
        if self.user_items is not None:
            for k in self.user_items:
                result['user_items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.group_items = []
        if m.get('group_items') is not None:
            for k in m.get('group_items'):
                temp_model = Group()
                self.group_items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        self.user_items = []
        if m.get('user_items') is not None:
            for k in m.get('user_items'):
                temp_model = User()
                self.user_items.append(temp_model.from_map(k))
        return self


class ListGroupMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListGroupMemberResponseBody = None,
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
            temp_model = ListGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIdentityRoleRequest(TeaModel):
    def __init__(
        self,
        identity: Identity = None,
    ):
        # This parameter is required.
        self.identity = identity

    def validate(self):
        if self.identity:
            self.identity.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity is not None:
            result['identity'] = self.identity.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identity') is not None:
            temp_model = Identity()
            self.identity = temp_model.from_map(m['identity'])
        return self


class ListIdentityRoleResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: BaseRoleMemberResponse = None,
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
            temp_model = BaseRoleMemberResponse()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIdentityToBenefitPkgMappingRequest(TeaModel):
    def __init__(
        self,
        identity_id: str = None,
        identity_type: str = None,
        include_expired: bool = None,
    ):
        # The unique identifier of the entity.
        # 
        # If you call this operation to manage the benefits of a user, set this parameter to the ID of the user.
        # 
        # This parameter is required.
        self.identity_id = identity_id
        # The type of the entity. If you call this operation to manage the benefits of a user, set this parameter to user.
        # 
        # This parameter is required.
        self.identity_type = identity_type
        # Specifies whether to return the benefit packages that expire. Default value: false.
        self.include_expired = include_expired

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.identity_id is not None:
            result['identity_id'] = self.identity_id
        if self.identity_type is not None:
            result['identity_type'] = self.identity_type
        if self.include_expired is not None:
            result['include_expired'] = self.include_expired
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')
        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')
        if m.get('include_expired') is not None:
            self.include_expired = m.get('include_expired')
        return self


class ListIdentityToBenefitPkgMappingResponseBody(TeaModel):
    def __init__(
        self,
        items: List[IdentityToBenefitPkgMapping] = None,
    ):
        # The information about the benefit packages that are associated with an entity.
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = IdentityToBenefitPkgMapping()
                self.items.append(temp_model.from_map(k))
        return self


class ListIdentityToBenefitPkgMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListIdentityToBenefitPkgMappingResponseBody = None,
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
            temp_model = ListIdentityToBenefitPkgMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMyDrivesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        # The maximum number of results to return. Default value: 100. Valid values: 1 to 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListMyDrivesResponseBody(TeaModel):
    def __init__(
        self,
        items: List[Drive] = None,
        next_marker: str = None,
    ):
        # The queried drives.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Drive()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListMyDrivesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMyDrivesResponseBody = None,
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
            temp_model = ListMyDrivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMyGroupDriveRequest(TeaModel):
    def __init__(
        self,
        drive_name: str = None,
        limit: int = None,
        marker: str = None,
    ):
        self.drive_name = drive_name
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is left empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListMyGroupDriveResponseBody(TeaModel):
    def __init__(
        self,
        items: List[Drive] = None,
        next_marker: str = None,
        root_group_drive: Drive = None,
    ):
        # The information about the team drives.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker
        self.root_group_drive = root_group_drive

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()
        if self.root_group_drive:
            self.root_group_drive.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        if self.root_group_drive is not None:
            result['root_group_drive'] = self.root_group_drive.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Drive()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        if m.get('root_group_drive') is not None:
            temp_model = Drive()
            self.root_group_drive = temp_model.from_map(m['root_group_drive'])
        return self


class ListMyGroupDriveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListMyGroupDriveResponseBody = None,
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
            temp_model = ListMyGroupDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListReceivedFileRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListReceivedFileResponseBody(TeaModel):
    def __init__(
        self,
        items: List[File] = None,
        next_marker: str = None,
    ):
        # The queried files.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = File()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListReceivedFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListReceivedFileResponseBody = None,
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
            temp_model = ListReceivedFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRecyclebinRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        limit: int = None,
        marker: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # Specifies the returned fields.
        # 
        # 1\\. If you set this parameter to \\*, all fields of the file are returned.
        # 
        # 2\\. If you set this parameter to a null value or leave this parameter empty, the fields, such as file creator, file modifier, and custom tags, are not returned.
        # 
        # The default value is a null value, which indicates that only some fields are returned.
        self.fields = fields
        # The maximum number of results to return. Valid values: 1 to 200. Default value: 50.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is left empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListRecyclebinResponseBody(TeaModel):
    def __init__(
        self,
        items: List[File] = None,
        next_marker: str = None,
    ):
        # The information about the files and folders in the recycle bin.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = File()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListRecyclebinResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRecyclebinResponseBody = None,
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
            temp_model = ListRecyclebinResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListRevisionRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        file_id: str = None,
        limit: int = None,
        marker: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # Specifies the returned fields.
        # 
        # By default, this parameter is left empty. If you set this parameter to \\*, all fields are returned. If you leave this parameter empty, the creator of the file is not returned.
        self.fields = fields
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The maximum number of results to return. Valid values: 1 to 100.
        # 
        # Default value: 50.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.
        # 
        # By default, this parameter is left empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListRevisionResponseBody(TeaModel):
    def __init__(
        self,
        items: List[Revision] = None,
        next_marker: str = None,
    ):
        # The information about the versions.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Revision()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListRevisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListRevisionResponseBody = None,
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
            temp_model = ListRevisionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListShareLinkRequest(TeaModel):
    def __init__(
        self,
        creator: str = None,
        include_cancelled: bool = None,
        limit: int = None,
        marker: str = None,
        order_by: str = None,
        order_direction: str = None,
    ):
        # The creator of the share.
        self.creator = creator
        # Specifies whether to return the shares that are canceled.
        self.include_cancelled = include_cancelled
        # The maximum number of results to return. Valid values: 0 to 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The field by which to sort the returned results. Default value: created_at. Valid values:
        # 
        # *   share_name: sorts the results by the name of the share.
        # *   updated_at: sorts the results by the time when the share was modified.
        # *   description: sorts the results by the description of the share.
        # *   created_at: sorts the results by the time when the share was created.
        self.order_by = order_by
        # The order in which you want to sort the returned results. By default, order_direction is set to DESC if order_by is set to created_at or updated_at, and is set to ASC if order_by is set to other values. Valid values:
        # 
        # *   ASC: sorts the results in ascending order.
        # *   DESC: sorts the results in descending order.
        self.order_direction = order_direction

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creator is not None:
            result['creator'] = self.creator
        if self.include_cancelled is not None:
            result['include_cancelled'] = self.include_cancelled
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.order_direction is not None:
            result['order_direction'] = self.order_direction
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')
        if m.get('include_cancelled') is not None:
            self.include_cancelled = m.get('include_cancelled')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')
        return self


class ListShareLinkResponseBody(TeaModel):
    def __init__(
        self,
        items: List[ShareLink] = None,
        next_marker: str = None,
    ):
        # The information about the shares.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ShareLink()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListShareLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListShareLinkResponseBody = None,
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
            temp_model = ListShareLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagsRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        video_thumbnail_process: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The method that is used to generate the thumbnail of an image.
        self.image_thumbnail_process = image_thumbnail_process
        # The method that is used to generate the thumbnail of a video.
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class ListTagsResponseBody(TeaModel):
    def __init__(
        self,
        tags: List[ImageTag] = None,
    ):
        # The information about the tags.
        self.tags = tags

    def validate(self):
        if self.tags:
            for k in self.tags:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['tags'] = []
        if self.tags is not None:
            for k in self.tags:
                result['tags'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.tags = []
        if m.get('tags') is not None:
            for k in m.get('tags'):
                temp_model = ImageTag()
                self.tags.append(temp_model.from_map(k))
        return self


class ListTagsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListTagsResponseBody = None,
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
            temp_model = ListTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUploadedPartsRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        limit: int = None,
        part_number_marker: int = None,
        share_id: str = None,
        upload_id: str = None,
    ):
        # The drive ID. This parameter is required if the file is not uploaded by using the share URL of the file.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is left empty.
        self.part_number_marker = part_number_marker
        # The share ID. This parameter is required if the file is uploaded by using the share URL of the file.
        self.share_id = share_id
        # The ID of the upload task.
        # 
        # This parameter is required.
        self.upload_id = upload_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.limit is not None:
            result['limit'] = self.limit
        if self.part_number_marker is not None:
            result['part_number_marker'] = self.part_number_marker
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('part_number_marker') is not None:
            self.part_number_marker = m.get('part_number_marker')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        return self


class ListUploadedPartsResponseBody(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        next_part_number_marker: str = None,
        parallel_upload: bool = None,
        upload_id: str = None,
        uploaded_parts: List[UploadPartInfo] = None,
    ):
        # The file ID.
        self.file_id = file_id
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_part_number_marker = next_part_number_marker
        # Indicates whether the parallel upload feature is enabled.
        self.parallel_upload = parallel_upload
        # The ID of the upload task.
        self.upload_id = upload_id
        # The information about the file parts.
        self.uploaded_parts = uploaded_parts

    def validate(self):
        if self.uploaded_parts:
            for k in self.uploaded_parts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.next_part_number_marker is not None:
            result['next_part_number_marker'] = self.next_part_number_marker
        if self.parallel_upload is not None:
            result['parallel_upload'] = self.parallel_upload
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        result['uploaded_parts'] = []
        if self.uploaded_parts is not None:
            for k in self.uploaded_parts:
                result['uploaded_parts'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('next_part_number_marker') is not None:
            self.next_part_number_marker = m.get('next_part_number_marker')
        if m.get('parallel_upload') is not None:
            self.parallel_upload = m.get('parallel_upload')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
        self.uploaded_parts = []
        if m.get('uploaded_parts') is not None:
            for k in m.get('uploaded_parts'):
                temp_model = UploadPartInfo()
                self.uploaded_parts.append(temp_model.from_map(k))
        return self


class ListUploadedPartsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUploadedPartsResponseBody = None,
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
            temp_model = ListUploadedPartsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker. By default, this parameter is left empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ListUserResponseBody(TeaModel):
    def __init__(
        self,
        items: List[User] = None,
        next_marker: str = None,
    ):
        # The information about the users.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = User()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ListUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ListUserResponseBody = None,
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
            temp_model = ListUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveFileRequest(TeaModel):
    def __init__(
        self,
        check_name_mode: str = None,
        drive_id: str = None,
        file_id: str = None,
        to_parent_file_id: str = None,
    ):
        # The processing method that is used if the file that you want to move has the same name as an existing file in the destination directory. Valid values:
        # 
        # ignore: allows you to move the file by using the same name as an existing file in the destination directory.
        # 
        # auto_rename: automatically renames the file that has the same name exists in the destination directory. By default, the current point in time is added to the end of the file name. Example: xxx_20060102_150405.
        # 
        # refuse: does not move the file that you want to move but returns the information about the file that has the same name in the destination directory.
        # 
        # Default value: ignore.
        self.check_name_mode = check_name_mode
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The ID of the destination parent directory to which you want to move a file or folder. If you want to move a file or folder to the root directory, set this parameter to root.
        # 
        # This parameter is required.
        self.to_parent_file_id = to_parent_file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name_mode is not None:
            result['check_name_mode'] = self.check_name_mode
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.to_parent_file_id is not None:
            result['to_parent_file_id'] = self.to_parent_file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_name_mode') is not None:
            self.check_name_mode = m.get('check_name_mode')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('to_parent_file_id') is not None:
            self.to_parent_file_id = m.get('to_parent_file_id')
        return self


class MoveFileResponseBody(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        exist: bool = None,
        file_id: str = None,
    ):
        # The ID of the asynchronous task.
        # 
        # If an empty string is returned, the file is moved.
        # 
        # If a non-empty string is returned, an asynchronous task is required. You can call the GetAsyncTask operation to obtain the information about an asynchronous task based on the task ID.
        self.async_task_id = async_task_id
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # Indicates whether the file already exists in the destination directory.
        self.exist = exist
        # The file ID.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.exist is not None:
            result['exist'] = self.exist
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('exist') is not None:
            self.exist = m.get('exist')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class MoveFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: MoveFileResponseBody = None,
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
            temp_model = MoveFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class QueryOrderPriceRequest(TeaModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        order_type: str = None,
        package: str = None,
        period: int = None,
        period_unit: str = None,
        total_size: int = None,
        user_count: int = None,
    ):
        # This parameter is required.
        self.code = code
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.order_type = order_type
        # This parameter is required.
        self.package = package
        # This parameter is required.
        self.period = period
        # This parameter is required.
        self.period_unit = period_unit
        # This parameter is required.
        self.total_size = total_size
        # This parameter is required.
        self.user_count = user_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.instance_id is not None:
            result['instance_id'] = self.instance_id
        if self.order_type is not None:
            result['order_type'] = self.order_type
        if self.package is not None:
            result['package'] = self.package
        if self.period is not None:
            result['period'] = self.period
        if self.period_unit is not None:
            result['period_unit'] = self.period_unit
        if self.total_size is not None:
            result['total_size'] = self.total_size
        if self.user_count is not None:
            result['user_count'] = self.user_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('instance_id') is not None:
            self.instance_id = m.get('instance_id')
        if m.get('order_type') is not None:
            self.order_type = m.get('order_type')
        if m.get('package') is not None:
            self.package = m.get('package')
        if m.get('period') is not None:
            self.period = m.get('period')
        if m.get('period_unit') is not None:
            self.period_unit = m.get('period_unit')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        if m.get('user_count') is not None:
            self.user_count = m.get('user_count')
        return self


class QueryOrderPriceResponseBody(TeaModel):
    def __init__(
        self,
        discount_price: float = None,
        original_price: float = None,
        trade_price: float = None,
    ):
        self.discount_price = discount_price
        self.original_price = original_price
        self.trade_price = trade_price

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.discount_price is not None:
            result['discount_price'] = self.discount_price
        if self.original_price is not None:
            result['original_price'] = self.original_price
        if self.trade_price is not None:
            result['trade_price'] = self.trade_price
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('discount_price') is not None:
            self.discount_price = m.get('discount_price')
        if m.get('original_price') is not None:
            self.original_price = m.get('original_price')
        if m.get('trade_price') is not None:
            self.trade_price = m.get('trade_price')
        return self


class QueryOrderPriceResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: QueryOrderPriceResponseBody = None,
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
            temp_model = QueryOrderPriceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFaceGroupFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        face_group_id: str = None,
        file_id: str = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.face_group_id = face_group_id
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.face_group_id is not None:
            result['face_group_id'] = self.face_group_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('face_group_id') is not None:
            self.face_group_id = m.get('face_group_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class RemoveFaceGroupFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class RemoveGroupMemberRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        member_id: str = None,
        member_type: str = None,
    ):
        # The ID of the group from which you want to remove a member.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The ID of the member. If member_type is set to user, set this parameter to the ID of the corresponding user.
        # 
        # This parameter is required.
        self.member_id = member_id
        # The type of the member that you want to remove from the group. Only common users can be removed. If you want to remove all members from a group, you can directly delete the group. Valid value:
        # 
        # *   user
        # 
        # Note: A group can be a member of only one group. It cannot be a member of multiple groups. A user can be a member of multiple groups.
        # 
        # This parameter is required.
        self.member_type = member_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.member_id is not None:
            result['member_id'] = self.member_id
        if self.member_type is not None:
            result['member_type'] = self.member_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('member_id') is not None:
            self.member_id = m.get('member_id')
        if m.get('member_type') is not None:
            self.member_type = m.get('member_type')
        return self


class RemoveGroupMemberResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class RemoveStoryFilesRequestFiles(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        revision_id: str = None,
    ):
        # This parameter is required.
        self.file_id = file_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class RemoveStoryFilesRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        files: List[RemoveStoryFilesRequestFiles] = None,
        story_id: str = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id
        self.files = files
        # This parameter is required.
        self.story_id = story_id

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        if self.story_id is not None:
            result['story_id'] = self.story_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = RemoveStoryFilesRequestFiles()
                self.files.append(temp_model.from_map(k))
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        return self


class RemoveStoryFilesResponseBody(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        story_id: str = None,
    ):
        self.drive_id = drive_id
        self.story_id = story_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.story_id is not None:
            result['story_id'] = self.story_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        return self


class RemoveStoryFilesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RemoveStoryFilesResponseBody = None,
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
            temp_model = RemoveStoryFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The ID of the file or folder.
        # 
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class RestoreFileResponseBody(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
    ):
        # The ID of the asynchronous task.
        # 
        # If an empty string is returned, the file or folder is restored.
        # 
        # If a non-empty string is returned, an asynchronous task is required. You can call the GetAsyncTask operation to obtain the information about an asynchronous task based on the task ID.
        self.async_task_id = async_task_id
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # The ID of the file or folder.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class RestoreFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: RestoreFileResponseBody = None,
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
            temp_model = RestoreFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreRevisionRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        revision_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # The version ID.
        # 
        # This parameter is required.
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class RestoreRevisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Revision = None,
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
            temp_model = Revision()
            self.body = temp_model.from_map(m['body'])
        return self


class ScanFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        limit: int = None,
        marker: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file properties to return.
        # 
        # *   If you want to return all file properties, set this parameter to \\*.
        # *   By default, if you do not specify this parameter, the following properties of a file are returned: - file_id, - drive_id, - parent_file_id, - type, - created_at, - updated_at, - file_extention, - size, - starred, - status, - category, and - permissions.
        # *   You can also specify properties to return. Separate multiple properties with commas (,).
        self.fields = fields
        # The maximum number of results to return. Valid values: 1 to 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is left empty.
        self.marker = marker

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        return self


class ScanFileResponseBody(TeaModel):
    def __init__(
        self,
        items: List[File] = None,
        next_marker: str = None,
    ):
        # The information about the files.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = File()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class ScanFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ScanFileResponseBody = None,
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
            temp_model = ScanFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchAddressGroupsRequest(TeaModel):
    def __init__(
        self,
        address_level: str = None,
        address_names: List[str] = None,
        br_geo_point: str = None,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        tl_geo_point: str = None,
        video_thumbnail_process: str = None,
    ):
        # The level of the location.
        # 
        # Valid values:
        # 
        # *   country
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   province
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   city
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   district
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        # *   township
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        # 
        #     <!-- -->
        self.address_level = address_level
        # The locations.
        self.address_names = address_names
        # The coordinates of the bottom right vertex of the rectangle. Set the value in the format of latitude,longitude.
        self.br_geo_point = br_geo_point
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The method used to generate the thumbnail of an image.
        self.image_thumbnail_process = image_thumbnail_process
        # The coordinates of the top left vertex of the rectangle. Set the value in the format of latitude,longitude.
        self.tl_geo_point = tl_geo_point
        # The method used to generate the thumbnail of a video.
        self.video_thumbnail_process = video_thumbnail_process

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.address_level is not None:
            result['address_level'] = self.address_level
        if self.address_names is not None:
            result['address_names'] = self.address_names
        if self.br_geo_point is not None:
            result['br_geo_point'] = self.br_geo_point
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.tl_geo_point is not None:
            result['tl_geo_point'] = self.tl_geo_point
        if self.video_thumbnail_process is not None:
            result['video_thumbnail_process'] = self.video_thumbnail_process
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('address_level') is not None:
            self.address_level = m.get('address_level')
        if m.get('address_names') is not None:
            self.address_names = m.get('address_names')
        if m.get('br_geo_point') is not None:
            self.br_geo_point = m.get('br_geo_point')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('tl_geo_point') is not None:
            self.tl_geo_point = m.get('tl_geo_point')
        if m.get('video_thumbnail_process') is not None:
            self.video_thumbnail_process = m.get('video_thumbnail_process')
        return self


class SearchAddressGroupsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[AddressGroup] = None,
    ):
        # The location-based groups.
        self.items = items

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = AddressGroup()
                self.items.append(temp_model.from_map(k))
        return self


class SearchAddressGroupsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchAddressGroupsResponseBody = None,
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
            temp_model = SearchAddressGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchDomainsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
        name: str = None,
        order_by: str = None,
    ):
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is empty.
        self.marker = marker
        # The name of the domain. Fuzzy search is supported.
        self.name = name
        # The sorting rule. Set the value to created_at, which specifies that the results are sorted based on the time when the domain was created.
        self.order_by = order_by

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.name is not None:
            result['name'] = self.name
        if self.order_by is not None:
            result['order_by'] = self.order_by
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        return self


class SearchDomainsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[Domain] = None,
        next_marker: str = None,
    ):
        # The queried domains.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Domain()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class SearchDomainsResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchDomainsResponseBody = None,
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
            temp_model = SearchDomainsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchDriveRequest(TeaModel):
    def __init__(
        self,
        drive_name: str = None,
        limit: int = None,
        marker: str = None,
        owner: str = None,
        owner_type: str = None,
    ):
        # The drive name.
        self.drive_name = drive_name
        # The maximum number of asynchronous tasks to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The owner of the drive.
        self.owner = owner
        # The type of the owner. Valid values:
        # 
        # user group
        self.owner_type = owner_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.owner is not None:
            result['owner'] = self.owner
        if self.owner_type is not None:
            result['owner_type'] = self.owner_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('owner_type') is not None:
            self.owner_type = m.get('owner_type')
        return self


class SearchDriveResponseBody(TeaModel):
    def __init__(
        self,
        items: List[Drive] = None,
        next_marker: str = None,
    ):
        # The information about the drives.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Drive()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class SearchDriveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchDriveResponseBody = None,
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
            temp_model = SearchDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        fields: str = None,
        limit: int = None,
        marker: str = None,
        order_by: str = None,
        query: str = None,
        recursive: bool = None,
        return_total_count: bool = None,
    ):
        # The drive ID.
        self.drive_id = drive_id
        self.fields = fields
        # The maximum number of results to return. Valid values: 1 to 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The field by which to sort the returned results. Default value: created_at. Valid values:
        # 
        # *   created_at: sorts the results by the time when the file was created.
        # *   updated_at: sorts the results by the time when the file was modified.
        # *   size: sorts the results by the size of the file.
        # *   name: sorts the results by the name of the file.
        # 
        # The order in which you want to sort the returned results. Valid values:
        # 
        # *   ASC: sorts the results in ascending order.
        # *   DESC: sorts the results in descending order.
        # 
        # You must specify this parameter in the \\<field name> \\<ASC or DESC> format. Separate multiple field names with commas (,). A preceding field has a higher priority than a following field. Examples:
        # 
        # *   If you want to sort the results based on the file name in ascending order, set this parameter to "name ASC".
        # *   If you want to sort the results based on the creation time in descending order, set this parameter to "created_at DESC".
        # *   If you want to sort the results based on the creation time in descending order first, and then sort the results based on the file name in ascending order if the creation time is the same, set this parameter to "created_at DESC,name ASC".
        self.order_by = order_by
        # The search condition. Fuzzy searches based on the file name or directory name are supported. The search condition can be up to 4,096 characters in length.
        # 
        # This parameter is required.
        self.query = query
        self.recursive = recursive
        # Specifies whether to return the total number of retrieved files.
        self.return_total_count = return_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.fields is not None:
            result['fields'] = self.fields
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.query is not None:
            result['query'] = self.query
        if self.recursive is not None:
            result['recursive'] = self.recursive
        if self.return_total_count is not None:
            result['return_total_count'] = self.return_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('fields') is not None:
            self.fields = m.get('fields')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('recursive') is not None:
            self.recursive = m.get('recursive')
        if m.get('return_total_count') is not None:
            self.return_total_count = m.get('return_total_count')
        return self


class SearchFileResponseBody(TeaModel):
    def __init__(
        self,
        items: List[File] = None,
        next_marker: str = None,
        total_count: int = None,
    ):
        # The information about the files.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker
        # The total number of retrieved files.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = File()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class SearchFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchFileResponseBody = None,
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
            temp_model = SearchFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchShareLinkRequest(TeaModel):
    def __init__(
        self,
        creators: List[str] = None,
        limit: int = None,
        marker: str = None,
        order_by: str = None,
        order_direction: str = None,
        query: str = None,
        return_total_count: bool = None,
    ):
        # The creators of shares. Set this parameter to a user ID. If you do not specify this parameter, Drive and Photo Service automatically queries shares based on your permissions. If you are a drive administrator or the super administrator, the shares created by all members are queried. If you are a team administrator, the shares created by all team members are queried. If you are a common user, only the shares created by yourself are queried.
        # 
        # If you specify this parameter, this parameter must be set to the ID of the super administrator, a drive administrator, or a team administrator.
        self.creators = creators
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        # 
        # The number of returned results must be less than or equal to the specified number.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The field by which to sort the returned results. Default value: created_at. Valid values:
        # 
        # *   share_name: sorts the results by the name of the share.
        # *   updated_at: sorts the results by the time when the share was modified.
        # *   description: sorts the results by the description of the share.
        # *   created_at: sorts the results by the time when the share was created.
        self.order_by = order_by
        # The order in which you want to sort the returned results. By default, order_direction is set to DESC if order_by is set to created_at or updated_at, and is set to ASC if order_by is set to other values. Valid values:
        # 
        # *   ASC: sorts the results in ascending order.
        # *   DESC: sorts the results in descending order.
        self.order_direction = order_direction
        # The query condition that is used to search for share URLs. You can use the following fields to specify query conditions: created_at: queries a share URL based on the time when the share URL was created. updated_at: queries a share URL based on the time when the share URL was modified. share_name_for_fuzzy: queries a share URL based on the name of the share. A fuzzy match is supported. status: queries a share URL based on the status of the share. Valid values: enabled and disabled. A value of enabled indicates that the share is valid. A value of disabled indicates that the share is canceled. expired_time: queries a share URL based on the expiration time of the share. If the share never expires, set this field to 1970-01-01T00:00:00. Otherwise, set this field to 1970-01-02T00:00:00.
        self.query = query
        # Specifies whether to return the total number of returned results.
        self.return_total_count = return_total_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.creators is not None:
            result['creators'] = self.creators
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.order_direction is not None:
            result['order_direction'] = self.order_direction
        if self.query is not None:
            result['query'] = self.query
        if self.return_total_count is not None:
            result['return_total_count'] = self.return_total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creators') is not None:
            self.creators = m.get('creators')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('order_direction') is not None:
            self.order_direction = m.get('order_direction')
        if m.get('query') is not None:
            self.query = m.get('query')
        if m.get('return_total_count') is not None:
            self.return_total_count = m.get('return_total_count')
        return self


class SearchShareLinkResponseBody(TeaModel):
    def __init__(
        self,
        items: List[ShareLink] = None,
        next_marker: str = None,
        total_count: int = None,
    ):
        # The share URLs.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        if self.total_count is not None:
            result['total_count'] = self.total_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = ShareLink()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        if m.get('total_count') is not None:
            self.total_count = m.get('total_count')
        return self


class SearchShareLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchShareLinkResponseBody = None,
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
            temp_model = SearchShareLinkResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchSimilarImageClustersRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        image_thumbnail_process: str = None,
        limit: int = None,
        marker: str = None,
        order: str = None,
    ):
        # This parameter is required.
        self.drive_id = drive_id
        self.image_thumbnail_process = image_thumbnail_process
        self.limit = limit
        self.marker = marker
        self.order = order

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.image_thumbnail_process is not None:
            result['image_thumbnail_process'] = self.image_thumbnail_process
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order is not None:
            result['order'] = self.order
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('image_thumbnail_process') is not None:
            self.image_thumbnail_process = m.get('image_thumbnail_process')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order') is not None:
            self.order = m.get('order')
        return self


class SearchSimilarImageClustersResponseBodySimilarImageClusters(TeaModel):
    def __init__(
        self,
        files: List[File] = None,
    ):
        self.files = files

    def validate(self):
        if self.files:
            for k in self.files:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['files'] = []
        if self.files is not None:
            for k in self.files:
                result['files'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.files = []
        if m.get('files') is not None:
            for k in m.get('files'):
                temp_model = File()
                self.files.append(temp_model.from_map(k))
        return self


class SearchSimilarImageClustersResponseBody(TeaModel):
    def __init__(
        self,
        next_marker: str = None,
        similar_image_clusters: List[SearchSimilarImageClustersResponseBodySimilarImageClusters] = None,
    ):
        self.next_marker = next_marker
        self.similar_image_clusters = similar_image_clusters

    def validate(self):
        if self.similar_image_clusters:
            for k in self.similar_image_clusters:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        result['similar_image_clusters'] = []
        if self.similar_image_clusters is not None:
            for k in self.similar_image_clusters:
                result['similar_image_clusters'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        self.similar_image_clusters = []
        if m.get('similar_image_clusters') is not None:
            for k in m.get('similar_image_clusters'):
                temp_model = SearchSimilarImageClustersResponseBodySimilarImageClusters()
                self.similar_image_clusters.append(temp_model.from_map(k))
        return self


class SearchSimilarImageClustersResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchSimilarImageClustersResponseBody = None,
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
            temp_model = SearchSimilarImageClustersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchStoriesRequestCreateTimeRange(TeaModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class SearchStoriesRequestStoryEndTimeRange(TeaModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class SearchStoriesRequestStoryStartTimeRange(TeaModel):
    def __init__(
        self,
        end: str = None,
        start: str = None,
    ):
        self.end = end
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.end is not None:
            result['end'] = self.end
        if self.start is not None:
            result['start'] = self.start
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('end') is not None:
            self.end = m.get('end')
        if m.get('start') is not None:
            self.start = m.get('start')
        return self


class SearchStoriesRequest(TeaModel):
    def __init__(
        self,
        cover_image_thumbnail_process: str = None,
        cover_video_thumbnail_process: str = None,
        create_time_range: SearchStoriesRequestCreateTimeRange = None,
        custom_labels: str = None,
        drive_id: str = None,
        face_group_ids: List[str] = None,
        limit: int = None,
        marker: str = None,
        order: str = None,
        sort: str = None,
        story_end_time_range: SearchStoriesRequestStoryEndTimeRange = None,
        story_id: str = None,
        story_name: str = None,
        story_start_time_range: SearchStoriesRequestStoryStartTimeRange = None,
        story_type: str = None,
        url_expire_sec: int = None,
        with_empty_stories: bool = None,
    ):
        self.cover_image_thumbnail_process = cover_image_thumbnail_process
        self.cover_video_thumbnail_process = cover_video_thumbnail_process
        self.create_time_range = create_time_range
        self.custom_labels = custom_labels
        # This parameter is required.
        self.drive_id = drive_id
        self.face_group_ids = face_group_ids
        self.limit = limit
        self.marker = marker
        self.order = order
        self.sort = sort
        self.story_end_time_range = story_end_time_range
        self.story_id = story_id
        self.story_name = story_name
        self.story_start_time_range = story_start_time_range
        self.story_type = story_type
        self.url_expire_sec = url_expire_sec
        self.with_empty_stories = with_empty_stories

    def validate(self):
        if self.create_time_range:
            self.create_time_range.validate()
        if self.story_end_time_range:
            self.story_end_time_range.validate()
        if self.story_start_time_range:
            self.story_start_time_range.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover_image_thumbnail_process is not None:
            result['cover_image_thumbnail_process'] = self.cover_image_thumbnail_process
        if self.cover_video_thumbnail_process is not None:
            result['cover_video_thumbnail_process'] = self.cover_video_thumbnail_process
        if self.create_time_range is not None:
            result['create_time_range'] = self.create_time_range.to_map()
        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.face_group_ids is not None:
            result['face_group_ids'] = self.face_group_ids
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.order is not None:
            result['order'] = self.order
        if self.sort is not None:
            result['sort'] = self.sort
        if self.story_end_time_range is not None:
            result['story_end_time_range'] = self.story_end_time_range.to_map()
        if self.story_id is not None:
            result['story_id'] = self.story_id
        if self.story_name is not None:
            result['story_name'] = self.story_name
        if self.story_start_time_range is not None:
            result['story_start_time_range'] = self.story_start_time_range.to_map()
        if self.story_type is not None:
            result['story_type'] = self.story_type
        if self.url_expire_sec is not None:
            result['url_expire_sec'] = self.url_expire_sec
        if self.with_empty_stories is not None:
            result['with_empty_stories'] = self.with_empty_stories
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover_image_thumbnail_process') is not None:
            self.cover_image_thumbnail_process = m.get('cover_image_thumbnail_process')
        if m.get('cover_video_thumbnail_process') is not None:
            self.cover_video_thumbnail_process = m.get('cover_video_thumbnail_process')
        if m.get('create_time_range') is not None:
            temp_model = SearchStoriesRequestCreateTimeRange()
            self.create_time_range = temp_model.from_map(m['create_time_range'])
        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('face_group_ids') is not None:
            self.face_group_ids = m.get('face_group_ids')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('order') is not None:
            self.order = m.get('order')
        if m.get('sort') is not None:
            self.sort = m.get('sort')
        if m.get('story_end_time_range') is not None:
            temp_model = SearchStoriesRequestStoryEndTimeRange()
            self.story_end_time_range = temp_model.from_map(m['story_end_time_range'])
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        if m.get('story_name') is not None:
            self.story_name = m.get('story_name')
        if m.get('story_start_time_range') is not None:
            temp_model = SearchStoriesRequestStoryStartTimeRange()
            self.story_start_time_range = temp_model.from_map(m['story_start_time_range'])
        if m.get('story_type') is not None:
            self.story_type = m.get('story_type')
        if m.get('url_expire_sec') is not None:
            self.url_expire_sec = m.get('url_expire_sec')
        if m.get('with_empty_stories') is not None:
            self.with_empty_stories = m.get('with_empty_stories')
        return self


class SearchStoriesResponseBody(TeaModel):
    def __init__(
        self,
        items: List[Story] = None,
        next_marker: str = None,
    ):
        self.items = items
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = Story()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class SearchStoriesResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchStoriesResponseBody = None,
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
            temp_model = SearchStoriesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchUserRequest(TeaModel):
    def __init__(
        self,
        email: str = None,
        limit: int = None,
        marker: str = None,
        nick_name: str = None,
        nick_name_for_fuzzy: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        user_name: str = None,
    ):
        # The email address of the user.
        self.email = email
        # The maximum number of results to return. Valid values: 1 to 100. Default value: 100.
        self.limit = limit
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of marker.\\
        # By default, this parameter is left empty.
        self.marker = marker
        # The nickname of the user. The nickname can be up to 128 characters in length.
        self.nick_name = nick_name
        # The nickname used for fuzzy searches. The nickname can be up to 128 characters in length.
        self.nick_name_for_fuzzy = nick_name_for_fuzzy
        # The mobile number of the user.
        self.phone = phone
        # The role of the user. Valid values:
        # 
        # *   superadmin
        # *   admin
        # *   user
        self.role = role
        # The state of the user. Valid values:
        # 
        # *   disabled: The user is prohibited from logon.
        # *   enabled: The user is in a normal state.
        self.status = status
        # The name of the user. The name can be up to 128 characters in length.
        self.user_name = user_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.email is not None:
            result['email'] = self.email
        if self.limit is not None:
            result['limit'] = self.limit
        if self.marker is not None:
            result['marker'] = self.marker
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.nick_name_for_fuzzy is not None:
            result['nick_name_for_fuzzy'] = self.nick_name_for_fuzzy
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.user_name is not None:
            result['user_name'] = self.user_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('email') is not None:
            self.email = m.get('email')
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('nick_name_for_fuzzy') is not None:
            self.nick_name_for_fuzzy = m.get('nick_name_for_fuzzy')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
        return self


class SearchUserResponseBody(TeaModel):
    def __init__(
        self,
        items: List[User] = None,
        next_marker: str = None,
    ):
        # The information about the users.
        self.items = items
        # A pagination token. It can be used in the next request to retrieve a new page of results. If next_marker is empty, no next page exists.
        self.next_marker = next_marker

    def validate(self):
        if self.items:
            for k in self.items:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        result['items'] = []
        if self.items is not None:
            for k in self.items:
                result['items'].append(k.to_map() if k else None)
        if self.next_marker is not None:
            result['next_marker'] = self.next_marker
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('items') is not None:
            for k in m.get('items'):
                temp_model = User()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
        return self


class SearchUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: SearchUserResponseBody = None,
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
            temp_model = SearchUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TokenRequest(TeaModel):
    def __init__(
        self,
        assertion: str = None,
        client_id: str = None,
        client_secret: str = None,
        code: str = None,
        grant_type: str = None,
        redirect_uri: str = None,
        refresh_token: str = None,
    ):
        # The JWT assertion that is signed by using the JWT private key. The JWT assertion contains the information about the user to be authorized and the authorization parameters. For more information about the structure of the JWT assertion, see JWTPayload. This parameter is required if grant_type is set to urn:ietf:params:oauth:grant-type:jwt-bearer.
        self.assertion = assertion
        # The AppId of the application that is created in the Drive and Photo Service console.
        # 
        # This parameter is required.
        self.client_id = client_id
        # The AppSecret of the application that is created in the Drive and Photo Service console. This parameter is required if the application is of the WebServer type.
        self.client_secret = client_secret
        # The authorization code in the redirect URI that is specified after the authorization process is complete. This parameter is required if grant_type is set to authorization_code.
        self.code = code
        # The method that is used to generate an access token. Valid values:
        # 
        # authorization_code: generates an access token by using the authorization code that is returned after the authorization process is complete.
        # 
        # refresh_token: generates an access token by using the refresh token that is returned after the authorization process is complete.
        # 
        # urn:ietf:params:oauth:grant-type:jwt-bearer: generates an access token by using a JWT assertion.
        # 
        # This parameter is required.
        self.grant_type = grant_type
        # The redirect URI that is specified when you initiate the authorization request. This parameter is required if grant_type is set to authorization_code.
        self.redirect_uri = redirect_uri
        # The refresh token that is used to refresh the access token. This parameter is required if grant_type is set to refresh_token.
        self.refresh_token = refresh_token

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.assertion is not None:
            result['assertion'] = self.assertion
        if self.client_id is not None:
            result['client_id'] = self.client_id
        if self.client_secret is not None:
            result['client_secret'] = self.client_secret
        if self.code is not None:
            result['code'] = self.code
        if self.grant_type is not None:
            result['grant_type'] = self.grant_type
        if self.redirect_uri is not None:
            result['redirect_uri'] = self.redirect_uri
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('assertion') is not None:
            self.assertion = m.get('assertion')
        if m.get('client_id') is not None:
            self.client_id = m.get('client_id')
        if m.get('client_secret') is not None:
            self.client_secret = m.get('client_secret')
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('grant_type') is not None:
            self.grant_type = m.get('grant_type')
        if m.get('redirect_uri') is not None:
            self.redirect_uri = m.get('redirect_uri')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        return self


class TokenResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Token = None,
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
            temp_model = Token()
            self.body = temp_model.from_map(m['body'])
        return self


class TrashFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The ID of the file or folder.
        # 
        # This parameter is required.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class TrashFileResponseBody(TeaModel):
    def __init__(
        self,
        async_task_id: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
    ):
        # The ID of the asynchronous task.
        # 
        # If an empty string is returned, the file or folder is moved to the recycle bin.
        # 
        # If a non-empty string is returned, an asynchronous task is required. You can call the GetAsyncTask operation to obtain the information about an asynchronous task based on the task ID.
        self.async_task_id = async_task_id
        # The domain ID.
        self.domain_id = domain_id
        # The drive ID.
        self.drive_id = drive_id
        # The ID of the file or folder.
        self.file_id = file_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.async_task_id is not None:
            result['async_task_id'] = self.async_task_id
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('async_task_id') is not None:
            self.async_task_id = m.get('async_task_id')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        return self


class TrashFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: TrashFileResponseBody = None,
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
            temp_model = TrashFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnLinkAccountRequest(TeaModel):
    def __init__(
        self,
        extra: str = None,
        identity: str = None,
        type: str = None,
        user_id: str = None,
    ):
        # Additional information for the unique account identifier. For example, when the account is a phone number, this field should be filled with the area code of the phone, such as 86 for Mainland China. If not provided, it defaults to 86.
        self.extra = extra
        # Unique identifier of the account, such as a phone number
        # 
        # This parameter is required.
        self.identity = identity
        # Account type
        # 
        # mobile: Phone number
        # 
        # email: Email address
        # 
        # ding: DingTalk
        # 
        # ram: Alibaba Cloud RAM User
        # 
        # wechat: WeCom
        # 
        # ldap: LDAP account
        # 
        # custom: Custom account
        # 
        # This parameter is required.
        self.type = type
        # User identifier
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.extra is not None:
            result['extra'] = self.extra
        if self.identity is not None:
            result['identity'] = self.identity
        if self.type is not None:
            result['type'] = self.type
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extra') is not None:
            self.extra = m.get('extra')
        if m.get('identity') is not None:
            self.identity = m.get('identity')
        if m.get('type') is not None:
            self.type = m.get('type')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class UnLinkAccountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateDomainRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        domain_id: str = None,
        domain_name: str = None,
        init_drive_enable: bool = None,
        init_drive_size: int = None,
        published_app_access_strategy: AppAccessStrategy = None,
        size_quota: int = None,
        user_count_quota: int = None,
    ):
        # The description of the domain.
        self.description = description
        # The domain ID.
        # 
        # This parameter is required.
        self.domain_id = domain_id
        # The name of the domain.
        self.domain_name = domain_name
        # Specifies whether to enable the default drive feature. A value of true specifies that all users are assigned a drive by default on the first logon. Default value: false.
        self.init_drive_enable = init_drive_enable
        # The size of the default drive. Unit: bytes. You must specify init_drive_size if you set init_drive_enable to true. Default value: 0. A value of 0 specifies that the size of the default drive is 0 bytes and you cannot upload files to the drive. To initialize the default drive, set init_drive_size to 0. A value of -1 specifies that the size is unlimited.
        self.init_drive_size = init_drive_size
        # The access policy of the application.
        self.published_app_access_strategy = published_app_access_strategy
        # The total storage quota for all drives in the domain. A value of 0 specifies that the quota is unlimited.
        self.size_quota = size_quota
        # The maximum number of users that can be created in the domain.
        self.user_count_quota = user_count_quota

    def validate(self):
        if self.published_app_access_strategy:
            self.published_app_access_strategy.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.domain_name is not None:
            result['domain_name'] = self.domain_name
        if self.init_drive_enable is not None:
            result['init_drive_enable'] = self.init_drive_enable
        if self.init_drive_size is not None:
            result['init_drive_size'] = self.init_drive_size
        if self.published_app_access_strategy is not None:
            result['published_app_access_strategy'] = self.published_app_access_strategy.to_map()
        if self.size_quota is not None:
            result['size_quota'] = self.size_quota
        if self.user_count_quota is not None:
            result['user_count_quota'] = self.user_count_quota
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('domain_name') is not None:
            self.domain_name = m.get('domain_name')
        if m.get('init_drive_enable') is not None:
            self.init_drive_enable = m.get('init_drive_enable')
        if m.get('init_drive_size') is not None:
            self.init_drive_size = m.get('init_drive_size')
        if m.get('published_app_access_strategy') is not None:
            temp_model = AppAccessStrategy()
            self.published_app_access_strategy = temp_model.from_map(m['published_app_access_strategy'])
        if m.get('size_quota') is not None:
            self.size_quota = m.get('size_quota')
        if m.get('user_count_quota') is not None:
            self.user_count_quota = m.get('user_count_quota')
        return self


class UpdateDomainResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Domain = None,
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
            temp_model = Domain()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateDriveRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        drive_id: str = None,
        drive_name: str = None,
        owner: str = None,
        status: str = None,
        total_size: int = None,
    ):
        # The description of the drive. The description can be up to 1,024 characters in length.
        self.description = description
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The name of the drive. The name can be up to 128 characters in length.
        self.drive_name = drive_name
        # The owner of the drive. Note: You can modify the owner of a personal drive only by using an AccessKey pair.
        self.owner = owner
        # The state of the drive. Valid values:
        # 
        # enabled and disabled.
        self.status = status
        # The total size of the drive. Unit: bytes. A value of -1 specifies that the size is unlimited.
        self.total_size = total_size

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.drive_name is not None:
            result['drive_name'] = self.drive_name
        if self.owner is not None:
            result['owner'] = self.owner
        if self.status is not None:
            result['status'] = self.status
        if self.total_size is not None:
            result['total_size'] = self.total_size
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('drive_name') is not None:
            self.drive_name = m.get('drive_name')
        if m.get('owner') is not None:
            self.owner = m.get('owner')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('total_size') is not None:
            self.total_size = m.get('total_size')
        return self


class UpdateDriveResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Drive = None,
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
            temp_model = Drive()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFacegroupRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        group_cover_face_id: str = None,
        group_id: str = None,
        group_name: str = None,
        remarks: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The face ID of the thumbnail of the face-based group. You can obtain the face ID from the **image_media_metadata** parameter in the returned results of the GetFile, ListFile, or SearchFile operation.
        self.group_cover_face_id = group_cover_face_id
        # The ID of the face-based group. You can call the ListFacegroups operation to query the group ID.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the face-based group. The name can be up to 128 characters in length.
        self.group_name = group_name
        # The remarks. The remarks can be up to 128 characters in length.
        self.remarks = remarks

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.group_cover_face_id is not None:
            result['group_cover_face_id'] = self.group_cover_face_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        if self.remarks is not None:
            result['remarks'] = self.remarks
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('group_cover_face_id') is not None:
            self.group_cover_face_id = m.get('group_cover_face_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        if m.get('remarks') is not None:
            self.remarks = m.get('remarks')
        return self


class UpdateFacegroupResponseBody(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        group_id: str = None,
    ):
        # The drive ID.
        self.drive_id = drive_id
        # The group ID.
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self


class UpdateFacegroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateFacegroupResponseBody = None,
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
            temp_model = UpdateFacegroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateFileRequest(TeaModel):
    def __init__(
        self,
        check_name_mode: str = None,
        description: str = None,
        drive_id: str = None,
        file_id: str = None,
        hidden: bool = None,
        labels: List[str] = None,
        local_modified_at: str = None,
        name: str = None,
        starred: bool = None,
    ):
        # The processing method that is used if the file that you want to modify has the same name as an existing file on the cloud. Valid values:
        # 
        # ignore: allows you to modify the file by using the same name as an existing file on the cloud.
        # 
        # auto_rename: automatically renames the file that has the same name on the cloud. By default, the current point in time is added to the end of the file name. Example: xxx_20060102_150405.
        # 
        # refuse: does not modify the file that you want to modify but returns the information about the file that has the same name on the cloud.
        # 
        # Default value: ignore.
        self.check_name_mode = check_name_mode
        # The description of the file. The description can be up to 1,024 characters in length.
        self.description = description
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # Specifies whether to hide the file.
        self.hidden = hidden
        # The tags of the file. You can specify up to 100 tags.
        self.labels = labels
        # The local time when the file was modified. The time is in the yyyy-MM-ddTHH:mm:ssZ format based on the UTC+0 time zone.
        self.local_modified_at = local_modified_at
        # The name of the file. The name can be up to 1,024 bytes in length based on the UTF-8 encoding rule.
        self.name = name
        # Specifies whether to add the file to favorites.
        self.starred = starred

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.check_name_mode is not None:
            result['check_name_mode'] = self.check_name_mode
        if self.description is not None:
            result['description'] = self.description
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.labels is not None:
            result['labels'] = self.labels
        if self.local_modified_at is not None:
            result['local_modified_at'] = self.local_modified_at
        if self.name is not None:
            result['name'] = self.name
        if self.starred is not None:
            result['starred'] = self.starred
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('check_name_mode') is not None:
            self.check_name_mode = m.get('check_name_mode')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('labels') is not None:
            self.labels = m.get('labels')
        if m.get('local_modified_at') is not None:
            self.local_modified_at = m.get('local_modified_at')
        if m.get('name') is not None:
            self.name = m.get('name')
        if m.get('starred') is not None:
            self.starred = m.get('starred')
        return self


class UpdateFileResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: File = None,
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
            temp_model = File()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateGroupRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        group_name: str = None,
    ):
        # The description of the group after modification.
        self.description = description
        # The ID of the group that you want to modify.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the group after modification.
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.group_id is not None:
            result['group_id'] = self.group_id
        if self.group_name is not None:
            result['group_name'] = self.group_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        if m.get('group_name') is not None:
            self.group_name = m.get('group_name')
        return self


class UpdateGroupResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Group = None,
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
            temp_model = Group()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateIdentityToBenefitPkgMappingRequest(TeaModel):
    def __init__(
        self,
        amount: int = None,
        benefit_pkg_id: str = None,
        expire_time: int = None,
        identity_id: str = None,
        identity_type: str = None,
    ):
        # The number of benefit packages.
        # 
        # This parameter specifies the number of benefit packages of the resource type. Default value: 1.
        self.amount = amount
        # The unique identifier of the benefit package.
        # 
        # This parameter is required.
        self.benefit_pkg_id = benefit_pkg_id
        # The expiration time of the benefit package. Set this parameter to a UNIX timestamp representing the number of milliseconds that have elapsed since January 1, 1970, 00:00:00 UTC.
        # 
        # By default, the benefit package never expires.
        self.expire_time = expire_time
        # The unique identifier of the entity.
        # 
        # If you call this operation to manage the benefits of a user, set this parameter to the ID of the user.
        # 
        # This parameter is required.
        self.identity_id = identity_id
        # The type of the entity. If you call this operation to manage the benefits of a user, set this parameter to user.
        # 
        # This parameter is required.
        self.identity_type = identity_type

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.amount is not None:
            result['amount'] = self.amount
        if self.benefit_pkg_id is not None:
            result['benefit_pkg_id'] = self.benefit_pkg_id
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.identity_id is not None:
            result['identity_id'] = self.identity_id
        if self.identity_type is not None:
            result['identity_type'] = self.identity_type
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('amount') is not None:
            self.amount = m.get('amount')
        if m.get('benefit_pkg_id') is not None:
            self.benefit_pkg_id = m.get('benefit_pkg_id')
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('identity_id') is not None:
            self.identity_id = m.get('identity_id')
        if m.get('identity_type') is not None:
            self.identity_type = m.get('identity_type')
        return self


class UpdateIdentityToBenefitPkgMappingResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        return self


class UpdateRevisionRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
        keep_forever: bool = None,
        revision_description: str = None,
        revision_id: str = None,
    ):
        # The drive ID.
        # 
        # This parameter is required.
        self.drive_id = drive_id
        # The file ID.
        # 
        # This parameter is required.
        self.file_id = file_id
        # Specifies whether to permanently retain a version.
        # 
        # By default, this parameter is not specified, which indicates that you do not modify the permanent retention configuration of the version.
        self.keep_forever = keep_forever
        # The description of the version. The description can be up to 1,024 characters in length.
        # 
        # By default, this parameter is not specified, which indicates that you do not modify the description of the version.
        self.revision_description = revision_description
        # The version ID.
        # 
        # This parameter is required.
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.keep_forever is not None:
            result['keep_forever'] = self.keep_forever
        if self.revision_description is not None:
            result['revision_description'] = self.revision_description
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('keep_forever') is not None:
            self.keep_forever = m.get('keep_forever')
        if m.get('revision_description') is not None:
            self.revision_description = m.get('revision_description')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class UpdateRevisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: Revision = None,
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
            temp_model = Revision()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateShareLinkRequest(TeaModel):
    def __init__(
        self,
        description: str = None,
        disable_download: bool = None,
        disable_preview: bool = None,
        disable_save: bool = None,
        download_count: int = None,
        download_limit: int = None,
        expiration: str = None,
        office_editable: bool = None,
        preview_count: int = None,
        preview_limit: int = None,
        report_count: int = None,
        save_count: int = None,
        save_limit: int = None,
        share_id: str = None,
        share_name: str = None,
        share_pwd: str = None,
        status: str = None,
        video_preview_count: int = None,
    ):
        # The description of the share link. The description can be up to 1,024 characters in length.
        self.description = description
        # Specifies whether to prohibit the downloads of the shared files.
        self.disable_download = disable_download
        # Specifies whether to prohibit the previews of the shared files.
        self.disable_preview = disable_preview
        # Specifies whether to prohibit the saves of the shared files.
        self.disable_save = disable_save
        # The number of times that the shared files are downloaded. The value must be greater than or equal to 0.
        self.download_count = download_count
        # The maximum number of times that the shared files can be downloaded. The value must be greater than or equal to 0. A value of 0 specifies that the number is unlimited.
        self.download_limit = download_limit
        # The time when the share link expires. The time follows the RFC 3339 standard. Example: 2020-06-28T11:33:00.000+08:00. If you leave this parameter empty, the share link never expires.
        self.expiration = expiration
        self.office_editable = office_editable
        # The number of times that the shared files are previewed. The value must be greater than or equal to 0.
        self.preview_count = preview_count
        # The maximum number of times that the shared files can be previewed. The value must be greater than or equal to 0. A value of 0 specifies that the number is unlimited.
        self.preview_limit = preview_limit
        # The number of times that the shared files are reported. The value must be greater than or equal to 0.
        self.report_count = report_count
        # The number of times that the shared files are saved. The value must be greater than or equal to 0.
        self.save_count = save_count
        # The maximum number of times that the shared files can be saved. The value must be greater than or equal to 0. A value of 0 specifies that the number is unlimited.
        self.save_limit = save_limit
        # The share ID.
        # 
        # This parameter is required.
        self.share_id = share_id
        # The name of the share link. By default, the name of the first file is used. The name can be up to 128 characters in length.
        self.share_name = share_name
        # The access code. The access code can be up to 64 characters in length. A value of 0 specifies an empty string.
        self.share_pwd = share_pwd
        # The state of the share link. Valid values:
        # 
        # *   disabled: The share link is canceled.
        # *   enabled: The share link is effective.
        self.status = status
        # The number of times that the videos are previewed in the shared files. The value must be greater than or equal to 0.
        self.video_preview_count = video_preview_count

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['description'] = self.description
        if self.disable_download is not None:
            result['disable_download'] = self.disable_download
        if self.disable_preview is not None:
            result['disable_preview'] = self.disable_preview
        if self.disable_save is not None:
            result['disable_save'] = self.disable_save
        if self.download_count is not None:
            result['download_count'] = self.download_count
        if self.download_limit is not None:
            result['download_limit'] = self.download_limit
        if self.expiration is not None:
            result['expiration'] = self.expiration
        if self.office_editable is not None:
            result['office_editable'] = self.office_editable
        if self.preview_count is not None:
            result['preview_count'] = self.preview_count
        if self.preview_limit is not None:
            result['preview_limit'] = self.preview_limit
        if self.report_count is not None:
            result['report_count'] = self.report_count
        if self.save_count is not None:
            result['save_count'] = self.save_count
        if self.save_limit is not None:
            result['save_limit'] = self.save_limit
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.share_name is not None:
            result['share_name'] = self.share_name
        if self.share_pwd is not None:
            result['share_pwd'] = self.share_pwd
        if self.status is not None:
            result['status'] = self.status
        if self.video_preview_count is not None:
            result['video_preview_count'] = self.video_preview_count
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('disable_download') is not None:
            self.disable_download = m.get('disable_download')
        if m.get('disable_preview') is not None:
            self.disable_preview = m.get('disable_preview')
        if m.get('disable_save') is not None:
            self.disable_save = m.get('disable_save')
        if m.get('download_count') is not None:
            self.download_count = m.get('download_count')
        if m.get('download_limit') is not None:
            self.download_limit = m.get('download_limit')
        if m.get('expiration') is not None:
            self.expiration = m.get('expiration')
        if m.get('office_editable') is not None:
            self.office_editable = m.get('office_editable')
        if m.get('preview_count') is not None:
            self.preview_count = m.get('preview_count')
        if m.get('preview_limit') is not None:
            self.preview_limit = m.get('preview_limit')
        if m.get('report_count') is not None:
            self.report_count = m.get('report_count')
        if m.get('save_count') is not None:
            self.save_count = m.get('save_count')
        if m.get('save_limit') is not None:
            self.save_limit = m.get('save_limit')
        if m.get('share_id') is not None:
            self.share_id = m.get('share_id')
        if m.get('share_name') is not None:
            self.share_name = m.get('share_name')
        if m.get('share_pwd') is not None:
            self.share_pwd = m.get('share_pwd')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('video_preview_count') is not None:
            self.video_preview_count = m.get('video_preview_count')
        return self


class UpdateShareLinkResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: ShareLink = None,
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
            temp_model = ShareLink()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateStoryRequestCover(TeaModel):
    def __init__(
        self,
        file_id: str = None,
        revision_id: str = None,
    ):
        self.file_id = file_id
        self.revision_id = revision_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.revision_id is not None:
            result['revision_id'] = self.revision_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('revision_id') is not None:
            self.revision_id = m.get('revision_id')
        return self


class UpdateStoryRequest(TeaModel):
    def __init__(
        self,
        cover: UpdateStoryRequestCover = None,
        custom_labels: Dict[str, str] = None,
        drive_id: str = None,
        story_id: str = None,
        story_name: str = None,
    ):
        self.cover = cover
        self.custom_labels = custom_labels
        # This parameter is required.
        self.drive_id = drive_id
        # This parameter is required.
        self.story_id = story_id
        self.story_name = story_name

    def validate(self):
        if self.cover:
            self.cover.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.cover is not None:
            result['cover'] = self.cover.to_map()
        if self.custom_labels is not None:
            result['custom_labels'] = self.custom_labels
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.story_id is not None:
            result['story_id'] = self.story_id
        if self.story_name is not None:
            result['story_name'] = self.story_name
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('cover') is not None:
            temp_model = UpdateStoryRequestCover()
            self.cover = temp_model.from_map(m['cover'])
        if m.get('custom_labels') is not None:
            self.custom_labels = m.get('custom_labels')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        if m.get('story_name') is not None:
            self.story_name = m.get('story_name')
        return self


class UpdateStoryResponseBody(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        story_id: str = None,
    ):
        self.drive_id = drive_id
        self.story_id = story_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.story_id is not None:
            result['story_id'] = self.story_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('story_id') is not None:
            self.story_id = m.get('story_id')
        return self


class UpdateStoryResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: UpdateStoryResponseBody = None,
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
            temp_model = UpdateStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequestGroupInfoList(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
        # The group ID.
        self.group_id = group_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.group_id is not None:
            result['group_id'] = self.group_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group_id') is not None:
            self.group_id = m.get('group_id')
        return self


class UpdateUserRequest(TeaModel):
    def __init__(
        self,
        avatar: str = None,
        description: str = None,
        email: str = None,
        group_info_list: List[UpdateUserRequestGroupInfoList] = None,
        nick_name: str = None,
        phone: str = None,
        role: str = None,
        status: str = None,
        user_data: Dict[str, str] = None,
        user_id: str = None,
    ):
        # The URL of the profile picture.
        # 
        # If you specify the parameter in the HTTP URL format, the URL must start with http:// or https:// and can be up to 4 KB in size.
        # 
        # If you specify the parameter in the DATA URL format, the URL must start with data:// and be encoded in Base64. The URL can be up to 300 KB in size.
        self.avatar = avatar
        # The description of the user. The description can be up to 1,024 characters in length.
        self.description = description
        # The email address of the user.
        self.email = email
        # The information about the group.
        self.group_info_list = group_info_list
        # The nickname of the user. The nickname can be up to 128 characters in length.
        self.nick_name = nick_name
        # The mobile number of the user.
        self.phone = phone
        # The role of the user. Valid values:
        # 
        # *   superadmin
        # *   admin
        # *   user
        self.role = role
        # The state of the user. Valid values:
        # 
        # *   disabled: The user is prohibited from logon.
        # *   enabled: The user is in a normal state.
        self.status = status
        # The custom data. The data can be up to 1,024 characters in length.
        self.user_data = user_data
        # The user ID. The ID can be up to 64 characters in length and cannot contain a number sign (#).
        # 
        # This parameter is required.
        self.user_id = user_id

    def validate(self):
        if self.group_info_list:
            for k in self.group_info_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.avatar is not None:
            result['avatar'] = self.avatar
        if self.description is not None:
            result['description'] = self.description
        if self.email is not None:
            result['email'] = self.email
        result['group_info_list'] = []
        if self.group_info_list is not None:
            for k in self.group_info_list:
                result['group_info_list'].append(k.to_map() if k else None)
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.phone is not None:
            result['phone'] = self.phone
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.user_data is not None:
            result['user_data'] = self.user_data
        if self.user_id is not None:
            result['user_id'] = self.user_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('avatar') is not None:
            self.avatar = m.get('avatar')
        if m.get('description') is not None:
            self.description = m.get('description')
        if m.get('email') is not None:
            self.email = m.get('email')
        self.group_info_list = []
        if m.get('group_info_list') is not None:
            for k in m.get('group_info_list'):
                temp_model = UpdateUserRequestGroupInfoList()
                self.group_info_list.append(temp_model.from_map(k))
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('phone') is not None:
            self.phone = m.get('phone')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('user_data') is not None:
            self.user_data = m.get('user_data')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        return self


class UpdateUserResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: User = None,
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
            temp_model = User()
            self.body = temp_model.from_map(m['body'])
        return self



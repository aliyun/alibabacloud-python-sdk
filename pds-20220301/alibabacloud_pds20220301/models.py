# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel
from typing import List, Dict, Any


class AccountLinkInfo(TeaModel):
    def __init__(
        self,
        authentication_type: str = None,
        created_at: int = None,
        display_name: str = None,
        domain_id: str = None,
        extra: str = None,
        identity: str = None,
        user_id: str = None,
    ):
        self.authentication_type = authentication_type
        self.created_at = created_at
        self.display_name = display_name
        self.domain_id = domain_id
        self.extra = extra
        self.identity = identity
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


class AudioPreviewPlayInfoMeta(TeaModel):
    def __init__(
        self,
        duration: float = None,
    ):
        self.duration = duration

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        return self


class AudioPreviewPlayInfoOfflineAudioList(TeaModel):
    def __init__(
        self,
        status: str = None,
        template_id: str = None,
        url: str = None,
    ):
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
        if self.status is not None:
            result['status'] = self.status
        if self.template_id is not None:
            result['template_id'] = self.template_id
        if self.url is not None:
            result['url'] = self.url
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('template_id') is not None:
            self.template_id = m.get('template_id')
        if m.get('url') is not None:
            self.url = m.get('url')
        return self


class AudioPreviewPlayInfo(TeaModel):
    def __init__(
        self,
        meta: AudioPreviewPlayInfoMeta = None,
        offline_audio_list: List[AudioPreviewPlayInfoOfflineAudioList] = None,
    ):
        self.meta = meta
        self.offline_audio_list = offline_audio_list

    def validate(self):
        if self.meta:
            self.meta.validate()
        if self.offline_audio_list:
            for k in self.offline_audio_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.meta is not None:
            result['meta'] = self.meta.to_map()
        result['offline_audio_list'] = []
        if self.offline_audio_list is not None:
            for k in self.offline_audio_list:
                result['offline_audio_list'].append(k.to_map() if k else None)
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('meta') is not None:
            temp_model = AudioPreviewPlayInfoMeta()
            self.meta = temp_model.from_map(m['meta'])
        self.offline_audio_list = []
        if m.get('offline_audio_list') is not None:
            for k in m.get('offline_audio_list'):
                temp_model = AudioPreviewPlayInfoOfflineAudioList()
                self.offline_audio_list.append(temp_model.from_map(k))
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
        self.bucket = bucket
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.expire = expire
        self.file_id = file_id
        self.object = object
        self.token = token
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


class Condition(TeaModel):
    def __init__(
        self,
        int_equals: List[int] = None,
        int_not_equals: List[int] = None,
        string_equals: List[str] = None,
        string_not_equals: List[str] = None,
    ):
        self.int_equals = int_equals
        self.int_not_equals = int_not_equals
        self.string_equals = string_equals
        self.string_not_equals = string_not_equals

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.int_equals is not None:
            result['int_equals'] = self.int_equals
        if self.int_not_equals is not None:
            result['int_not_equals'] = self.int_not_equals
        if self.string_equals is not None:
            result['string_equals'] = self.string_equals
        if self.string_not_equals is not None:
            result['string_not_equals'] = self.string_not_equals
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('int_equals') is not None:
            self.int_equals = m.get('int_equals')
        if m.get('int_not_equals') is not None:
            self.int_not_equals = m.get('int_not_equals')
        if m.get('string_equals') is not None:
            self.string_equals = m.get('string_equals')
        if m.get('string_not_equals') is not None:
            self.string_not_equals = m.get('string_not_equals')
        return self


class CsiCondition(TeaModel):
    def __init__(
        self,
        file_data_punish: Condition = None,
    ):
        self.file_data_punish = file_data_punish

    def validate(self):
        if self.file_data_punish:
            self.file_data_punish.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.file_data_punish is not None:
            result['file_data_punish'] = self.file_data_punish.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('file_data_punish') is not None:
            temp_model = Condition()
            self.file_data_punish = temp_model.from_map(m['file_data_punish'])
        return self


class DataCName(TeaModel):
    def __init__(
        self,
        data_cname: str = None,
        location: str = None,
    ):
        self.data_cname = data_cname
        self.location = location

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.data_cname is not None:
            result['data_cname'] = self.data_cname
        if self.location is not None:
            result['location'] = self.location
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data_cname') is not None:
            self.data_cname = m.get('data_cname')
        if m.get('location') is not None:
            self.location = m.get('location')
        return self


class Domain(TeaModel):
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
        size_quota: int = None,
        size_quota_used: int = None,
        status: int = None,
        updated_at: str = None,
        used_size: int = None,
        user_count_quota: int = None,
    ):
        self.created_at = created_at
        self.description = description
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.init_drive_enable = init_drive_enable
        self.init_drive_size = init_drive_size
        self.parent_domain_id = parent_domain_id
        self.published_app_access_strategy = published_app_access_strategy
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
            result['height'] = self.height
        if self.left is not None:
            result['left'] = self.left
        if self.top is not None:
            result['top'] = self.top
        if self.width is not None:
            result['width'] = self.width
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('height') is not None:
            self.height = m.get('height')
        if m.get('left') is not None:
            self.left = m.get('left')
        if m.get('top') is not None:
            self.top = m.get('top')
        if m.get('width') is not None:
            self.width = m.get('width')
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


class FileInvestigationInfo(TeaModel):
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


class File(TeaModel):
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
        file_extension: str = None,
        file_id: str = None,
        hidden: bool = None,
        investigation_info: FileInvestigationInfo = None,
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
        user_tags: Dict[str, str] = None,
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
        self.file_extension = file_extension
        self.file_id = file_id
        self.hidden = hidden
        self.investigation_info = investigation_info
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
        self.user_tags = user_tags

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
        if self.file_extension is not None:
            result['file_extension'] = self.file_extension
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.hidden is not None:
            result['hidden'] = self.hidden
        if self.investigation_info is not None:
            result['investigation_info'] = self.investigation_info.to_map()
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
        if self.user_tags is not None:
            result['user_tags'] = self.user_tags
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
        if m.get('file_extension') is not None:
            self.file_extension = m.get('file_extension')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('hidden') is not None:
            self.hidden = m.get('hidden')
        if m.get('investigation_info') is not None:
            temp_model = FileInvestigationInfo()
            self.investigation_info = temp_model.from_map(m['investigation_info'])
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
        if m.get('user_tags') is not None:
            self.user_tags = m.get('user_tags')
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
        self.bucket = bucket
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.file_id = file_id
        self.object = object
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


class UploadPartInfo(TeaModel):
    def __init__(
        self,
        etag: str = None,
        internal_upload_url: str = None,
        parallel_sha_1ctx: UploadPartInfoParallelSha1Ctx = None,
        part_number: int = None,
        part_size: int = None,
        upload_url: str = None,
    ):
        self.etag = etag
        self.internal_upload_url = internal_upload_url
        self.parallel_sha_1ctx = parallel_sha_1ctx
        self.part_number = part_number
        self.part_size = part_size
        self.upload_url = upload_url

    def validate(self):
        if self.parallel_sha_1ctx:
            self.parallel_sha_1ctx.validate()

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
        faces: str = None,
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
        self.faces = faces
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
        if self.faces is not None:
            result['faces'] = self.faces
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
        if m.get('faces') is not None:
            self.faces = m.get('faces')
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
        preview_count: int = None,
        preview_limit: int = None,
        report_count: int = None,
        save_count: int = None,
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
        self.preview_count = preview_count
        self.preview_limit = preview_limit
        self.report_count = report_count
        self.save_count = save_count
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


class StreamUploadInfo(TeaModel):
    def __init__(
        self,
        location: str = None,
        part_info_list: List[UploadPartInfo] = None,
        pre_rapid_upload: bool = None,
        rapid_upload: bool = None,
        upload_id: str = None,
    ):
        self.location = location
        self.part_info_list = part_info_list
        self.pre_rapid_upload = pre_rapid_upload
        self.rapid_upload = rapid_upload
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
        if self.location is not None:
            result['location'] = self.location
        result['part_info_list'] = []
        if self.part_info_list is not None:
            for k in self.part_info_list:
                result['part_info_list'].append(k.to_map() if k else None)
        if self.pre_rapid_upload is not None:
            result['pre_rapid_upload'] = self.pre_rapid_upload
        if self.rapid_upload is not None:
            result['rapid_upload'] = self.rapid_upload
        if self.upload_id is not None:
            result['upload_id'] = self.upload_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('location') is not None:
            self.location = m.get('location')
        self.part_info_list = []
        if m.get('part_info_list') is not None:
            for k in m.get('part_info_list'):
                temp_model = UploadPartInfo()
                self.part_info_list.append(temp_model.from_map(k))
        if m.get('pre_rapid_upload') is not None:
            self.pre_rapid_upload = m.get('pre_rapid_upload')
        if m.get('rapid_upload') is not None:
            self.rapid_upload = m.get('rapid_upload')
        if m.get('upload_id') is not None:
            self.upload_id = m.get('upload_id')
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
        device_id: str = None,
        device_name: str = None,
        domain_id: str = None,
        expire_time: str = None,
        expires_in: int = None,
        is_first_login: bool = None,
        nick_name: str = None,
        refresh_token: str = None,
        role: str = None,
        status: str = None,
        token_type: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.access_token = access_token
        self.avatar = avatar
        self.default_drive_id = default_drive_id
        self.device_id = device_id
        self.device_name = device_name
        self.domain_id = domain_id
        self.expire_time = expire_time
        self.expires_in = expires_in
        self.is_first_login = is_first_login
        self.nick_name = nick_name
        self.refresh_token = refresh_token
        self.role = role
        self.status = status
        self.token_type = token_type
        self.user_id = user_id
        self.user_name = user_name

    def validate(self):
        pass

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
        if self.device_id is not None:
            result['device_id'] = self.device_id
        if self.device_name is not None:
            result['device_name'] = self.device_name
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.expire_time is not None:
            result['expire_time'] = self.expire_time
        if self.expires_in is not None:
            result['expires_in'] = self.expires_in
        if self.is_first_login is not None:
            result['is_first_login'] = self.is_first_login
        if self.nick_name is not None:
            result['nick_name'] = self.nick_name
        if self.refresh_token is not None:
            result['refresh_token'] = self.refresh_token
        if self.role is not None:
            result['role'] = self.role
        if self.status is not None:
            result['status'] = self.status
        if self.token_type is not None:
            result['token_type'] = self.token_type
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
        if m.get('device_id') is not None:
            self.device_id = m.get('device_id')
        if m.get('device_name') is not None:
            self.device_name = m.get('device_name')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('expire_time') is not None:
            self.expire_time = m.get('expire_time')
        if m.get('expires_in') is not None:
            self.expires_in = m.get('expires_in')
        if m.get('is_first_login') is not None:
            self.is_first_login = m.get('is_first_login')
        if m.get('nick_name') is not None:
            self.nick_name = m.get('nick_name')
        if m.get('refresh_token') is not None:
            self.refresh_token = m.get('refresh_token')
        if m.get('role') is not None:
            self.role = m.get('role')
        if m.get('status') is not None:
            self.status = m.get('status')
        if m.get('token_type') is not None:
            self.token_type = m.get('token_type')
        if m.get('user_id') is not None:
            self.user_id = m.get('user_id')
        if m.get('user_name') is not None:
            self.user_name = m.get('user_name')
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
        object_key: str = None,
        oss_access_key_id: str = None,
        oss_end_point: str = None,
        oss_security_token: str = None,
        policy: str = None,
        signature: str = None,
    ):
        self.bucket_name = bucket_name
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


class UserTag(TeaModel):
    def __init__(
        self,
        value: str = None,
        key: str = None,
    ):
        self.value = value
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.value is not None:
            result['Value'] = self.value
        if self.key is not None:
            result['key'] = self.key
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Value') is not None:
            self.value = m.get('Value')
        if m.get('key') is not None:
            self.key = m.get('key')
        return self


class VideoMediaMetadata(TeaModel):
    def __init__(
        self,
        duration: str = None,
        taken_at: str = None,
    ):
        self.duration = duration
        self.taken_at = taken_at

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.duration is not None:
            result['duration'] = self.duration
        if self.taken_at is not None:
            result['taken_at'] = self.taken_at
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('duration') is not None:
            self.duration = m.get('duration')
        if m.get('taken_at') is not None:
            self.taken_at = m.get('taken_at')
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


class VideoPreviewPlayInfo(TeaModel):
    def __init__(
        self,
        category: str = None,
        live_transcoding_task_list: List[VideoPreviewPlayInfoLiveTranscodingTaskList] = None,
        meta: VideoPreviewPlayInfoMeta = None,
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
                temp_model = VideoPreviewPlayInfoLiveTranscodingTaskList()
                self.live_transcoding_task_list.append(temp_model.from_map(k))
        if m.get('meta') is not None:
            temp_model = VideoPreviewPlayInfoMeta()
            self.meta = temp_model.from_map(m['meta'])
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


class AddGroupMemberRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
        member_id: str = None,
        member_type: str = None,
    ):
        self.group_id = group_id
        self.member_id = member_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.drive_id = drive_id
        self.files = files
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
        self.identity = identity
        self.manage_resource_id = manage_resource_id
        self.manage_resource_type = manage_resource_type
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.client_id = client_id
        self.hide_consent = hide_consent
        self.login_type = login_type
        self.redirect_uri = redirect_uri
        self.response_type = response_type
        self.scope = scope
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
        self.client_id = client_id
        self.hide_consent = hide_consent
        self.login_type = login_type
        self.redirect_uri = redirect_uri
        self.response_type = response_type
        self.scope_shrink = scope_shrink
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        body: Dict[str, str] = None,
        headers: Dict[str, str] = None,
        id: str = None,
        method: str = None,
        url: str = None,
    ):
        self.body = body
        self.headers = headers
        self.id = id
        self.method = method
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
        self.requests = requests
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
        body: Dict[str, str] = None,
        id: str = None,
        status: int = None,
    ):
        self.body = body
        self.id = id
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
        self.identity = identity
        self.manage_resource_id = manage_resource_id
        self.manage_resource_type = manage_resource_type
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.async_task_id = async_task_id
        self.domain_id = domain_id
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
        self.drive_id = drive_id
        self.file_id = file_id
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
        self.auto_rename = auto_rename
        self.drive_id = drive_id
        self.file_id = file_id
        self.share_id = share_id
        self.to_drive_id = to_drive_id
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
        self.async_task_id = async_task_id
        self.domain_id = domain_id
        self.drive_id = drive_id
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
            temp_model = CopyFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateCustomizedStoryRequestStoryCover(TeaModel):
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


class CreateCustomizedStoryRequestStoryFiles(TeaModel):
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
        self.drive_id = drive_id
        self.story_cover = story_cover
        self.story_files = story_files
        self.story_name = story_name
        self.story_sub_type = story_sub_type
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
        self.description = description
        self.domain_name = domain_name
        self.init_drive_enable = init_drive_enable
        self.init_drive_size = init_drive_size
        self.parent_domain_id = parent_domain_id
        self.size_quota = size_quota
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
        self.default = default
        self.description = description
        self.drive_name = drive_name
        self.drive_type = drive_type
        self.owner = owner
        self.owner_type = owner_type
        self.status = status
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
        domain_id: str = None,
        drive_id: str = None,
    ):
        self.domain_id = domain_id
        self.drive_id = drive_id

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
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
            temp_model = CreateDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateFileRequestPartInfoList(TeaModel):
    def __init__(
        self,
        content_md_5: str = None,
        part_number: int = None,
    ):
        self.content_md_5 = content_md_5
        self.part_number = part_number

    def validate(self):
        pass

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.content_md_5 is not None:
            result['content_md5'] = self.content_md_5
        if self.part_number is not None:
            result['part_number'] = self.part_number
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('content_md5') is not None:
            self.content_md_5 = m.get('content_md5')
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
        self.check_name_mode = check_name_mode
        self.content_hash = content_hash
        self.content_hash_name = content_hash_name
        self.content_type = content_type
        self.description = description
        self.drive_id = drive_id
        self.file_id = file_id
        self.hidden = hidden
        self.image_media_metadata = image_media_metadata
        self.local_created_at = local_created_at
        self.local_modified_at = local_modified_at
        self.name = name
        self.parallel_upload = parallel_upload
        self.parent_file_id = parent_file_id
        self.part_info_list = part_info_list
        self.pre_hash = pre_hash
        self.share_id = share_id
        self.size = size
        self.type = type
        self.user_tags = user_tags
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
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.exist = exist
        self.file_id = file_id
        self.file_name = file_name
        self.parent_file_id = parent_file_id
        self.part_info_list = part_info_list
        self.rapid_upload = rapid_upload
        self.status = status
        self.type = type
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
        self.description = description
        self.group_name = group_name
        self.is_root = is_root
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
        self.amount = amount
        self.benefit_pkg_id = benefit_pkg_id
        self.expire_time = expire_time
        self.identity_id = identity_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class CreateShareLinkRequest(TeaModel):
    def __init__(
        self,
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
        save_limit: int = None,
        share_all_files: bool = None,
        share_name: str = None,
        share_pwd: str = None,
        user_id: str = None,
    ):
        self.description = description
        self.disable_download = disable_download
        self.disable_preview = disable_preview
        self.disable_save = disable_save
        self.download_limit = download_limit
        self.drive_id = drive_id
        self.expiration = expiration
        self.file_id_list = file_id_list
        self.office_editable = office_editable
        self.preview_limit = preview_limit
        self.save_limit = save_limit
        self.share_all_files = share_all_files
        self.share_name = share_name
        self.share_pwd = share_pwd
        self.user_id = user_id

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
            temp_model = ShareLink()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateSimilarImageClusterTaskRequest(TeaModel):
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
        self.drive_id = drive_id
        self.max_image_count = max_image_count
        self.min_image_count = min_image_count
        self.story_end_time = story_end_time
        self.story_id = story_id
        self.story_name = story_name
        self.story_start_time = story_start_time
        self.story_sub_type = story_sub_type
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
            temp_model = CreateStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequestGroupInfoList(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
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
        user_data: str = None,
        user_id: str = None,
        user_name: str = None,
    ):
        self.avatar = avatar
        self.description = description
        self.email = email
        self.group_info_list = group_info_list
        self.nick_name = nick_name
        self.phone = phone
        self.role = role
        self.status = status
        self.user_data = user_data
        self.user_id = user_id
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
        self.drive_id = drive_id
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
            temp_model = CsiGetFileInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteDomainRequest(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
    ):
        # domain id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.drive_id = drive_id
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
        self.async_task_id = async_task_id
        self.domain_id = domain_id
        self.drive_id = drive_id
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
            temp_model = DeleteFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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


class DeleteRevisionResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
            temp_model = DeleteStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.drive_id = drive_id
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
        self.drive_id = drive_id
        self.file_id = file_id
        self.image_thumbnail_process = image_thumbnail_process
        self.office_thumbnail_process = office_thumbnail_process
        self.share_id = share_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.drive_id = drive_id
        self.file_id = file_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.drive_id = drive_id
        self.file_id = file_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.drive_id = drive_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
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
        self.drive_id = drive_id
        self.file_id = file_id
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
            temp_model = FilePutUserTagsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class FileRemovePermissionRequestMemberList(TeaModel):
    def __init__(
        self,
        identity: Identity = None,
        role_id: str = None,
    ):
        # 可授权对象，表示一个用户或者一个群组
        self.identity = identity
        # 目前支持两种方式设置权限，一种是通过指定角色设置权限，另一种是自定义操作权限，此字段用于指定角色设置权限，与action\_list互斥，当两个字段同时设置时，以此字段为准
        # 
        # 目前支持：
        # 
        # SystemFileOwner（文件协同）
        # 
        # SystemFileDownloader（下载者）
        # 
        # SystemFileEditor（编辑者）
        # 
        # SystemFileEditorWithoutDelete（无删除编辑者）
        # 
        # SystemFileEditorWithoutShareLink（无分享编辑者）
        # 
        # SystemFileMetaViewer（可见列表）
        # 
        # SystemFileUploader（上传者）、SystemFileUploaderAndDownloader（上传/下载者）
        # 
        # SystemFileDownloaderWithShareLink（下载/分享者）
        # 
        # SystemFileUploaderAndDownloaderWithShareLink（上传/下载/分享者）
        # 
        # SystemFileUploaderAndViewer（预览/上传者）
        # 
        # SystemFileUploaderWithShareLink（上传/分享者）
        # 
        # SystemFileViewer（预览者）
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
        # 空间id
        self.drive_id = drive_id
        # 文件id
        self.file_id = file_id
        # 共享的用户对象集合
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        finished_at: str = None,
        message: str = None,
        started_at: str = None,
        state: str = None,
        status: str = None,
        total_process: int = None,
        uncompress_file_list: List[UncompressedFileInfo] = None,
        url: str = None,
    ):
        self.async_task_id = async_task_id
        self.category = category
        self.consumed_process = consumed_process
        self.created_at = created_at
        self.err_code = err_code
        self.error_code = error_code
        self.error_message = error_message
        self.finished_at = finished_at
        self.message = message
        self.started_at = started_at
        self.state = state
        self.status = status
        self.total_process = total_process
        self.uncompress_file_list = uncompress_file_list
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
        if self.finished_at is not None:
            result['finished_at'] = self.finished_at
        if self.message is not None:
            result['message'] = self.message
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
        if m.get('finished_at') is not None:
            self.finished_at = m.get('finished_at')
        if m.get('message') is not None:
            self.message = m.get('message')
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
            temp_model = GetAsyncTaskResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDefaultDriveRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
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
            temp_model = Drive()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDomainRequest(TeaModel):
    def __init__(
        self,
        domain_id: str = None,
        get_quota_used: bool = None,
    ):
        # domain id
        self.domain_id = domain_id
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
        if self.get_quota_used is not None:
            result['get_quota_used'] = self.get_quota_used
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
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
            temp_model = Domain()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDownloadUrlRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        expire_sec: int = None,
        file_id: str = None,
        file_name: str = None,
        share_id: str = None,
    ):
        self.drive_id = drive_id
        self.expire_sec = expire_sec
        self.file_id = file_id
        self.file_name = file_name
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
        self.cdn_url = cdn_url
        self.content_hash = content_hash
        self.content_hash_name = content_hash_name
        self.crc_64hash = crc_64hash
        self.expiration = expiration
        self.internal_url = internal_url
        self.size = size
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
            temp_model = GetDownloadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetDriveRequest(TeaModel):
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
        url_expire_sec: int = None,
    ):
        self.drive_id = drive_id
        self.fields = fields
        self.file_id = file_id
        self.share_id = share_id
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
        if self.share_id is not None:
            result['share_id'] = self.share_id
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
            temp_model = File()
            self.body = temp_model.from_map(m['body'])
        return self


class GetGroupRequest(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
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
        self.benefit_pkg_id = benefit_pkg_id
        self.identity_id = identity_id
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
            temp_model = AccountLinkInfo()
            self.body = temp_model.from_map(m['body'])
        return self


class GetLinkInfoByUserIdRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
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
        self.drive_id = drive_id
        self.fields = fields
        self.file_id = file_id
        self.revision_id = revision_id
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
            temp_model = Revision()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareLinkRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
    ):
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
            temp_model = ShareLink()
            self.body = temp_model.from_map(m['body'])
        return self


class GetShareLinkByAnonymousRequest(TeaModel):
    def __init__(
        self,
        share_id: str = None,
    ):
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
        self.access_count = access_count
        self.avatar = avatar
        self.creator_id = creator_id
        self.creator_name = creator_name
        self.creator_phone = creator_phone
        self.disable_download = disable_download
        self.disable_preview = disable_preview
        self.disable_save = disable_save
        self.download_count = download_count
        self.download_limit = download_limit
        self.expiration = expiration
        self.preview_count = preview_count
        self.preview_limit = preview_limit
        self.report_count = report_count
        self.save_count = save_count
        self.save_download_limit = save_download_limit
        self.save_limit = save_limit
        self.share_name = share_name
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
        self.expire_sec = expire_sec
        self.share_id = share_id
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
        self.expires_in = expires_in
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
        self.drive_id = drive_id
        self.image_thumbnail_process = image_thumbnail_process
        self.image_url_process = image_url_process
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
            temp_model = Story()
            self.body = temp_model.from_map(m['body'])
        return self


class GetTaskStatusRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        task_id: str = None,
    ):
        self.drive_id = drive_id
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
            temp_model = GetTaskStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUploadUrlRequestPartInfoListParallelSha1Ctx(TeaModel):
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
        part_number: int = None,
    ):
        self.content_md_5 = content_md_5
        self.content_type = content_type
        self.parallel_sha_1ctx = parallel_sha_1ctx
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
        if self.content_type is not None:
            result['content_type'] = self.content_type
        if self.parallel_sha_1ctx is not None:
            result['parallel_sha1_ctx'] = self.parallel_sha_1ctx.to_map()
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
        self.drive_id = drive_id
        self.file_id = file_id
        self.part_info_list = part_info_list
        self.share_id = share_id
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
        self.create_at = create_at
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.file_id = file_id
        self.part_info_list = part_info_list
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
            temp_model = GetUploadUrlResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(
        self,
        user_id: str = None,
    ):
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
            temp_model = User()
            self.body = temp_model.from_map(m['body'])
        return self


class GetVideoPreviewPlayInfoRequest(TeaModel):
    def __init__(
        self,
        category: str = None,
        drive_id: str = None,
        file_id: str = None,
        get_without_url: bool = None,
        share_id: str = None,
        template_id: str = None,
        url_expire_sec: int = None,
    ):
        self.category = category
        self.drive_id = drive_id
        self.file_id = file_id
        self.get_without_url = get_without_url
        self.share_id = share_id
        self.template_id = template_id
        # url超时时间，单位：秒。
        # 默认15分钟，最大4小时。
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
        if self.get_without_url is not None:
            result['get_without_url'] = self.get_without_url
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
        if m.get('get_without_url') is not None:
            self.get_without_url = m.get('get_without_url')
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
        code: str = None,
        domain_id: str = None,
        drive_id: str = None,
        file_id: str = None,
        message: str = None,
        share_id: str = None,
        video_preview_play_info: VideoPreviewPlayInfo = None,
    ):
        self.code = code
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.file_id = file_id
        self.message = message
        self.share_id = share_id
        self.video_preview_play_info = video_preview_play_info

    def validate(self):
        if self.video_preview_play_info:
            self.video_preview_play_info.validate()

    def to_map(self):
        _map = super().to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['code'] = self.code
        if self.domain_id is not None:
            result['domain_id'] = self.domain_id
        if self.drive_id is not None:
            result['drive_id'] = self.drive_id
        if self.file_id is not None:
            result['file_id'] = self.file_id
        if self.message is not None:
            result['message'] = self.message
        if self.share_id is not None:
            result['share_id'] = self.share_id
        if self.video_preview_play_info is not None:
            result['video_preview_play_info'] = self.video_preview_play_info.to_map()
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')
        if m.get('domain_id') is not None:
            self.domain_id = m.get('domain_id')
        if m.get('drive_id') is not None:
            self.drive_id = m.get('drive_id')
        if m.get('file_id') is not None:
            self.file_id = m.get('file_id')
        if m.get('message') is not None:
            self.message = m.get('message')
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
        self.category = category
        self.drive_id = drive_id
        self.file_id = file_id
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
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.file_id = file_id
        self.share_id = share_id
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
            temp_model = GetVideoPreviewPlayMetaResponseBody()
            self.body = temp_model.from_map(m['body'])
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
        self.authentication_display_name = authentication_display_name
        self.authentication_type = authentication_type
        self.auto_create_drive = auto_create_drive
        self.drive_total_size = drive_total_size
        self.extra = extra
        self.identity = identity
        self.nick_name = nick_name
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
            temp_model = User()
            self.body = temp_model.from_map(m['body'])
        return self


class InvestigateFileRequestDriveFileIds(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
    ):
        self.drive_id = drive_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.extra = extra
        self.identity = identity
        self.type = type
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
        self.drive_id = drive_id
        self.image_thumbnail_process = image_thumbnail_process
        self.limit = limit
        self.marker = marker
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
        self.limit = limit
        self.manage_resource_id = manage_resource_id
        self.manage_resource_type = manage_resource_type
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
        self.created_at = created_at
        self.creator = creator
        self.domain_id = domain_id
        self.identity = identity
        self.manage_resource_id = manage_resource_id
        self.manage_resource_type = manage_resource_type
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
        self.assignment_list = assignment_list
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
        self.cursor = cursor
        self.drive_id = drive_id
        self.limit = limit
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
        self.file = file
        self.file_id = file_id
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
        self.cursor = cursor
        self.has_more = has_more
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
            temp_model = ListDeltaResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListDomainsRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
        parent_domain_id: str = None,
    ):
        self.limit = limit
        self.marker = marker
        self.parent_domain_id = parent_domain_id

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
        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('limit') is not None:
            self.limit = m.get('limit')
        if m.get('marker') is not None:
            self.marker = m.get('marker')
        if m.get('parent_domain_id') is not None:
            self.parent_domain_id = m.get('parent_domain_id')
        return self


class ListDomainsResponseBody(TeaModel):
    def __init__(
        self,
        items: List[Domain] = None,
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
        self.limit = limit
        self.marker = marker
        self.owner = owner
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
        self.drive_id = drive_id
        self.limit = limit
        self.marker = marker
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
        self.items = items
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
        self.category = category
        self.drive_id = drive_id
        self.fields = fields
        self.limit = limit
        self.marker = marker
        self.order_by = order_by
        self.order_direction = order_direction
        self.parent_file_id = parent_file_id
        self.share_id = share_id
        self.status = status
        self.thumbnail_processes = thumbnail_processes
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
            temp_model = ListFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListGroupRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        self.limit = limit
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
        self.group_id = group_id
        self.limit = limit
        self.marker = marker
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
        self.group_items = group_items
        self.next_marker = next_marker
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
            temp_model = ListGroupMemberResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListIdentityToBenefitPkgMappingRequest(TeaModel):
    def __init__(
        self,
        identity_id: str = None,
        identity_type: str = None,
        include_expired: bool = None,
    ):
        self.identity_id = identity_id
        self.identity_type = identity_type
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
            temp_model = ListIdentityToBenefitPkgMappingResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMyDrivesRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        self.limit = limit
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
            temp_model = ListMyDrivesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListMyGroupDriveRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        self.limit = limit
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


class ListMyGroupDriveResponseBody(TeaModel):
    def __init__(
        self,
        items: List[Drive] = None,
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
                temp_model = Drive()
                self.items.append(temp_model.from_map(k))
        if m.get('next_marker') is not None:
            self.next_marker = m.get('next_marker')
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
            temp_model = ListMyGroupDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListReceivedFileRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        self.limit = limit
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
        self.drive_id = drive_id
        self.fields = fields
        self.limit = limit
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
        self.drive_id = drive_id
        self.fields = fields
        self.file_id = file_id
        self.limit = limit
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
        self.creator = creator
        self.include_cancelled = include_cancelled
        self.limit = limit
        self.marker = marker
        self.order_by = order_by
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
        self.drive_id = drive_id
        self.image_thumbnail_process = image_thumbnail_process
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
        self.drive_id = drive_id
        self.file_id = file_id
        self.limit = limit
        self.part_number_marker = part_number_marker
        self.share_id = share_id
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
        self.file_id = file_id
        self.next_part_number_marker = next_part_number_marker
        self.parallel_upload = parallel_upload
        self.upload_id = upload_id
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
            temp_model = ListUploadedPartsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserRequest(TeaModel):
    def __init__(
        self,
        limit: int = None,
        marker: str = None,
    ):
        self.limit = limit
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
        self.check_name_mode = check_name_mode
        self.drive_id = drive_id
        self.file_id = file_id
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
        self.async_task_id = async_task_id
        self.domain_id = domain_id
        self.drive_id = drive_id
        self.exist = exist
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
            temp_model = MoveFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveFaceGroupFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        face_group_id: str = None,
        file_id: str = None,
    ):
        self.drive_id = drive_id
        self.face_group_id = face_group_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.group_id = group_id
        self.member_id = member_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.drive_id = drive_id
        self.files = files
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
            temp_model = RemoveStoryFilesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RestoreFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
    ):
        self.drive_id = drive_id
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
        self.async_task_id = async_task_id
        self.domain_id = domain_id
        self.drive_id = drive_id
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
        self.drive_id = drive_id
        self.fields = fields
        self.limit = limit
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
        self.address_level = address_level
        self.address_names = address_names
        self.br_geo_point = br_geo_point
        self.drive_id = drive_id
        self.image_thumbnail_process = image_thumbnail_process
        self.tl_geo_point = tl_geo_point
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
        self.limit = limit
        self.marker = marker
        self.name = name
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
        self.drive_name = drive_name
        self.limit = limit
        self.marker = marker
        self.owner = owner
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
            temp_model = SearchDriveResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class SearchFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        limit: int = None,
        marker: str = None,
        order_by: str = None,
        query: str = None,
        return_total_count: bool = None,
    ):
        self.drive_id = drive_id
        self.limit = limit
        self.marker = marker
        self.order_by = order_by
        self.query = query
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
        if self.order_by is not None:
            result['order_by'] = self.order_by
        if self.query is not None:
            result['query'] = self.query
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
        if m.get('order_by') is not None:
            self.order_by = m.get('order_by')
        if m.get('query') is not None:
            self.query = m.get('query')
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
        self.items = items
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
        self.creators = creators
        self.limit = limit
        self.marker = marker
        self.order_by = order_by
        self.order_direction = order_direction
        self.query = query
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
        self.items = items
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
        self.email = email
        self.limit = limit
        self.marker = marker
        self.nick_name = nick_name
        self.nick_name_for_fuzzy = nick_name_for_fuzzy
        self.phone = phone
        self.role = role
        self.status = status
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
        self.assertion = assertion
        self.client_id = client_id
        self.client_secret = client_secret
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
            temp_model = Token()
            self.body = temp_model.from_map(m['body'])
        return self


class TrashFileRequest(TeaModel):
    def __init__(
        self,
        drive_id: str = None,
        file_id: str = None,
    ):
        self.drive_id = drive_id
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
        self.async_task_id = async_task_id
        self.domain_id = domain_id
        self.drive_id = drive_id
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
            temp_model = TrashFileResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnLinkAcountRequest(TeaModel):
    def __init__(
        self,
        extra: str = None,
        identity: str = None,
        type: str = None,
        user_id: str = None,
    ):
        self.extra = extra
        self.identity = identity
        self.type = type
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


class UnLinkAcountResponse(TeaModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
    ):
        self.headers = headers
        self.status_code = status_code

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.description = description
        # domain id
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.init_drive_enable = init_drive_enable
        self.init_drive_size = init_drive_size
        self.published_app_access_strategy = published_app_access_strategy
        self.size_quota = size_quota
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
        self.description = description
        self.drive_id = drive_id
        self.drive_name = drive_name
        # 归属者
        # 注意，当前只允许通过 ak 来修改个人 drive 的所有者。
        self.owner = owner
        self.status = status
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
        self.drive_id = drive_id
        self.group_cover_face_id = group_cover_face_id
        self.group_id = group_id
        self.group_name = group_name
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
        self.drive_id = drive_id
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
        self.check_name_mode = check_name_mode
        self.description = description
        self.drive_id = drive_id
        self.file_id = file_id
        self.hidden = hidden
        self.labels = labels
        self.local_modified_at = local_modified_at
        self.name = name
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
        self.description = description
        self.group_id = group_id
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
        self.amount = amount
        self.benefit_pkg_id = benefit_pkg_id
        self.expire_time = expire_time
        self.identity_id = identity_id
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
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')

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
        self.drive_id = drive_id
        self.file_id = file_id
        self.keep_forever = keep_forever
        self.revision_description = revision_description
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
        self.description = description
        self.disable_download = disable_download
        self.disable_preview = disable_preview
        self.disable_save = disable_save
        self.download_count = download_count
        self.download_limit = download_limit
        self.expiration = expiration
        self.preview_count = preview_count
        self.preview_limit = preview_limit
        self.report_count = report_count
        self.save_count = save_count
        self.save_limit = save_limit
        self.share_id = share_id
        self.share_name = share_name
        self.share_pwd = share_pwd
        self.status = status
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
        self.drive_id = drive_id
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
            temp_model = UpdateStoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateUserRequestGroupInfoList(TeaModel):
    def __init__(
        self,
        group_id: str = None,
    ):
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
        self.avatar = avatar
        self.description = description
        self.email = email
        self.group_info_list = group_info_list
        self.nick_name = nick_name
        self.phone = phone
        self.role = role
        self.status = status
        self.user_data = user_data
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
            temp_model = User()
            self.body = temp_model.from_map(m['body'])
        return self



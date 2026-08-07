# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_outboundbot20251111 import models as main_models
from darabonba.model import DaraModel

class ListVoiceAccessProfilesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListVoiceAccessProfilesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # 返回码
        self.code = code
        # 返回数据
        self.data = data
        # HTTP状态码
        self.http_status_code = http_status_code
        # 错误信息
        self.message = message
        # 错误信息中的变量值列表
        self.params = params
        # 请求ID
        self.request_id = request_id
        # 是否调用成功
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.params is not None:
            result['Params'] = self.params

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
            temp_model = main_models.ListVoiceAccessProfilesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListVoiceAccessProfilesResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
        voice_access_profiles: List[main_models.ListVoiceAccessProfilesResponseBodyDataVoiceAccessProfiles] = None,
    ):
        # 页码，从1开始
        self.page_number = page_number
        # 每页记录数
        self.page_size = page_size
        # 符合条件的记录总数
        self.total_count = total_count
        # 数据列表
        self.voice_access_profiles = voice_access_profiles

    def validate(self):
        if self.voice_access_profiles:
            for v1 in self.voice_access_profiles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        result['VoiceAccessProfiles'] = []
        if self.voice_access_profiles is not None:
            for k1 in self.voice_access_profiles:
                result['VoiceAccessProfiles'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        self.voice_access_profiles = []
        if m.get('VoiceAccessProfiles') is not None:
            for k1 in m.get('VoiceAccessProfiles'):
                temp_model = main_models.ListVoiceAccessProfilesResponseBodyDataVoiceAccessProfiles()
                self.voice_access_profiles.append(temp_model.from_map(k1))

        return self

class ListVoiceAccessProfilesResponseBodyDataVoiceAccessProfiles(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
        capabilities: List[str] = None,
        created_time: int = None,
        instance_id: str = None,
        nls_engine: str = None,
        nls_engine_name: str = None,
        profile: main_models.ListVoiceAccessProfilesResponseBodyDataVoiceAccessProfilesProfile = None,
        updated_time: int = None,
    ):
        # 接入配置ID
        self.access_profile_id = access_profile_id
        # 能力列表
        self.capabilities = capabilities
        # 创建时间，毫秒级时间戳
        self.created_time = created_time
        # 实例ID
        self.instance_id = instance_id
        # 目前支持IFLYTEK、VOLC
        self.nls_engine = nls_engine
        # 引擎显示名称(例如：豆包、货拉拉)
        self.nls_engine_name = nls_engine_name
        # 配置
        self.profile = profile
        # 更新时间，毫秒级时间戳
        self.updated_time = updated_time

    def validate(self):
        if self.profile:
            self.profile.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_profile_id is not None:
            result['AccessProfileId'] = self.access_profile_id

        if self.capabilities is not None:
            result['Capabilities'] = self.capabilities

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.nls_engine is not None:
            result['NlsEngine'] = self.nls_engine

        if self.nls_engine_name is not None:
            result['NlsEngineName'] = self.nls_engine_name

        if self.profile is not None:
            result['Profile'] = self.profile.to_map()

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessProfileId') is not None:
            self.access_profile_id = m.get('AccessProfileId')

        if m.get('Capabilities') is not None:
            self.capabilities = m.get('Capabilities')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('NlsEngine') is not None:
            self.nls_engine = m.get('NlsEngine')

        if m.get('NlsEngineName') is not None:
            self.nls_engine_name = m.get('NlsEngineName')

        if m.get('Profile') is not None:
            temp_model = main_models.ListVoiceAccessProfilesResponseBodyDataVoiceAccessProfilesProfile()
            self.profile = temp_model.from_map(m.get('Profile'))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

class ListVoiceAccessProfilesResponseBodyDataVoiceAccessProfilesProfile(DaraModel):
    def __init__(
        self,
        access_key: str = None,
        api_key: str = None,
        api_secret: str = None,
        app_id: str = None,
        app_key: str = None,
        asr_app_key: str = None,
        secret_id: str = None,
        secret_key: str = None,
        tts_api_key: str = None,
    ):
        # 访问密钥
        self.access_key = access_key
        # 百炼同时使用
        self.api_key = api_key
        # API密钥
        self.api_secret = api_secret
        # 科大讯飞使用
        self.app_id = app_id
        # 豆包使用
        self.app_key = app_key
        # 货拉拉使用
        self.asr_app_key = asr_app_key
        # 腾讯云使用，appId 已存在
        self.secret_id = secret_id
        # 密钥
        self.secret_key = secret_key
        # TTS服务API Key
        self.tts_api_key = tts_api_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_key is not None:
            result['AccessKey'] = self.access_key

        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.api_secret is not None:
            result['ApiSecret'] = self.api_secret

        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_key is not None:
            result['AppKey'] = self.app_key

        if self.asr_app_key is not None:
            result['AsrAppKey'] = self.asr_app_key

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        if self.secret_key is not None:
            result['SecretKey'] = self.secret_key

        if self.tts_api_key is not None:
            result['TtsApiKey'] = self.tts_api_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessKey') is not None:
            self.access_key = m.get('AccessKey')

        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ApiSecret') is not None:
            self.api_secret = m.get('ApiSecret')

        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')

        if m.get('AsrAppKey') is not None:
            self.asr_app_key = m.get('AsrAppKey')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        if m.get('SecretKey') is not None:
            self.secret_key = m.get('SecretKey')

        if m.get('TtsApiKey') is not None:
            self.tts_api_key = m.get('TtsApiKey')

        return self


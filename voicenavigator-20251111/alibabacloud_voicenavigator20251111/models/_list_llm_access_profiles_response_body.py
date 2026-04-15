# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class ListLlmAccessProfilesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ListLlmAccessProfilesResponseBodyData = None,
        http_status_code: int = None,
        message: str = None,
        params: List[str] = None,
        request_id: str = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.params = params
        self.request_id = request_id

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ListLlmAccessProfilesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListLlmAccessProfilesResponseBodyData(DaraModel):
    def __init__(
        self,
        llm_access_profiles: List[main_models.ListLlmAccessProfilesResponseBodyDataLlmAccessProfiles] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.llm_access_profiles = llm_access_profiles
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.llm_access_profiles:
            for v1 in self.llm_access_profiles:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LlmAccessProfiles'] = []
        if self.llm_access_profiles is not None:
            for k1 in self.llm_access_profiles:
                result['LlmAccessProfiles'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.llm_access_profiles = []
        if m.get('LlmAccessProfiles') is not None:
            for k1 in m.get('LlmAccessProfiles'):
                temp_model = main_models.ListLlmAccessProfilesResponseBodyDataLlmAccessProfiles()
                self.llm_access_profiles.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListLlmAccessProfilesResponseBodyDataLlmAccessProfiles(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
        created_time: int = None,
        instance_id: str = None,
        profile: main_models.ListLlmAccessProfilesResponseBodyDataLlmAccessProfilesProfile = None,
        updated_time: int = None,
    ):
        self.access_profile_id = access_profile_id
        self.created_time = created_time
        self.instance_id = instance_id
        self.profile = profile
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

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.profile is not None:
            result['Profile'] = self.profile.to_map()

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessProfileId') is not None:
            self.access_profile_id = m.get('AccessProfileId')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Profile') is not None:
            temp_model = main_models.ListLlmAccessProfilesResponseBodyDataLlmAccessProfilesProfile()
            self.profile = temp_model.from_map(m.get('Profile'))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        return self

class ListLlmAccessProfilesResponseBodyDataLlmAccessProfilesProfile(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        endpoint: str = None,
        name: str = None,
        nlu_access_type: str = None,
        nlu_engine: str = None,
    ):
        self.api_key = api_key
        self.endpoint = endpoint
        self.name = name
        self.nlu_access_type = nlu_access_type
        self.nlu_engine = nlu_engine

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.name is not None:
            result['Name'] = self.name

        if self.nlu_access_type is not None:
            result['NluAccessType'] = self.nlu_access_type

        if self.nlu_engine is not None:
            result['NluEngine'] = self.nlu_engine

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NluAccessType') is not None:
            self.nlu_access_type = m.get('NluAccessType')

        if m.get('NluEngine') is not None:
            self.nlu_engine = m.get('NluEngine')

        return self


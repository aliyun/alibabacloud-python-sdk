# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_voicenavigator20251111 import models as main_models
from darabonba.model import DaraModel

class UpdateLlmAccessProfileRequest(DaraModel):
    def __init__(
        self,
        access_profile_id: str = None,
        instance_id: str = None,
        profile: main_models.UpdateLlmAccessProfileRequestProfile = None,
    ):
        self.access_profile_id = access_profile_id
        self.instance_id = instance_id
        self.profile = profile

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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.profile is not None:
            result['Profile'] = self.profile.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessProfileId') is not None:
            self.access_profile_id = m.get('AccessProfileId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Profile') is not None:
            temp_model = main_models.UpdateLlmAccessProfileRequestProfile()
            self.profile = temp_model.from_map(m.get('Profile'))

        return self

class UpdateLlmAccessProfileRequestProfile(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        endpoint: str = None,
        name: str = None,
    ):
        self.api_key = api_key
        self.endpoint = endpoint
        self.name = name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self


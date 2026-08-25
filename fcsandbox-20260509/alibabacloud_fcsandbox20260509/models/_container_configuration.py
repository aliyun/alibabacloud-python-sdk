# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_fcsandbox20260509 import models as main_models
from darabonba.model import DaraModel

class ContainerConfiguration(DaraModel):
    def __init__(
        self,
        acr_instance_id: str = None,
        image: str = None,
        registry_credential: main_models.ContainerConfigurationRegistryCredential = None,
    ):
        self.acr_instance_id = acr_instance_id
        self.image = image
        self.registry_credential = registry_credential

    def validate(self):
        if self.registry_credential:
            self.registry_credential.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acr_instance_id is not None:
            result['acrInstanceId'] = self.acr_instance_id

        if self.image is not None:
            result['image'] = self.image

        if self.registry_credential is not None:
            result['registryCredential'] = self.registry_credential.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('acrInstanceId') is not None:
            self.acr_instance_id = m.get('acrInstanceId')

        if m.get('image') is not None:
            self.image = m.get('image')

        if m.get('registryCredential') is not None:
            temp_model = main_models.ContainerConfigurationRegistryCredential()
            self.registry_credential = temp_model.from_map(m.get('registryCredential'))

        return self



class ContainerConfigurationRegistryCredential(DaraModel):
    def __init__(
        self,
        password: str = None,
        username: str = None,
    ):
        self.password = password
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.password is not None:
            result['password'] = self.password

        if self.username is not None:
            result['username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('password') is not None:
            self.password = m.get('password')

        if m.get('username') is not None:
            self.username = m.get('username')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListEdgeContainerAppImageSecretsResponseBody(DaraModel):
    def __init__(
        self,
        image_secret_list: List[main_models.ListEdgeContainerAppImageSecretsResponseBodyImageSecretList] = None,
        request_id: str = None,
    ):
        # List of image secrets.
        self.image_secret_list = image_secret_list
        # Request ID.
        self.request_id = request_id

    def validate(self):
        if self.image_secret_list:
            for v1 in self.image_secret_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImageSecretList'] = []
        if self.image_secret_list is not None:
            for k1 in self.image_secret_list:
                result['ImageSecretList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.image_secret_list = []
        if m.get('ImageSecretList') is not None:
            for k1 in m.get('ImageSecretList'):
                temp_model = main_models.ListEdgeContainerAppImageSecretsResponseBodyImageSecretList()
                self.image_secret_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListEdgeContainerAppImageSecretsResponseBodyImageSecretList(DaraModel):
    def __init__(
        self,
        name: str = None,
        registry: str = None,
        username: str = None,
    ):
        # Name of the image secret.
        self.name = name
        # Registry address.
        self.registry = registry
        # Username for the image repository
        self.username = username

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.registry is not None:
            result['Registry'] = self.registry

        if self.username is not None:
            result['Username'] = self.username

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Registry') is not None:
            self.registry = m.get('Registry')

        if m.get('Username') is not None:
            self.username = m.get('Username')

        return self


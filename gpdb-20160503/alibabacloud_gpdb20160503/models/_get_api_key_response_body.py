# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_gpdb20160503 import models as main_models
from darabonba.model import DaraModel

class GetApiKeyResponseBody(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        auth_services: List[main_models.GetApiKeyResponseBodyAuthServices] = None,
        create_time: str = None,
        description: str = None,
        key_id: str = None,
        key_name: str = None,
        key_prefix: str = None,
        request_id: str = None,
    ):
        self.api_key = api_key
        self.auth_services = auth_services
        self.create_time = create_time
        self.description = description
        self.key_id = key_id
        self.key_name = key_name
        self.key_prefix = key_prefix
        self.request_id = request_id

    def validate(self):
        if self.auth_services:
            for v1 in self.auth_services:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        result['AuthServices'] = []
        if self.auth_services is not None:
            for k1 in self.auth_services:
                result['AuthServices'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.key_id is not None:
            result['KeyId'] = self.key_id

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.key_prefix is not None:
            result['KeyPrefix'] = self.key_prefix

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        self.auth_services = []
        if m.get('AuthServices') is not None:
            for k1 in m.get('AuthServices'):
                temp_model = main_models.GetApiKeyResponseBodyAuthServices()
                self.auth_services.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('KeyId') is not None:
            self.key_id = m.get('KeyId')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('KeyPrefix') is not None:
            self.key_prefix = m.get('KeyPrefix')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetApiKeyResponseBodyAuthServices(DaraModel):
    def __init__(
        self,
        service_id: str = None,
        service_type: str = None,
    ):
        self.service_id = service_id
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        return self


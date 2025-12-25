# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class CreatePrometheusVirtualInstanceResponseBody(DaraModel):
    def __init__(
        self,
        instance: main_models.CreatePrometheusVirtualInstanceResponseBodyInstance = None,
        request_id: str = None,
    ):
        # Instance ID
        self.instance = instance
        # ID of the request
        self.request_id = request_id

    def validate(self):
        if self.instance:
            self.instance.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance is not None:
            result['instance'] = self.instance.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('instance') is not None:
            temp_model = main_models.CreatePrometheusVirtualInstanceResponseBodyInstance()
            self.instance = temp_model.from_map(m.get('instance'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class CreatePrometheusVirtualInstanceResponseBodyInstance(DaraModel):
    def __init__(
        self,
        created_at: str = None,
        http_api_url: str = None,
        instance_id: str = None,
        namespace: str = None,
        region_id: str = None,
        user_id: str = None,
    ):
        # Creation time
        self.created_at = created_at
        # HTTP API query address
        self.http_api_url = http_api_url
        # Region ID
        self.instance_id = instance_id
        # Cloud product
        self.namespace = namespace
        # User ID
        self.region_id = region_id
        # User ID
        self.user_id = user_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_at is not None:
            result['createdAt'] = self.created_at

        if self.http_api_url is not None:
            result['httpApiUrl'] = self.http_api_url

        if self.instance_id is not None:
            result['instanceId'] = self.instance_id

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.user_id is not None:
            result['userId'] = self.user_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('createdAt') is not None:
            self.created_at = m.get('createdAt')

        if m.get('httpApiUrl') is not None:
            self.http_api_url = m.get('httpApiUrl')

        if m.get('instanceId') is not None:
            self.instance_id = m.get('instanceId')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        return self


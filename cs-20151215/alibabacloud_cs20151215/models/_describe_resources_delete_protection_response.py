# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class DescribeResourcesDeleteProtectionResponse(DaraModel):
    def __init__(
        self,
        headers: Dict[str, str] = None,
        status_code: int = None,
        body: List[main_models.DescribeResourcesDeleteProtectionResponseBody] = None,
    ):
        self.headers = headers
        self.status_code = status_code
        self.body = body

    def validate(self):
        if self.body:
            for v1 in self.body:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['headers'] = self.headers

        if self.status_code is not None:
            result['statusCode'] = self.status_code

        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')

        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')

        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.DescribeResourcesDeleteProtectionResponseBody()
                self.body.append(temp_model.from_map(k1))

        return self

class DescribeResourcesDeleteProtectionResponseBody(DaraModel):
    def __init__(
        self,
        name: str = None,
        namespace: str = None,
        resource: str = None,
        protection: bool = None,
    ):
        # The resource name.
        # 
        # This parameter is required.
        self.name = name
        # The namespace to which the resource belongs.
        self.namespace = namespace
        # The type of the resource.
        self.resource = resource
        # Indicates whether deletion protection is enabled.
        # 
        # *   true: deletion protection is enabled.
        # *   false: deletion protection is disabled.
        self.protection = protection

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['name'] = self.name

        if self.namespace is not None:
            result['namespace'] = self.namespace

        if self.resource is not None:
            result['resource'] = self.resource

        if self.protection is not None:
            result['protection'] = self.protection

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('namespace') is not None:
            self.namespace = m.get('namespace')

        if m.get('resource') is not None:
            self.resource = m.get('resource')

        if m.get('protection') is not None:
            self.protection = m.get('protection')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cs20151215 import models as main_models
from darabonba.model import DaraModel

class InstallClusterAddonsRequest(DaraModel):
    def __init__(
        self,
        body: List[main_models.InstallClusterAddonsRequestBody] = None,
    ):
        # The request body parameters.
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
        result['body'] = []
        if self.body is not None:
            for k1 in self.body:
                result['body'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.body = []
        if m.get('body') is not None:
            for k1 in m.get('body'):
                temp_model = main_models.InstallClusterAddonsRequestBody()
                self.body.append(temp_model.from_map(k1))

        return self

class InstallClusterAddonsRequestBody(DaraModel):
    def __init__(
        self,
        config: str = None,
        name: str = None,
        version: str = None,
    ):
        # The custom parameters of the component, encoded as a JSON string.
        self.config = config
        # The component name. You can call the [ListAddons](https://help.aliyun.com/document_detail/2667939.html) operation to query information about available components, including component names and versions.
        # 
        # This parameter is required.
        self.name = name
        # The component version. You can call the [ListAddons](https://help.aliyun.com/document_detail/2667939.html) operation to query information about available components, including component names and versions.
        # 
        # This parameter is required.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.config is not None:
            result['config'] = self.config

        if self.name is not None:
            result['name'] = self.name

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('config') is not None:
            self.config = m.get('config')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self


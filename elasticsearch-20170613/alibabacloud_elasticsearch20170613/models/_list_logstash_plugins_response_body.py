# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListLogstashPluginsResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.ListLogstashPluginsResponseBodyResult] = None,
    ):
        # The address of the documentation for the plug-in.
        self.request_id = request_id
        # The status of the plug-in. Valid values:
        # 
        # *   INSTALLED: Installed
        # *   UNINSTALLED: Not installed
        # *   INSTALLING: The instance is being installed.
        # *   UNINSTALLING: The instance is being uninstalled.
        # *   UPGRADING: The backup gateway is being upgraded.
        # *   FAILED: Installation failed
        # *   UNKNOWN: The cluster is lost and cannot be created.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListLogstashPluginsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListLogstashPluginsResponseBodyResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        source: str = None,
        specification_url: str = None,
        state: str = None,
    ):
        # The source of the plug-in.
        self.description = description
        self.name = name
        self.source = source
        # The name of the plug-in.
        self.specification_url = specification_url
        self.state = state

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['description'] = self.description

        if self.name is not None:
            result['name'] = self.name

        if self.source is not None:
            result['source'] = self.source

        if self.specification_url is not None:
            result['specificationUrl'] = self.specification_url

        if self.state is not None:
            result['state'] = self.state

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('specificationUrl') is not None:
            self.specification_url = m.get('specificationUrl')

        if m.get('state') is not None:
            self.state = m.get('state')

        return self


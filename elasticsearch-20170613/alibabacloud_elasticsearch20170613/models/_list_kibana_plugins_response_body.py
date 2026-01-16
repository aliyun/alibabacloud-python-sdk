# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_elasticsearch20170613 import models as main_models
from darabonba.model import DaraModel

class ListKibanaPluginsResponseBody(DaraModel):
    def __init__(
        self,
        headers: main_models.ListKibanaPluginsResponseBodyHeaders = None,
        request_id: str = None,
        result: List[main_models.ListKibanaPluginsResponseBodyResult] = None,
    ):
        # The request header.
        self.headers = headers
        # The request ID.
        self.request_id = request_id
        # The information about the plug-ins.
        self.result = result

    def validate(self):
        if self.headers:
            self.headers.validate()
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.headers is not None:
            result['Headers'] = self.headers.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Headers') is not None:
            temp_model = main_models.ListKibanaPluginsResponseBodyHeaders()
            self.headers = temp_model.from_map(m.get('Headers'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListKibanaPluginsResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class ListKibanaPluginsResponseBodyResult(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        source: str = None,
        specification_url: str = None,
        state: str = None,
    ):
        # The description of the plug-in.
        self.description = description
        # The name of the plug-in.
        self.name = name
        # The source of the plug-in.
        self.source = source
        # The URL of the introduction to the plug-in. The value null is supported.
        self.specification_url = specification_url
        # The installation status of the plug-in.
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

class ListKibanaPluginsResponseBodyHeaders(DaraModel):
    def __init__(
        self,
        x_total_count: int = None,
    ):
        # The total number of entries returned.
        self.x_total_count = x_total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x_total_count is not None:
            result['X-Total-Count'] = self.x_total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X-Total-Count') is not None:
            self.x_total_count = m.get('X-Total-Count')

        return self


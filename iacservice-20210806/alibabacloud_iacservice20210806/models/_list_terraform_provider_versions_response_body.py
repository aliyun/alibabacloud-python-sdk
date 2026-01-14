# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_iacservice20210806 import models as main_models
from darabonba.model import DaraModel

class ListTerraformProviderVersionsResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
        versions: List[main_models.ListTerraformProviderVersionsResponseBodyVersions] = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        self.request_id = request_id
        self.total_count = total_count
        self.versions = versions

    def validate(self):
        if self.versions:
            for v1 in self.versions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['maxResults'] = self.max_results

        if self.next_token is not None:
            result['nextToken'] = self.next_token

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        result['versions'] = []
        if self.versions is not None:
            for k1 in self.versions:
                result['versions'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('maxResults') is not None:
            self.max_results = m.get('maxResults')

        if m.get('nextToken') is not None:
            self.next_token = m.get('nextToken')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        self.versions = []
        if m.get('versions') is not None:
            for k1 in m.get('versions'):
                temp_model = main_models.ListTerraformProviderVersionsResponseBodyVersions()
                self.versions.append(temp_model.from_map(k1))

        return self

class ListTerraformProviderVersionsResponseBodyVersions(DaraModel):
    def __init__(
        self,
        published_time: str = None,
        status: str = None,
        version: str = None,
    ):
        self.published_time = published_time
        self.status = status
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.published_time is not None:
            result['publishedTime'] = self.published_time

        if self.status is not None:
            result['status'] = self.status

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('publishedTime') is not None:
            self.published_time = m.get('publishedTime')

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self


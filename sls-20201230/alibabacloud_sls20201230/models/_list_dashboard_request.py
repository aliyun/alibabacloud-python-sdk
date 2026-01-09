# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ListDashboardRequest(DaraModel):
    def __init__(
        self,
        dashboard_name: str = None,
        display_name: str = None,
        offset: int = None,
        size: int = None,
        tags: List[main_models.ListDashboardRequestTags] = None,
    ):
        self.dashboard_name = dashboard_name
        self.display_name = display_name
        # The line from which the query starts. Default value: 0.
        self.offset = offset
        # The number of entries per page. Maximum value: 500. Default value: 500.
        self.size = size
        self.tags = tags

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_name is not None:
            result['dashboardName'] = self.dashboard_name

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.offset is not None:
            result['offset'] = self.offset

        if self.size is not None:
            result['size'] = self.size

        result['tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['tags'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dashboardName') is not None:
            self.dashboard_name = m.get('dashboardName')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('offset') is not None:
            self.offset = m.get('offset')

        if m.get('size') is not None:
            self.size = m.get('size')

        self.tags = []
        if m.get('tags') is not None:
            for k1 in m.get('tags'):
                temp_model = main_models.ListDashboardRequestTags()
                self.tags.append(temp_model.from_map(k1))

        return self

class ListDashboardRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        self.key = key
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['key'] = self.key

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('key') is not None:
            self.key = m.get('key')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self


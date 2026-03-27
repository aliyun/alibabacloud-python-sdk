# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListPrometheusDashboardsResponseBody(DaraModel):
    def __init__(
        self,
        prometheus_dashboards: List[main_models.ListPrometheusDashboardsResponseBodyPrometheusDashboards] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # List of Prometheus instance dashboards.
        self.prometheus_dashboards = prometheus_dashboards
        # ID of the request
        self.request_id = request_id
        # Total number of instances
        self.total_count = total_count

    def validate(self):
        if self.prometheus_dashboards:
            for v1 in self.prometheus_dashboards:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['prometheusDashboards'] = []
        if self.prometheus_dashboards is not None:
            for k1 in self.prometheus_dashboards:
                result['prometheusDashboards'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total_count is not None:
            result['totalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.prometheus_dashboards = []
        if m.get('prometheusDashboards') is not None:
            for k1 in m.get('prometheusDashboards'):
                temp_model = main_models.ListPrometheusDashboardsResponseBodyPrometheusDashboards()
                self.prometheus_dashboards.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('totalCount') is not None:
            self.total_count = m.get('totalCount')

        return self

class ListPrometheusDashboardsResponseBodyPrometheusDashboards(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
        tags: List[str] = None,
        title: str = None,
        uid: str = None,
        url: str = None,
    ):
        # Dashboard ID.
        self.id = id
        # Dashboard name.
        self.name = name
        # Tags.
        self.tags = tags
        # Dashboard title.
        self.title = title
        # Dashboard UID.
        self.uid = uid
        # Dashboard URL address.
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.tags is not None:
            result['tags'] = self.tags

        if self.title is not None:
            result['title'] = self.title

        if self.uid is not None:
            result['uid'] = self.uid

        if self.url is not None:
            result['url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self


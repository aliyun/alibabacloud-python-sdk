# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class ListIntegrationPolicyDashboardsResponseBody(DaraModel):
    def __init__(
        self,
        dashboards: List[main_models.ListIntegrationPolicyDashboardsResponseBodyDashboards] = None,
        request_id: str = None,
        total: int = None,
    ):
        # List of dashboards.
        self.dashboards = dashboards
        # ID of the request
        self.request_id = request_id
        # Number of components.
        self.total = total

    def validate(self):
        if self.dashboards:
            for v1 in self.dashboards:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dashboards'] = []
        if self.dashboards is not None:
            for k1 in self.dashboards:
                result['dashboards'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.total is not None:
            result['total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboards = []
        if m.get('dashboards') is not None:
            for k1 in m.get('dashboards'):
                temp_model = main_models.ListIntegrationPolicyDashboardsResponseBodyDashboards()
                self.dashboards.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('total') is not None:
            self.total = m.get('total')

        return self

class ListIntegrationPolicyDashboardsResponseBodyDashboards(DaraModel):
    def __init__(
        self,
        engine: str = None,
        folder_uid: str = None,
        name: str = None,
        region: str = None,
        tags: List[str] = None,
        title: str = None,
        uid: str = None,
        url: str = None,
    ):
        # Dashboard engine:
        # grafana: shared grafana.
        # cms: cms self-developed dashboard engine.
        self.engine = engine
        # UID of the dashboard folder.
        self.folder_uid = folder_uid
        # Dashboard name
        self.name = name
        # Region
        self.region = region
        # List of tags.
        self.tags = tags
        # Title of the UI module (not name)
        self.title = title
        # ID of the current Alibaba Cloud primary account, read-only
        self.uid = uid
        # pagerDuty integration webhook. Supports V1 and V2 versions
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.engine is not None:
            result['engine'] = self.engine

        if self.folder_uid is not None:
            result['folderUid'] = self.folder_uid

        if self.name is not None:
            result['name'] = self.name

        if self.region is not None:
            result['region'] = self.region

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
        if m.get('engine') is not None:
            self.engine = m.get('engine')

        if m.get('folderUid') is not None:
            self.folder_uid = m.get('folderUid')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('tags') is not None:
            self.tags = m.get('tags')

        if m.get('title') is not None:
            self.title = m.get('title')

        if m.get('uid') is not None:
            self.uid = m.get('uid')

        if m.get('url') is not None:
            self.url = m.get('url')

        return self


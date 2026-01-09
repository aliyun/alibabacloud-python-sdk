# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class ListDashboardResponseBody(DaraModel):
    def __init__(
        self,
        dashboard_items: List[main_models.ListDashboardResponseBodyDashboardItems] = None,
        dashboards: List[str] = None,
    ):
        # The details of the dashboard.
        self.dashboard_items = dashboard_items
        # The queried dashboards. Each dashboard in the array is specified by dashboardName.
        self.dashboards = dashboards

    def validate(self):
        if self.dashboard_items:
            for v1 in self.dashboard_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['dashboardItems'] = []
        if self.dashboard_items is not None:
            for k1 in self.dashboard_items:
                result['dashboardItems'].append(k1.to_map() if k1 else None)

        if self.dashboards is not None:
            result['dashboards'] = self.dashboards

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.dashboard_items = []
        if m.get('dashboardItems') is not None:
            for k1 in m.get('dashboardItems'):
                temp_model = main_models.ListDashboardResponseBodyDashboardItems()
                self.dashboard_items.append(temp_model.from_map(k1))

        if m.get('dashboards') is not None:
            self.dashboards = m.get('dashboards')

        return self

class ListDashboardResponseBodyDashboardItems(DaraModel):
    def __init__(
        self,
        dashboard_name: str = None,
        description: str = None,
        display_name: str = None,
    ):
        # The dashboard ID. The ID must be unique in a project. Fuzzy search is supported. For example, if you enter da, all dashboards whose IDs start with da are queried.
        self.dashboard_name = dashboard_name
        self.description = description
        # The display name of the dashboard.
        self.display_name = display_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dashboard_name is not None:
            result['dashboardName'] = self.dashboard_name

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('dashboardName') is not None:
            self.dashboard_name = m.get('dashboardName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        return self


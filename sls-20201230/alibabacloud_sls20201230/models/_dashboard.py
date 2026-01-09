# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class Dashboard(DaraModel):
    def __init__(
        self,
        attribute: Dict[str, str] = None,
        charts: List[main_models.Chart] = None,
        dashboard_name: str = None,
        description: str = None,
        display_name: str = None,
    ):
        self.attribute = attribute
        # This parameter is required.
        self.charts = charts
        # This parameter is required.
        self.dashboard_name = dashboard_name
        self.description = description
        # This parameter is required.
        self.display_name = display_name

    def validate(self):
        if self.charts:
            for v1 in self.charts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.attribute is not None:
            result['attribute'] = self.attribute

        result['charts'] = []
        if self.charts is not None:
            for k1 in self.charts:
                result['charts'].append(k1.to_map() if k1 else None)

        if self.dashboard_name is not None:
            result['dashboardName'] = self.dashboard_name

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['displayName'] = self.display_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('attribute') is not None:
            self.attribute = m.get('attribute')

        self.charts = []
        if m.get('charts') is not None:
            for k1 in m.get('charts'):
                temp_model = main_models.Chart()
                self.charts.append(temp_model.from_map(k1))

        if m.get('dashboardName') is not None:
            self.dashboard_name = m.get('dashboardName')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        return self


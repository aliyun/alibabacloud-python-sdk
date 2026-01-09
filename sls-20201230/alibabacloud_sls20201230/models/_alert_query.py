# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AlertQuery(DaraModel):
    def __init__(
        self,
        chart_title: str = None,
        dashboard_id: str = None,
        end: str = None,
        power_sql_mode: str = None,
        project: str = None,
        query: str = None,
        region: str = None,
        role_arn: str = None,
        start: str = None,
        store: str = None,
        store_type: str = None,
        time_span_type: str = None,
        ui: str = None,
    ):
        self.chart_title = chart_title
        self.dashboard_id = dashboard_id
        # This parameter is required.
        self.end = end
        self.power_sql_mode = power_sql_mode
        # This parameter is required.
        self.project = project
        # This parameter is required.
        self.query = query
        # This parameter is required.
        self.region = region
        self.role_arn = role_arn
        # This parameter is required.
        self.start = start
        # This parameter is required.
        self.store = store
        # This parameter is required.
        self.store_type = store_type
        # This parameter is required.
        self.time_span_type = time_span_type
        self.ui = ui

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chart_title is not None:
            result['chartTitle'] = self.chart_title

        if self.dashboard_id is not None:
            result['dashboardId'] = self.dashboard_id

        if self.end is not None:
            result['end'] = self.end

        if self.power_sql_mode is not None:
            result['powerSqlMode'] = self.power_sql_mode

        if self.project is not None:
            result['project'] = self.project

        if self.query is not None:
            result['query'] = self.query

        if self.region is not None:
            result['region'] = self.region

        if self.role_arn is not None:
            result['roleArn'] = self.role_arn

        if self.start is not None:
            result['start'] = self.start

        if self.store is not None:
            result['store'] = self.store

        if self.store_type is not None:
            result['storeType'] = self.store_type

        if self.time_span_type is not None:
            result['timeSpanType'] = self.time_span_type

        if self.ui is not None:
            result['ui'] = self.ui

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('chartTitle') is not None:
            self.chart_title = m.get('chartTitle')

        if m.get('dashboardId') is not None:
            self.dashboard_id = m.get('dashboardId')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('powerSqlMode') is not None:
            self.power_sql_mode = m.get('powerSqlMode')

        if m.get('project') is not None:
            self.project = m.get('project')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('roleArn') is not None:
            self.role_arn = m.get('roleArn')

        if m.get('start') is not None:
            self.start = m.get('start')

        if m.get('store') is not None:
            self.store = m.get('store')

        if m.get('storeType') is not None:
            self.store_type = m.get('storeType')

        if m.get('timeSpanType') is not None:
            self.time_span_type = m.get('timeSpanType')

        if m.get('ui') is not None:
            self.ui = m.get('ui')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class QueryApmGrafanaDataRequest(DaraModel):
    def __init__(
        self,
        component_name: str = None,
        dashboard_id: str = None,
        end: str = None,
        provider: str = None,
        query: str = None,
        query_params: main_models.QueryApmGrafanaDataRequestQueryParams = None,
        query_url: str = None,
        region_id: str = None,
        start: str = None,
        step: str = None,
        time: str = None,
        variables: str = None,
        workspace_id: str = None,
    ):
        # The name of the monitoring dashboard.
        self.component_name = component_name
        # The dashboard ID.
        self.dashboard_id = dashboard_id
        # The end time of the query. The value is a UNIX timestamp in seconds.
        self.end = end
        # The datasource provider.
        self.provider = provider
        # The PromQL query expression.
        self.query = query
        # The panel-level query parameters.
        self.query_params = query_params
        # The Grafana datasource proxy path.
        # 
        # This parameter is required.
        self.query_url = query_url
        # The region ID.
        self.region_id = region_id
        # The start time of the query. The value is a UNIX timestamp in seconds.
        self.start = start
        # The query step, in seconds.
        self.step = step
        # The time point for an instant query. The value is a UNIX timestamp in seconds.
        self.time = time
        # The dashboard variables, as a JSON string.
        self.variables = variables
        # The workspace ID.
        # 
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.query_params:
            self.query_params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.component_name is not None:
            result['componentName'] = self.component_name

        if self.dashboard_id is not None:
            result['dashboardId'] = self.dashboard_id

        if self.end is not None:
            result['end'] = self.end

        if self.provider is not None:
            result['provider'] = self.provider

        if self.query is not None:
            result['query'] = self.query

        if self.query_params is not None:
            result['queryParams'] = self.query_params.to_map()

        if self.query_url is not None:
            result['queryUrl'] = self.query_url

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.start is not None:
            result['start'] = self.start

        if self.step is not None:
            result['step'] = self.step

        if self.time is not None:
            result['time'] = self.time

        if self.variables is not None:
            result['variables'] = self.variables

        if self.workspace_id is not None:
            result['workspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('componentName') is not None:
            self.component_name = m.get('componentName')

        if m.get('dashboardId') is not None:
            self.dashboard_id = m.get('dashboardId')

        if m.get('end') is not None:
            self.end = m.get('end')

        if m.get('provider') is not None:
            self.provider = m.get('provider')

        if m.get('query') is not None:
            self.query = m.get('query')

        if m.get('queryParams') is not None:
            temp_model = main_models.QueryApmGrafanaDataRequestQueryParams()
            self.query_params = temp_model.from_map(m.get('queryParams'))

        if m.get('queryUrl') is not None:
            self.query_url = m.get('queryUrl')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('start') is not None:
            self.start = m.get('start')

        if m.get('step') is not None:
            self.step = m.get('step')

        if m.get('time') is not None:
            self.time = m.get('time')

        if m.get('variables') is not None:
            self.variables = m.get('variables')

        if m.get('workspaceId') is not None:
            self.workspace_id = m.get('workspaceId')

        return self

class QueryApmGrafanaDataRequestQueryParams(DaraModel):
    def __init__(
        self,
        panel_id: int = None,
        ref_id: str = None,
        variable_name: str = None,
    ):
        # The panel ID.
        self.panel_id = panel_id
        # The query reference ID in the panel.
        self.ref_id = ref_id
        # The variable name. Used when querying the dropdown values of dashboard variables.
        self.variable_name = variable_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.panel_id is not None:
            result['panelId'] = self.panel_id

        if self.ref_id is not None:
            result['refId'] = self.ref_id

        if self.variable_name is not None:
            result['variableName'] = self.variable_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('panelId') is not None:
            self.panel_id = m.get('panelId')

        if m.get('refId') is not None:
            self.ref_id = m.get('refId')

        if m.get('variableName') is not None:
            self.variable_name = m.get('variableName')

        return self


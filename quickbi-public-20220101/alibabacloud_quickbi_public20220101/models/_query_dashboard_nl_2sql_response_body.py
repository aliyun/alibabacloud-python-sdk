# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_quickbi_public20220101 import models as main_models
from darabonba.model import DaraModel

class QueryDashboardNl2sqlResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.QueryDashboardNl2sqlResponseBodyResult] = None,
        success: bool = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The execution result of the API operation. Valid values:
        # 
        # - true: The request succeeded.
        # - false: The request failed.
        self.result = result
        # Specifies whether the request is successful. Valid values: 
        # 
        # - true: The request succeeded.
        # - false: The request failed.
        self.success = success

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

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.QueryDashboardNl2sqlResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryDashboardNl2sqlResponseBodyResult(DaraModel):
    def __init__(
        self,
        authorities: List[str] = None,
        dashboard_name: str = None,
        dashboard_nl_2sql_id: str = None,
        owner_id: str = None,
    ):
        # The permissions on the dashboard NL2SQL resource. If this parameter has a value and contains READ, it indicates that the user has NL2SQL permissions on the dashboard NL2SQL resource.
        self.authorities = authorities
        # The name of the dashboard.
        self.dashboard_name = dashboard_name
        # The NL2SQL resource ID of the dashboard.
        self.dashboard_nl_2sql_id = dashboard_nl_2sql_id
        # The user ID of the dashboard creator.
        self.owner_id = owner_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.authorities is not None:
            result['Authorities'] = self.authorities

        if self.dashboard_name is not None:
            result['DashboardName'] = self.dashboard_name

        if self.dashboard_nl_2sql_id is not None:
            result['DashboardNl2sqlId'] = self.dashboard_nl_2sql_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Authorities') is not None:
            self.authorities = m.get('Authorities')

        if m.get('DashboardName') is not None:
            self.dashboard_name = m.get('DashboardName')

        if m.get('DashboardNl2sqlId') is not None:
            self.dashboard_nl_2sql_id = m.get('DashboardNl2sqlId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListLogicTableRouteConfigResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        logic_table_route_config_list: main_models.ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigList = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned.
        self.error_code = error_code
        # The error message returned.
        self.error_message = error_message
        # The routing algorithms.
        self.logic_table_route_config_list = logic_table_route_config_list
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - **true**: The request was successful.
        # - **false**: The request failed.
        self.success = success

    def validate(self):
        if self.logic_table_route_config_list:
            self.logic_table_route_config_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.logic_table_route_config_list is not None:
            result['LogicTableRouteConfigList'] = self.logic_table_route_config_list.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('LogicTableRouteConfigList') is not None:
            temp_model = main_models.ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigList()
            self.logic_table_route_config_list = temp_model.from_map(m.get('LogicTableRouteConfigList'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigList(DaraModel):
    def __init__(
        self,
        logic_table_route_config: List[main_models.ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigListLogicTableRouteConfig] = None,
    ):
        self.logic_table_route_config = logic_table_route_config

    def validate(self):
        if self.logic_table_route_config:
            for v1 in self.logic_table_route_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LogicTableRouteConfig'] = []
        if self.logic_table_route_config is not None:
            for k1 in self.logic_table_route_config:
                result['LogicTableRouteConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.logic_table_route_config = []
        if m.get('LogicTableRouteConfig') is not None:
            for k1 in m.get('LogicTableRouteConfig'):
                temp_model = main_models.ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigListLogicTableRouteConfig()
                self.logic_table_route_config.append(temp_model.from_map(k1))

        return self

class ListLogicTableRouteConfigResponseBodyLogicTableRouteConfigListLogicTableRouteConfig(DaraModel):
    def __init__(
        self,
        route_expr: str = None,
        route_key: str = None,
        table_id: int = None,
    ):
        # The routing algorithm expression.
        self.route_expr = route_expr
        # The unique key of the routing algorithm.
        self.route_key = route_key
        # The ID of the logical table.
        self.table_id = table_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_expr is not None:
            result['RouteExpr'] = self.route_expr

        if self.route_key is not None:
            result['RouteKey'] = self.route_key

        if self.table_id is not None:
            result['TableId'] = self.table_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteExpr') is not None:
            self.route_expr = m.get('RouteExpr')

        if m.get('RouteKey') is not None:
            self.route_key = m.get('RouteKey')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        return self


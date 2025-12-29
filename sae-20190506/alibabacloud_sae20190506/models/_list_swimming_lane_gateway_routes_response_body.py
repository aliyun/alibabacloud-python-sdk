# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class ListSwimmingLaneGatewayRoutesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListSwimmingLaneGatewayRoutesResponseBodyData] = None,
        error_code: str = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trace_id: str = None,
    ):
        # The HTTP status code. Valid values:
        # 
        # *   **2xx**: The request was successful.
        # *   **3xx**: The request was redirected.
        # *   **4xx**: The request failed.
        # *   **5xx**: A server error occurred.
        self.code = code
        # Responses.
        self.data = data
        # The status code. Value values:
        # 
        # *   If the request was successful, **ErrorCode** is not returned.
        # *   If the request failed, **ErrorCode** is returned. For more information, see **Error codes** in this topic.
        self.error_code = error_code
        # Additional information. Valid values:
        # 
        # *   The error message returned because the request is normal and **success** is returned.
        # *   If the request is abnormal, the specific exception error code is returned.
        self.message = message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values: Valid values:
        # 
        # *   **true**: The configurations were obtained.
        # *   **false**: The configurations failed to be queried.
        self.success = success
        # The ID of the trace. This parameter is used to query the exact call information.
        self.trace_id = trace_id

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSwimmingLaneGatewayRoutesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self

class ListSwimmingLaneGatewayRoutesResponseBodyData(DaraModel):
    def __init__(
        self,
        route_id: int = None,
        route_name: str = None,
        route_predicate: main_models.ListSwimmingLaneGatewayRoutesResponseBodyDataRoutePredicate = None,
    ):
        # The ID of the route.
        self.route_id = route_id
        # The name of the route.
        self.route_name = route_name
        # The routing rule.
        self.route_predicate = route_predicate

    def validate(self):
        if self.route_predicate:
            self.route_predicate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.route_id is not None:
            result['RouteId'] = self.route_id

        if self.route_name is not None:
            result['RouteName'] = self.route_name

        if self.route_predicate is not None:
            result['RoutePredicate'] = self.route_predicate.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')

        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')

        if m.get('RoutePredicate') is not None:
            temp_model = main_models.ListSwimmingLaneGatewayRoutesResponseBodyDataRoutePredicate()
            self.route_predicate = temp_model.from_map(m.get('RoutePredicate'))

        return self

class ListSwimmingLaneGatewayRoutesResponseBodyDataRoutePredicate(DaraModel):
    def __init__(
        self,
        path_predicate: main_models.ListSwimmingLaneGatewayRoutesResponseBodyDataRoutePredicatePathPredicate = None,
    ):
        # The path matching rule.
        self.path_predicate = path_predicate

    def validate(self):
        if self.path_predicate:
            self.path_predicate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path_predicate is not None:
            result['PathPredicate'] = self.path_predicate.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PathPredicate') is not None:
            temp_model = main_models.ListSwimmingLaneGatewayRoutesResponseBodyDataRoutePredicatePathPredicate()
            self.path_predicate = temp_model.from_map(m.get('PathPredicate'))

        return self

class ListSwimmingLaneGatewayRoutesResponseBodyDataRoutePredicatePathPredicate(DaraModel):
    def __init__(
        self,
        path: str = None,
        type: str = None,
    ):
        # The route URL.
        self.path = path
        # The type of the protection rule.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


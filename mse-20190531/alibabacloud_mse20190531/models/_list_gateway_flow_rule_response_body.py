# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mse20190531 import models as main_models
from darabonba.model import DaraModel

class ListGatewayFlowRuleResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListGatewayFlowRuleResponseBodyData = None,
        request_id: str = None,
    ):
        # The Meta return information.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.ListGatewayFlowRuleResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListGatewayFlowRuleResponseBodyData(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        result: List[main_models.ListGatewayFlowRuleResponseBodyDataResult] = None,
        results: List[main_models.ListGatewayFlowRuleResponseBodyDataResults] = None,
        total_size: int = None,
    ):
        # The page number of the instance list.
        self.page_number = page_number
        # The number of rows per page set during input.
        self.page_size = page_size
        # The returned data.
        self.result = result
        # The paged data collection.
        self.results = results
        # The total number of instances queried.
        self.total_size = total_size

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.ListGatewayFlowRuleResponseBodyDataResult()
                self.result.append(temp_model.from_map(k1))

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.ListGatewayFlowRuleResponseBodyDataResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListGatewayFlowRuleResponseBodyDataResults(DaraModel):
    def __init__(
        self,
        behavior_type: int = None,
        body_encoding: int = None,
        enable: int = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
        id_list: List[int] = None,
        limit_mode: int = None,
        response_additional_headers: str = None,
        response_content_body: str = None,
        response_redirect_url: str = None,
        response_status_code: int = None,
        route_id: int = None,
        route_name: str = None,
        stat_duration_ms: int = None,
        threshold: int = None,
    ):
        # The Web fallback behavior type.
        # 
        # 0: Return specified content
        # 
        # 1: Redirect to specified page
        self.behavior_type = behavior_type
        # The encoding type.
        # 
        # 0: Plain text
        # 
        # 1: JSON
        self.body_encoding = body_encoding
        # Indicates whether the rule is enabled.
        # 
        # 0: Disabled.
        # 
        # 1: Enabled.
        self.enable = enable
        # The gateway ID.
        self.gateway_id = gateway_id
        # The unique gateway identity ID.
        self.gateway_unique_id = gateway_unique_id
        # The routing throttle rule ID.
        self.id = id
        # The filtered rule IDs.
        self.id_list = id_list
        # The threshold conversion mode.
        # 
        # 0: Single machine.
        # 
        # 1: Cluster.
        # 
        # 2: Cluster to single machine.
        self.limit_mode = limit_mode
        # The custom headers, entered as key-value pairs.
        self.response_additional_headers = response_additional_headers
        # The HTTP response text.
        self.response_content_body = response_content_body
        # The redirect URL.
        self.response_redirect_url = response_redirect_url
        # The HTTP status code.
        self.response_status_code = response_status_code
        # The routing ID.
        self.route_id = route_id
        # The routing name.
        self.route_name = route_name
        # The statistics duration.
        self.stat_duration_ms = stat_duration_ms
        # The overall QPS threshold.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.behavior_type is not None:
            result['BehaviorType'] = self.behavior_type

        if self.body_encoding is not None:
            result['BodyEncoding'] = self.body_encoding

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.id is not None:
            result['Id'] = self.id

        if self.id_list is not None:
            result['IdList'] = self.id_list

        if self.limit_mode is not None:
            result['LimitMode'] = self.limit_mode

        if self.response_additional_headers is not None:
            result['ResponseAdditionalHeaders'] = self.response_additional_headers

        if self.response_content_body is not None:
            result['ResponseContentBody'] = self.response_content_body

        if self.response_redirect_url is not None:
            result['ResponseRedirectUrl'] = self.response_redirect_url

        if self.response_status_code is not None:
            result['ResponseStatusCode'] = self.response_status_code

        if self.route_id is not None:
            result['RouteId'] = self.route_id

        if self.route_name is not None:
            result['RouteName'] = self.route_name

        if self.stat_duration_ms is not None:
            result['StatDurationMs'] = self.stat_duration_ms

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BehaviorType') is not None:
            self.behavior_type = m.get('BehaviorType')

        if m.get('BodyEncoding') is not None:
            self.body_encoding = m.get('BodyEncoding')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IdList') is not None:
            self.id_list = m.get('IdList')

        if m.get('LimitMode') is not None:
            self.limit_mode = m.get('LimitMode')

        if m.get('ResponseAdditionalHeaders') is not None:
            self.response_additional_headers = m.get('ResponseAdditionalHeaders')

        if m.get('ResponseContentBody') is not None:
            self.response_content_body = m.get('ResponseContentBody')

        if m.get('ResponseRedirectUrl') is not None:
            self.response_redirect_url = m.get('ResponseRedirectUrl')

        if m.get('ResponseStatusCode') is not None:
            self.response_status_code = m.get('ResponseStatusCode')

        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')

        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')

        if m.get('StatDurationMs') is not None:
            self.stat_duration_ms = m.get('StatDurationMs')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self

class ListGatewayFlowRuleResponseBodyDataResult(DaraModel):
    def __init__(
        self,
        behavior_type: int = None,
        body_encoding: int = None,
        enable: int = None,
        gateway_id: int = None,
        gateway_unique_id: str = None,
        id: int = None,
        response_content_body: str = None,
        response_redirect_url: str = None,
        response_status_code: int = None,
        route_id: int = None,
        route_name: str = None,
        threshold: int = None,
    ):
        # The Web fallback behavior type.
        # 
        # 0: Return specified content
        # 
        # 1: Redirect to specified page
        self.behavior_type = behavior_type
        # The encoding type.
        # 
        # 0: Plain text
        # 
        # 1: JSON
        self.body_encoding = body_encoding
        # Indicates whether the rule is enabled.
        # 
        # 0: Disabled.
        # 
        # 1: Enabled.
        self.enable = enable
        # The gateway ID.
        self.gateway_id = gateway_id
        # The unique gateway identity ID.
        self.gateway_unique_id = gateway_unique_id
        # The routing throttle rule ID.
        self.id = id
        # The HTTP response text.
        self.response_content_body = response_content_body
        # The redirect URL.
        self.response_redirect_url = response_redirect_url
        # The HTTP status code.
        self.response_status_code = response_status_code
        # The routing ID.
        self.route_id = route_id
        # The routing name.
        self.route_name = route_name
        # The overall QPS threshold.
        self.threshold = threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.behavior_type is not None:
            result['BehaviorType'] = self.behavior_type

        if self.body_encoding is not None:
            result['BodyEncoding'] = self.body_encoding

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.gateway_id is not None:
            result['GatewayId'] = self.gateway_id

        if self.gateway_unique_id is not None:
            result['GatewayUniqueId'] = self.gateway_unique_id

        if self.id is not None:
            result['Id'] = self.id

        if self.response_content_body is not None:
            result['ResponseContentBody'] = self.response_content_body

        if self.response_redirect_url is not None:
            result['ResponseRedirectUrl'] = self.response_redirect_url

        if self.response_status_code is not None:
            result['ResponseStatusCode'] = self.response_status_code

        if self.route_id is not None:
            result['RouteId'] = self.route_id

        if self.route_name is not None:
            result['RouteName'] = self.route_name

        if self.threshold is not None:
            result['Threshold'] = self.threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BehaviorType') is not None:
            self.behavior_type = m.get('BehaviorType')

        if m.get('BodyEncoding') is not None:
            self.body_encoding = m.get('BodyEncoding')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('GatewayId') is not None:
            self.gateway_id = m.get('GatewayId')

        if m.get('GatewayUniqueId') is not None:
            self.gateway_unique_id = m.get('GatewayUniqueId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ResponseContentBody') is not None:
            self.response_content_body = m.get('ResponseContentBody')

        if m.get('ResponseRedirectUrl') is not None:
            self.response_redirect_url = m.get('ResponseRedirectUrl')

        if m.get('ResponseStatusCode') is not None:
            self.response_status_code = m.get('ResponseStatusCode')

        if m.get('RouteId') is not None:
            self.route_id = m.get('RouteId')

        if m.get('RouteName') is not None:
            self.route_name = m.get('RouteName')

        if m.get('Threshold') is not None:
            self.threshold = m.get('Threshold')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_wss20211221 import models as main_models
from darabonba.model import DaraModel

class DescribeAICallDetailsResponseBody(DaraModel):
    def __init__(
        self,
        call_details: List[main_models.DescribeAICallDetailsResponseBodyCallDetails] = None,
        page_number: int = None,
        page_size: int = None,
        query_end_time: str = None,
        query_start_time: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of AI invocation details on the current page. If no records exist, an empty array is returned.
        self.call_details = call_details
        # The current page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The actual end time of the query, in ISO 8601 format and UTC+08:00 time zone. Reuse this value when you turn pages.
        self.query_end_time = query_end_time
        # The actual start time of the query, in ISO 8601 format and UTC+08:00 time zone. Reuse this value when you turn pages.
        self.query_start_time = query_start_time
        # The request ID of the current API operation, which is used to troubleshoot issues.
        self.request_id = request_id
        # The total number of invocation records that meet the query conditions, including records that do not match any deducted points.
        self.total_count = total_count

    def validate(self):
        if self.call_details:
            for v1 in self.call_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CallDetails'] = []
        if self.call_details is not None:
            for k1 in self.call_details:
                result['CallDetails'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.query_end_time is not None:
            result['QueryEndTime'] = self.query_end_time

        if self.query_start_time is not None:
            result['QueryStartTime'] = self.query_start_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.call_details = []
        if m.get('CallDetails') is not None:
            for k1 in m.get('CallDetails'):
                temp_model = main_models.DescribeAICallDetailsResponseBodyCallDetails()
                self.call_details.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('QueryEndTime') is not None:
            self.query_end_time = m.get('QueryEndTime')

        if m.get('QueryStartTime') is not None:
            self.query_start_time = m.get('QueryStartTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAICallDetailsResponseBodyCallDetails(DaraModel):
    def __init__(
        self,
        agent_type: str = None,
        call_status: str = None,
        call_time: str = None,
        first_token_latency_ms: int = None,
        gateway_region: str = None,
        http_status_code: int = None,
        input_token: int = None,
        instance_id: str = None,
        model: str = None,
        points: str = None,
        points_breakdown: main_models.DescribeAICallDetailsResponseBodyCallDetailsPointsBreakdown = None,
        request_id: str = None,
        wy_id: str = None,
    ):
        # The product or agent type associated with the invocation, which retains the original value from the deduction record. If no match is found or the query fails, this parameter is not returned.
        self.agent_type = agent_type
        # The invocation status. Valid values: SUCCESS (successful, HTTP 2xx), RATE_LIMITED (throttled, HTTP 429), TIMEOUT (timed out, HTTP 504), and FAILED (other failure statuses).
        self.call_status = call_status
        # The time of the model invocation log, in ISO 8601 format and UTC+08:00 time zone.
        self.call_time = call_time
        # The latency of the first token, in milliseconds. If the invocation fails or no first token data exists, this parameter is empty.
        self.first_token_latency_ms = first_token_latency_ms
        # The actual data region of the invocation log.
        self.gateway_region = gateway_region
        # The HTTP status code returned by the AI gateway.
        self.http_status_code = http_status_code
        # The number of original input tokens. If no valid data exists, this parameter is empty.
        self.input_token = input_token
        # The instance ID of the product associated with the model invocation.
        self.instance_id = instance_id
        # The ID of the actually invoked model. If the actual model is missing, the requested model is used as a fallback.
        self.model = model
        # The actual deducted points matched, returned as a decimal string. A true zero value is returned as 0. If no match is found or the query fails, this parameter is not returned. Do not treat a missing value as zero.
        self.points = points
        # The point breakdown of the matched deduction record for this invocation, which comes from the same record as Points. If valid details are missing, this object is not returned. If the object exists, all five point types are returned. The sum of the five point types equals Points, and a true zero value is returned as the string 0.
        self.points_breakdown = points_breakdown
        # The request ID of the AI gateway invocation, which is different from the request ID of the outer API operation.
        self.request_id = request_id
        # The ID of the user who initiated the model invocation. If no valid data exists, this parameter is empty.
        self.wy_id = wy_id

    def validate(self):
        if self.points_breakdown:
            self.points_breakdown.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_type is not None:
            result['AgentType'] = self.agent_type

        if self.call_status is not None:
            result['CallStatus'] = self.call_status

        if self.call_time is not None:
            result['CallTime'] = self.call_time

        if self.first_token_latency_ms is not None:
            result['FirstTokenLatencyMs'] = self.first_token_latency_ms

        if self.gateway_region is not None:
            result['GatewayRegion'] = self.gateway_region

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.input_token is not None:
            result['InputToken'] = self.input_token

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.model is not None:
            result['Model'] = self.model

        if self.points is not None:
            result['Points'] = self.points

        if self.points_breakdown is not None:
            result['PointsBreakdown'] = self.points_breakdown.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.wy_id is not None:
            result['WyId'] = self.wy_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentType') is not None:
            self.agent_type = m.get('AgentType')

        if m.get('CallStatus') is not None:
            self.call_status = m.get('CallStatus')

        if m.get('CallTime') is not None:
            self.call_time = m.get('CallTime')

        if m.get('FirstTokenLatencyMs') is not None:
            self.first_token_latency_ms = m.get('FirstTokenLatencyMs')

        if m.get('GatewayRegion') is not None:
            self.gateway_region = m.get('GatewayRegion')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('InputToken') is not None:
            self.input_token = m.get('InputToken')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Model') is not None:
            self.model = m.get('Model')

        if m.get('Points') is not None:
            self.points = m.get('Points')

        if m.get('PointsBreakdown') is not None:
            temp_model = main_models.DescribeAICallDetailsResponseBodyCallDetailsPointsBreakdown()
            self.points_breakdown = temp_model.from_map(m.get('PointsBreakdown'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('WyId') is not None:
            self.wy_id = m.get('WyId')

        return self

class DescribeAICallDetailsResponseBodyCallDetailsPointsBreakdown(DaraModel):
    def __init__(
        self,
        explicit_cache_creation: str = None,
        explicit_cache_hit: str = None,
        implicit_cache_hit: str = None,
        normal_input: str = None,
        output: str = None,
    ):
        # The explicit cache creation points, in points, represented as a decimal string. A true zero value is 0.
        self.explicit_cache_creation = explicit_cache_creation
        # The explicit cache hit points, in points, represented as a decimal string. A true zero value is 0.
        self.explicit_cache_hit = explicit_cache_hit
        # The implicit cache hit points, in points, represented as a decimal string. A true zero value is 0.
        self.implicit_cache_hit = implicit_cache_hit
        # The normal input points, in points, represented as a decimal string. A true zero value is 0.
        self.normal_input = normal_input
        # The output points, in points, represented as a decimal string. A true zero value is 0.
        self.output = output

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.explicit_cache_creation is not None:
            result['ExplicitCacheCreation'] = self.explicit_cache_creation

        if self.explicit_cache_hit is not None:
            result['ExplicitCacheHit'] = self.explicit_cache_hit

        if self.implicit_cache_hit is not None:
            result['ImplicitCacheHit'] = self.implicit_cache_hit

        if self.normal_input is not None:
            result['NormalInput'] = self.normal_input

        if self.output is not None:
            result['Output'] = self.output

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExplicitCacheCreation') is not None:
            self.explicit_cache_creation = m.get('ExplicitCacheCreation')

        if m.get('ExplicitCacheHit') is not None:
            self.explicit_cache_hit = m.get('ExplicitCacheHit')

        if m.get('ImplicitCacheHit') is not None:
            self.implicit_cache_hit = m.get('ImplicitCacheHit')

        if m.get('NormalInput') is not None:
            self.normal_input = m.get('NormalInput')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        return self


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
        # 调用明细列表。
        self.call_details = call_details
        # 当前页码。
        self.page_number = page_number
        # 当前页大小。
        self.page_size = page_size
        # 实际查询终点。翻页时应复用此值。
        self.query_end_time = query_end_time
        # 实际查询起点。翻页时应复用此值。
        self.query_start_time = query_start_time
        # POP 请求 ID。
        self.request_id = request_id
        # 满足条件的总记录数。
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
        # 售卖 deduction 记录中的原始 agent_type；未匹配或 ADB 查询失败时不返回。
        self.agent_type = agent_type
        # 调用状态：SUCCESS、RATE_LIMITED、TIMEOUT 或 FAILED。
        self.call_status = call_status
        # 日志时间，ISO 8601。
        self.call_time = call_time
        # 首包时延，单位毫秒；失败或无首包数据时为空。
        self.first_token_latency_ms = first_token_latency_ms
        # 本条调用日志的实际数据地域，取值为 cn-shanghai、cn-hangzhou、cn-hongkong、ap-southeast-1 或 us-east-1；杭州预发返回 cn-hangzhou。
        self.gateway_region = gateway_region
        # AI 网关返回的 HTTP 状态码。
        self.http_status_code = http_status_code
        # 原始输入 token 数，前端据此转换上下文规模。
        self.input_token = input_token
        # 产品实例 ID。
        self.instance_id = instance_id
        # 实际调用模型。
        self.model = model
        # 按请求 ID 和输入输出 token 匹配的实际抵扣积分，十进制字符串；积分查询失败或超时时为空。
        self.points = points
        # 本条调用已匹配抵扣记录的积分构成，与 Points 来自同一条记录。缺少有效明细时不返回此对象；对象存在时完整返回五项积分，五项之和等于 Points，真实零值返回字符串 0。
        self.points_breakdown = points_breakdown
        # AI 网关请求 ID，与外层 POP 请求 ID 不同。
        self.request_id = request_id
        # 用户 WyId，用户名由前端组装。
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
        # 显式缓存创建积分，单位为积分，使用十进制字符串表示；真实零值为 0。
        self.explicit_cache_creation = explicit_cache_creation
        # 显式缓存命中积分，单位为积分，使用十进制字符串表示；真实零值为 0。
        self.explicit_cache_hit = explicit_cache_hit
        # 隐式缓存命中积分，单位为积分，使用十进制字符串表示；真实零值为 0。
        self.implicit_cache_hit = implicit_cache_hit
        # 普通输入积分，单位为积分，使用十进制字符串表示；真实零值为 0。
        self.normal_input = normal_input
        # 输出积分，单位为积分，使用十进制字符串表示；真实零值为 0。
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


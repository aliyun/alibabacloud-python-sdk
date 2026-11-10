# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class DescribeAICallDetailsRequest(DaraModel):
    def __init__(
        self,
        biz_type: str = None,
        end_time: str = None,
        gateway_region: str = None,
        model_id: str = None,
        page_number: int = None,
        page_size: int = None,
        search_request_id: str = None,
        start_time: str = None,
        wy_ids: List[str] = None,
    ):
        # 业务版本，沿用售卖 BizType：ENTERPRISE 或 1 为企业版；BUSINESS 或 20 为商业版。未传默认企业版。
        self.biz_type = biz_type
        # 带时区的 ISO 8601 结束时间，整秒精度，默认当前时间；应大于开始时间且不晚于当前时间，区间左闭右开。
        self.end_time = end_time
        # 网关日志地域：cn-shanghai（国内）、cn-hongkong（香港）、ap-southeast-1（新加坡）、us-east-1（美国）；兼容 cn-hangzhou，仅查询路由等同 cn-shanghai；杭州预发实际数据地域为 cn-hangzhou。不传时使用当前站点默认地域；预发只查询预发日志，国内映射杭州预发，美国预发未配置时返回 ServiceUnavailable。
        self.gateway_region = gateway_region
        # 可选请求模型 ID；不传或空白时不筛选，非空时精确匹配 custom_log.requestedModel 或 ai_log.request_model 任一字段，与 SearchRequestId、WyIds 等条件取交集。不按 ai_log.model 筛选，不支持模糊匹配。
        self.model_id = model_id
        # 页码，从 1 开始；分页偏移超过查询上限时返回 InvalidParameter。
        self.page_number = page_number
        # 每页返回数量，最大 50。
        self.page_size = page_size
        # 可选请求 ID；不传或空白时不筛选，非空时精确匹配 SLS request_id，与 ModelId、WyIds 等条件取交集。不得包含控制字符或管道符。
        self.search_request_id = search_request_id
        # 带时区的 ISO 8601 开始时间，整秒精度，默认 UTC+8 今日零点；不得早于当前时间按 UTC+8 回退 3 个自然月，区间不超过 30 天。
        self.start_time = start_time
        # 可选用户 ID 列表，最多 50 项；不传或空数组时不筛选。非空时精确匹配 custom_log.wyId，列表内取 OR，与租户、BizType、SearchRequestId 和 ModelId 条件取 AND。每项去除首尾空白后为 1 至 128 个字符，不允许控制字符或管道符。
        self.wy_ids = wy_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_type is not None:
            result['BizType'] = self.biz_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gateway_region is not None:
            result['GatewayRegion'] = self.gateway_region

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.search_request_id is not None:
            result['SearchRequestId'] = self.search_request_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.wy_ids is not None:
            result['WyIds'] = self.wy_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizType') is not None:
            self.biz_type = m.get('BizType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GatewayRegion') is not None:
            self.gateway_region = m.get('GatewayRegion')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SearchRequestId') is not None:
            self.search_request_id = m.get('SearchRequestId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('WyIds') is not None:
            self.wy_ids = m.get('WyIds')

        return self


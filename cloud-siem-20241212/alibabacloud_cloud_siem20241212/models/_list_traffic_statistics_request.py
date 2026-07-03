# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListTrafficStatisticsRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        log_user_ids: List[int] = None,
        product_id: str = None,
        region_id: str = None,
        region_tag: int = None,
        role_for: int = None,
        traffic_statistic_period: str = None,
        traffic_statistic_period_type: str = None,
        traffic_statistic_type: str = None,
        traffic_type: str = None,
    ):
        # The language of the response messages. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # A list of user IDs for batch data ingestion.
        self.log_user_ids = log_user_ids
        # The product ID.
        self.product_id = product_id
        # The region of the Data Management center for threat analysis. Select a region based on the location of your asset. Valid values:
        # 
        # - cn-hangzhou: Your asset is in the Chinese mainland.
        # 
        # - ap-southeast-1: Your asset is outside China.
        self.region_id = region_id
        # The region.
        self.region_tag = region_tag
        # The user ID of a member. This parameter is used by an administrator to switch to the perspective of the member.
        self.role_for = role_for
        # The statistical period.
        self.traffic_statistic_period = traffic_statistic_period
        # The statistic granularity. Valid values:
        # 
        # - day: day. This is the default value.
        # 
        # - hour: hour.
        self.traffic_statistic_period_type = traffic_statistic_period_type
        # The statistic dimension. Valid values:
        # 
        # - Region
        # 
        # - Product
        # 
        # - DataIngetion
        # 
        # - logUserId
        self.traffic_statistic_type = traffic_statistic_type
        # The type of the log traffic.
        self.traffic_type = traffic_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_user_ids is not None:
            result['LogUserIds'] = self.log_user_ids

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_tag is not None:
            result['RegionTag'] = self.region_tag

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.traffic_statistic_period is not None:
            result['TrafficStatisticPeriod'] = self.traffic_statistic_period

        if self.traffic_statistic_period_type is not None:
            result['TrafficStatisticPeriodType'] = self.traffic_statistic_period_type

        if self.traffic_statistic_type is not None:
            result['TrafficStatisticType'] = self.traffic_statistic_type

        if self.traffic_type is not None:
            result['TrafficType'] = self.traffic_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogUserIds') is not None:
            self.log_user_ids = m.get('LogUserIds')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionTag') is not None:
            self.region_tag = m.get('RegionTag')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('TrafficStatisticPeriod') is not None:
            self.traffic_statistic_period = m.get('TrafficStatisticPeriod')

        if m.get('TrafficStatisticPeriodType') is not None:
            self.traffic_statistic_period_type = m.get('TrafficStatisticPeriodType')

        if m.get('TrafficStatisticType') is not None:
            self.traffic_statistic_type = m.get('TrafficStatisticType')

        if m.get('TrafficType') is not None:
            self.traffic_type = m.get('TrafficType')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListTrafficStatisticsShrinkRequest(DaraModel):
    def __init__(
        self,
        lang: str = None,
        log_user_ids_shrink: str = None,
        product_id: str = None,
        region_id: str = None,
        region_tag: int = None,
        role_for: int = None,
        traffic_statistic_period: str = None,
        traffic_statistic_period_type: str = None,
        traffic_statistic_type: str = None,
        traffic_type: str = None,
    ):
        self.lang = lang
        self.log_user_ids_shrink = log_user_ids_shrink
        self.product_id = product_id
        self.region_id = region_id
        self.region_tag = region_tag
        self.role_for = role_for
        self.traffic_statistic_period = traffic_statistic_period
        self.traffic_statistic_period_type = traffic_statistic_period_type
        self.traffic_statistic_type = traffic_statistic_type
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

        if self.log_user_ids_shrink is not None:
            result['LogUserIds'] = self.log_user_ids_shrink

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
            self.log_user_ids_shrink = m.get('LogUserIds')

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


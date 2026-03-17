# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_smartag20180313 import models as main_models
from darabonba.model import DaraModel

class DescribeRouteDistributionStrategiesResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        strategies: main_models.DescribeRouteDistributionStrategiesResponseBodyStrategies = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        self.strategies = strategies
        # The total number of routes.
        self.total_count = total_count

    def validate(self):
        if self.strategies:
            self.strategies.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.strategies is not None:
            result['Strategies'] = self.strategies.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Strategies') is not None:
            temp_model = main_models.DescribeRouteDistributionStrategiesResponseBodyStrategies()
            self.strategies = temp_model.from_map(m.get('Strategies'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeRouteDistributionStrategiesResponseBodyStrategies(DaraModel):
    def __init__(
        self,
        strategy: List[main_models.DescribeRouteDistributionStrategiesResponseBodyStrategiesStrategy] = None,
    ):
        self.strategy = strategy

    def validate(self):
        if self.strategy:
            for v1 in self.strategy:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Strategy'] = []
        if self.strategy is not None:
            for k1 in self.strategy:
                result['Strategy'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.strategy = []
        if m.get('Strategy') is not None:
            for k1 in m.get('Strategy'):
                temp_model = main_models.DescribeRouteDistributionStrategiesResponseBodyStrategiesStrategy()
                self.strategy.append(temp_model.from_map(k1))

        return self

class DescribeRouteDistributionStrategiesResponseBodyStrategiesStrategy(DaraModel):
    def __init__(
        self,
        conflict_info: str = None,
        create_time: int = None,
        dest_cidr_block: str = None,
        hc_instance_id: str = None,
        is_conflict: bool = None,
        route_distribution: str = None,
        route_source: str = None,
        smart_agid: str = None,
        source_type: str = None,
        status: str = None,
        strategy_publish_status: str = None,
    ):
        self.conflict_info = conflict_info
        self.create_time = create_time
        self.dest_cidr_block = dest_cidr_block
        self.hc_instance_id = hc_instance_id
        self.is_conflict = is_conflict
        self.route_distribution = route_distribution
        self.route_source = route_source
        self.smart_agid = smart_agid
        self.source_type = source_type
        self.status = status
        self.strategy_publish_status = strategy_publish_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conflict_info is not None:
            result['ConflictInfo'] = self.conflict_info

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dest_cidr_block is not None:
            result['DestCidrBlock'] = self.dest_cidr_block

        if self.hc_instance_id is not None:
            result['HcInstanceId'] = self.hc_instance_id

        if self.is_conflict is not None:
            result['IsConflict'] = self.is_conflict

        if self.route_distribution is not None:
            result['RouteDistribution'] = self.route_distribution

        if self.route_source is not None:
            result['RouteSource'] = self.route_source

        if self.smart_agid is not None:
            result['SmartAGId'] = self.smart_agid

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.status is not None:
            result['Status'] = self.status

        if self.strategy_publish_status is not None:
            result['StrategyPublishStatus'] = self.strategy_publish_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConflictInfo') is not None:
            self.conflict_info = m.get('ConflictInfo')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DestCidrBlock') is not None:
            self.dest_cidr_block = m.get('DestCidrBlock')

        if m.get('HcInstanceId') is not None:
            self.hc_instance_id = m.get('HcInstanceId')

        if m.get('IsConflict') is not None:
            self.is_conflict = m.get('IsConflict')

        if m.get('RouteDistribution') is not None:
            self.route_distribution = m.get('RouteDistribution')

        if m.get('RouteSource') is not None:
            self.route_source = m.get('RouteSource')

        if m.get('SmartAGId') is not None:
            self.smart_agid = m.get('SmartAGId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StrategyPublishStatus') is not None:
            self.strategy_publish_status = m.get('StrategyPublishStatus')

        return self


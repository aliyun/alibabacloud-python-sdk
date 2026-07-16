# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeApikeyAttributeResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeApikeyAttributeResponseBodyItems] = None,
        request_id: str = None,
    ):
        # The list of consumer objects.
        self.items = items
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeApikeyAttributeResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeApikeyAttributeResponseBodyItems(DaraModel):
    def __init__(
        self,
        consumer: main_models.DescribeApikeyAttributeResponseBodyItemsConsumer = None,
        usage_statistics: List[main_models.DescribeApikeyAttributeResponseBodyItemsUsageStatistics] = None,
    ):
        # The consumer information.
        self.consumer = consumer
        # The usage statistics for the consumer.
        self.usage_statistics = usage_statistics

    def validate(self):
        if self.consumer:
            self.consumer.validate()
        if self.usage_statistics:
            for v1 in self.usage_statistics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.consumer is not None:
            result['Consumer'] = self.consumer.to_map()

        result['UsageStatistics'] = []
        if self.usage_statistics is not None:
            for k1 in self.usage_statistics:
                result['UsageStatistics'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Consumer') is not None:
            temp_model = main_models.DescribeApikeyAttributeResponseBodyItemsConsumer()
            self.consumer = temp_model.from_map(m.get('Consumer'))

        self.usage_statistics = []
        if m.get('UsageStatistics') is not None:
            for k1 in m.get('UsageStatistics'):
                temp_model = main_models.DescribeApikeyAttributeResponseBodyItemsUsageStatistics()
                self.usage_statistics.append(temp_model.from_map(k1))

        return self

class DescribeApikeyAttributeResponseBodyItemsUsageStatistics(DaraModel):
    def __init__(
        self,
        dimension_ref_id: str = None,
        dimension_type: str = None,
        gw_cluster_id: str = None,
        monthly_cache_token: str = None,
        monthly_cost_points: str = None,
        monthly_input_token: str = None,
        monthly_output_token: str = None,
        monthly_token: str = None,
        total_cache_token: str = None,
        total_cost_points: str = None,
        total_input_token: str = None,
        total_output_token: str = None,
        total_token: str = None,
    ):
        # The dimension reference ID, which is the ConsumerId.
        self.dimension_ref_id = dimension_ref_id
        # The statistics dimension. The value is typically Consumer.
        self.dimension_type = dimension_type
        # The gateway instance ID.
        self.gw_cluster_id = gw_cluster_id
        # The number of cache tokens for the current month.
        self.monthly_cache_token = monthly_cache_token
        # The cost points consumed for the current month.
        self.monthly_cost_points = monthly_cost_points
        # The number of input tokens for the current month.
        self.monthly_input_token = monthly_input_token
        # The number of output tokens for the current month.
        self.monthly_output_token = monthly_output_token
        # The number of tokens for the current month.
        self.monthly_token = monthly_token
        # The cumulative number of cache tokens.
        self.total_cache_token = total_cache_token
        # The cumulative cost points consumed.
        self.total_cost_points = total_cost_points
        # The cumulative number of input tokens.
        self.total_input_token = total_input_token
        # The cumulative number of output tokens.
        self.total_output_token = total_output_token
        # The cumulative number of tokens.
        self.total_token = total_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dimension_ref_id is not None:
            result['DimensionRefId'] = self.dimension_ref_id

        if self.dimension_type is not None:
            result['DimensionType'] = self.dimension_type

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.monthly_cache_token is not None:
            result['MonthlyCacheToken'] = self.monthly_cache_token

        if self.monthly_cost_points is not None:
            result['MonthlyCostPoints'] = self.monthly_cost_points

        if self.monthly_input_token is not None:
            result['MonthlyInputToken'] = self.monthly_input_token

        if self.monthly_output_token is not None:
            result['MonthlyOutputToken'] = self.monthly_output_token

        if self.monthly_token is not None:
            result['MonthlyToken'] = self.monthly_token

        if self.total_cache_token is not None:
            result['TotalCacheToken'] = self.total_cache_token

        if self.total_cost_points is not None:
            result['TotalCostPoints'] = self.total_cost_points

        if self.total_input_token is not None:
            result['TotalInputToken'] = self.total_input_token

        if self.total_output_token is not None:
            result['TotalOutputToken'] = self.total_output_token

        if self.total_token is not None:
            result['TotalToken'] = self.total_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DimensionRefId') is not None:
            self.dimension_ref_id = m.get('DimensionRefId')

        if m.get('DimensionType') is not None:
            self.dimension_type = m.get('DimensionType')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('MonthlyCacheToken') is not None:
            self.monthly_cache_token = m.get('MonthlyCacheToken')

        if m.get('MonthlyCostPoints') is not None:
            self.monthly_cost_points = m.get('MonthlyCostPoints')

        if m.get('MonthlyInputToken') is not None:
            self.monthly_input_token = m.get('MonthlyInputToken')

        if m.get('MonthlyOutputToken') is not None:
            self.monthly_output_token = m.get('MonthlyOutputToken')

        if m.get('MonthlyToken') is not None:
            self.monthly_token = m.get('MonthlyToken')

        if m.get('TotalCacheToken') is not None:
            self.total_cache_token = m.get('TotalCacheToken')

        if m.get('TotalCostPoints') is not None:
            self.total_cost_points = m.get('TotalCostPoints')

        if m.get('TotalInputToken') is not None:
            self.total_input_token = m.get('TotalInputToken')

        if m.get('TotalOutputToken') is not None:
            self.total_output_token = m.get('TotalOutputToken')

        if m.get('TotalToken') is not None:
            self.total_token = m.get('TotalToken')

        return self

class DescribeApikeyAttributeResponseBodyItemsConsumer(DaraModel):
    def __init__(
        self,
        api_key: str = None,
        consumer_group_id: str = None,
        consumer_id: str = None,
        consumer_tag: str = None,
        create_time: str = None,
        gw_cluster_id: str = None,
        modify_time: str = None,
        name: str = None,
        status: str = None,
    ):
        # The API key.
        self.api_key = api_key
        # The user group ID.
        self.consumer_group_id = consumer_group_id
        # The consumer ID.
        self.consumer_id = consumer_id
        # The consumer tag.
        self.consumer_tag = consumer_tag
        # The creation time.
        self.create_time = create_time
        # The gateway instance ID.
        self.gw_cluster_id = gw_cluster_id
        # The last modification time.
        self.modify_time = modify_time
        # The consumer name.
        self.name = name
        # The consumer status.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id

        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.consumer_tag is not None:
            result['ConsumerTag'] = self.consumer_tag

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.gw_cluster_id is not None:
            result['GwClusterId'] = self.gw_cluster_id

        if self.modify_time is not None:
            result['ModifyTime'] = self.modify_time

        if self.name is not None:
            result['Name'] = self.name

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('ConsumerTag') is not None:
            self.consumer_tag = m.get('ConsumerTag')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('GwClusterId') is not None:
            self.gw_cluster_id = m.get('GwClusterId')

        if m.get('ModifyTime') is not None:
            self.modify_time = m.get('ModifyTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


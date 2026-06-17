# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeConsumersResponseBody(DaraModel):
    def __init__(
        self,
        items: List[main_models.DescribeConsumersResponseBodyItems] = None,
        page_number: int = None,
        page_record_count: int = None,
        page_size: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        # A list of consumers.
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of entries returned on the current page.
        self.page_record_count = page_record_count
        # The page size. Valid values: 30, 50, and 100. The default value is 30.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of records.
        self.total_record_count = total_record_count

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

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeConsumersResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeConsumersResponseBodyItems(DaraModel):
    def __init__(
        self,
        allowed_models: str = None,
        api_key: str = None,
        consumer_group_id: str = None,
        consumer_group_name: str = None,
        consumer_id: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        lifetime_cost_count: int = None,
        lifetime_token_count: int = None,
        mtd_cost_count: int = None,
        mtd_token_count: int = None,
        name: str = None,
        nick_name: str = None,
    ):
        # The models that the consumer is allowed to access, specified as a JSON array in string format.
        self.allowed_models = allowed_models
        # The full API key. This value is returned only by this operation.
        self.api_key = api_key
        # The consumer group ID.
        self.consumer_group_id = consumer_group_id
        # The consumer group name.
        self.consumer_group_name = consumer_group_name
        # The consumer ID.
        self.consumer_id = consumer_id
        # The time when the consumer was created.
        self.gmt_created = gmt_created
        # The time when the consumer was last modified.
        self.gmt_modified = gmt_modified
        # The total usage.
        self.lifetime_cost_count = lifetime_cost_count
        # The total number of tokens consumed.
        self.lifetime_token_count = lifetime_token_count
        # The month-to-date usage.
        self.mtd_cost_count = mtd_cost_count
        # The number of tokens consumed month-to-date.
        self.mtd_token_count = mtd_token_count
        # The consumer name.
        self.name = name
        # The consumer nickname.
        self.nick_name = nick_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allowed_models is not None:
            result['AllowedModels'] = self.allowed_models

        if self.api_key is not None:
            result['ApiKey'] = self.api_key

        if self.consumer_group_id is not None:
            result['ConsumerGroupId'] = self.consumer_group_id

        if self.consumer_group_name is not None:
            result['ConsumerGroupName'] = self.consumer_group_name

        if self.consumer_id is not None:
            result['ConsumerId'] = self.consumer_id

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.lifetime_cost_count is not None:
            result['LifetimeCostCount'] = self.lifetime_cost_count

        if self.lifetime_token_count is not None:
            result['LifetimeTokenCount'] = self.lifetime_token_count

        if self.mtd_cost_count is not None:
            result['MtdCostCount'] = self.mtd_cost_count

        if self.mtd_token_count is not None:
            result['MtdTokenCount'] = self.mtd_token_count

        if self.name is not None:
            result['Name'] = self.name

        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowedModels') is not None:
            self.allowed_models = m.get('AllowedModels')

        if m.get('ApiKey') is not None:
            self.api_key = m.get('ApiKey')

        if m.get('ConsumerGroupId') is not None:
            self.consumer_group_id = m.get('ConsumerGroupId')

        if m.get('ConsumerGroupName') is not None:
            self.consumer_group_name = m.get('ConsumerGroupName')

        if m.get('ConsumerId') is not None:
            self.consumer_id = m.get('ConsumerId')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('LifetimeCostCount') is not None:
            self.lifetime_cost_count = m.get('LifetimeCostCount')

        if m.get('LifetimeTokenCount') is not None:
            self.lifetime_token_count = m.get('LifetimeTokenCount')

        if m.get('MtdCostCount') is not None:
            self.mtd_cost_count = m.get('MtdCostCount')

        if m.get('MtdTokenCount') is not None:
            self.mtd_token_count = m.get('MtdTokenCount')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        return self


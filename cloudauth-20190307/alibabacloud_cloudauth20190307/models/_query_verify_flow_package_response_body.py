# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudauth20190307 import models as main_models
from darabonba.model import DaraModel

class QueryVerifyFlowPackageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        items: List[main_models.QueryVerifyFlowPackageResponseBodyItems] = None,
        request_id: str = None,
        success: bool = None,
        total_count: str = None,
    ):
        # Return code
        self.code = code
        # HTTP status code.
        self.http_status_code = http_status_code
        # List of returned data.
        self.items = items
        # ID of the request
        self.request_id = request_id
        # Indicates whether the response was successful.
        self.success = success
        # Total count.
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.QueryVerifyFlowPackageResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryVerifyFlowPackageResponseBodyItems(DaraModel):
    def __init__(
        self,
        commodity_name: str = None,
        curr_capacity: float = None,
        curr_proportion: str = None,
        flow_details: List[main_models.QueryVerifyFlowPackageResponseBodyItemsFlowDetails] = None,
        total_capacity: float = None,
        used_capacity: float = None,
    ):
        # Name of the resource package.
        self.commodity_name = commodity_name
        # Current available capacity.
        self.curr_capacity = curr_capacity
        # Proportion of current remaining capacity to total capacity.
        self.curr_proportion = curr_proportion
        # Details of the flow package.
        self.flow_details = flow_details
        # Total quota.
        self.total_capacity = total_capacity
        # Used capacity.
        self.used_capacity = used_capacity

    def validate(self):
        if self.flow_details:
            for v1 in self.flow_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity

        if self.curr_proportion is not None:
            result['CurrProportion'] = self.curr_proportion

        result['FlowDetails'] = []
        if self.flow_details is not None:
            for k1 in self.flow_details:
                result['FlowDetails'].append(k1.to_map() if k1 else None)

        if self.total_capacity is not None:
            result['TotalCapacity'] = self.total_capacity

        if self.used_capacity is not None:
            result['UsedCapacity'] = self.used_capacity

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')

        if m.get('CurrProportion') is not None:
            self.curr_proportion = m.get('CurrProportion')

        self.flow_details = []
        if m.get('FlowDetails') is not None:
            for k1 in m.get('FlowDetails'):
                temp_model = main_models.QueryVerifyFlowPackageResponseBodyItemsFlowDetails()
                self.flow_details.append(temp_model.from_map(k1))

        if m.get('TotalCapacity') is not None:
            self.total_capacity = m.get('TotalCapacity')

        if m.get('UsedCapacity') is not None:
            self.used_capacity = m.get('UsedCapacity')

        return self

class QueryVerifyFlowPackageResponseBodyItemsFlowDetails(DaraModel):
    def __init__(
        self,
        capacity: float = None,
        commodity_name: str = None,
        curr_capacity: float = None,
        curr_proportion: str = None,
        expire_date: str = None,
        instance_name: str = None,
        status: str = None,
        take_effect_date: str = None,
    ):
        # Total amount.
        self.capacity = capacity
        # Name of the flow package.
        self.commodity_name = commodity_name
        # Remaining amount.
        self.curr_capacity = curr_capacity
        # Proportion of remaining amount.
        self.curr_proportion = curr_proportion
        # Expiration date.
        self.expire_date = expire_date
        # Instance name
        self.instance_name = instance_name
        # Status.
        self.status = status
        # Effective date.
        self.take_effect_date = take_effect_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.commodity_name is not None:
            result['CommodityName'] = self.commodity_name

        if self.curr_capacity is not None:
            result['CurrCapacity'] = self.curr_capacity

        if self.curr_proportion is not None:
            result['CurrProportion'] = self.curr_proportion

        if self.expire_date is not None:
            result['ExpireDate'] = self.expire_date

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.status is not None:
            result['Status'] = self.status

        if self.take_effect_date is not None:
            result['TakeEffectDate'] = self.take_effect_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('CommodityName') is not None:
            self.commodity_name = m.get('CommodityName')

        if m.get('CurrCapacity') is not None:
            self.curr_capacity = m.get('CurrCapacity')

        if m.get('CurrProportion') is not None:
            self.curr_proportion = m.get('CurrProportion')

        if m.get('ExpireDate') is not None:
            self.expire_date = m.get('ExpireDate')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TakeEffectDate') is not None:
            self.take_effect_date = m.get('TakeEffectDate')

        return self


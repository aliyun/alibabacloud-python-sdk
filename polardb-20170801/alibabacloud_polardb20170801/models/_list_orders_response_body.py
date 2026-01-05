# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class ListOrdersResponseBody(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        order_list: List[main_models.ListOrdersResponseBodyOrderList] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.max_results = max_results
        self.next_token = next_token
        # This parameter is required.
        self.order_list = order_list
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.order_list:
            for v1 in self.order_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['OrderList'] = []
        if self.order_list is not None:
            for k1 in self.order_list:
                result['OrderList'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.order_list = []
        if m.get('OrderList') is not None:
            for k1 in m.get('OrderList'):
                temp_model = main_models.ListOrdersResponseBodyOrderList()
                self.order_list.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListOrdersResponseBodyOrderList(DaraModel):
    def __init__(
        self,
        ali_uid: str = None,
        charge_type: str = None,
        commodity_code: str = None,
        created_time: str = None,
        instance_id: str = None,
        order_id: str = None,
        order_status: str = None,
        order_type: str = None,
        produce_code: str = None,
        region: str = None,
    ):
        self.ali_uid = ali_uid
        self.charge_type = charge_type
        self.commodity_code = commodity_code
        self.created_time = created_time
        self.instance_id = instance_id
        self.order_id = order_id
        self.order_status = order_status
        self.order_type = order_type
        self.produce_code = produce_code
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.order_status is not None:
            result['OrderStatus'] = self.order_status

        if self.order_type is not None:
            result['OrderType'] = self.order_type

        if self.produce_code is not None:
            result['ProduceCode'] = self.produce_code

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('OrderStatus') is not None:
            self.order_status = m.get('OrderStatus')

        if m.get('OrderType') is not None:
            self.order_type = m.get('OrderType')

        if m.get('ProduceCode') is not None:
            self.produce_code = m.get('ProduceCode')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self


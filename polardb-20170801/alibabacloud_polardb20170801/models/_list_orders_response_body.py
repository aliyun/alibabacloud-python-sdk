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
        # The maximum number of entries returned for the current request. Default value: 10.
        self.max_results = max_results
        # A pagination token. If the query results are not returned in a single call, this token is returned. Use this token in a subsequent call to retrieve the remaining results.
        self.next_token = next_token
        # The list of orders.
        # 
        # This parameter is required.
        self.order_list = order_list
        # The page number of the returned page. Default value: 1.
        self.page_number = page_number
        # The number of entries returned per page. Valid values:
        # 
        # - **30**
        # 
        # - **50**
        # 
        # - **100**
        # 
        # Default value: 30.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
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
        # The ID of the Alibaba Cloud account.
        self.ali_uid = ali_uid
        # The billing method of the instance. Valid values:
        # 
        # - **Postpaid**: pay-as-you-go
        # 
        # - **Prepaid**: subscription
        self.charge_type = charge_type
        # The commodity code. Valid values:
        # 
        # - polardb_sub: subscription in the Chinese mainland.
        # 
        # - polardb_sub_intl: subscription in Hong Kong (China) and regions outside China.
        # 
        # - polardb_payg: pay-as-you-go in the Chinese mainland.
        # 
        # - polardb_payg_intl: pay-as-you-go in Hong Kong (China) and regions outside China.
        # 
        # - polardb_sub_jushita: Jushita subscription.
        # 
        # - polardb_payg_jushita: Jushita pay-as-you-go.
        # 
        # - polardb_sub_cainiao: Cainiao subscription.
        # 
        # - polardb_payg_cainiao: Cainiao pay-as-you-go.
        # 
        # > * If you use an Alibaba Cloud account for the China site, you can view only the commodity codes for the Chinese mainland.
        # >
        # > * If you use an Alibaba Cloud international site account, you can view only the commodity codes for regions outside the Chinese mainland.
        # >
        # > * If you use a Jushita account, you can view only the commodity codes for Jushita.
        # >
        # > * If you use a Cainiao account, you can view only the commodity codes for Cainiao.
        self.commodity_code = commodity_code
        # The time when the order was created.
        self.created_time = created_time
        # The cluster ID.
        self.instance_id = instance_id
        # The order ID.
        self.order_id = order_id
        # The status of the order.
        # 
        # - **pending**: The task is waiting to start.
        # 
        # - **create**: The order is placed and is being processed.
        # 
        # - **fail**: The instance failed to be created.
        # 
        # - **cancel**: The order is canceled.
        # 
        # - **success**: The instance is created.
        self.order_status = order_status
        # The type of the order. Valid values:
        # 
        # - BUY: The instance is purchased.
        # 
        # - UPGRADE: The instance configuration is changed.
        # 
        # - RENEW: The subscription is renewed.
        # 
        # - CONVERT: The billing method is changed.
        self.order_type = order_type
        # The product code.
        self.produce_code = produce_code
        # The region information
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


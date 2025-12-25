# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class ListEffectiveOrdersResponseBody(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        order_summary: List[main_models.ListEffectiveOrdersResponseBodyOrderSummary] = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned if the request failed.
        self.error_code = error_code
        # The error message returned if the request failed.
        self.error_message = error_message
        # The information about orders.
        self.order_summary = order_summary
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**: The request was successful.
        # *   **false**: The request failed.
        self.success = success

    def validate(self):
        if self.order_summary:
            for v1 in self.order_summary:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        result['OrderSummary'] = []
        if self.order_summary is not None:
            for k1 in self.order_summary:
                result['OrderSummary'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        self.order_summary = []
        if m.get('OrderSummary') is not None:
            for k1 in m.get('OrderSummary'):
                temp_model = main_models.ListEffectiveOrdersResponseBodyOrderSummary()
                self.order_summary.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListEffectiveOrdersResponseBodyOrderSummary(DaraModel):
    def __init__(
        self,
        commodity_code: str = None,
        commodity_type: str = None,
        order_list: List[main_models.ListEffectiveOrdersResponseBodyOrderSummaryOrderList] = None,
        total_quota: int = None,
        version_type: str = None,
    ):
        # The commodity code of DMS.
        # 
        # *   dms_pre_public_cn: DMS that uses the subscription billing method
        # *   dms_post_public_cn: DMS that uses the pay-as-you-go billing method
        self.commodity_code = commodity_code
        # The type of the service.
        # 
        # *   **VersionType**: DMS that supports control modes
        # *   **SensitiveDataProtection**: DMS that supports sensitive data protection
        self.commodity_type = commodity_type
        # Details about the orders.
        self.order_list = order_list
        # The sum of the number of instances that you can use DMS to manage in all orders.
        self.total_quota = total_quota
        # The control mode of DMS. Valid values:
        # 
        # *   **stand**: Stable Change
        # *   **safety**: Security Collaboration
        self.version_type = version_type

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
        if self.commodity_code is not None:
            result['CommodityCode'] = self.commodity_code

        if self.commodity_type is not None:
            result['CommodityType'] = self.commodity_type

        result['OrderList'] = []
        if self.order_list is not None:
            for k1 in self.order_list:
                result['OrderList'].append(k1.to_map() if k1 else None)

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.version_type is not None:
            result['VersionType'] = self.version_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CommodityCode') is not None:
            self.commodity_code = m.get('CommodityCode')

        if m.get('CommodityType') is not None:
            self.commodity_type = m.get('CommodityType')

        self.order_list = []
        if m.get('OrderList') is not None:
            for k1 in m.get('OrderList'):
                temp_model = main_models.ListEffectiveOrdersResponseBodyOrderSummaryOrderList()
                self.order_list.append(temp_model.from_map(k1))

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('VersionType') is not None:
            self.version_type = m.get('VersionType')

        return self

class ListEffectiveOrdersResponseBodyOrderSummaryOrderList(DaraModel):
    def __init__(
        self,
        buyer_id: str = None,
        end_time: str = None,
        ins_num: str = None,
        instance_id: str = None,
        order_id: str = None,
        start_time: str = None,
    ):
        # The UID of the user who placed the order.
        self.buyer_id = buyer_id
        # The time when the instance expires.
        self.end_time = end_time
        # The maximum number of database instances that you can use DMS to manage.
        self.ins_num = ins_num
        # The ID of the instance for the purchased service.
        self.instance_id = instance_id
        # The ID of the order.
        self.order_id = order_id
        # The time when the instance is started.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.buyer_id is not None:
            result['BuyerId'] = self.buyer_id

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.ins_num is not None:
            result['InsNum'] = self.ins_num

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.order_id is not None:
            result['OrderId'] = self.order_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuyerId') is not None:
            self.buyer_id = m.get('BuyerId')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('InsNum') is not None:
            self.ins_num = m.get('InsNum')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('OrderId') is not None:
            self.order_id = m.get('OrderId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self


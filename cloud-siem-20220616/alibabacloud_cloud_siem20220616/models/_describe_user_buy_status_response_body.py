# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeUserBuyStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeUserBuyStatusResponseBodyData = None,
        request_id: str = None,
    ):
        # The response parameters.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeUserBuyStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserBuyStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        can_buy: bool = None,
        capacity: int = None,
        duration_days: int = None,
        end_time: int = None,
        main_user_id: int = None,
        main_user_name: str = None,
        master_user_id: int = None,
        master_user_name: str = None,
        rd_order: int = None,
        sas_instance_id: str = None,
        sub_user_id: int = None,
        sub_user_name: str = None,
    ):
        # Indicates whether the current account can perform operations on threat analysis orders. Valid values:
        # 
        # - true: The account can purchase, upgrade, or downgrade threat analysis.
        # 
        # - false: The account cannot perform operations on threat analysis orders.
        self.can_buy = can_buy
        # The purchased capacity of Simple Log Service (SLS) for threat analysis. Unit: GB.
        self.capacity = capacity
        # The number of days before threat analysis expires.
        self.duration_days = duration_days
        # The expiration time of threat analysis. This value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The ID of the Alibaba Cloud account that purchased threat analysis.
        self.main_user_id = main_user_id
        # The name of the Alibaba Cloud account that purchased threat analysis.
        self.main_user_name = main_user_name
        # The ID of the master account of the resource directory.
        self.master_user_id = master_user_id
        # The display name of the master account of the resource directory.
        self.master_user_name = master_user_name
        # The type of the current order.
        # 
        # - 0: The order includes threat analysis traffic and capacity.
        # 
        # - 1: The order includes only threat analysis capacity.
        self.rd_order = rd_order
        # The ID of the Security Center instance.
        self.sas_instance_id = sas_instance_id
        # The ID of the currently logged-on Alibaba Cloud account.
        self.sub_user_id = sub_user_id
        # The name of the currently logged-on Alibaba Cloud account.
        self.sub_user_name = sub_user_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_buy is not None:
            result['CanBuy'] = self.can_buy

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.duration_days is not None:
            result['DurationDays'] = self.duration_days

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id

        if self.main_user_name is not None:
            result['MainUserName'] = self.main_user_name

        if self.master_user_id is not None:
            result['MasterUserId'] = self.master_user_id

        if self.master_user_name is not None:
            result['MasterUserName'] = self.master_user_name

        if self.rd_order is not None:
            result['RdOrder'] = self.rd_order

        if self.sas_instance_id is not None:
            result['SasInstanceId'] = self.sas_instance_id

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.sub_user_name is not None:
            result['SubUserName'] = self.sub_user_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanBuy') is not None:
            self.can_buy = m.get('CanBuy')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('DurationDays') is not None:
            self.duration_days = m.get('DurationDays')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')

        if m.get('MainUserName') is not None:
            self.main_user_name = m.get('MainUserName')

        if m.get('MasterUserId') is not None:
            self.master_user_id = m.get('MasterUserId')

        if m.get('MasterUserName') is not None:
            self.master_user_name = m.get('MasterUserName')

        if m.get('RdOrder') is not None:
            self.rd_order = m.get('RdOrder')

        if m.get('SasInstanceId') is not None:
            self.sas_instance_id = m.get('SasInstanceId')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('SubUserName') is not None:
            self.sub_user_name = m.get('SubUserName')

        return self


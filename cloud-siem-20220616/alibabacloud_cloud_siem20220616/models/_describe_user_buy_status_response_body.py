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
        # The data returned.
        self.data = data
        # The request ID.
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
        # Indicates whether the logon Alibaba Cloud account can be used to place orders for the threat analysis feature, such as purchase, upgrade, and specifications change orders. Valid values:
        # 
        # *   true
        # *   false
        self.can_buy = can_buy
        # The log storage capacity that is purchased for the threat analysis feature. Unit: GB.
        self.capacity = capacity
        # The number of days before the expiration time of the threat analysis feature.
        self.duration_days = duration_days
        # The timestamp when the threat analysis feature expires. Unit: milliseconds.
        self.end_time = end_time
        # The ID of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_id = main_user_id
        # The username of the Alibaba Cloud account that is used to purchase the threat analysis feature.
        self.main_user_name = main_user_name
        # The ID of the management account of the resource directory.
        self.master_user_id = master_user_id
        # The display name of the management account of the resource directory.
        self.master_user_name = master_user_name
        self.rd_order = rd_order
        # The instance ID of Security Center.
        self.sas_instance_id = sas_instance_id
        # The ID of the logon Alibaba Cloud account.
        self.sub_user_id = sub_user_id
        # The username of the logon Alibaba Cloud account.
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


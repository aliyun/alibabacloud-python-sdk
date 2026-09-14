# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class DescribeUserSiemOrderStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeUserSiemOrderStatusResponseBodyData = None,
        request_id: str = None,
    ):
        # The response data.
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
            temp_model = main_models.DescribeUserSiemOrderStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeUserSiemOrderStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        asoc_instance_id: str = None,
        asoc_subscription_instance_end_time: int = None,
        asoc_subscription_instance_start_time: int = None,
        can_buy: bool = None,
        capacity: int = None,
        capacity_order_from: str = None,
        delivery_capacity: int = None,
        duration_days: int = None,
        end_time: int = None,
        flow_capacity: int = None,
        main_user_id: int = None,
        master_user_id: int = None,
        rd_id: str = None,
        rd_order: int = None,
        sas_instance_id: str = None,
        siem_order_from: str = None,
        siem_order_status: int = None,
        sub_user_id: int = None,
        user_type: str = None,
    ):
        # The Agentic SOC Credits instance ID. If SiemOrderFrom is CREDITS_PRE_PAY, this field returns the Credits subscription instance ID for prepaid orders. If SiemOrderFrom is CREDITS_POST_PAY, this field returns the Credits pay-as-you-go instance ID. This field is empty if no Credits instance is found. For legacy orders, the Security Center instance ID is returned by SasInstanceId.
        self.asoc_instance_id = asoc_instance_id
        # The end time of the Agentic SOC Credits prepaid subscription, expressed as a 13-digit Unix timestamp in milliseconds. This field is returned only when SiemOrderFrom is CREDITS_PRE_PAY. In other cases, this field is empty.
        self.asoc_subscription_instance_end_time = asoc_subscription_instance_end_time
        # The start time of the Agentic SOC Credits prepaid subscription, expressed as a 13-digit Unix timestamp in milliseconds. This field is returned only when SiemOrderFrom is CREDITS_PRE_PAY. In other cases, this field is empty.
        self.asoc_subscription_instance_start_time = asoc_subscription_instance_start_time
        # Indicates whether the current account can perform order operations for threat detection and response. Valid values:
        # - true: The account can purchase, upgrade, or change specifications.
        # - false: The account cannot perform order operations for threat detection and response.
        self.can_buy = can_buy
        # The SLS log storage capacity purchased for threat detection and response, in GB.
        self.capacity = capacity
        # The source of the log storage capacity order. Valid values:
        # - PRE_PAY_CAPACITY: a prepaid capacity order.
        # - POST_PAY_CAPACITY: a pay-as-you-go capacity order.
        # 
        # The capacity order source is independent of the traffic order source indicated by SiemOrderFrom.
        self.capacity_order_from = capacity_order_from
        # The SLS log storage capacity purchased for threat detection and response 1.0, in GB.
        self.delivery_capacity = delivery_capacity
        # The number of days until the threat detection and response service expires.
        self.duration_days = duration_days
        # The expiration time of threat detection and response, expressed as a millisecond-level timestamp.
        self.end_time = end_time
        # The traffic capacity purchased for threat detection and response, in GB.
        self.flow_capacity = flow_capacity
        # The Alibaba Cloud account ID that purchased threat detection and response.
        self.main_user_id = main_user_id
        # The master account ID of the resource directory.
        self.master_user_id = master_user_id
        # The resource directory ID.
        self.rd_id = rd_id
        # Indicates whether the order is a SIEM public preview order.
        self.rd_order = rd_order
        # The Security Center instance ID.
        self.sas_instance_id = sas_instance_id
        # The source of the traffic order. Valid values:
        # - PRE_PAY_FLOW: a prepaid traffic order for threat detection and response.
        # - POST_PAY_FLOW: a pay-as-you-go traffic order for threat detection and response.
        # - CREDITS_PRE_PAY: an Agentic SOC Credits prepaid subscription.
        # - CREDITS_POST_PAY: an Agentic SOC Credits pay-as-you-go instance.
        # 
        # This field describes the traffic order source. The log storage capacity order source is independently indicated by CapacityOrderFrom.
        self.siem_order_from = siem_order_from
        # Indicates whether a valid SIEM order exists. Valid values:
        # - 1: The SIEM order is valid.
        # - 0: The SIEM order is invalid.
        self.siem_order_status = siem_order_status
        # The Alibaba Cloud account ID of the current logon.
        self.sub_user_id = sub_user_id
        # The user type.
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asoc_instance_id is not None:
            result['AsocInstanceId'] = self.asoc_instance_id

        if self.asoc_subscription_instance_end_time is not None:
            result['AsocSubscriptionInstanceEndTime'] = self.asoc_subscription_instance_end_time

        if self.asoc_subscription_instance_start_time is not None:
            result['AsocSubscriptionInstanceStartTime'] = self.asoc_subscription_instance_start_time

        if self.can_buy is not None:
            result['CanBuy'] = self.can_buy

        if self.capacity is not None:
            result['Capacity'] = self.capacity

        if self.capacity_order_from is not None:
            result['CapacityOrderFrom'] = self.capacity_order_from

        if self.delivery_capacity is not None:
            result['DeliveryCapacity'] = self.delivery_capacity

        if self.duration_days is not None:
            result['DurationDays'] = self.duration_days

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.flow_capacity is not None:
            result['FlowCapacity'] = self.flow_capacity

        if self.main_user_id is not None:
            result['MainUserId'] = self.main_user_id

        if self.master_user_id is not None:
            result['MasterUserId'] = self.master_user_id

        if self.rd_id is not None:
            result['RdId'] = self.rd_id

        if self.rd_order is not None:
            result['RdOrder'] = self.rd_order

        if self.sas_instance_id is not None:
            result['SasInstanceId'] = self.sas_instance_id

        if self.siem_order_from is not None:
            result['SiemOrderFrom'] = self.siem_order_from

        if self.siem_order_status is not None:
            result['SiemOrderStatus'] = self.siem_order_status

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsocInstanceId') is not None:
            self.asoc_instance_id = m.get('AsocInstanceId')

        if m.get('AsocSubscriptionInstanceEndTime') is not None:
            self.asoc_subscription_instance_end_time = m.get('AsocSubscriptionInstanceEndTime')

        if m.get('AsocSubscriptionInstanceStartTime') is not None:
            self.asoc_subscription_instance_start_time = m.get('AsocSubscriptionInstanceStartTime')

        if m.get('CanBuy') is not None:
            self.can_buy = m.get('CanBuy')

        if m.get('Capacity') is not None:
            self.capacity = m.get('Capacity')

        if m.get('CapacityOrderFrom') is not None:
            self.capacity_order_from = m.get('CapacityOrderFrom')

        if m.get('DeliveryCapacity') is not None:
            self.delivery_capacity = m.get('DeliveryCapacity')

        if m.get('DurationDays') is not None:
            self.duration_days = m.get('DurationDays')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('FlowCapacity') is not None:
            self.flow_capacity = m.get('FlowCapacity')

        if m.get('MainUserId') is not None:
            self.main_user_id = m.get('MainUserId')

        if m.get('MasterUserId') is not None:
            self.master_user_id = m.get('MasterUserId')

        if m.get('RdId') is not None:
            self.rd_id = m.get('RdId')

        if m.get('RdOrder') is not None:
            self.rd_order = m.get('RdOrder')

        if m.get('SasInstanceId') is not None:
            self.sas_instance_id = m.get('SasInstanceId')

        if m.get('SiemOrderFrom') is not None:
            self.siem_order_from = m.get('SiemOrderFrom')

        if m.get('SiemOrderStatus') is not None:
            self.siem_order_status = m.get('SiemOrderStatus')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self


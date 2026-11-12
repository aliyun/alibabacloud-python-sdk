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
        credits_postpaid_info: main_models.DescribeUserSiemOrderStatusResponseBodyDataCreditsPostpaidInfo = None,
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
        # The ID of the Agentic SOC Credits instance. If SiemOrderFrom is CREDITS_PRE_PAY, the ID of the subscription Credits instance is returned. If SiemOrderFrom is CREDITS_POST_PAY, the ID of the pay-as-you-go Credits instance is returned. This field is empty if no Credits instance is found. The ID of the Security Center instance for legacy orders is returned by SasInstanceId.
        self.asoc_instance_id = asoc_instance_id
        # The end time of the Agentic SOC Credits subscription. The value is a 13-digit UNIX timestamp in milliseconds. This field is returned only when SiemOrderFrom is CREDITS_PRE_PAY. Otherwise, this field is empty.
        self.asoc_subscription_instance_end_time = asoc_subscription_instance_end_time
        # The start time of the Agentic SOC Credits subscription. The value is a 13-digit UNIX timestamp in milliseconds. This field is returned only when SiemOrderFrom is CREDITS_PRE_PAY. Otherwise, this field is empty.
        self.asoc_subscription_instance_start_time = asoc_subscription_instance_start_time
        # Specifies whether the current account can manage Threat Analysis orders. Valid values:
        # - true: The account can purchase, upgrade, or modify Threat Analysis.
        # - false: The account cannot manage Threat Analysis orders.
        self.can_buy = can_buy
        # The purchased Simple Log Service (SLS) capacity for Threat Analysis. Unit: GB.
        self.capacity = capacity
        # The source of the log storage capacity order. Valid values:
        # - PRE_PAY_CAPACITY: The subscription capacity order.
        # - POST_PAY_CAPACITY: The pay-as-you-go capacity order.
        # The source of the capacity order is independent of the source of the traffic order represented by SiemOrderFrom.
        self.capacity_order_from = capacity_order_from
        # The information about the pay-as-you-go Credits instance. This field is returned when a pay-as-you-go Credits instance is found. It can be returned together with a valid legacy traffic order.
        self.credits_postpaid_info = credits_postpaid_info
        # The purchased SLS capacity for Threat Analysis 1.0. Unit: GB.
        self.delivery_capacity = delivery_capacity
        # The number of days until Threat Analysis expires.
        self.duration_days = duration_days
        # The expiration time of Threat Analysis. The value is a UNIX timestamp in milliseconds.
        self.end_time = end_time
        # The purchased traffic for Threat Analysis. Unit: GB.
        self.flow_capacity = flow_capacity
        # The Alibaba Cloud account ID used to purchase Threat Analysis.
        self.main_user_id = main_user_id
        # The ID of the master account in the resource directory.
        self.master_user_id = master_user_id
        # The ID of the resource directory.
        self.rd_id = rd_id
        # Specifies whether the order is for the public preview version of SIEM.
        self.rd_order = rd_order
        # The Security Center instance ID.
        self.sas_instance_id = sas_instance_id
        # The source of the traffic order. Valid values:
        # - PRE_PAY_FLOW: The subscription traffic order for Threat Analysis.
        # - POST_PAY_FLOW: The pay-as-you-go traffic order for Threat Analysis.
        # - CREDITS_PRE_PAY: The subscription of Agentic SOC Credits.
        # - CREDITS_POST_PAY: The pay-as-you-go instance of Agentic SOC Credits.
        # This field describes the source of the traffic order. The source of the log storage capacity order is independently represented by CapacityOrderFrom.
        self.siem_order_from = siem_order_from
        # Indicates whether a valid SIEM order exists. Valid values:
        # - 1: The SIEM order is valid.
        # - 0: The SIEM order is invalid.
        self.siem_order_status = siem_order_status
        # The current logon Alibaba Cloud account ID.
        self.sub_user_id = sub_user_id
        # The user type.
        self.user_type = user_type

    def validate(self):
        if self.credits_postpaid_info:
            self.credits_postpaid_info.validate()

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

        if self.credits_postpaid_info is not None:
            result['CreditsPostpaidInfo'] = self.credits_postpaid_info.to_map()

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

        if m.get('CreditsPostpaidInfo') is not None:
            temp_model = main_models.DescribeUserSiemOrderStatusResponseBodyDataCreditsPostpaidInfo()
            self.credits_postpaid_info = temp_model.from_map(m.get('CreditsPostpaidInfo'))

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

class DescribeUserSiemOrderStatusResponseBodyDataCreditsPostpaidInfo(DaraModel):
    def __init__(
        self,
        billing_status: int = None,
        instance_source: str = None,
        user_switch_status: int = None,
    ):
        # The billing status of the instance. Valid values:
        # - 1: Normal.
        # - 2: Suspended due to overdue payment.
        self.billing_status = billing_status
        # The source of the instance. Valid values:
        # - POSTPAID: The independent pay-as-you-go instance.
        # - SUBSCRIPTION_DEFAULT_PAYG: The default pay-as-you-go instance for the subscription.
        self.instance_source = instance_source
        # The user switch status. Valid values:
        # - 1: Enabled.
        # - 0: Disabled.
        self.user_switch_status = user_switch_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_status is not None:
            result['BillingStatus'] = self.billing_status

        if self.instance_source is not None:
            result['InstanceSource'] = self.instance_source

        if self.user_switch_status is not None:
            result['UserSwitchStatus'] = self.user_switch_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingStatus') is not None:
            self.billing_status = m.get('BillingStatus')

        if m.get('InstanceSource') is not None:
            self.instance_source = m.get('InstanceSource')

        if m.get('UserSwitchStatus') is not None:
            self.user_switch_status = m.get('UserSwitchStatus')

        return self


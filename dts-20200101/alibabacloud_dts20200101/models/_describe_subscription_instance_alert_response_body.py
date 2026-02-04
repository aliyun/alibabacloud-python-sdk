# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSubscriptionInstanceAlertResponseBody(DaraModel):
    def __init__(
        self,
        delay_alert_phone: str = None,
        delay_alert_status: str = None,
        delay_over_seconds: str = None,
        err_code: str = None,
        err_message: str = None,
        error_alert_phone: str = None,
        error_alert_status: str = None,
        request_id: str = None,
        subscription_instance_id: str = None,
        subscription_instance_name: str = None,
        success: str = None,
    ):
        # The mobile phone numbers that receive latency-related alerts.
        self.delay_alert_phone = delay_alert_phone
        # Indicates whether task latency is monitored. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.delay_alert_status = delay_alert_status
        # The threshold for triggering latency alerts. The unit is seconds and the value is an integer. The recommended value is 10 seconds.
        self.delay_over_seconds = delay_over_seconds
        # The error code returned if the call failed.
        self.err_code = err_code
        # The error message returned if the call failed.
        self.err_message = err_message
        # The mobile phone numbers that receive status-related alerts.
        self.error_alert_phone = error_alert_phone
        # Indicates whether task status is monitored. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        self.error_alert_status = error_alert_status
        # The ID of the request.
        self.request_id = request_id
        # The ID of the change tracking instance.
        self.subscription_instance_id = subscription_instance_id
        # The name of the change tracking instance.
        self.subscription_instance_name = subscription_instance_name
        # Indicates whether the call was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone

        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status

        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds

        if self.err_code is not None:
            result['ErrCode'] = self.err_code

        if self.err_message is not None:
            result['ErrMessage'] = self.err_message

        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone

        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.subscription_instance_id is not None:
            result['SubscriptionInstanceID'] = self.subscription_instance_id

        if self.subscription_instance_name is not None:
            result['SubscriptionInstanceName'] = self.subscription_instance_name

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')

        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')

        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')

        if m.get('ErrCode') is not None:
            self.err_code = m.get('ErrCode')

        if m.get('ErrMessage') is not None:
            self.err_message = m.get('ErrMessage')

        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')

        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubscriptionInstanceID') is not None:
            self.subscription_instance_id = m.get('SubscriptionInstanceID')

        if m.get('SubscriptionInstanceName') is not None:
            self.subscription_instance_name = m.get('SubscriptionInstanceName')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self


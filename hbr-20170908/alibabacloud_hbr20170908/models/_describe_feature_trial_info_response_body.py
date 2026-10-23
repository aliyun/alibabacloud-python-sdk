# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeFeatureTrialInfoResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        feature_enabled: bool = None,
        in_trial_period: bool = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
        trial_expire_time: int = None,
    ):
        # The return code. The value 200 indicates success.
        self.code = code
        # Indicates whether the feature is activated. The value false is returned if the feature is not activated. In this case, InTrialPeriod is false and TrialExpireTime is 0.
        self.feature_enabled = feature_enabled
        # Indicates whether the feature is within the free trial period. The value false is returned if the feature is not activated or the free trial has expired.
        self.in_trial_period = in_trial_period
        # The returned message. The value "successful" is returned upon success. An error message is returned upon failure.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # - true: The request was successful.
        # - false: The request failed.
        self.success = success
        # The expiration time of the free trial. The value is a UNIX timestamp, in seconds. The value 0 is returned if the feature is not activated.
        self.trial_expire_time = trial_expire_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.feature_enabled is not None:
            result['FeatureEnabled'] = self.feature_enabled

        if self.in_trial_period is not None:
            result['InTrialPeriod'] = self.in_trial_period

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.trial_expire_time is not None:
            result['TrialExpireTime'] = self.trial_expire_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('FeatureEnabled') is not None:
            self.feature_enabled = m.get('FeatureEnabled')

        if m.get('InTrialPeriod') is not None:
            self.in_trial_period = m.get('InTrialPeriod')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TrialExpireTime') is not None:
            self.trial_expire_time = m.get('TrialExpireTime')

        return self


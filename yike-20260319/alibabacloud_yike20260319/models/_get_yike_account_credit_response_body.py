# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_yike20260319 import models as main_models
from darabonba.model import DaraModel

class GetYikeAccountCreditResponseBody(DaraModel):
    def __init__(
        self,
        credit_info: main_models.GetYikeAccountCreditResponseBodyCreditInfo = None,
        membership_info: main_models.GetYikeAccountCreditResponseBodyMembershipInfo = None,
        request_id: str = None,
    ):
        # The credit information.
        self.credit_info = credit_info
        # The membership information.
        self.membership_info = membership_info
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.credit_info:
            self.credit_info.validate()
        if self.membership_info:
            self.membership_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.credit_info is not None:
            result['CreditInfo'] = self.credit_info.to_map()

        if self.membership_info is not None:
            result['MembershipInfo'] = self.membership_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreditInfo') is not None:
            temp_model = main_models.GetYikeAccountCreditResponseBodyCreditInfo()
            self.credit_info = temp_model.from_map(m.get('CreditInfo'))

        if m.get('MembershipInfo') is not None:
            temp_model = main_models.GetYikeAccountCreditResponseBodyMembershipInfo()
            self.membership_info = temp_model.from_map(m.get('MembershipInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetYikeAccountCreditResponseBodyMembershipInfo(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        membership: str = None,
        start_time: str = None,
    ):
        # The end time.
        self.end_time = end_time
        # The membership level. Valid values:
        # 
        # - basic: Basic Edition.
        # - standard: Standard Edition.
        # - professional: Ultimate Edition.
        # - ultra: Ultra Edition.
        self.membership = membership
        # The start time.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.membership is not None:
            result['Membership'] = self.membership

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Membership') is not None:
            self.membership = m.get('Membership')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class GetYikeAccountCreditResponseBodyCreditInfo(DaraModel):
    def __init__(
        self,
        granted_credit_quota: float = None,
        granted_credit_quota_usage: float = None,
        pack_credit_quota: float = None,
        pack_credit_quota_usage: float = None,
        resource_credit_quota: float = None,
        resource_credit_quota_usage: float = None,
    ):
        # The total granted credits.
        self.granted_credit_quota = granted_credit_quota
        # The remaining granted credits.
        self.granted_credit_quota_usage = granted_credit_quota_usage
        # The total credits of the booster pack.
        self.pack_credit_quota = pack_credit_quota
        # The remaining credits of the booster pack.
        self.pack_credit_quota_usage = pack_credit_quota_usage
        # The total credits of the membership plan.
        self.resource_credit_quota = resource_credit_quota
        # The remaining credits of the membership plan.
        self.resource_credit_quota_usage = resource_credit_quota_usage

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.granted_credit_quota is not None:
            result['GrantedCreditQuota'] = self.granted_credit_quota

        if self.granted_credit_quota_usage is not None:
            result['GrantedCreditQuotaUsage'] = self.granted_credit_quota_usage

        if self.pack_credit_quota is not None:
            result['PackCreditQuota'] = self.pack_credit_quota

        if self.pack_credit_quota_usage is not None:
            result['PackCreditQuotaUsage'] = self.pack_credit_quota_usage

        if self.resource_credit_quota is not None:
            result['ResourceCreditQuota'] = self.resource_credit_quota

        if self.resource_credit_quota_usage is not None:
            result['ResourceCreditQuotaUsage'] = self.resource_credit_quota_usage

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GrantedCreditQuota') is not None:
            self.granted_credit_quota = m.get('GrantedCreditQuota')

        if m.get('GrantedCreditQuotaUsage') is not None:
            self.granted_credit_quota_usage = m.get('GrantedCreditQuotaUsage')

        if m.get('PackCreditQuota') is not None:
            self.pack_credit_quota = m.get('PackCreditQuota')

        if m.get('PackCreditQuotaUsage') is not None:
            self.pack_credit_quota_usage = m.get('PackCreditQuotaUsage')

        if m.get('ResourceCreditQuota') is not None:
            self.resource_credit_quota = m.get('ResourceCreditQuota')

        if m.get('ResourceCreditQuotaUsage') is not None:
            self.resource_credit_quota_usage = m.get('ResourceCreditQuotaUsage')

        return self


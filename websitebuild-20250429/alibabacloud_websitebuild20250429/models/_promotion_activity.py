# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PromotionActivity(DaraModel):
    def __init__(
        self,
        activity_code: str = None,
        activity_name: str = None,
        activity_type: str = None,
        consumed_quota: int = None,
        create_time: str = None,
        created_by: str = None,
        eligibility_config: str = None,
        end_date: str = None,
        offer_config: str = None,
        offer_config_summary: str = None,
        remaining_quota: int = None,
        start_date: str = None,
        status: str = None,
        total_quota: int = None,
        touchpoint_config: str = None,
        update_time: str = None,
        updated_by: str = None,
        warning_threshold: int = None,
    ):
        self.activity_code = activity_code
        self.activity_name = activity_name
        self.activity_type = activity_type
        self.consumed_quota = consumed_quota
        self.create_time = create_time
        self.created_by = created_by
        self.eligibility_config = eligibility_config
        self.end_date = end_date
        self.offer_config = offer_config
        self.offer_config_summary = offer_config_summary
        self.remaining_quota = remaining_quota
        self.start_date = start_date
        self.status = status
        self.total_quota = total_quota
        self.touchpoint_config = touchpoint_config
        self.update_time = update_time
        self.updated_by = updated_by
        self.warning_threshold = warning_threshold

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.activity_code is not None:
            result['ActivityCode'] = self.activity_code

        if self.activity_name is not None:
            result['ActivityName'] = self.activity_name

        if self.activity_type is not None:
            result['ActivityType'] = self.activity_type

        if self.consumed_quota is not None:
            result['ConsumedQuota'] = self.consumed_quota

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_by is not None:
            result['CreatedBy'] = self.created_by

        if self.eligibility_config is not None:
            result['EligibilityConfig'] = self.eligibility_config

        if self.end_date is not None:
            result['EndDate'] = self.end_date

        if self.offer_config is not None:
            result['OfferConfig'] = self.offer_config

        if self.offer_config_summary is not None:
            result['OfferConfigSummary'] = self.offer_config_summary

        if self.remaining_quota is not None:
            result['RemainingQuota'] = self.remaining_quota

        if self.start_date is not None:
            result['StartDate'] = self.start_date

        if self.status is not None:
            result['Status'] = self.status

        if self.total_quota is not None:
            result['TotalQuota'] = self.total_quota

        if self.touchpoint_config is not None:
            result['TouchpointConfig'] = self.touchpoint_config

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.updated_by is not None:
            result['UpdatedBy'] = self.updated_by

        if self.warning_threshold is not None:
            result['WarningThreshold'] = self.warning_threshold

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActivityCode') is not None:
            self.activity_code = m.get('ActivityCode')

        if m.get('ActivityName') is not None:
            self.activity_name = m.get('ActivityName')

        if m.get('ActivityType') is not None:
            self.activity_type = m.get('ActivityType')

        if m.get('ConsumedQuota') is not None:
            self.consumed_quota = m.get('ConsumedQuota')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedBy') is not None:
            self.created_by = m.get('CreatedBy')

        if m.get('EligibilityConfig') is not None:
            self.eligibility_config = m.get('EligibilityConfig')

        if m.get('EndDate') is not None:
            self.end_date = m.get('EndDate')

        if m.get('OfferConfig') is not None:
            self.offer_config = m.get('OfferConfig')

        if m.get('OfferConfigSummary') is not None:
            self.offer_config_summary = m.get('OfferConfigSummary')

        if m.get('RemainingQuota') is not None:
            self.remaining_quota = m.get('RemainingQuota')

        if m.get('StartDate') is not None:
            self.start_date = m.get('StartDate')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TotalQuota') is not None:
            self.total_quota = m.get('TotalQuota')

        if m.get('TouchpointConfig') is not None:
            self.touchpoint_config = m.get('TouchpointConfig')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdatedBy') is not None:
            self.updated_by = m.get('UpdatedBy')

        if m.get('WarningThreshold') is not None:
            self.warning_threshold = m.get('WarningThreshold')

        return self


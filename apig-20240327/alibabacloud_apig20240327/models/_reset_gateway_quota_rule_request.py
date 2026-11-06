# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ResetGatewayQuotaRuleRequest(DaraModel):
    def __init__(
        self,
        conflict_hash: str = None,
        dry_run: bool = None,
        overwrite: bool = None,
        period_multiplier: int = None,
        period_type: str = None,
        quota_limit: int = None,
        timezone: str = None,
        window_alignment: str = None,
    ):
        # The conflict snapshot hash, which is used to prevent concurrent dirty overwrites when overwriting is confirmed. You can obtain this value by first executing a request with dryRun=true and extracting it from the returned data.
        # 
        # This parameter is not required in the following scenarios: no conflicts exist; the request is only a dry run with dryRun=true; overwrite=false, meaning overwriting is not confirmed.
        # 
        # If dryRun=false and overwrite=true but this parameter is not provided or has expired and does not match, the backend returns accepted=false along with a new conflict preview. You must perform a dry run again to confirm the new conflicts.
        self.conflict_hash = conflict_hash
        # Specifies whether to perform a dry run only without saving to the database or delivering actual configurations. This is used to check whether conflicting rules exist on the bound subjects. A single subject cannot be configured with two natural period quotas of the same period. For example, a subject that already has a natural daily quota cannot be added with another natural daily quota rule.
        self.dry_run = dry_run
        # Specifies whether to allow overwriting when a conflict occurs. Note that if overwriting is allowed, the conflicting subjects (consumers or consumer groups) are unbound from the old rule and bound to the new rule.
        self.overwrite = overwrite
        # The period multiplier, which specifies the number of periods after which the quota is reset. This parameter is returned when the rule uses a custom period. Minimum value: 1. Maximum value: 60.
        self.period_multiplier = period_multiplier
        # The period type. Natural periods support daily, weekly, and monthly statistics, and valid values are day, week, and month. Custom periods support only daily statistics, and the fixed value is day.
        self.period_type = period_type
        # The total available quota per period after the reset.
        self.quota_limit = quota_limit
        # The time zone corresponding to the natural period, in UTC+x format.
        self.timezone = timezone
        # The period type for the reset. Natural periods (windowAlignment=calendar) and custom periods (windowAlignment=epoch) are supported.
        self.window_alignment = window_alignment

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.conflict_hash is not None:
            result['conflictHash'] = self.conflict_hash

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.overwrite is not None:
            result['overwrite'] = self.overwrite

        if self.period_multiplier is not None:
            result['periodMultiplier'] = self.period_multiplier

        if self.period_type is not None:
            result['periodType'] = self.period_type

        if self.quota_limit is not None:
            result['quotaLimit'] = self.quota_limit

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.window_alignment is not None:
            result['windowAlignment'] = self.window_alignment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conflictHash') is not None:
            self.conflict_hash = m.get('conflictHash')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')

        if m.get('periodMultiplier') is not None:
            self.period_multiplier = m.get('periodMultiplier')

        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')

        if m.get('quotaLimit') is not None:
            self.quota_limit = m.get('quotaLimit')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('windowAlignment') is not None:
            self.window_alignment = m.get('windowAlignment')

        return self


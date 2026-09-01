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
        # The conflict snapshot hash, used to prevent concurrent dirty overwrites when confirming an overwrite. Obtain this value from the response of a previous dryRun=true call.
        # 
        # You do not need to specify this parameter in the following cases: no conflicts exist, you are performing a dry run (dryRun=true), or you are not confirming an overwrite (overwrite=false).
        # 
        # When dryRun is set to false and overwrite is set to true, if this parameter is not specified or the value has expired and no longer matches, the backend returns accepted=false with a new conflict preview. You must perform the dry run again to confirm the new conflicts.
        self.conflict_hash = conflict_hash
        # Specifies whether to perform only a dry run without persisting or applying the configuration. A dry run checks whether conflicting rules exist on the bound subjects. The same subject cannot have two calendar-period quotas with the same period. For example, a subject that already has a daily calendar quota cannot have another daily calendar quota rule added.
        self.dry_run = dry_run
        # Specifies whether to allow overwriting when conflicts exist. If you allow overwriting, the conflicting subjects (consumers or consumer groups) are unbound from the old rule and bound to the new rule.
        self.overwrite = overwrite
        # The period multiplier, which specifies the number of periods after which the quota is reset. This parameter is returned when the rule uses a custom period. Minimum value: 1. Maximum value: 60.
        self.period_multiplier = period_multiplier
        # The period type. Calendar periods support daily, weekly, and monthly statistics. Valid values: day, week, and month. Custom periods support only daily statistics. The value is fixed to day.
        self.period_type = period_type
        # The total available quota per period after the reset.
        self.quota_limit = quota_limit
        # The time zone for the calendar period, in UTC+x format.
        self.timezone = timezone
        # The period alignment type after the reset. Valid values:
        # - calendar: calendar period.
        # - epoch: custom period.
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


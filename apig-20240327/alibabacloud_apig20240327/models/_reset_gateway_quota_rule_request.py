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
        # The conflict snapshot hash, used to prevent concurrent dirty overwrites when confirming an overwrite. Obtain this value from the response of a dryRun=true request.
        # 
        # This parameter is not required in the following cases: no conflict exists, the request is a dry run (dryRun=true), or overwrite=false (overwrite not confirmed).
        # 
        # When dryRun=false and overwrite=true, if this parameter is not provided or the value has expired and does not match, the backend returns accepted=false with a new conflict preview. You must perform a dry run again to confirm the new conflict.
        self.conflict_hash = conflict_hash
        # Specifies whether to perform only a dry run without delivering the actual configuration. A dry run checks whether conflicting rules exist on the bound consumers. For example, a consumer that already has a calendar-day quota cannot have another calendar-day quota rule added.
        self.dry_run = dry_run
        # Specifies whether to allow overwriting on conflict. If overwriting is allowed, the conflicting subject (consumer) is unbound from the old rule and bound to the new rule.
        self.overwrite = overwrite
        # The period multiplier. Specifies how many periods elapse before the quota resets. Returned when the rule uses a custom period. Minimum value: 1. Maximum value: 60.
        self.period_multiplier = period_multiplier
        # The period type. Calendar periods support daily, weekly, and monthly statistics. Valid values: day, week, and month. Custom periods support only daily statistics. The value is fixed to day.
        self.period_type = period_type
        # The total available quota per period after the reset.
        self.quota_limit = quota_limit
        # The time zone for the calendar period in UTC+x format.
        self.timezone = timezone
        # The period type after the reset. Valid values:
        # 
        # - calendar: calendar period.
        # - epoch: custom period. Custom periods are supported only on dedicated instances with version 2.1.19 or later.
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


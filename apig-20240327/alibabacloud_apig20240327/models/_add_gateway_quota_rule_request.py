# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class AddGatewayQuotaRuleRequest(DaraModel):
    def __init__(
        self,
        conflict_hash: str = None,
        consumer_group_ids: List[str] = None,
        consumer_ids: List[str] = None,
        dry_run: bool = None,
        overwrite: bool = None,
        period_multiplier: int = None,
        period_type: str = None,
        quota_dimension: str = None,
        quota_limit: int = None,
        rule_name: str = None,
        subject_type: str = None,
        timezone: str = None,
        window_alignment: str = None,
    ):
        # The conflict snapshot hash, used to prevent concurrent dirty overwrites during confirmation. Obtain this value from the response of a previous dryRun=true request.
        # 
        # This parameter is not required in the following cases: no conflicts exist, the request is a dry run (dryRun=true), or overwrite=false (no overwrite confirmation).
        # 
        # When dryRun=false and overwrite=true, if this parameter is not provided or the value has expired and no longer matches, the backend returns accepted=false with a new conflict preview. Perform a dry run again to confirm the new conflicts.
        self.conflict_hash = conflict_hash
        # The list of consumer group IDs (not supported currently).
        self.consumer_group_ids = consumer_group_ids
        # The list of consumer IDs to bind to the rule. A maximum of 1000 consumers can be specified in a single request.
        self.consumer_ids = consumer_ids
        # Specifies whether to perform only a dry run without applying the configuration. A dry run checks whether conflicting rules exist on the bound consumers. For example, a consumer that already has a calendar-day quota cannot have another calendar-day quota rule added.
        self.dry_run = dry_run
        # Specifies whether to allow overwriting when conflicts exist. If overwriting is allowed, the conflicting subjects (consumers) are unbound from the old rule and bound to the new rule.
        self.overwrite = overwrite
        # The period multiplier. This parameter applies to epoch period rules.
        self.period_multiplier = period_multiplier
        # The period type. For calendar periods, statistics are collected by day, week, or month. Valid values: day, week, and month. For epoch periods, only day is supported.
        # 
        # This parameter is required.
        self.period_type = period_type
        # The quota dimension or throttling type. Valid values: token and credit. The credit quota applies only to dedicated instances running version 2.1.19 or later.
        # 
        # This parameter is required.
        self.quota_dimension = quota_dimension
        # The total available quota per period (limit).
        # 
        # This parameter is required.
        self.quota_limit = quota_limit
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The rule subject type. Valid values: consumer (a consumer) and consumer_group (a consumer group). Default value: consumer.
        self.subject_type = subject_type
        # The time zone for the calendar period, in UTC+x format.
        self.timezone = timezone
        # The reset period type. Valid values: calendar (the period starts from the beginning of a calendar day, week, or month) and epoch (the period starts from when the rule is applied). The epoch type applies only to dedicated instances running version 2.1.19 or later.
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

        if self.consumer_group_ids is not None:
            result['consumerGroupIds'] = self.consumer_group_ids

        if self.consumer_ids is not None:
            result['consumerIds'] = self.consumer_ids

        if self.dry_run is not None:
            result['dryRun'] = self.dry_run

        if self.overwrite is not None:
            result['overwrite'] = self.overwrite

        if self.period_multiplier is not None:
            result['periodMultiplier'] = self.period_multiplier

        if self.period_type is not None:
            result['periodType'] = self.period_type

        if self.quota_dimension is not None:
            result['quotaDimension'] = self.quota_dimension

        if self.quota_limit is not None:
            result['quotaLimit'] = self.quota_limit

        if self.rule_name is not None:
            result['ruleName'] = self.rule_name

        if self.subject_type is not None:
            result['subjectType'] = self.subject_type

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.window_alignment is not None:
            result['windowAlignment'] = self.window_alignment

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('conflictHash') is not None:
            self.conflict_hash = m.get('conflictHash')

        if m.get('consumerGroupIds') is not None:
            self.consumer_group_ids = m.get('consumerGroupIds')

        if m.get('consumerIds') is not None:
            self.consumer_ids = m.get('consumerIds')

        if m.get('dryRun') is not None:
            self.dry_run = m.get('dryRun')

        if m.get('overwrite') is not None:
            self.overwrite = m.get('overwrite')

        if m.get('periodMultiplier') is not None:
            self.period_multiplier = m.get('periodMultiplier')

        if m.get('periodType') is not None:
            self.period_type = m.get('periodType')

        if m.get('quotaDimension') is not None:
            self.quota_dimension = m.get('quotaDimension')

        if m.get('quotaLimit') is not None:
            self.quota_limit = m.get('quotaLimit')

        if m.get('ruleName') is not None:
            self.rule_name = m.get('ruleName')

        if m.get('subjectType') is not None:
            self.subject_type = m.get('subjectType')

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('windowAlignment') is not None:
            self.window_alignment = m.get('windowAlignment')

        return self


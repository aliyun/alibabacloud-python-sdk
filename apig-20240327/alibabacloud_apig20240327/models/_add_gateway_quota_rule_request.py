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
        # The conflict snapshot hash used to prevent concurrent dirty overwrites during confirmation. Obtain this value from the response of a previous dry run (dryRun=true).
        # 
        # This parameter is not required in the following cases: no conflicts exist, the request is a dry run (dryRun=true), or overwrite is set to false.
        # 
        # When dryRun is set to false and overwrite is set to true, if this parameter is not provided or the value has expired and no longer matches, the backend returns accepted=false with a new conflict preview. In this case, perform a new dry run to confirm the latest conflicts.
        self.conflict_hash = conflict_hash
        # The list of API consumer group IDs to bind to the rule. This parameter is used when subjectType is set to consumer_group and cannot be specified together with consumerIds.
        self.consumer_group_ids = consumer_group_ids
        # The list of API consumer IDs to bind to the rule. A maximum of 1,000 consumers can be specified in a single request.
        self.consumer_ids = consumer_ids
        # Specifies whether to perform only a dry run without persisting or applying the configuration. A dry run checks whether conflicting rules exist on the bound consumer subjects. For example, a consumer subject that already has a calendar-day quota rule cannot have another calendar-day quota rule added.
        self.dry_run = dry_run
        # Specifies whether to allow overwriting when conflicts exist. If overwriting is allowed, the conflicting subjects (consumers or consumer groups) are unbound from the old rule and bound to the new rule.
        self.overwrite = overwrite
        # The period multiplier, which specifies the number of periods after which the quota resets. This parameter is required for custom (epoch) period rules. Minimum value: 1. Maximum value: 60.
        self.period_multiplier = period_multiplier
        # The period type. For calendar periods, the quota can be calculated by day, week, or month. Valid values: day, week, and month. For custom (epoch) periods, only day is supported.
        # 
        # This parameter is required.
        self.period_type = period_type
        # The quota dimension or throttling type. Valid values: token and credit.
        # 
        # This parameter is required.
        self.quota_dimension = quota_dimension
        # The total available quota per period.
        # 
        # This parameter is required.
        self.quota_limit = quota_limit
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The type of the rule subject. Valid values:
        # - consumer: API consumer.
        # - consumer_group: API consumer group.
        # 
        # Default value: consumer.
        self.subject_type = subject_type
        # The time zone for calendar periods, in UTC+x format.
        self.timezone = timezone
        # The reset period alignment type. Valid values:
        # - calendar: The quota resets at the beginning of a calendar day, week, or month.
        # - epoch: The quota resets based on a custom period that starts when the rule takes effect.
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


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
        # The conflict snapshot hash, which is used to prevent concurrent dirty overwrites when you confirm to overwrite. You can obtain this value by first setting dryRun to true and extracting it from the response.
        # 
        # You do not need to specify this parameter in the following scenarios: no conflicts exist; you only perform a dry run by setting dryRun to true; or you do not confirm overwriting by setting overwrite to false.
        # 
        # If you set dryRun to false and overwrite to true but do not specify this parameter or the parameter expires and does not match, the backend returns accepted=false along with a new conflict preview. In this case, you must perform a dry run again to confirm the new conflicts.
        self.conflict_hash = conflict_hash
        # The IDs of the consumer groups to which the rule is bound. This parameter is used when subjectType is set to consumer_group and cannot be specified together with consumerIds.
        self.consumer_group_ids = consumer_group_ids
        # The IDs of the consumers to which the rule is bound. You can specify up to 1,000 consumers in a single request.
        self.consumer_ids = consumer_ids
        # Specifies whether to perform only a dry run without saving or delivering the actual configuration. This is used to check whether conflicting rules exist on the bound consumption subjects. A single consumption subject cannot be configured with two natural period quotas of the same period. For example, a consumption subject that already has a natural day quota cannot be added with another natural day quota rule.
        self.dry_run = dry_run
        # Specifies whether to allow overwriting when a conflict occurs. If overwriting is allowed, the conflicting subjects (consumers or consumer groups) are unbound from the old rule and bound to the new rule.
        self.overwrite = overwrite
        # The period multiplier in days. This parameter is required for custom period rules and applies when windowAlignment is set to epoch. Valid values: 1 to 106751. Do not set this parameter for natural periods.
        self.period_multiplier = period_multiplier
        # The period type. For natural periods, valid values are day, week, and month. For custom periods, only day is supported.
        # 
        # This parameter is required.
        self.period_type = period_type
        # The quota dimension or limit type. Valid values: token, credit.
        # 
        # This parameter is required.
        self.quota_dimension = quota_dimension
        # The total available quota (limit) per period.
        # 
        # This parameter is required.
        self.quota_limit = quota_limit
        # The name of the rule.
        # 
        # This parameter is required.
        self.rule_name = rule_name
        # The subject type of the rule. Valid values: consumer, consumer_group. Default value: consumer.
        self.subject_type = subject_type
        # The time zone for the natural period in UTC+x format.
        self.timezone = timezone
        # The reset period type. A natural period starts from the beginning of a natural day, week, or month. A custom period starts when the rule is delivered. Valid values: calendar, epoch.
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


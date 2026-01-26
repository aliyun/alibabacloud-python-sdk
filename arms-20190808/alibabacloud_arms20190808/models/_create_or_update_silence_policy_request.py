# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateOrUpdateSilencePolicyRequest(DaraModel):
    def __init__(
        self,
        effective_time_type: str = None,
        id: int = None,
        matching_rules: str = None,
        name: str = None,
        region_id: str = None,
        state: str = None,
        time_period: str = None,
        time_slots: str = None,
    ):
        # The effective duration of the silence policy. Valid values: PERMANENT, CUSTOM_TIME, and CYCLE_EFFECT.
        self.effective_time_type = effective_time_type
        # The ID of the silence policy.
        # 
        # *   If you do not configure this parameter, a new silence policy is created.
        # *   If you configure this parameter, the specified silence policy is modified.
        self.id = id
        # The matching rules. The following code shows the format of matching rules:
        # 
        #     [
        #          {
        #     	 "matchingConditions": [
        #     	 {
        #     	 "value": "test", // The value of the matching condition. 
        #     	 "key": "altertname", // The key of the matching condition. 
        #     	 "operator": "eq" // The logical operator of the matching condition, including eq (equal to), neq (not equal to), in (contains), nin (does not contain), re (regular expression match), and nre (regular expression mismatch).   
        #     	 }
        #     	 ]
        #          }
        #     	 ]
        self.matching_rules = matching_rules
        # The name of the silence policy.
        # 
        # This parameter is required.
        self.name = name
        # The ID of the region.
        self.region_id = region_id
        # Specifies whether to enable the silence policy. Valid values: enable and disable.
        self.state = state
        # The recurring period. This parameter is required when EffectiveTimeType is set to CYCLE_EFFECT. DAY: The silence policy is effective by day. WEEK: The silence policy is effective by week.
        self.time_period = time_period
        # The time period during which the silence policy is effective. If you set EffectiveTimeType to CUSTOM_TIME, specify a custom time period in the following format: [{"startTime":"2024-08-04 22:13","endTime":"2024-08-04 22:21"}] If you set EffectiveTimeType to CYCLE_EFFECT and TimePeriod to DAY, specify a custom time period in the following format: [{"startTime":"22:13","endTime":"22:21"}]. The start time cannot be later than the end time. If you set EffectiveTimeType to CYCLE_EFFECT and TimePeriod to WEEK, specify a custom time period in the following format: [{"startWeek":"1", "endWeek":"2" "startTime":"22:13","endTime":"22:21"}]. Valid values of startWeek and endWeek: 1 to 7. The start time cannot be later than the end time.
        self.time_slots = time_slots

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.effective_time_type is not None:
            result['EffectiveTimeType'] = self.effective_time_type

        if self.id is not None:
            result['Id'] = self.id

        if self.matching_rules is not None:
            result['MatchingRules'] = self.matching_rules

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.state is not None:
            result['State'] = self.state

        if self.time_period is not None:
            result['TimePeriod'] = self.time_period

        if self.time_slots is not None:
            result['TimeSlots'] = self.time_slots

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EffectiveTimeType') is not None:
            self.effective_time_type = m.get('EffectiveTimeType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('MatchingRules') is not None:
            self.matching_rules = m.get('MatchingRules')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('TimePeriod') is not None:
            self.time_period = m.get('TimePeriod')

        if m.get('TimeSlots') is not None:
            self.time_slots = m.get('TimeSlots')

        return self


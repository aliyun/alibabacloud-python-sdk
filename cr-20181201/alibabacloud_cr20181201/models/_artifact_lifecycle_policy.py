# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_cr20181201 import models as main_models
from darabonba.model import DaraModel

class ArtifactLifecyclePolicy(DaraModel):
    def __init__(
        self,
        condition: main_models.ArtifactLifecyclePolicyCondition = None,
        filter: main_models.ArtifactLifecyclePolicyFilter = None,
        type: str = None,
    ):
        self.condition = condition
        self.filter = filter
        self.type = type

    def validate(self):
        if self.condition:
            self.condition.validate()
        if self.filter:
            self.filter.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.condition is not None:
            result['Condition'] = self.condition.to_map()

        if self.filter is not None:
            result['Filter'] = self.filter.to_map()

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Condition') is not None:
            temp_model = main_models.ArtifactLifecyclePolicyCondition()
            self.condition = temp_model.from_map(m.get('Condition'))

        if m.get('Filter') is not None:
            temp_model = main_models.ArtifactLifecyclePolicyFilter()
            self.filter = temp_model.from_map(m.get('Filter'))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class ArtifactLifecyclePolicyFilter(DaraModel):
    def __init__(
        self,
        tag_wildcard: str = None,
    ):
        self.tag_wildcard = tag_wildcard

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_wildcard is not None:
            result['TagWildcard'] = self.tag_wildcard

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagWildcard') is not None:
            self.tag_wildcard = m.get('TagWildcard')

        return self



class ArtifactLifecyclePolicyCondition(DaraModel):
    def __init__(
        self,
        last_pull_older_than_days: int = None,
        last_push_older_than_days: int = None,
        latest_tag_count: int = None,
    ):
        self.last_pull_older_than_days = last_pull_older_than_days
        self.last_push_older_than_days = last_push_older_than_days
        self.latest_tag_count = latest_tag_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.last_pull_older_than_days is not None:
            result['LastPullOlderThanDays'] = self.last_pull_older_than_days

        if self.last_push_older_than_days is not None:
            result['LastPushOlderThanDays'] = self.last_push_older_than_days

        if self.latest_tag_count is not None:
            result['LatestTagCount'] = self.latest_tag_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LastPullOlderThanDays') is not None:
            self.last_pull_older_than_days = m.get('LastPullOlderThanDays')

        if m.get('LastPushOlderThanDays') is not None:
            self.last_push_older_than_days = m.get('LastPushOlderThanDays')

        if m.get('LatestTagCount') is not None:
            self.latest_tag_count = m.get('LatestTagCount')

        return self


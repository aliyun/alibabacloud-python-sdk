# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class ListEvaluationResultsRequest(DaraModel):
    def __init__(
        self,
        account_id: int = None,
        filters: List[main_models.ListEvaluationResultsRequestFilters] = None,
        lens_code: str = None,
        region_id: str = None,
        scope: str = None,
        snapshot_id: str = None,
        topic_code: str = None,
    ):
        # The Alibaba Cloud account ID of the member. This parameter takes effect only when a multi-account governance maturity check is performed.
        self.account_id = account_id
        # The filter conditions.
        self.filters = filters
        self.lens_code = lens_code
        # The region ID.
        self.region_id = region_id
        self.scope = scope
        self.snapshot_id = snapshot_id
        self.topic_code = topic_code

    def validate(self):
        if self.filters:
            for v1 in self.filters:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        result['Filters'] = []
        if self.filters is not None:
            for k1 in self.filters:
                result['Filters'].append(k1.to_map() if k1 else None)

        if self.lens_code is not None:
            result['LensCode'] = self.lens_code

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.snapshot_id is not None:
            result['SnapshotId'] = self.snapshot_id

        if self.topic_code is not None:
            result['TopicCode'] = self.topic_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        self.filters = []
        if m.get('Filters') is not None:
            for k1 in m.get('Filters'):
                temp_model = main_models.ListEvaluationResultsRequestFilters()
                self.filters.append(temp_model.from_map(k1))

        if m.get('LensCode') is not None:
            self.lens_code = m.get('LensCode')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SnapshotId') is not None:
            self.snapshot_id = m.get('SnapshotId')

        if m.get('TopicCode') is not None:
            self.topic_code = m.get('TopicCode')

        return self

class ListEvaluationResultsRequestFilters(DaraModel):
    def __init__(
        self,
        key: str = None,
        values: List[str] = None,
    ):
        # The key of the filter condition. Valid values:
        # 
        # *   ResourceId: the resource ID.
        # *   ResourceName: the name of the resource.
        # *   ResourceType: the resource type.
        self.key = key
        # The list of filter condition values.
        self.values = values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.values is not None:
            result['Values'] = self.values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Values') is not None:
            self.values = m.get('Values')

        return self


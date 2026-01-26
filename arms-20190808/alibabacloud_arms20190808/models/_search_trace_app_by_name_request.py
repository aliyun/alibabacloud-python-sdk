# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_arms20190808 import models as main_models
from darabonba.model import DaraModel

class SearchTraceAppByNameRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        tags: List[main_models.SearchTraceAppByNameRequestTags] = None,
        trace_app_name: str = None,
    ):
        # The region ID.
        self.region_id = region_id
        # The list of tags.
        self.tags = tags
        # The name of the application.
        # 
        # > If you do not specify this parameter, all application monitoring tasks in the specified region are queried.
        self.trace_app_name = trace_app_name

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.trace_app_name is not None:
            result['TraceAppName'] = self.trace_app_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.SearchTraceAppByNameRequestTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('TraceAppName') is not None:
            self.trace_app_name = m.get('TraceAppName')

        return self

class SearchTraceAppByNameRequestTags(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


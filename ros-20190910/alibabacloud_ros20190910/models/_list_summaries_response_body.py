# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ros20190910 import models as main_models
from darabonba.model import DaraModel

class ListSummariesResponseBody(DaraModel):
    def __init__(
        self,
        center_summary: main_models.ListSummariesResponseBodyCenterSummary = None,
        region_summaries: List[main_models.ListSummariesResponseBodyRegionSummaries] = None,
        request_id: str = None,
    ):
        self.center_summary = center_summary
        self.region_summaries = region_summaries
        self.request_id = request_id

    def validate(self):
        if self.center_summary:
            self.center_summary.validate()
        if self.region_summaries:
            for v1 in self.region_summaries:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.center_summary is not None:
            result['CenterSummary'] = self.center_summary.to_map()

        result['RegionSummaries'] = []
        if self.region_summaries is not None:
            for k1 in self.region_summaries:
                result['RegionSummaries'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CenterSummary') is not None:
            temp_model = main_models.ListSummariesResponseBodyCenterSummary()
            self.center_summary = temp_model.from_map(m.get('CenterSummary'))

        self.region_summaries = []
        if m.get('RegionSummaries') is not None:
            for k1 in m.get('RegionSummaries'):
                temp_model = main_models.ListSummariesResponseBodyRegionSummaries()
                self.region_summaries.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListSummariesResponseBodyRegionSummaries(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        stack_count: str = None,
        stack_details: List[main_models.ListSummariesResponseBodyRegionSummariesStackDetails] = None,
        stack_group_count: str = None,
        template_scratch_count: int = None,
    ):
        self.region_id = region_id
        self.stack_count = stack_count
        self.stack_details = stack_details
        self.stack_group_count = stack_group_count
        self.template_scratch_count = template_scratch_count

    def validate(self):
        if self.stack_details:
            for v1 in self.stack_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.stack_count is not None:
            result['StackCount'] = self.stack_count

        result['StackDetails'] = []
        if self.stack_details is not None:
            for k1 in self.stack_details:
                result['StackDetails'].append(k1.to_map() if k1 else None)

        if self.stack_group_count is not None:
            result['StackGroupCount'] = self.stack_group_count

        if self.template_scratch_count is not None:
            result['TemplateScratchCount'] = self.template_scratch_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('StackCount') is not None:
            self.stack_count = m.get('StackCount')

        self.stack_details = []
        if m.get('StackDetails') is not None:
            for k1 in m.get('StackDetails'):
                temp_model = main_models.ListSummariesResponseBodyRegionSummariesStackDetails()
                self.stack_details.append(temp_model.from_map(k1))

        if m.get('StackGroupCount') is not None:
            self.stack_group_count = m.get('StackGroupCount')

        if m.get('TemplateScratchCount') is not None:
            self.template_scratch_count = m.get('TemplateScratchCount')

        return self

class ListSummariesResponseBodyRegionSummariesStackDetails(DaraModel):
    def __init__(
        self,
        brief_status: str = None,
        count: str = None,
    ):
        self.brief_status = brief_status
        self.count = count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.brief_status is not None:
            result['BriefStatus'] = self.brief_status

        if self.count is not None:
            result['Count'] = self.count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BriefStatus') is not None:
            self.brief_status = m.get('BriefStatus')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        return self

class ListSummariesResponseBodyCenterSummary(DaraModel):
    def __init__(
        self,
        registered_resource_type_count: int = None,
        template_count: str = None,
    ):
        self.registered_resource_type_count = registered_resource_type_count
        self.template_count = template_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.registered_resource_type_count is not None:
            result['RegisteredResourceTypeCount'] = self.registered_resource_type_count

        if self.template_count is not None:
            result['TemplateCount'] = self.template_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegisteredResourceTypeCount') is not None:
            self.registered_resource_type_count = m.get('RegisteredResourceTypeCount')

        if m.get('TemplateCount') is not None:
            self.template_count = m.get('TemplateCount')

        return self


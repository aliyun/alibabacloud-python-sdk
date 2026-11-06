# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarClawSkillTemplatesRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        application_type: str = None,
        end_time: str = None,
        page_number: int = None,
        page_size: int = None,
        region_id: str = None,
        skill_template_id: str = None,
        start_time: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The application type.
        # 
        # > If this is your first time calling this operation, you do not need to specify this parameter.
        self.application_type = application_type
        # The end time of the query in UTC.
        self.end_time = end_time
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to view all available regions for the current account, including region IDs.
        self.region_id = region_id
        # The skill template ID.
        self.skill_template_id = skill_template_id
        # The start time of the query in UTC.
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.application_type is not None:
            result['ApplicationType'] = self.application_type

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.skill_template_id is not None:
            result['SkillTemplateId'] = self.skill_template_id

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('ApplicationType') is not None:
            self.application_type = m.get('ApplicationType')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SkillTemplateId') is not None:
            self.skill_template_id = m.get('SkillTemplateId')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self


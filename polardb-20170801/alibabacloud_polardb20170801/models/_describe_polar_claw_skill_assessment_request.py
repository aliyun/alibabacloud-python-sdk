# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribePolarClawSkillAssessmentRequest(DaraModel):
    def __init__(
        self,
        application_id: str = None,
        region_id: str = None,
        skill_name: str = None,
        skill_version: str = None,
        source: str = None,
    ):
        # The application ID.
        self.application_id = application_id
        # The region ID.
        # 
        # > You can call the [DescribeRegions](https://help.aliyun.com/document_detail/98041.html) operation to query all available regions for the current account, including region IDs.
        self.region_id = region_id
        # The name of the skill. This parameter is required. If it is not provided, the API returns an InvalidParameter.SkillName error (HTTP 400).
        self.skill_name = skill_name
        # The version of the skill. This parameter is required. If it is not provided, the API returns an InvalidParameter.SkillVersion error (HTTP 400).
        self.skill_version = skill_version
        # The source of the skill. Valid values: PUBLIC, SELF, and OTHER. This parameter is required. If it is not provided, the API returns an InvalidParameter.Source error (HTTP 400).
        self.source = source

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_id is not None:
            result['ApplicationId'] = self.application_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.skill_version is not None:
            result['SkillVersion'] = self.skill_version

        if self.source is not None:
            result['Source'] = self.source

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationId') is not None:
            self.application_id = m.get('ApplicationId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SkillVersion') is not None:
            self.skill_version = m.get('SkillVersion')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        return self


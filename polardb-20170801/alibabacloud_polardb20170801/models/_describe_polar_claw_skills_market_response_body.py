# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribePolarClawSkillsMarketResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        skill_list: List[main_models.DescribePolarClawSkillsMarketResponseBodySkillList] = None,
        total_record_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The skill list.
        self.skill_list = skill_list
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.skill_list:
            for v1 in self.skill_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SkillList'] = []
        if self.skill_list is not None:
            for k1 in self.skill_list:
                result['SkillList'].append(k1.to_map() if k1 else None)

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.skill_list = []
        if m.get('SkillList') is not None:
            for k1 in m.get('SkillList'):
                temp_model = main_models.DescribePolarClawSkillsMarketResponseBodySkillList()
                self.skill_list.append(temp_model.from_map(k1))

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribePolarClawSkillsMarketResponseBodySkillList(DaraModel):
    def __init__(
        self,
        assessment_status: str = None,
        download_count: str = None,
        skill_name: str = None,
        skill_version: str = None,
        summary: str = None,
        tag_list: List[str] = None,
        title: str = None,
    ):
        # The assessment status.
        self.assessment_status = assessment_status
        # The number of downloads.
        self.download_count = download_count
        # The skill name.
        self.skill_name = skill_name
        # The skill version.
        self.skill_version = skill_version
        # The OpenAPI summary.
        self.summary = summary
        # The tag list.
        self.tag_list = tag_list
        # The title.
        self.title = title

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assessment_status is not None:
            result['AssessmentStatus'] = self.assessment_status

        if self.download_count is not None:
            result['DownloadCount'] = self.download_count

        if self.skill_name is not None:
            result['SkillName'] = self.skill_name

        if self.skill_version is not None:
            result['SkillVersion'] = self.skill_version

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        if self.title is not None:
            result['Title'] = self.title

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssessmentStatus') is not None:
            self.assessment_status = m.get('AssessmentStatus')

        if m.get('DownloadCount') is not None:
            self.download_count = m.get('DownloadCount')

        if m.get('SkillName') is not None:
            self.skill_name = m.get('SkillName')

        if m.get('SkillVersion') is not None:
            self.skill_version = m.get('SkillVersion')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        return self


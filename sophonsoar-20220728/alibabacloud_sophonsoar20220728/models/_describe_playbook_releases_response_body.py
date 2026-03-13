# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribePlaybookReleasesResponseBody(DaraModel):
    def __init__(
        self,
        page: main_models.DescribePlaybookReleasesResponseBodyPage = None,
        records: List[main_models.DescribePlaybookReleasesResponseBodyRecords] = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.page = page
        # The information about the playbook version.
        self.records = records
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.page:
            self.page.validate()
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page is not None:
            result['Page'] = self.page.to_map()

        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Page') is not None:
            temp_model = main_models.DescribePlaybookReleasesResponseBodyPage()
            self.page = temp_model.from_map(m.get('Page'))

        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.DescribePlaybookReleasesResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribePlaybookReleasesResponseBodyRecords(DaraModel):
    def __init__(
        self,
        creator: str = None,
        description: str = None,
        gmt_create: int = None,
        gmt_modified: int = None,
        id: int = None,
        taskflow_md_5: str = None,
    ):
        # The ID of the Alibaba Cloud account that is used to publish the version.
        self.creator = creator
        # The description of the layer version.
        self.description = description
        # The time when the version was created. The value is a 13-digit timestamp.
        self.gmt_create = gmt_create
        # The time when the version was modified. The value is a 13-digit timestamp.
        self.gmt_modified = gmt_modified
        # The record ID.
        self.id = id
        # The MD5 value configured for the published version of the playbook.
        self.taskflow_md_5 = taskflow_md_5

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')

        return self

class DescribePlaybookReleasesResponseBodyPage(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self


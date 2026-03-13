# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sophonsoar20220728 import models as main_models
from darabonba.model import DaraModel

class DescribeDistinctReleasesResponseBody(DaraModel):
    def __init__(
        self,
        records: List[main_models.DescribeDistinctReleasesResponseBodyRecords] = None,
        request_id: str = None,
    ):
        # The information about versions.
        self.records = records
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['Records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('Records') is not None:
            for k1 in m.get('Records'):
                temp_model = main_models.DescribeDistinctReleasesResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeDistinctReleasesResponseBodyRecords(DaraModel):
    def __init__(
        self,
        description: str = None,
        taskflow_md_5: str = None,
        taskflow_type: str = None,
    ):
        # The version description.
        self.description = description
        # The MD5 value of the version XML configuration.
        self.taskflow_md_5 = taskflow_md_5
        # The format of the playbook. Valid values:
        # 
        # *   **xml**: XML format.
        # *   **x6**: JSON format.
        self.taskflow_type = taskflow_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.taskflow_md_5 is not None:
            result['TaskflowMd5'] = self.taskflow_md_5

        if self.taskflow_type is not None:
            result['TaskflowType'] = self.taskflow_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('TaskflowMd5') is not None:
            self.taskflow_md_5 = m.get('TaskflowMd5')

        if m.get('TaskflowType') is not None:
            self.taskflow_type = m.get('TaskflowType')

        return self


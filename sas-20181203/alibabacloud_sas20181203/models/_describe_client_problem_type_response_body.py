# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeClientProblemTypeResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        problem_types: List[main_models.DescribeClientProblemTypeResponseBodyProblemTypes] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
        self.current_page = current_page
        # The number of entries per page. Default value: **20**.
        self.page_size = page_size
        # The issue types.
        self.problem_types = problem_types
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.problem_types:
            for v1 in self.problem_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ProblemTypes'] = []
        if self.problem_types is not None:
            for k1 in self.problem_types:
                result['ProblemTypes'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.problem_types = []
        if m.get('ProblemTypes') is not None:
            for k1 in m.get('ProblemTypes'):
                temp_model = main_models.DescribeClientProblemTypeResponseBodyProblemTypes()
                self.problem_types.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeClientProblemTypeResponseBodyProblemTypes(DaraModel):
    def __init__(
        self,
        problem_detail: str = None,
        problem_id: str = None,
        problem_type: str = None,
    ):
        # The description of the issue type.
        self.problem_detail = problem_detail
        # The ID of the issue type.
        self.problem_id = problem_id
        # The name of the issue type.
        self.problem_type = problem_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.problem_detail is not None:
            result['problemDetail'] = self.problem_detail

        if self.problem_id is not None:
            result['problemId'] = self.problem_id

        if self.problem_type is not None:
            result['problemType'] = self.problem_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('problemDetail') is not None:
            self.problem_detail = m.get('problemDetail')

        if m.get('problemId') is not None:
            self.problem_id = m.get('problemId')

        if m.get('problemType') is not None:
            self.problem_type = m.get('problemType')

        return self


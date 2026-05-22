# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenestsupplier20210521 import models as main_models
from darabonba.model import DaraModel

class ListServiceTestCasesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListServiceTestCasesResponseBodyData] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The data returned.
        self.data = data
        # The number of entries per page. Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of NextToken.
        self.next_token = next_token
        # Request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListServiceTestCasesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListServiceTestCasesResponseBodyData(DaraModel):
    def __init__(
        self,
        template_name: str = None,
        test_case_id: str = None,
        test_case_name: str = None,
        test_config: str = None,
    ):
        # The template name.
        self.template_name = template_name
        # The service test case id.
        self.test_case_id = test_case_id
        # The service test case name.
        self.test_case_name = test_case_name
        # The service test config.
        self.test_config = test_config

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.test_case_id is not None:
            result['TestCaseId'] = self.test_case_id

        if self.test_case_name is not None:
            result['TestCaseName'] = self.test_case_name

        if self.test_config is not None:
            result['TestConfig'] = self.test_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TestCaseId') is not None:
            self.test_case_id = m.get('TestCaseId')

        if m.get('TestCaseName') is not None:
            self.test_case_name = m.get('TestCaseName')

        if m.get('TestConfig') is not None:
            self.test_config = m.get('TestConfig')

        return self


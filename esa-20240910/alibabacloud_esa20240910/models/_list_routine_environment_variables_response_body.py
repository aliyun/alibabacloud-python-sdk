# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class ListRoutineEnvironmentVariablesResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        environment_variables: Dict[str, main_models.EnvironmentVariablesValue] = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of environment variables.
        self.count = count
        # The environment variable dictionary.
        self.environment_variables = environment_variables
        # The page number.
        self.page_number = page_number
        # The page size.
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        # The total number of environment variables.
        self.total_count = total_count

    def validate(self):
        if self.environment_variables:
            for v1 in self.environment_variables.values():
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        result['EnvironmentVariables'] = {}
        if self.environment_variables is not None:
            for k1, v1 in self.environment_variables.items():
                result['EnvironmentVariables'][k1] = v1.to_map() if v1 else None

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.environment_variables = {}
        if m.get('EnvironmentVariables') is not None:
            for k1, v1 in m.get('EnvironmentVariables').items():
                temp_model = main_models.EnvironmentVariablesValue()
                self.environment_variables[k1] = temp_model.from_map(v1)

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self


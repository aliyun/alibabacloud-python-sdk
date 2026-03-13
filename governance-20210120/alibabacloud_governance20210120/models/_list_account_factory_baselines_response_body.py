# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_governance20210120 import models as main_models
from darabonba.model import DaraModel

class ListAccountFactoryBaselinesResponseBody(DaraModel):
    def __init__(
        self,
        baselines: List[main_models.ListAccountFactoryBaselinesResponseBodyBaselines] = None,
        next_token: str = None,
        request_id: str = None,
    ):
        # The baselines.
        self.baselines = baselines
        # The returned value of NextToken is a pagination token, which can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.baselines:
            for v1 in self.baselines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Baselines'] = []
        if self.baselines is not None:
            for k1 in self.baselines:
                result['Baselines'].append(k1.to_map() if k1 else None)

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.baselines = []
        if m.get('Baselines') is not None:
            for k1 in m.get('Baselines'):
                temp_model = main_models.ListAccountFactoryBaselinesResponseBodyBaselines()
                self.baselines.append(temp_model.from_map(k1))

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListAccountFactoryBaselinesResponseBodyBaselines(DaraModel):
    def __init__(
        self,
        baseline_id: str = None,
        baseline_name: str = None,
        create_time: str = None,
        description: str = None,
        type: str = None,
        update_time: str = None,
    ):
        # The baseline ID.
        self.baseline_id = baseline_id
        # The name of the baseline.
        self.baseline_name = baseline_name
        # The time at which the baseline was created.
        self.create_time = create_time
        # The description of the baseline.
        self.description = description
        # The type of the baseline. Valid values:
        # 
        # *   System: default baseline.
        # *   Custom: custom baseline.
        self.type = type
        # The time when the baseline was updated.
        self.update_time = update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.baseline_id is not None:
            result['BaselineId'] = self.baseline_id

        if self.baseline_name is not None:
            result['BaselineName'] = self.baseline_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BaselineId') is not None:
            self.baseline_id = m.get('BaselineId')

        if m.get('BaselineName') is not None:
            self.baseline_name = m.get('BaselineName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self


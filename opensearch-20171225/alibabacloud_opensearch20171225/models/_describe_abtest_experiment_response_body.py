# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class DescribeABTestExperimentResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeABTestExperimentResponseBodyResult = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The details of the test.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.DescribeABTestExperimentResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class DescribeABTestExperimentResponseBodyResult(DaraModel):
    def __init__(
        self,
        created: int = None,
        id: str = None,
        name: str = None,
        online: bool = None,
        params: main_models.DescribeABTestExperimentResponseBodyResultParams = None,
        traffic: int = None,
        updated: int = None,
    ):
        # The time when the test was created.
        self.created = created
        # The ID of the test.
        self.id = id
        # The name of the test.
        self.name = name
        # The status of the test. Valid values:
        # 
        # *   true: in effect
        # *   false: not in effect
        self.online = online
        # The parameters of the test.
        self.params = params
        # The percentage of traffic that is routed to the test.
        self.traffic = traffic
        # The time when the test was last modified.
        self.updated = updated

    def validate(self):
        if self.params:
            self.params.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created is not None:
            result['created'] = self.created

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.online is not None:
            result['online'] = self.online

        if self.params is not None:
            result['params'] = self.params.to_map()

        if self.traffic is not None:
            result['traffic'] = self.traffic

        if self.updated is not None:
            result['updated'] = self.updated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('created') is not None:
            self.created = m.get('created')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('online') is not None:
            self.online = m.get('online')

        if m.get('params') is not None:
            temp_model = main_models.DescribeABTestExperimentResponseBodyResultParams()
            self.params = temp_model.from_map(m.get('params'))

        if m.get('traffic') is not None:
            self.traffic = m.get('traffic')

        if m.get('updated') is not None:
            self.updated = m.get('updated')

        return self

class DescribeABTestExperimentResponseBodyResultParams(DaraModel):
    def __init__(
        self,
        first_formula_name: str = None,
    ):
        # The name of the rough sort policy.
        self.first_formula_name = first_formula_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_formula_name is not None:
            result['first_formula_name'] = self.first_formula_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('first_formula_name') is not None:
            self.first_formula_name = m.get('first_formula_name')

        return self


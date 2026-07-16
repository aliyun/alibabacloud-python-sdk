# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_emr20210320 import models as main_models
from darabonba.model import DaraModel

class ListComponentsResponseBody(DaraModel):
    def __init__(
        self,
        components: List[main_models.ListComponentsResponseBodyComponents] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of component information.
        self.components = components
        # The maximum number of entries returned.
        self.max_results = max_results
        # A pagination token. It can be used in the next request to retrieve a new page of results.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.components:
            for v1 in self.components:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Components'] = []
        if self.components is not None:
            for k1 in self.components:
                result['Components'].append(k1.to_map() if k1 else None)

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
        self.components = []
        if m.get('Components') is not None:
            for k1 in m.get('Components'):
                temp_model = main_models.ListComponentsResponseBodyComponents()
                self.components.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListComponentsResponseBodyComponents(DaraModel):
    def __init__(
        self,
        application_name: str = None,
        attributes: List[main_models.Attribute] = None,
        component_name: str = None,
        namespace: str = None,
        replica: int = None,
    ):
        # The application name.
        self.application_name = application_name
        # The list of attributes.
        self.attributes = attributes
        # The component name.
        self.component_name = component_name
        # The reserved field.
        self.namespace = namespace
        # The total number of instances on which the component is installed.
        self.replica = replica

    def validate(self):
        if self.attributes:
            for v1 in self.attributes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.application_name is not None:
            result['ApplicationName'] = self.application_name

        result['Attributes'] = []
        if self.attributes is not None:
            for k1 in self.attributes:
                result['Attributes'].append(k1.to_map() if k1 else None)

        if self.component_name is not None:
            result['ComponentName'] = self.component_name

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.replica is not None:
            result['Replica'] = self.replica

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApplicationName') is not None:
            self.application_name = m.get('ApplicationName')

        self.attributes = []
        if m.get('Attributes') is not None:
            for k1 in m.get('Attributes'):
                temp_model = main_models.Attribute()
                self.attributes.append(temp_model.from_map(k1))

        if m.get('ComponentName') is not None:
            self.component_name = m.get('ComponentName')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('Replica') is not None:
            self.replica = m.get('Replica')

        return self


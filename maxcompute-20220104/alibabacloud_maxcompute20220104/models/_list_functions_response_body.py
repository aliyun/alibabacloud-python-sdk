# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListFunctionsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListFunctionsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListFunctionsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListFunctionsResponseBodyData(DaraModel):
    def __init__(
        self,
        functions: List[main_models.ListFunctionsResponseBodyDataFunctions] = None,
        marker: str = None,
        max_item: int = None,
    ):
        # The information about each function.
        self.functions = functions
        # Indicates the marker after which the returned list begins.
        self.marker = marker
        # The maximum number of entries returned per page.
        self.max_item = max_item

    def validate(self):
        if self.functions:
            for v1 in self.functions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['functions'] = []
        if self.functions is not None:
            for k1 in self.functions:
                result['functions'].append(k1.to_map() if k1 else None)

        if self.marker is not None:
            result['marker'] = self.marker

        if self.max_item is not None:
            result['maxItem'] = self.max_item

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.functions = []
        if m.get('functions') is not None:
            for k1 in m.get('functions'):
                temp_model = main_models.ListFunctionsResponseBodyDataFunctions()
                self.functions.append(temp_model.from_map(k1))

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')

        return self

class ListFunctionsResponseBodyDataFunctions(DaraModel):
    def __init__(
        self,
        class_: str = None,
        creation_time: int = None,
        display_name: str = None,
        name: str = None,
        owner: str = None,
        resources: str = None,
        schema: str = None,
    ):
        # The class in which the function was defined.
        self.class_ = class_
        # The time when the function was created. Unit: milliseconds.
        self.creation_time = creation_time
        # The display name of the function.
        self.display_name = display_name
        # The name of the function.
        self.name = name
        # The owner of the function.
        self.owner = owner
        # The name of the resource that was associated with the function.
        self.resources = resources
        # The schema of the function.
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_ is not None:
            result['class'] = self.class_

        if self.creation_time is not None:
            result['creationTime'] = self.creation_time

        if self.display_name is not None:
            result['displayName'] = self.display_name

        if self.name is not None:
            result['name'] = self.name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.resources is not None:
            result['resources'] = self.resources

        if self.schema is not None:
            result['schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('class') is not None:
            self.class_ = m.get('class')

        if m.get('creationTime') is not None:
            self.creation_time = m.get('creationTime')

        if m.get('displayName') is not None:
            self.display_name = m.get('displayName')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('resources') is not None:
            self.resources = m.get('resources')

        if m.get('schema') is not None:
            self.schema = m.get('schema')

        return self


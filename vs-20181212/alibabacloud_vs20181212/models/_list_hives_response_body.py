# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_vs20181212 import models as main_models
from darabonba.model import DaraModel

class ListHivesResponseBody(DaraModel):
    def __init__(
        self,
        hives: List[main_models.ListHivesResponseBodyHives] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.hives = hives
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.hives:
            for v1 in self.hives:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Hives'] = []
        if self.hives is not None:
            for k1 in self.hives:
                result['Hives'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hives = []
        if m.get('Hives') is not None:
            for k1 in m.get('Hives'):
                temp_model = main_models.ListHivesResponseBodyHives()
                self.hives.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListHivesResponseBodyHives(DaraModel):
    def __init__(
        self,
        creation_time: str = None,
        description: str = None,
        hive_id: str = None,
        name: str = None,
    ):
        self.creation_time = creation_time
        self.description = description
        self.hive_id = hive_id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.description is not None:
            result['Description'] = self.description

        if self.hive_id is not None:
            result['HiveId'] = self.hive_id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('HiveId') is not None:
            self.hive_id = m.get('HiveId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self


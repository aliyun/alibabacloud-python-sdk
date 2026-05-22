# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class GetRoutineUserInfoResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        routines: List[main_models.GetRoutineUserInfoResponseBodyRoutines] = None,
        subdomains: List[str] = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The routines.
        self.routines = routines
        # The subdomains.
        self.subdomains = subdomains

    def validate(self):
        if self.routines:
            for v1 in self.routines:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Routines'] = []
        if self.routines is not None:
            for k1 in self.routines:
                result['Routines'].append(k1.to_map() if k1 else None)

        if self.subdomains is not None:
            result['Subdomains'] = self.subdomains

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.routines = []
        if m.get('Routines') is not None:
            for k1 in m.get('Routines'):
                temp_model = main_models.GetRoutineUserInfoResponseBodyRoutines()
                self.routines.append(temp_model.from_map(k1))

        if m.get('Subdomains') is not None:
            self.subdomains = m.get('Subdomains')

        return self

class GetRoutineUserInfoResponseBodyRoutines(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        routine_name: str = None,
    ):
        # The time when the routine was created.
        self.create_time = create_time
        # The routine description, which is Base64-encoded.
        self.description = description
        # The routine name.
        self.routine_name = routine_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.routine_name is not None:
            result['RoutineName'] = self.routine_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('RoutineName') is not None:
            self.routine_name = m.get('RoutineName')

        return self


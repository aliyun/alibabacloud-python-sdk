# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListProgramTypeCountResponseBody(DaraModel):
    def __init__(
        self,
        program_type_and_counts: List[main_models.ListProgramTypeCountResponseBodyProgramTypeAndCounts] = None,
        request_id: str = None,
    ):
        # The list of node types and quantity.
        self.program_type_and_counts = program_type_and_counts
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.program_type_and_counts:
            for v1 in self.program_type_and_counts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProgramTypeAndCounts'] = []
        if self.program_type_and_counts is not None:
            for k1 in self.program_type_and_counts:
                result['ProgramTypeAndCounts'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.program_type_and_counts = []
        if m.get('ProgramTypeAndCounts') is not None:
            for k1 in m.get('ProgramTypeAndCounts'):
                temp_model = main_models.ListProgramTypeCountResponseBodyProgramTypeAndCounts()
                self.program_type_and_counts.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListProgramTypeCountResponseBodyProgramTypeAndCounts(DaraModel):
    def __init__(
        self,
        count: int = None,
        program_type: str = None,
    ):
        # The number of nodes.
        self.count = count
        # The node type.
        self.program_type = program_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.program_type is not None:
            result['ProgramType'] = self.program_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('ProgramType') is not None:
            self.program_type = m.get('ProgramType')

        return self


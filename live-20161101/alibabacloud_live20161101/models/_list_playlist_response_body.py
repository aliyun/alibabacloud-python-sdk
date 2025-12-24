# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_live20161101 import models as main_models
from darabonba.model import DaraModel

class ListPlaylistResponseBody(DaraModel):
    def __init__(
        self,
        program_list: List[main_models.ListPlaylistResponseBodyProgramList] = None,
        request_id: str = None,
        total: int = None,
    ):
        # The episode lists.
        self.program_list = program_list
        # The request ID.
        self.request_id = request_id
        # The total number of episode lists returned.
        self.total = total

    def validate(self):
        if self.program_list:
            for v1 in self.program_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ProgramList'] = []
        if self.program_list is not None:
            for k1 in self.program_list:
                result['ProgramList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.program_list = []
        if m.get('ProgramList') is not None:
            for k1 in m.get('ProgramList'):
                temp_model = main_models.ListPlaylistResponseBodyProgramList()
                self.program_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class ListPlaylistResponseBodyProgramList(DaraModel):
    def __init__(
        self,
        caster_id: str = None,
        domain_name: str = None,
        program_id: str = None,
        program_name: str = None,
        repeat_number: int = None,
        status: int = None,
    ):
        # The ID of the production studio to which the episode list belongs. You can use the ID as a request parameter in the API operation that is used to add a layout to the virtual studio, delete a layout in the virtual studio, modify a layout of the virtual studio, or query layouts of the virtual studio.
        self.caster_id = caster_id
        # The main streaming domain.
        self.domain_name = domain_name
        # The ID of the episode list.
        self.program_id = program_id
        # The name of the episode list.
        self.program_name = program_name
        # The number of playbacks after the first playback is complete. Valid values:
        # 
        # *   **0** (default): specifies that the episode list is played only once.
        # *   **-1**: specifies that the episode list is played in loop mode.
        # *   Positive integer: specifies the number of times the episode list repeats after the first playback is complete.
        self.repeat_number = repeat_number
        # The status of the episode list. Valid values:
        # 
        # *   **0**: stopped
        # *   **1**: running
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caster_id is not None:
            result['CasterId'] = self.caster_id

        if self.domain_name is not None:
            result['DomainName'] = self.domain_name

        if self.program_id is not None:
            result['ProgramId'] = self.program_id

        if self.program_name is not None:
            result['ProgramName'] = self.program_name

        if self.repeat_number is not None:
            result['RepeatNumber'] = self.repeat_number

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CasterId') is not None:
            self.caster_id = m.get('CasterId')

        if m.get('DomainName') is not None:
            self.domain_name = m.get('DomainName')

        if m.get('ProgramId') is not None:
            self.program_id = m.get('ProgramId')

        if m.get('ProgramName') is not None:
            self.program_name = m.get('ProgramName')

        if m.get('RepeatNumber') is not None:
            self.repeat_number = m.get('RepeatNumber')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


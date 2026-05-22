# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRoutineCodeVersionResponseBody(DaraModel):
    def __init__(
        self,
        code_description: str = None,
        create_time: str = None,
        request_id: str = None,
        routine_code: str = None,
    ):
        # The description of the code version.
        self.code_description = code_description
        # The time when the version was created.
        self.create_time = create_time
        # The request ID.
        self.request_id = request_id
        # The code content.
        self.routine_code = routine_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_description is not None:
            result['CodeDescription'] = self.code_description

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.routine_code is not None:
            result['RoutineCode'] = self.routine_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('RoutineCode') is not None:
            self.routine_code = m.get('RoutineCode')

        return self


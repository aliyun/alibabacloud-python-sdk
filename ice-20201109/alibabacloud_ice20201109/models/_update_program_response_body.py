# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ice20201109 import models as main_models
from darabonba.model import DaraModel

class UpdateProgramResponseBody(DaraModel):
    def __init__(
        self,
        program: main_models.ChannelAssemblyProgram = None,
        request_id: str = None,
    ):
        # The information about the program.
        self.program = program
        # **Request ID**
        self.request_id = request_id

    def validate(self):
        if self.program:
            self.program.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.program is not None:
            result['Program'] = self.program.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Program') is not None:
            temp_model = main_models.ChannelAssemblyProgram()
            self.program = temp_model.from_map(m.get('Program'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


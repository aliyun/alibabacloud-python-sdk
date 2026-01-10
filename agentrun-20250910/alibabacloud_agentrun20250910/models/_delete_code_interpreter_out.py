# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DeleteCodeInterpreterOut(DaraModel):
    def __init__(
        self,
        code_interpreter_id: str = None,
        code_interpreter_name: str = None,
        status: str = None,
    ):
        self.code_interpreter_id = code_interpreter_id
        self.code_interpreter_name = code_interpreter_name
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code_interpreter_id is not None:
            result['codeInterpreterId'] = self.code_interpreter_id

        if self.code_interpreter_name is not None:
            result['codeInterpreterName'] = self.code_interpreter_name

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('codeInterpreterId') is not None:
            self.code_interpreter_id = m.get('codeInterpreterId')

        if m.get('codeInterpreterName') is not None:
            self.code_interpreter_name = m.get('codeInterpreterName')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self


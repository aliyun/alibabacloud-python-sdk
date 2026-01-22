# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeJobResultsResponseBody(DaraModel):
    def __init__(
        self,
        exit_code: int = None,
        output: str = None,
        request_id: str = None,
    ):
        self.exit_code = exit_code
        self.output = output
        # Id of the request
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exit_code is not None:
            result['ExitCode'] = self.exit_code

        if self.output is not None:
            result['Output'] = self.output

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExitCode') is not None:
            self.exit_code = m.get('ExitCode')

        if m.get('Output') is not None:
            self.output = m.get('Output')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


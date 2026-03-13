# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSoarRecordInOutputResponseBody(DaraModel):
    def __init__(
        self,
        in_output_info: str = None,
        request_id: str = None,
    ):
        # The execution result of the component action.
        self.in_output_info = in_output_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.in_output_info is not None:
            result['InOutputInfo'] = self.in_output_info

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InOutputInfo') is not None:
            self.in_output_info = m.get('InOutputInfo')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


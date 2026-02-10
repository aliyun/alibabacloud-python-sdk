# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSoarStrategyParamResponseBody(DaraModel):
    def __init__(
        self,
        params: str = None,
        process_info: str = None,
        request_id: str = None,
    ):
        # The parameters of the policy.
        self.params = params
        # The process information of the policy.
        self.process_info = process_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.params is not None:
            result['Params'] = self.params

        if self.process_info is not None:
            result['ProcessInfo'] = self.process_info

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Params') is not None:
            self.params = m.get('Params')

        if m.get('ProcessInfo') is not None:
            self.process_info = m.get('ProcessInfo')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetOptionValueForProjectResponseBody(DaraModel):
    def __init__(
        self,
        option_value: str = None,
        request_id: str = None,
    ):
        # The data returned In the example, cuNumber is a custom key.
        self.option_value = option_value
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.option_value is not None:
            result['OptionValue'] = self.option_value

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OptionValue') is not None:
            self.option_value = m.get('OptionValue')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


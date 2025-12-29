# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateWhitelistSettingResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result_object: bool = None,
    ):
        # The ID of this request.
        self.request_id = request_id
        # Return result, whether the creation was successful:
        # - true: Success
        # - false: Failure
        self.result_object = result_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_object is not None:
            result['ResultObject'] = self.result_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultObject') is not None:
            self.result_object = m.get('ResultObject')

        return self


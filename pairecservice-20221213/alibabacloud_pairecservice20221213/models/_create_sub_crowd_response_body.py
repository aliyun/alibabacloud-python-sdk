# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSubCrowdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        sub_crowd_id: str = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.sub_crowd_id = sub_crowd_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sub_crowd_id is not None:
            result['SubCrowdId'] = self.sub_crowd_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SubCrowdId') is not None:
            self.sub_crowd_id = m.get('SubCrowdId')

        return self


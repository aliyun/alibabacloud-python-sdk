# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConvertBandwidthPackageResponseBody(DaraModel):
    def __init__(
        self,
        convert_instance_id: str = None,
        request_id: str = None,
    ):
        # The ID of the Internet Shared Bandwidth instance.
        self.convert_instance_id = convert_instance_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.convert_instance_id is not None:
            result['ConvertInstanceId'] = self.convert_instance_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ConvertInstanceId') is not None:
            self.convert_instance_id = m.get('ConvertInstanceId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateContactGroupForAlertResponseBody(DaraModel):
    def __init__(
        self,
        msg: str = None,
        status: bool = None,
    ):
        # The message returned when the operation failed.
        self.msg = msg
        # The status of the update result. Valid values:
        # - true: The operation is successful.
        # - false: The operation failed.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.msg is not None:
            result['msg'] = self.msg

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('msg') is not None:
            self.msg = m.get('msg')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self


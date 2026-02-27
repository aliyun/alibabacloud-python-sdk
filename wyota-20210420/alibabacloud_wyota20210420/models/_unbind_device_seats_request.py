# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UnbindDeviceSeatsRequest(DaraModel):
    def __init__(
        self,
        serial_no_list: List[str] = None,
    ):
        self.serial_no_list = serial_no_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.serial_no_list is not None:
            result['SerialNoList'] = self.serial_no_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SerialNoList') is not None:
            self.serial_no_list = m.get('SerialNoList')

        return self


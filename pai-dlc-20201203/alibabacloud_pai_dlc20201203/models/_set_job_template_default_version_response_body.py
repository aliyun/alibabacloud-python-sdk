# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SetJobTemplateDefaultVersionResponseBody(DaraModel):
    def __init__(
        self,
        default_version: int = None,
        gmt_modify_time: str = None,
        request_id: str = None,
    ):
        # The current default version number.
        self.default_version = default_version
        # The time the template was last modified.
        # 
        # Use the UTC time format: yyyy-MM-ddTHH:mmZ
        self.gmt_modify_time = gmt_modify_time
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version

        if self.gmt_modify_time is not None:
            result['GmtModifyTime'] = self.gmt_modify_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')

        if m.get('GmtModifyTime') is not None:
            self.gmt_modify_time = m.get('GmtModifyTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


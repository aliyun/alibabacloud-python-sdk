# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class SuspendJobRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        suspend: bool = None,
    ):
        # The ID of the job template.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Start or suspend a job template.
        # 
        # *   true: Start a job template.
        # *   false: Suspend a job template.
        # 
        # This parameter is required.
        self.suspend = suspend

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.suspend is not None:
            result['Suspend'] = self.suspend

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('Suspend') is not None:
            self.suspend = m.get('Suspend')

        return self


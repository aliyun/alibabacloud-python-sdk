# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeApplicationMseServiceRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        enable_ahas: bool = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # Specifies whether to enable traffic limiting and degradation. Set to true to check traffic limiting and degradation permissions when accessing related APIs; set to false otherwise.
        # 
        # This parameter is required.
        self.enable_ahas = enable_ahas

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.enable_ahas is not None:
            result['EnableAhas'] = self.enable_ahas

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('EnableAhas') is not None:
            self.enable_ahas = m.get('EnableAhas')

        return self


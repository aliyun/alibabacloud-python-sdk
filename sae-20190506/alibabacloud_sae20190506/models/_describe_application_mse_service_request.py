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
        # Specifies whether the throttling and degradation feature is enabled. Set this parameter to true when you call API operations related to throttling and degradation. Otherwise, set this parameter to false. Valid values:
        # - true: Checks the permissions for throttling and degradation.
        # - false: Does not check the permissions for throttling and degradation.
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


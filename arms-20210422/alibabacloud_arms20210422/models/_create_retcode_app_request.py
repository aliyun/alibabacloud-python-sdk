# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateRetcodeAppRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        retcode_app_name: str = None,
        retcode_app_type: str = None,
    ):
        # This parameter is required.
        self.region_id = region_id
        # This parameter is required.
        self.retcode_app_name = retcode_app_name
        # This parameter is required.
        self.retcode_app_type = retcode_app_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.retcode_app_name is not None:
            result['RetcodeAppName'] = self.retcode_app_name

        if self.retcode_app_type is not None:
            result['RetcodeAppType'] = self.retcode_app_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RetcodeAppName') is not None:
            self.retcode_app_name = m.get('RetcodeAppName')

        if m.get('RetcodeAppType') is not None:
            self.retcode_app_type = m.get('RetcodeAppType')

        return self


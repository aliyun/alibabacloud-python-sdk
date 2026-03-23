# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetGroupMiscAggTimeSerRequest(DaraModel):
    def __init__(
        self,
        apgroup_uuid: str = None,
        app_code: str = None,
        app_name: str = None,
        end: int = None,
        start: int = None,
    ):
        # This parameter is required.
        self.apgroup_uuid = apgroup_uuid
        # This parameter is required.
        self.app_code = app_code
        # This parameter is required.
        self.app_name = app_name
        # This parameter is required.
        self.end = end
        # This parameter is required.
        self.start = start

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apgroup_uuid is not None:
            result['ApgroupUuid'] = self.apgroup_uuid

        if self.app_code is not None:
            result['AppCode'] = self.app_code

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.end is not None:
            result['End'] = self.end

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApgroupUuid') is not None:
            self.apgroup_uuid = m.get('ApgroupUuid')

        if m.get('AppCode') is not None:
            self.app_code = m.get('AppCode')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('End') is not None:
            self.end = m.get('End')

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self


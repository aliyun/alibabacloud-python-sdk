# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeEdgeContainerAppStatsRequest(DaraModel):
    def __init__(
        self,
        app: str = None,
        end_time: str = None,
        fields: str = None,
        isp: str = None,
        locate: str = None,
        start_time: str = None,
        tenant: str = None,
    ):
        # This parameter is required.
        self.app = app
        self.end_time = end_time
        # This parameter is required.
        self.fields = fields
        self.isp = isp
        self.locate = locate
        self.start_time = start_time
        # The tenant ID.
        self.tenant = tenant

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app is not None:
            result['App'] = self.app

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.fields is not None:
            result['Fields'] = self.fields

        if self.isp is not None:
            result['Isp'] = self.isp

        if self.locate is not None:
            result['Locate'] = self.locate

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.tenant is not None:
            result['Tenant'] = self.tenant

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('App') is not None:
            self.app = m.get('App')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Fields') is not None:
            self.fields = m.get('Fields')

        if m.get('Isp') is not None:
            self.isp = m.get('Isp')

        if m.get('Locate') is not None:
            self.locate = m.get('Locate')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('Tenant') is not None:
            self.tenant = m.get('Tenant')

        return self


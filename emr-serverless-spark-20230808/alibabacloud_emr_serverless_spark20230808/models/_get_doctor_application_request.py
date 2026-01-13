# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetDoctorApplicationRequest(DaraModel):
    def __init__(
        self,
        locale: str = None,
        query_time: str = None,
        region_id: str = None,
    ):
        # The language of diagnostic information.
        self.locale = locale
        # The query time.
        self.query_time = query_time
        # The region ID.
        self.region_id = region_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.locale is not None:
            result['locale'] = self.locale

        if self.query_time is not None:
            result['queryTime'] = self.query_time

        if self.region_id is not None:
            result['regionId'] = self.region_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('locale') is not None:
            self.locale = m.get('locale')

        if m.get('queryTime') is not None:
            self.query_time = m.get('queryTime')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        return self


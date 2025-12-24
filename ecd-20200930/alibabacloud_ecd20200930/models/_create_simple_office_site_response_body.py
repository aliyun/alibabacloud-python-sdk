# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateSimpleOfficeSiteResponseBody(DaraModel):
    def __init__(
        self,
        office_site_id: str = None,
        request_id: str = None,
    ):
        # The office network ID.
        self.office_site_id = office_site_id
        # The request ID.
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


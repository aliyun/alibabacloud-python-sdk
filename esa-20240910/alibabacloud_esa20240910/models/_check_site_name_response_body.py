# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CheckSiteNameResponseBody(DaraModel):
    def __init__(
        self,
        description: str = None,
        is_sub_site: bool = None,
        messeage: str = None,
        passed: bool = None,
        request_id: str = None,
    ):
        self.description = description
        self.is_sub_site = is_sub_site
        self.messeage = messeage
        self.passed = passed
        self.request_id = request_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.is_sub_site is not None:
            result['IsSubSite'] = self.is_sub_site

        if self.messeage is not None:
            result['Messeage'] = self.messeage

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('IsSubSite') is not None:
            self.is_sub_site = m.get('IsSubSite')

        if m.get('Messeage') is not None:
            self.messeage = m.get('Messeage')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self


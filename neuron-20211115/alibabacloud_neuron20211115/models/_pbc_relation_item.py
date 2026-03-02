# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class PbcRelationItem(DaraModel):
    def __init__(
        self,
        company: str = None,
        developer: str = None,
        pbc_name: str = None,
        pbc_version: str = None,
        summary: str = None,
    ):
        self.company = company
        self.developer = developer
        self.pbc_name = pbc_name
        self.pbc_version = pbc_version
        self.summary = summary

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company is not None:
            result['company'] = self.company

        if self.developer is not None:
            result['developer'] = self.developer

        if self.pbc_name is not None:
            result['pbcName'] = self.pbc_name

        if self.pbc_version is not None:
            result['pbcVersion'] = self.pbc_version

        if self.summary is not None:
            result['summary'] = self.summary

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('company') is not None:
            self.company = m.get('company')

        if m.get('developer') is not None:
            self.developer = m.get('developer')

        if m.get('pbcName') is not None:
            self.pbc_name = m.get('pbcName')

        if m.get('pbcVersion') is not None:
            self.pbc_version = m.get('pbcVersion')

        if m.get('summary') is not None:
            self.summary = m.get('summary')

        return self


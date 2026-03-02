# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class Provider(DaraModel):
    def __init__(
        self,
        company: str = None,
        company_id: int = None,
        contact: str = None,
        email: str = None,
        team: str = None,
        team_id: int = None,
    ):
        self.company = company
        self.company_id = company_id
        self.contact = contact
        self.email = email
        self.team = team
        self.team_id = team_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.company is not None:
            result['company'] = self.company

        if self.company_id is not None:
            result['companyId'] = self.company_id

        if self.contact is not None:
            result['contact'] = self.contact

        if self.email is not None:
            result['email'] = self.email

        if self.team is not None:
            result['team'] = self.team

        if self.team_id is not None:
            result['teamId'] = self.team_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('company') is not None:
            self.company = m.get('company')

        if m.get('companyId') is not None:
            self.company_id = m.get('companyId')

        if m.get('contact') is not None:
            self.contact = m.get('contact')

        if m.get('email') is not None:
            self.email = m.get('email')

        if m.get('team') is not None:
            self.team = m.get('team')

        if m.get('teamId') is not None:
            self.team_id = m.get('teamId')

        return self


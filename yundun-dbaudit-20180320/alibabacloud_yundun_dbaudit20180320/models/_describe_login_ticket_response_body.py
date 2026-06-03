# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_yundun_dbaudit20180320 import models as main_models
from darabonba.model import DaraModel

class DescribeLoginTicketResponseBody(DaraModel):
    def __init__(
        self,
        login_ticket: main_models.DescribeLoginTicketResponseBodyLoginTicket = None,
        request_id: str = None,
    ):
        self.login_ticket = login_ticket
        self.request_id = request_id

    def validate(self):
        if self.login_ticket:
            self.login_ticket.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.login_ticket is not None:
            result['LoginTicket'] = self.login_ticket.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LoginTicket') is not None:
            temp_model = main_models.DescribeLoginTicketResponseBodyLoginTicket()
            self.login_ticket = temp_model.from_map(m.get('LoginTicket'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeLoginTicketResponseBodyLoginTicket(DaraModel):
    def __init__(
        self,
        certificate: str = None,
        ticket: str = None,
        zones: List[main_models.DescribeLoginTicketResponseBodyLoginTicketZones] = None,
    ):
        self.certificate = certificate
        self.ticket = ticket
        self.zones = zones

    def validate(self):
        if self.zones:
            for v1 in self.zones:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.certificate is not None:
            result['Certificate'] = self.certificate

        if self.ticket is not None:
            result['Ticket'] = self.ticket

        result['Zones'] = []
        if self.zones is not None:
            for k1 in self.zones:
                result['Zones'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Certificate') is not None:
            self.certificate = m.get('Certificate')

        if m.get('Ticket') is not None:
            self.ticket = m.get('Ticket')

        self.zones = []
        if m.get('Zones') is not None:
            for k1 in m.get('Zones'):
                temp_model = main_models.DescribeLoginTicketResponseBodyLoginTicketZones()
                self.zones.append(temp_model.from_map(k1))

        return self

class DescribeLoginTicketResponseBodyLoginTicketZones(DaraModel):
    def __init__(
        self,
        local_name: str = None,
        zone_id: str = None,
    ):
        self.local_name = local_name
        self.zone_id = zone_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.local_name is not None:
            result['LocalName'] = self.local_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self


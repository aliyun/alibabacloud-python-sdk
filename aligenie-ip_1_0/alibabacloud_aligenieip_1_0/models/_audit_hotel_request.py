# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_aligenieip_1_0 import models as main_models
from darabonba.model import DaraModel

class AuditHotelRequest(DaraModel):
    def __init__(
        self,
        audit_hotel_req: main_models.AuditHotelRequestAuditHotelReq = None,
    ):
        # This parameter is required.
        self.audit_hotel_req = audit_hotel_req

    def validate(self):
        if self.audit_hotel_req:
            self.audit_hotel_req.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_hotel_req is not None:
            result['AuditHotelReq'] = self.audit_hotel_req.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditHotelReq') is not None:
            temp_model = main_models.AuditHotelRequestAuditHotelReq()
            self.audit_hotel_req = temp_model.from_map(m.get('AuditHotelReq'))

        return self

class AuditHotelRequestAuditHotelReq(DaraModel):
    def __init__(
        self,
        audit_opinion: str = None,
        hotel_id: str = None,
        status: int = None,
    ):
        self.audit_opinion = audit_opinion
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audit_opinion is not None:
            result['AuditOpinion'] = self.audit_opinion

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuditOpinion') is not None:
            self.audit_opinion = m.get('AuditOpinion')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


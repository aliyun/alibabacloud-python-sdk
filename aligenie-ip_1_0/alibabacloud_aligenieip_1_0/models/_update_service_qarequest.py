# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateServiceQARequest(DaraModel):
    def __init__(
        self,
        answer: str = None,
        hotel_id: str = None,
        service_qaid: int = None,
        is_active: bool = None,
    ):
        self.answer = answer
        # This parameter is required.
        self.hotel_id = hotel_id
        self.service_qaid = service_qaid
        self.is_active = is_active

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['Answer'] = self.answer

        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.service_qaid is not None:
            result['ServiceQAId'] = self.service_qaid

        if self.is_active is not None:
            result['isActive'] = self.is_active

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Answer') is not None:
            self.answer = m.get('Answer')

        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('ServiceQAId') is not None:
            self.service_qaid = m.get('ServiceQAId')

        if m.get('isActive') is not None:
            self.is_active = m.get('isActive')

        return self


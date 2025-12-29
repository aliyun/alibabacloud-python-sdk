# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ImportHotelConfigShrinkRequest(DaraModel):
    def __init__(
        self,
        hotel_id: str = None,
        import_hotel_config_shrink: str = None,
    ):
        # This parameter is required.
        self.hotel_id = hotel_id
        # This parameter is required.
        self.import_hotel_config_shrink = import_hotel_config_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.hotel_id is not None:
            result['HotelId'] = self.hotel_id

        if self.import_hotel_config_shrink is not None:
            result['ImportHotelConfig'] = self.import_hotel_config_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('HotelId') is not None:
            self.hotel_id = m.get('HotelId')

        if m.get('ImportHotelConfig') is not None:
            self.import_hotel_config_shrink = m.get('ImportHotelConfig')

        return self


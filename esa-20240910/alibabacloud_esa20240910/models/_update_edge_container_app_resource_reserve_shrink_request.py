# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class UpdateEdgeContainerAppResourceReserveShrinkRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        duration_time: str = None,
        enable: bool = None,
        forever: bool = None,
        reserve_set_shrink: str = None,
    ):
        # The application ID. You can call the [ListEdgeContainerApps](~~ListEdgeContainerApps~~) operation to obtain the application ID.
        # >Notice: The AppId format is the app- prefix followed by a numeric suffix, with a total length of 20 to 64 characters (example: app-8806886***83794688). Call ListEdgeContainerApps to obtain an existing AppId, or call CreateEdgeContainerApp to create an application first.</notice>.
        self.app_id = app_id
        # The reservation end time. This parameter uses UTC time. To convert from UTC+8, add 8 hours. For example, if the current time is 2006-01-02 06:04:05 in UTC+8, enter "2006-01-02T14:04:05Z".
        self.duration_time = duration_time
        # Specifies whether to enable resource reservation.
        self.enable = enable
        # Specifies whether to permanently enable reservation. Once enabled, you cannot set a reservation end time.
        self.forever = forever
        # The list of reserved resources.
        self.reserve_set_shrink = reserve_set_shrink

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.duration_time is not None:
            result['DurationTime'] = self.duration_time

        if self.enable is not None:
            result['Enable'] = self.enable

        if self.forever is not None:
            result['Forever'] = self.forever

        if self.reserve_set_shrink is not None:
            result['ReserveSet'] = self.reserve_set_shrink

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('DurationTime') is not None:
            self.duration_time = m.get('DurationTime')

        if m.get('Enable') is not None:
            self.enable = m.get('Enable')

        if m.get('Forever') is not None:
            self.forever = m.get('Forever')

        if m.get('ReserveSet') is not None:
            self.reserve_set_shrink = m.get('ReserveSet')

        return self


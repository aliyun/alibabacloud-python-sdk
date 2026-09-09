# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class AddAgendaSumRecordFlowPopRequest(DaraModel):
    def __init__(
        self,
        active_num: int = None,
        agenda_id: int = None,
        attendance_percent: str = None,
        flow_time: int = None,
        session_name: str = None,
        total_pv: int = None,
        total_uv: int = None,
    ):
        self.active_num = active_num
        # This parameter is required.
        self.agenda_id = agenda_id
        self.attendance_percent = attendance_percent
        # This parameter is required.
        self.flow_time = flow_time
        # This parameter is required.
        self.session_name = session_name
        # This parameter is required.
        self.total_pv = total_pv
        # This parameter is required.
        self.total_uv = total_uv

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.active_num is not None:
            result['ActiveNum'] = self.active_num

        if self.agenda_id is not None:
            result['AgendaId'] = self.agenda_id

        if self.attendance_percent is not None:
            result['AttendancePercent'] = self.attendance_percent

        if self.flow_time is not None:
            result['FlowTime'] = self.flow_time

        if self.session_name is not None:
            result['SessionName'] = self.session_name

        if self.total_pv is not None:
            result['TotalPv'] = self.total_pv

        if self.total_uv is not None:
            result['TotalUv'] = self.total_uv

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ActiveNum') is not None:
            self.active_num = m.get('ActiveNum')

        if m.get('AgendaId') is not None:
            self.agenda_id = m.get('AgendaId')

        if m.get('AttendancePercent') is not None:
            self.attendance_percent = m.get('AttendancePercent')

        if m.get('FlowTime') is not None:
            self.flow_time = m.get('FlowTime')

        if m.get('SessionName') is not None:
            self.session_name = m.get('SessionName')

        if m.get('TotalPv') is not None:
            self.total_pv = m.get('TotalPv')

        if m.get('TotalUv') is not None:
            self.total_uv = m.get('TotalUv')

        return self


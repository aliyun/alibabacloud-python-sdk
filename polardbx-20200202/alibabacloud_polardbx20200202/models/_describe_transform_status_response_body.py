# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict, Any

from alibabacloud_polardbx20200202 import models as main_models
from darabonba.model import DaraModel

class DescribeTransformStatusResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.DescribeTransformStatusResponseBodyData = None,
        request_id: str = None,
    ):
        self.data = data
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.DescribeTransformStatusResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeTransformStatusResponseBodyData(DaraModel):
    def __init__(
        self,
        can_cancel: bool = None,
        can_finish: bool = None,
        can_switch: bool = None,
        can_undo_switch: bool = None,
        enterprise_ins_name: str = None,
        phase: str = None,
        report_summary: Dict[str, Any] = None,
        report_time: int = None,
        standard_ins_name: str = None,
    ):
        self.can_cancel = can_cancel
        self.can_finish = can_finish
        self.can_switch = can_switch
        self.can_undo_switch = can_undo_switch
        self.enterprise_ins_name = enterprise_ins_name
        self.phase = phase
        self.report_summary = report_summary
        self.report_time = report_time
        self.standard_ins_name = standard_ins_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_cancel is not None:
            result['CanCancel'] = self.can_cancel

        if self.can_finish is not None:
            result['CanFinish'] = self.can_finish

        if self.can_switch is not None:
            result['CanSwitch'] = self.can_switch

        if self.can_undo_switch is not None:
            result['CanUndoSwitch'] = self.can_undo_switch

        if self.enterprise_ins_name is not None:
            result['EnterpriseInsName'] = self.enterprise_ins_name

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.report_summary is not None:
            result['ReportSummary'] = self.report_summary

        if self.report_time is not None:
            result['ReportTime'] = self.report_time

        if self.standard_ins_name is not None:
            result['StandardInsName'] = self.standard_ins_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanCancel') is not None:
            self.can_cancel = m.get('CanCancel')

        if m.get('CanFinish') is not None:
            self.can_finish = m.get('CanFinish')

        if m.get('CanSwitch') is not None:
            self.can_switch = m.get('CanSwitch')

        if m.get('CanUndoSwitch') is not None:
            self.can_undo_switch = m.get('CanUndoSwitch')

        if m.get('EnterpriseInsName') is not None:
            self.enterprise_ins_name = m.get('EnterpriseInsName')

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('ReportSummary') is not None:
            self.report_summary = m.get('ReportSummary')

        if m.get('ReportTime') is not None:
            self.report_time = m.get('ReportTime')

        if m.get('StandardInsName') is not None:
            self.standard_ins_name = m.get('StandardInsName')

        return self


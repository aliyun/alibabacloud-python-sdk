# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetAiReportRequest(DaraModel):
    def __init__(
        self,
        call_id: str = None,
        report_id: str = None,
    ):
        # The data call ID, which is obtained from the callId returned by InvokeDataProduct. You must specify either this parameter or reportId. You cannot specify both or leave both empty. The value must start with call- and be 1 to 64 characters in length. It can contain only ASCII letters, digits, underscores (_), and hyphens (-). The value is case-sensitive, and leading and trailing spaces are not trimmed. If the format is invalid, InvalidParameter.CallId is returned. If both parameters are specified or left empty, InvalidParameter.ReportReference is returned. This parameter is used to query the status of per-use reports. If you use this ID to query a periodic report, WAITING_PERIOD is always returned. Use the ReportId from the list instead.
        self.call_id = call_id
        # The report ID, which is obtained from the ReportId returned by ListProductReports or the Report.ReportId in the previous available result of GetAiReport. You must specify either this parameter or callId. You cannot specify both or leave both empty. The value must start with report- and be 1 to 64 characters in length. It can contain only ASCII letters, digits, underscores (_), and hyphens (-). The value is case-sensitive, and leading and trailing spaces are not trimmed. If the format is invalid, InvalidParameter.ReportId is returned. If both parameters are specified or left empty, InvalidParameter.ReportReference is returned. You can only query reports that belong to the current Alibaba Cloud account.
        self.report_id = report_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.call_id is not None:
            result['callId'] = self.call_id

        if self.report_id is not None:
            result['reportId'] = self.report_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('callId') is not None:
            self.call_id = m.get('callId')

        if m.get('reportId') is not None:
            self.report_id = m.get('reportId')

        return self


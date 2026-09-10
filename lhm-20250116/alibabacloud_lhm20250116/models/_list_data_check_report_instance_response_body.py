# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_lhm20250116 import models as main_models
from darabonba.model import DaraModel

class ListDataCheckReportInstanceResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListDataCheckReportInstanceResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The list of report historical instances.
        self.data = data
        # The error code. An empty string is returned if the call is successful.
        self.err_code = err_code
        # The error message. An empty string is returned if the call is successful.
        self.err_message = err_message
        # The request ID, which is used to locate and troubleshoot issues for this call.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # - true: The call is successful.
        # - false: The call failed. Troubleshoot by using errCode and errMessage.
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListDataCheckReportInstanceResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListDataCheckReportInstanceResponseBodyData(DaraModel):
    def __init__(
        self,
        batch_id: str = None,
        label: str = None,
        report_time: str = None,
    ):
        # The batch ID.
        self.batch_id = batch_id
        # The report label.
        self.label = label
        # The report generation time.
        self.report_time = report_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_id is not None:
            result['batchId'] = self.batch_id

        if self.label is not None:
            result['label'] = self.label

        if self.report_time is not None:
            result['reportTime'] = self.report_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('batchId') is not None:
            self.batch_id = m.get('batchId')

        if m.get('label') is not None:
            self.label = m.get('label')

        if m.get('reportTime') is not None:
            self.report_time = m.get('reportTime')

        return self


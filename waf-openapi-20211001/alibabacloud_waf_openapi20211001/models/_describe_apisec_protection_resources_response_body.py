# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeApisecProtectionResourcesResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.DescribeApisecProtectionResourcesResponseBodyData] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The protected objects.
        self.data = data
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

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
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeApisecProtectionResourcesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeApisecProtectionResourcesResponseBodyData(DaraModel):
    def __init__(
        self,
        apisec_status: int = None,
        report_status: int = None,
        resource: str = None,
        trace_status: int = None,
    ):
        # The switch of the API security module.
        self.apisec_status = apisec_status
        # The switch of the compliance check feature.
        self.report_status = report_status
        # The protected object.
        self.resource = resource
        # The switch of the tracing and auditing feature.
        self.trace_status = trace_status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apisec_status is not None:
            result['ApisecStatus'] = self.apisec_status

        if self.report_status is not None:
            result['ReportStatus'] = self.report_status

        if self.resource is not None:
            result['Resource'] = self.resource

        if self.trace_status is not None:
            result['TraceStatus'] = self.trace_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ApisecStatus') is not None:
            self.apisec_status = m.get('ApisecStatus')

        if m.get('ReportStatus') is not None:
            self.report_status = m.get('ReportStatus')

        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('TraceStatus') is not None:
            self.trace_status = m.get('TraceStatus')

        return self


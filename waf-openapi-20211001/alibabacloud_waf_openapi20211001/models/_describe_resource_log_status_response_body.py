# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeResourceLogStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: List[main_models.DescribeResourceLogStatusResponseBodyResult] = None,
    ):
        # The ID of the request.
        self.request_id = request_id
        # The returned result.
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.DescribeResourceLogStatusResponseBodyResult()
                self.result.append(temp_model.from_map(k1))

        return self

class DescribeResourceLogStatusResponseBodyResult(DaraModel):
    def __init__(
        self,
        resource: str = None,
        status: bool = None,
        trace_config: main_models.DescribeResourceLogStatusResponseBodyResultTraceConfig = None,
        trace_status: bool = None,
    ):
        # The protected object.
        self.resource = resource
        # Indicates whether the log collection feature is enabled for the protected object. Valid values:
        # 
        # *   **true:** The log collection feature is enabled.
        # *   **false:** The log collection feature is disabled.
        self.status = status
        self.trace_config = trace_config
        self.trace_status = trace_status

    def validate(self):
        if self.trace_config:
            self.trace_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource is not None:
            result['Resource'] = self.resource

        if self.status is not None:
            result['Status'] = self.status

        if self.trace_config is not None:
            result['TraceConfig'] = self.trace_config.to_map()

        if self.trace_status is not None:
            result['TraceStatus'] = self.trace_status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Resource') is not None:
            self.resource = m.get('Resource')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TraceConfig') is not None:
            temp_model = main_models.DescribeResourceLogStatusResponseBodyResultTraceConfig()
            self.trace_config = temp_model.from_map(m.get('TraceConfig'))

        if m.get('TraceStatus') is not None:
            self.trace_status = m.get('TraceStatus')

        return self

class DescribeResourceLogStatusResponseBodyResultTraceConfig(DaraModel):
    def __init__(
        self,
        rate_per_mille: int = None,
        workspace: str = None,
    ):
        self.rate_per_mille = rate_per_mille
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.rate_per_mille is not None:
            result['RatePerMille'] = self.rate_per_mille

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RatePerMille') is not None:
            self.rate_per_mille = m.get('RatePerMille')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self


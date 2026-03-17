# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSmartAGDpiAttributeResponseBody(DaraModel):
    def __init__(
        self,
        dpi_monitor_status: str = None,
        dpi_status: str = None,
        logstore_name: str = None,
        project_name: str = None,
        request_id: str = None,
        sls_region: str = None,
    ):
        # The status of the DPI-based monitoring feature. Valid values:
        # 
        # *   **Active**: enabled
        # *   **Inactive**: disabled
        self.dpi_monitor_status = dpi_monitor_status
        # The status of the DPI feature. Valid values:
        # 
        # *   **On**: enabled
        # *   **Off**: disabled
        self.dpi_status = dpi_status
        # The name of the Log Service Logstore that is associated with the DPI feature.
        self.logstore_name = logstore_name
        # The name of the Log Service project that is associated with the DPI feature.
        self.project_name = project_name
        # The ID of the request.
        self.request_id = request_id
        # The region where Log Service is deployed.
        self.sls_region = sls_region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dpi_monitor_status is not None:
            result['DpiMonitorStatus'] = self.dpi_monitor_status

        if self.dpi_status is not None:
            result['DpiStatus'] = self.dpi_status

        if self.logstore_name is not None:
            result['LogstoreName'] = self.logstore_name

        if self.project_name is not None:
            result['ProjectName'] = self.project_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.sls_region is not None:
            result['SlsRegion'] = self.sls_region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DpiMonitorStatus') is not None:
            self.dpi_monitor_status = m.get('DpiMonitorStatus')

        if m.get('DpiStatus') is not None:
            self.dpi_status = m.get('DpiStatus')

        if m.get('LogstoreName') is not None:
            self.logstore_name = m.get('LogstoreName')

        if m.get('ProjectName') is not None:
            self.project_name = m.get('ProjectName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SlsRegion') is not None:
            self.sls_region = m.get('SlsRegion')

        return self


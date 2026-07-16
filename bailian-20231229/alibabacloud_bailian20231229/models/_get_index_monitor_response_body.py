# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any

from darabonba.model import DaraModel

class GetIndexMonitorResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: Any = None,
        message: str = None,
        request_id: str = None,
        status: int = None,
        success: bool = None,
    ):
        # The status code.
        self.code = code
        # The core data object of the response.
        # 
        # **pipelineCommercialType** (String): The edition of the knowledge base.
        # 
        # - standard: Standard Edition
        # 
        # - enterprise: Ultimate Edition
        # 
        # **storageMonitorData** (Object): The storage monitoring data of the knowledge base.
        # 
        # - indexStorageLimit (Number): The index storage limit of the knowledge base, in GB.
        # 
        # - indexStorageUsage (Number): The current index storage usage of the knowledge base, in GB.
        # 
        # **pipelineCommercialCu** (Integer): The number of RCU for the Ultimate Edition knowledge base. For example: 2.
        # 
        # **qpsMonitorData** (Object): The aggregated retrieval monitoring data for the knowledge base over the entire query period.
        # 
        # - peakQps (Integer): The peak QPS over the entire time period.
        # 
        # - totalRequests (Integer): The total number of requests over the entire time period.
        # 
        # - avgQpsOfActiveSeconds (Number): The average QPS during active seconds over the entire time period. Active seconds are seconds in which calls were made.
        # 
        # - monitorData (Array): An array of detailed monitoring data broken down by time window. Each object in the array represents the performance statistics for a single time window.
        # 
        #   <details>
        # 
        #   <summary>
        # 
        #   Sub-properties
        # 
        #   </summary>
        # 
        #   - successData (Object): The statistics for successful requests within this window.
        # 
        #   - limitData (Object): The statistics for rate-limited requests within this window.
        # 
        #   - failData (Object): The statistics for failed calls within this window.
        # 
        #   - peakQpsInWindowRange (Integer): The total peak QPS within this window (successful + rate-limited + failed).
        # 
        #   - totalRequests (Integer): The total number of requests within this window (successful + rate-limited + failed).
        # 
        #   - windowRange (Integer): The start time of the time window (UNIX timestamp in seconds).
        # 
        #   - windowRangeEnd (Integer): The end time of the time window (UNIX timestamp in seconds).
        # 
        #   - avgQpsOfActiveSeconds (Number): The average QPS during active seconds within this window.
        # 
        #   **The successData, limitData, and failData objects have the same internal structure, as described below:**
        # 
        #   - peakQpsInWindowRange (Integer): The peak QPS for the corresponding status.
        # 
        #   - totalRequests (Integer): The total number of requests for the corresponding status.
        # 
        #   - avgQpsOfActiveSeconds (Number): The average QPS during active seconds for the corresponding status.
        # 
        #   </details>
        self.data = data
        # The status message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # The status code returned by the operation.
        self.status = status
        # Indicates whether the request was successful.
        self.success = success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status is not None:
            result['Status'] = self.status

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            self.data = m.get('Data')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self


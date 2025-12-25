# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeUserWafLogStatusResponseBody(DaraModel):
    def __init__(
        self,
        log_region_id: str = None,
        log_status: str = None,
        request_id: str = None,
        status_update_time: int = None,
    ):
        # The ID of the region where WAF logs are stored. Valid values:
        # 
        # *   **cn-hangzhou**: China (Hangzhou).
        # *   **cn-beijing**: China (Beijing).
        # *   **cn-hongkong**: China (Hong Kong).
        # *   **ap-southeast-1**: Singapore.
        # *   **ap-southeast-3**: Malaysia (Kuala Lumpur).
        # *   **ap-southeast-5**: Indonesia (Jakarta).
        # *   **ap-southeast-6**: Philippines (Manila).
        # *   **ap-southeast-7**: Thailand (Bangkok).
        # *   **me-east-1**: UAE (Dubai).
        # *   **eu-central-1**: Germany (Frankfurt).
        # *   **us-east-1**: US (Virginia).
        # *   **us-west-1**: US (Silicon Valley).
        # *   **ap-northeast-1**: Japan (Tokyo).
        # *   **ap-northeast-2**: South Korea (Seoul).
        # *   **eu-west-1**: UK (London).
        # *   **cn-hangzhou-finance**: China East 1 Finance.
        # *   **cn-shanghai-finance-1**: China East 2 Finance.
        # *   **cn-shenzhen-finance**: China South 1 Finance.
        # 
        # >  The China East 1 Finance, China East 2 Finance, and China South 1 Finance regions are available only for Alibaba Finance Cloud users. Alibaba Finance Cloud users are also limited to storing logs within these specific regions.
        self.log_region_id = log_region_id
        # The status of WAF logs.
        # 
        # *   **initializing**
        # *   **initialize_failed**
        # *   **normal**
        # *   **releasing**
        # *   **release_failed**
        self.log_status = log_status
        # The request ID.
        self.request_id = request_id
        # The time when the log status was modified. Unit: milliseconds.
        self.status_update_time = status_update_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.log_region_id is not None:
            result['LogRegionId'] = self.log_region_id

        if self.log_status is not None:
            result['LogStatus'] = self.log_status

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.status_update_time is not None:
            result['StatusUpdateTime'] = self.status_update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LogRegionId') is not None:
            self.log_region_id = m.get('LogRegionId')

        if m.get('LogStatus') is not None:
            self.log_status = m.get('LogStatus')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('StatusUpdateTime') is not None:
            self.status_update_time = m.get('StatusUpdateTime')

        return self


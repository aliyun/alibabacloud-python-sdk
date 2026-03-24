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
        # The ID of the region where logs are stored. Valid values:
        # 
        # - **cn-hangzhou**: indicates China East 1 (Hangzhou).
        # 
        # - **cn-beijing**: indicates China North 2 (Beijing).
        # 
        # - **cn-hongkong**: indicates China (Hong Kong).
        # 
        # - **ap-southeast-1**: indicates Singapore.
        # 
        # - **ap-southeast-3**: indicates Malaysia (Kuala Lumpur).
        # 
        # - **ap-southeast-5**: indicates Indonesia (Jakarta).
        # 
        # - **ap-southeast-6**: indicates Philippines (Manila).
        # 
        # - **ap-southeast-7**: indicates Thailand (Bangkok).
        # 
        # - **me-east-1**: indicates UAE (Dubai).
        # 
        # - **eu-central-1**: indicates Germany (Frankfurt).
        # 
        # - **us-east-1**: indicates US (Virginia).
        # 
        # - **us-west-1**: indicates US (Silicon Valley).
        # 
        # - **ap-northeast-1**: indicates Japan (Tokyo).
        # 
        # - **ap-northeast-2**: indicates South Korea (Seoul).
        # 
        # - **eu-west-1**: indicates UK (London).
        # 
        # - **cn-hangzhou-finance**: indicates China East 1 Hangzhou Finance Cloud.
        # 
        # - **cn-shanghai-finance-1**: indicates China East 2 Shanghai Finance Cloud.
        # 
        # - **cn-shenzhen-finance**: indicates China South 1 Shenzhen Finance Cloud.
        # 
        # > The Finance Cloud regions are available only to Finance Cloud users, and Finance Cloud users can obtain only these regions.
        self.log_region_id = log_region_id
        # The status of WAF logs.
        # 
        # - **initializing**: The logs are being initialized.
        # 
        # - **initialize_failed**: The initialization failed.
        # 
        # - **normal**: The logs are running properly.
        # 
        # - **releasing**: The logs are being released.
        # 
        # - **release_failed**: The release failed.
        self.log_status = log_status
        # The request ID, which is used to locate and troubleshoot issues.
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


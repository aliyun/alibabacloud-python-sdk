# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_waf_openapi20211001 import models as main_models
from darabonba.model import DaraModel

class DescribeAlarmBannerResponseBody(DaraModel):
    def __init__(
        self,
        banner_status: main_models.DescribeAlarmBannerResponseBodyBannerStatus = None,
        request_id: str = None,
    ):
        # The status information of the alert banner.
        self.banner_status = banner_status
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.banner_status:
            self.banner_status.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.banner_status is not None:
            result['BannerStatus'] = self.banner_status.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BannerStatus') is not None:
            temp_model = main_models.DescribeAlarmBannerResponseBodyBannerStatus()
            self.banner_status = temp_model.from_map(m.get('BannerStatus'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAlarmBannerResponseBodyBannerStatus(DaraModel):
    def __init__(
        self,
        cause: str = None,
        count: int = None,
        status: bool = None,
        type: str = None,
    ):
        # The cause of the alert. If **Type** is set to **sandbox**, valid values:
        # 
        # - **fivefold**: The queries per second (QPS) of your service exceeds five times the upper limit of your plan.
        # 
        # - **4count**: The QPS of your service has exceeded the upper limit of your plan for four or more days.
        # 
        # - **exceed10w**: The peak QPS of your service exceeds 100,000.
        # 
        # - **costProtection**: Billing protection is triggered.
        self.cause = cause
        # The count associated with the alert at the time it was triggered.
        # 
        # - If **Type** is set to **sandbox**, this parameter indicates the number of days that the QPS has exceeded the upper limit of your plan.
        self.count = count
        # Indicates whether an alert is triggered. Valid values:
        # 
        # - **true**: An alert is triggered. If **Type** is set to **sandbox**, the instance is in the sandbox.
        # 
        # - **false**: No alert is triggered. If **Type** is set to **sandbox**, the instance is not in the sandbox.
        self.status = status
        # The alert type. Valid value:
        # 
        # - **sandbox**: a sandbox alert.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cause is not None:
            result['Cause'] = self.cause

        if self.count is not None:
            result['Count'] = self.count

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Cause') is not None:
            self.cause = m.get('Cause')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


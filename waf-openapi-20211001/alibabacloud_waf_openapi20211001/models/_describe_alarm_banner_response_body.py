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
        self.banner_status = banner_status
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
        self.cause = cause
        self.count = count
        self.status = status
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


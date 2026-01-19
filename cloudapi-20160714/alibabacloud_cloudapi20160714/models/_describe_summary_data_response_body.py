# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeSummaryDataResponseBody(DaraModel):
    def __init__(
        self,
        expire_instance_num: int = None,
        region: str = None,
        request_id: str = None,
        usage_api_num: int = None,
        usage_group_num: int = None,
        usage_instance_num: int = None,
    ):
        # The number of subscription dedicated instances that expire in 14 days or less.
        self.expire_instance_num = expire_instance_num
        # The region ID.
        self.region = region
        # The request ID.
        self.request_id = request_id
        # The number of APIs.
        self.usage_api_num = usage_api_num
        # The number of API groups.
        self.usage_group_num = usage_group_num
        # The number of running dedicated instances.
        self.usage_instance_num = usage_instance_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.expire_instance_num is not None:
            result['ExpireInstanceNum'] = self.expire_instance_num

        if self.region is not None:
            result['Region'] = self.region

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.usage_api_num is not None:
            result['UsageApiNum'] = self.usage_api_num

        if self.usage_group_num is not None:
            result['UsageGroupNum'] = self.usage_group_num

        if self.usage_instance_num is not None:
            result['UsageInstanceNum'] = self.usage_instance_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExpireInstanceNum') is not None:
            self.expire_instance_num = m.get('ExpireInstanceNum')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('UsageApiNum') is not None:
            self.usage_api_num = m.get('UsageApiNum')

        if m.get('UsageGroupNum') is not None:
            self.usage_group_num = m.get('UsageGroupNum')

        if m.get('UsageInstanceNum') is not None:
            self.usage_instance_num = m.get('UsageInstanceNum')

        return self


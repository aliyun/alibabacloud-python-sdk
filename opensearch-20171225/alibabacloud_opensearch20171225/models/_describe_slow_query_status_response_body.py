# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_opensearch20171225 import models as main_models
from darabonba.model import DaraModel

class DescribeSlowQueryStatusResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        result: main_models.DescribeSlowQueryStatusResponseBodyResult = None,
    ):
        # The request ID.
        self.request_id = request_id
        # The result.
        self.result = result

    def validate(self):
        if self.result:
            self.result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.result is not None:
            result['result'] = self.result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('result') is not None:
            temp_model = main_models.DescribeSlowQueryStatusResponseBodyResult()
            self.result = temp_model.from_map(m.get('result'))

        return self

class DescribeSlowQueryStatusResponseBodyResult(DaraModel):
    def __init__(
        self,
        app_group_id: str = None,
        region: str = None,
        status: str = None,
    ):
        # The application ID.
        self.app_group_id = app_group_id
        # The region.
        # 
        # - outer: Public network
        # 
        # - internal: Internal network
        self.region = region
        # The activation status.
        # 
        # - enabled: Enabled
        # 
        # - disabled: Disabled
        # 
        # - n/a: Unknown
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_group_id is not None:
            result['appGroupId'] = self.app_group_id

        if self.region is not None:
            result['region'] = self.region

        if self.status is not None:
            result['status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('appGroupId') is not None:
            self.app_group_id = m.get('appGroupId')

        if m.get('region') is not None:
            self.region = m.get('region')

        if m.get('status') is not None:
            self.status = m.get('status')

        return self


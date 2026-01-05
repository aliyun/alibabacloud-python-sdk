# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eds_aic20230930 import models as main_models
from darabonba.model import DaraModel

class SetAdbSecureResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.SetAdbSecureResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned object.
        self.data = data
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.SetAdbSecureResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class SetAdbSecureResponseBodyData(DaraModel):
    def __init__(
        self,
        fail_count: int = None,
        instance_ids: List[str] = None,
        total_count: int = None,
    ):
        # The number of the cloud phone instances for which the ADB authentication feature failed to be enabled.
        self.fail_count = fail_count
        # The IDs of the cloud phone instances for which the ADB authentication feature is enabled.
        self.instance_ids = instance_ids
        # The total number of the cloud phone instances.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self


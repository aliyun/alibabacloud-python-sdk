# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class CreateInstanceResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        instance_ids: main_models.CreateInstanceResponseBodyInstanceIds = None,
        request_id: str = None,
    ):
        # The return code. A value of 0 indicates success.
        # 
        # > If you call this API operation by using an SDK, the return type is Integer. If you call this API operation by using a common method or HTTP, the return type is String.
        self.code = code
        self.instance_ids = instance_ids
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_ids:
            self.instance_ids.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('InstanceIds') is not None:
            temp_model = main_models.CreateInstanceResponseBodyInstanceIds()
            self.instance_ids = temp_model.from_map(m.get('InstanceIds'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CreateInstanceResponseBodyInstanceIds(DaraModel):
    def __init__(
        self,
        instance_id: List[str] = None,
    ):
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self


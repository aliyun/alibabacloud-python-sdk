# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DescribeCreatePrePaidInstanceResultResponseBody(DaraModel):
    def __init__(
        self,
        instance_create_result: main_models.DescribeCreatePrePaidInstanceResultResponseBodyInstanceCreateResult = None,
        request_id: str = None,
    ):
        # Returned results of creating an instance.
        self.instance_create_result = instance_create_result
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.instance_create_result:
            self.instance_create_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_create_result is not None:
            result['InstanceCreateResult'] = self.instance_create_result.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCreateResult') is not None:
            temp_model = main_models.DescribeCreatePrePaidInstanceResultResponseBodyInstanceCreateResult()
            self.instance_create_result = temp_model.from_map(m.get('InstanceCreateResult'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeCreatePrePaidInstanceResultResponseBodyInstanceCreateResult(DaraModel):
    def __init__(
        self,
        instance_create_status: str = None,
        instance_id: str = None,
    ):
        # The status of the instance creation.
        # 
        # *   Accepted
        # *   Creating
        # *   Failed
        # *   Successed
        self.instance_create_status = instance_create_status
        # The ID of the instance.
        self.instance_id = instance_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_create_status is not None:
            result['InstanceCreateStatus'] = self.instance_create_status

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceCreateStatus') is not None:
            self.instance_create_status = m.get('InstanceCreateStatus')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        return self


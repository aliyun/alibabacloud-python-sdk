# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ens20171110 import models as main_models
from darabonba.model import DaraModel

class DetachKeyPairResponseBody(DaraModel):
    def __init__(
        self,
        fail_count: int = None,
        key_pair_id: str = None,
        key_pair_name: str = None,
        request_id: str = None,
        results: List[main_models.DetachKeyPairResponseBodyResults] = None,
        total_count: int = None,
    ):
        # The number of instances to which the SSH key pair failed to be bound.
        self.fail_count = fail_count
        # The ID of the SSH key pair.
        self.key_pair_id = key_pair_id
        # The name of the SSH key pair.
        self.key_pair_name = key_pair_name
        # The request ID.
        self.request_id = request_id
        # The operation results.
        self.results = results
        # The total number of instances to which the SSH key pair is bound.
        self.total_count = total_count

    def validate(self):
        if self.results:
            for v1 in self.results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.key_pair_id is not None:
            result['KeyPairId'] = self.key_pair_id

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('KeyPairId') is not None:
            self.key_pair_id = m.get('KeyPairId')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.DetachKeyPairResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DetachKeyPairResponseBodyResults(DaraModel):
    def __init__(
        self,
        code: int = None,
        instance_id: str = None,
        message: str = None,
        success: bool = None,
    ):
        # The status code of the operation. 200 indicates that the operation succeeded.
        self.code = code
        # The instance ID.
        self.instance_id = instance_id
        # The message of the operation. If the value of the Code parameter is 200, the value of this parameter is successful.
        self.message = message
        # Indicates whether the operation is successful.
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

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.message is not None:
            result['Message'] = self.message

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self


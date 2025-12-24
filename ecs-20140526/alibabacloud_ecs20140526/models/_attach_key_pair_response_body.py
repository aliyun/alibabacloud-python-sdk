# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecs20140526 import models as main_models
from darabonba.model import DaraModel

class AttachKeyPairResponseBody(DaraModel):
    def __init__(
        self,
        fail_count: str = None,
        key_pair_name: str = None,
        request_id: str = None,
        results: main_models.AttachKeyPairResponseBodyResults = None,
        total_count: str = None,
    ):
        # The number of instances to which the SSH key pair fails to be bound.
        self.fail_count = fail_count
        # The name of the SSH key pair.
        self.key_pair_name = key_pair_name
        # The request ID.
        self.request_id = request_id
        # An array that contains the results of the operation.
        self.results = results
        # The total number of instances to which the SSH key pair is bound.
        self.total_count = total_count

    def validate(self):
        if self.results:
            self.results.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fail_count is not None:
            result['FailCount'] = self.fail_count

        if self.key_pair_name is not None:
            result['KeyPairName'] = self.key_pair_name

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.results is not None:
            result['Results'] = self.results.to_map()

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FailCount') is not None:
            self.fail_count = m.get('FailCount')

        if m.get('KeyPairName') is not None:
            self.key_pair_name = m.get('KeyPairName')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Results') is not None:
            temp_model = main_models.AttachKeyPairResponseBodyResults()
            self.results = temp_model.from_map(m.get('Results'))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class AttachKeyPairResponseBodyResults(DaraModel):
    def __init__(
        self,
        result: List[main_models.AttachKeyPairResponseBodyResultsResult] = None,
    ):
        self.result = result

    def validate(self):
        if self.result:
            for v1 in self.result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Result'] = []
        if self.result is not None:
            for k1 in self.result:
                result['Result'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.result = []
        if m.get('Result') is not None:
            for k1 in m.get('Result'):
                temp_model = main_models.AttachKeyPairResponseBodyResultsResult()
                self.result.append(temp_model.from_map(k1))

        return self

class AttachKeyPairResponseBodyResultsResult(DaraModel):
    def __init__(
        self,
        code: str = None,
        instance_id: str = None,
        message: str = None,
        success: str = None,
    ):
        # The operation status code returned. 200 indicates that the operation was successful.
        self.code = code
        # The instance ID.
        self.instance_id = instance_id
        # The operation information returned. When the value of Code is 200, the value of Message is successful.
        self.message = message
        # Indicates whether the request was successful.
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


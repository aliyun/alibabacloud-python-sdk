# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_computenest20210601 import models as main_models
from darabonba.model import DaraModel

class CheckServiceDeployableResponseBody(DaraModel):
    def __init__(
        self,
        check_results: List[main_models.CheckServiceDeployableResponseBodyCheckResults] = None,
        request_id: str = None,
    ):
        # Inspection result.
        self.check_results = check_results
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.check_results:
            for v1 in self.check_results:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckResults'] = []
        if self.check_results is not None:
            for k1 in self.check_results:
                result['CheckResults'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_results = []
        if m.get('CheckResults') is not None:
            for k1 in m.get('CheckResults'):
                temp_model = main_models.CheckServiceDeployableResponseBodyCheckResults()
                self.check_results.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class CheckServiceDeployableResponseBodyCheckResults(DaraModel):
    def __init__(
        self,
        message: str = None,
        skippable: bool = None,
        type: str = None,
        value: str = None,
    ):
        # Returns a hint message for the result.
        self.message = message
        self.skippable = skippable
        # Check type, invalid values:
        # 
        # - Balance ：Account balance.
        # 
        # - Quota:  Account quota.
        self.type = type
        # Inspection result.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.skippable is not None:
            result['Skippable'] = self.skippable

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Skippable') is not None:
            self.skippable = m.get('Skippable')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


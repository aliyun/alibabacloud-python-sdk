# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rdsai20250507 import models as main_models
from darabonba.model import DaraModel

class UpdateMOQuotaAlertThresholdResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        results: List[main_models.UpdateMOQuotaAlertThresholdResponseBodyResults] = None,
        success: bool = None,
    ):
        # Id of the request
        self.request_id = request_id
        self.results = results
        self.success = success

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
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Results'] = []
        if self.results is not None:
            for k1 in self.results:
                result['Results'].append(k1.to_map() if k1 else None)

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.results = []
        if m.get('Results') is not None:
            for k1 in m.get('Results'):
                temp_model = main_models.UpdateMOQuotaAlertThresholdResponseBodyResults()
                self.results.append(temp_model.from_map(k1))

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class UpdateMOQuotaAlertThresholdResponseBodyResults(DaraModel):
    def __init__(
        self,
        apikey: str = None,
        instance_id: str = None,
        key_name: str = None,
        key_type: str = None,
        threshold_percent: int = None,
    ):
        # API Key
        self.apikey = apikey
        self.instance_id = instance_id
        self.key_name = key_name
        self.key_type = key_type
        self.threshold_percent = threshold_percent

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.apikey is not None:
            result['Apikey'] = self.apikey

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.key_name is not None:
            result['KeyName'] = self.key_name

        if self.key_type is not None:
            result['KeyType'] = self.key_type

        if self.threshold_percent is not None:
            result['ThresholdPercent'] = self.threshold_percent

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Apikey') is not None:
            self.apikey = m.get('Apikey')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('KeyName') is not None:
            self.key_name = m.get('KeyName')

        if m.get('KeyType') is not None:
            self.key_type = m.get('KeyType')

        if m.get('ThresholdPercent') is not None:
            self.threshold_percent = m.get('ThresholdPercent')

        return self


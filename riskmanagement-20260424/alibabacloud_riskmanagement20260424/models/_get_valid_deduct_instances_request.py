# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetValidDeductInstancesRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        sdk_request: main_models.GetValidDeductInstancesRequestSdkRequest = None,
    ):
        self.region_id = region_id
        self.sdk_request = sdk_request

    def validate(self):
        if self.sdk_request:
            self.sdk_request.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.sdk_request is not None:
            result['SdkRequest'] = self.sdk_request.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('SdkRequest') is not None:
            temp_model = main_models.GetValidDeductInstancesRequestSdkRequest()
            self.sdk_request = temp_model.from_map(m.get('SdkRequest'))

        return self

class GetValidDeductInstancesRequestSdkRequest(DaraModel):
    def __init__(
        self,
        instance_id: str = None,
        modules: str = None,
        status: int = None,
    ):
        self.instance_id = instance_id
        self.modules = modules
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.modules is not None:
            result['Modules'] = self.modules

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Modules') is not None:
            self.modules = m.get('Modules')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


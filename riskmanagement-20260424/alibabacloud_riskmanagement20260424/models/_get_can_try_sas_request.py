# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class GetCanTrySasRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        sdk_request: main_models.GetCanTrySasRequestSdkRequest = None,
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
            temp_model = main_models.GetCanTrySasRequestSdkRequest()
            self.sdk_request = temp_model.from_map(m.get('SdkRequest'))

        return self

class GetCanTrySasRequestSdkRequest(DaraModel):
    def __init__(
        self,
        from_ecs: bool = None,
        lang: str = None,
    ):
        self.from_ecs = from_ecs
        self.lang = lang

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ecs is not None:
            result['FromEcs'] = self.from_ecs

        if self.lang is not None:
            result['Lang'] = self.lang

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromEcs') is not None:
            self.from_ecs = m.get('FromEcs')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        return self


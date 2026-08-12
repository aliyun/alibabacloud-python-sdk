# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_riskmanagement20260424 import models as main_models
from darabonba.model import DaraModel

class CreateSasTrialRequest(DaraModel):
    def __init__(
        self,
        region_id: str = None,
        sdk_request: main_models.CreateSasTrialRequestSdkRequest = None,
    ):
        # The region ID of the access control instance. You can call the DescribeRegions operation to query the region ID.
        self.region_id = region_id
        # The Security Center SDK request.
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
            temp_model = main_models.CreateSasTrialRequestSdkRequest()
            self.sdk_request = temp_model.from_map(m.get('SdkRequest'))

        return self

class CreateSasTrialRequestSdkRequest(DaraModel):
    def __init__(
        self,
        from_ecs: bool = None,
        lang: str = None,
        request_form: main_models.CreateSasTrialRequestSdkRequestRequestForm = None,
        try_type: int = None,
        try_version: int = None,
    ):
        # Specifies whether the request is from the ECS console. Valid values:
        # - **true**: The request is from the ECS console.
        # - **false**: The request is not from the ECS console.
        self.from_ecs = from_ecs
        # The language of the request and response. Valid values:
        # 
        # - **zh** (default): Chinese.
        # 
        # - **en**: English.
        self.lang = lang
        # The reason for applying for the trial.
        self.request_form = request_form
        # The trial type. Valid values:
        # - **0**: trial not allowed
        # - **1**: first trial
        # - **2**: second trial
        # 
        # 
        # > Call the [GetCanTrySas](https://help.aliyun.com/document_detail/2623574.html) operation to obtain this parameter. The trial can be started only when the value is not 0.
        self.try_type = try_type
        # The trial edition. Valid values:
        # - **3**: Enterprise Edition.
        # - **7**: Ultimate Edition.
        # 
        # > Call the [GetCanTrySas](https://help.aliyun.com/document_detail/2623574.html) operation to obtain this parameter.
        self.try_version = try_version

    def validate(self):
        if self.request_form:
            self.request_form.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ecs is not None:
            result['FromEcs'] = self.from_ecs

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.request_form is not None:
            result['RequestForm'] = self.request_form.to_map()

        if self.try_type is not None:
            result['TryType'] = self.try_type

        if self.try_version is not None:
            result['TryVersion'] = self.try_version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FromEcs') is not None:
            self.from_ecs = m.get('FromEcs')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RequestForm') is not None:
            temp_model = main_models.CreateSasTrialRequestSdkRequestRequestForm()
            self.request_form = temp_model.from_map(m.get('RequestForm'))

        if m.get('TryType') is not None:
            self.try_type = m.get('TryType')

        if m.get('TryVersion') is not None:
            self.try_version = m.get('TryVersion')

        return self

class CreateSasTrialRequestSdkRequestRequestForm(DaraModel):
    def __init__(
        self,
        try_reason: str = None,
    ):
        # The reason for applying for the trial.
        self.try_reason = try_reason

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.try_reason is not None:
            result['TryReason'] = self.try_reason

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TryReason') is not None:
            self.try_reason = m.get('TryReason')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateSasTrialRequest(DaraModel):
    def __init__(
        self,
        client_token: str = None,
        from_ecs: bool = None,
        lang: str = None,
        request_form: main_models.CreateSasTrialRequestRequestForm = None,
        try_type: int = None,
        try_version: int = None,
    ):
        # The client token that is used to ensure the idempotence of the request. Different requests should use different tokens. The token supports only ASCII characters and cannot exceed 64 characters in length.
        self.client_token = client_token
        # Specifies whether the request is from the ECS console. Valid values:
        # - **true**: yes.
        # - **false**: no.
        self.from_ecs = from_ecs
        # The language of the request and response. Valid values:
        # - **zh**: Chinese.
        # - **en**: English.
        self.lang = lang
        # The reason for applying for a trial. This parameter is required for a second trial.
        self.request_form = request_form
        # The trial type. Valid values:
        # - **0**: trial not allowed.
        # - **1**: first trial.
        # - **2**: second trial.
        # 
        # 
        # > Call the [GetCanTrySas](https://help.aliyun.com/document_detail/2623574.html) operation to obtain this parameter. A trial can be started only when the value is not 0.
        self.try_type = try_type
        # The trial version. Valid values:
        # - **3**: Enterprise Edition.
        # - **7**: Ultimate Edition.
        # 
        # >Call the [GetCanTrySas](https://help.aliyun.com/document_detail/2623574.html) operation to obtain this parameter.
        self.try_version = try_version

    def validate(self):
        if self.request_form:
            self.request_form.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.client_token is not None:
            result['ClientToken'] = self.client_token

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
        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('FromEcs') is not None:
            self.from_ecs = m.get('FromEcs')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('RequestForm') is not None:
            temp_model = main_models.CreateSasTrialRequestRequestForm()
            self.request_form = temp_model.from_map(m.get('RequestForm'))

        if m.get('TryType') is not None:
            self.try_type = m.get('TryType')

        if m.get('TryVersion') is not None:
            self.try_version = m.get('TryVersion')

        return self

class CreateSasTrialRequestRequestForm(DaraModel):
    def __init__(
        self,
        try_reason: str = None,
    ):
        # The reason for applying for a trial.
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class CreateSasTrialRequest(DaraModel):
    def __init__(
        self,
        from_ecs: bool = None,
        lang: str = None,
        request_form: main_models.CreateSasTrialRequestRequestForm = None,
        try_type: int = None,
        try_version: int = None,
    ):
        # Specifies whether the request is redirected from the Elastic Compute Service (ECS) console. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.from_ecs = from_ecs
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The reason why you apply for the trial. You must specify the reason for the second trial.
        self.request_form = request_form
        # The trial type. Valid values:
        # 
        # *   **0**: trial prohibited
        # *   **1**: first trial
        # *   **2**: second trial
        # 
        # >  You can call the [GetCanTrySas](https://help.aliyun.com/document_detail/2623574.html) operation to obtain the trial type. You can start a trial only if this parameter is not set to 0.
        self.try_type = try_type
        # The trial edition. Valid values:
        # 
        # *   **3**: Enterprise
        # *   **7**: Ultimate
        # 
        # >  You can call the [GetCanTrySas](https://help.aliyun.com/document_detail/2623574.html) operation to obtain the trial edition.
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
        # The reason why you apply for the trial.
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


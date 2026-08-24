# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class GetProhibitedSoftwareRequest(DaraModel):
    def __init__(
        self,
        software_id: main_models.GetProhibitedSoftwareRequestSoftwareId = None,
    ):
        # The prohibited software ID.
        self.software_id = software_id

    def validate(self):
        if self.software_id:
            self.software_id.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.software_id is not None:
            result['SoftwareId'] = self.software_id.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SoftwareId') is not None:
            temp_model = main_models.GetProhibitedSoftwareRequestSoftwareId()
            self.software_id = temp_model.from_map(m.get('SoftwareId'))

        return self

class GetProhibitedSoftwareRequestSoftwareId(DaraModel):
    def __init__(
        self,
        is_default: bool = None,
        software_id: str = None,
    ):
        # Indicates whether the prohibited software is a system built-in prohibited software. Valid values:
        # - **true**: A system built-in prohibited software that is shared across all Alibaba Cloud accounts and cannot be modified or deleted.
        # - **false**: A custom prohibited software under the current Alibaba Cloud account.
        self.is_default = is_default
        # The prohibited software ID. You can obtain the value from the following operations:
        # - [ListProhibitedSoftware](~~ListProhibitedSoftware~~): Lists prohibited software.
        # - [CreateProhibitedSoftware](~~CreateProhibitedSoftware~~): Creates custom prohibited software.
        self.software_id = software_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        if self.software_id is not None:
            result['SoftwareId'] = self.software_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')

        return self


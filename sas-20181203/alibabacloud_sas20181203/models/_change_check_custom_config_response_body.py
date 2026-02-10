# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ChangeCheckCustomConfigResponseBody(DaraModel):
    def __init__(
        self,
        illegal_custom_configs: List[main_models.ChangeCheckCustomConfigResponseBodyIllegalCustomConfigs] = None,
        illegal_repair_configs: List[main_models.ChangeCheckCustomConfigResponseBodyIllegalRepairConfigs] = None,
        request_id: str = None,
    ):
        # An array that consists of the invalid custom configuration items of the check item.
        self.illegal_custom_configs = illegal_custom_configs
        # An array that consists of the invalid parameters required for fixing risk items.
        self.illegal_repair_configs = illegal_repair_configs
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.illegal_custom_configs:
            for v1 in self.illegal_custom_configs:
                 if v1:
                    v1.validate()
        if self.illegal_repair_configs:
            for v1 in self.illegal_repair_configs:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['IllegalCustomConfigs'] = []
        if self.illegal_custom_configs is not None:
            for k1 in self.illegal_custom_configs:
                result['IllegalCustomConfigs'].append(k1.to_map() if k1 else None)

        result['IllegalRepairConfigs'] = []
        if self.illegal_repair_configs is not None:
            for k1 in self.illegal_repair_configs:
                result['IllegalRepairConfigs'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.illegal_custom_configs = []
        if m.get('IllegalCustomConfigs') is not None:
            for k1 in m.get('IllegalCustomConfigs'):
                temp_model = main_models.ChangeCheckCustomConfigResponseBodyIllegalCustomConfigs()
                self.illegal_custom_configs.append(temp_model.from_map(k1))

        self.illegal_repair_configs = []
        if m.get('IllegalRepairConfigs') is not None:
            for k1 in m.get('IllegalRepairConfigs'):
                temp_model = main_models.ChangeCheckCustomConfigResponseBodyIllegalRepairConfigs()
                self.illegal_repair_configs.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ChangeCheckCustomConfigResponseBodyIllegalRepairConfigs(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the invalid parameter required for fixing a risk item.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class ChangeCheckCustomConfigResponseBodyIllegalCustomConfigs(DaraModel):
    def __init__(
        self,
        name: str = None,
    ):
        # The name of the custom configuration item, which is unique in a check item.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self


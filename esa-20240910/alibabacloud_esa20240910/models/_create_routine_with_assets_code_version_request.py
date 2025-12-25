# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_esa20240910 import models as main_models
from darabonba.model import DaraModel

class CreateRoutineWithAssetsCodeVersionRequest(DaraModel):
    def __init__(
        self,
        build_id: int = None,
        code_description: str = None,
        conf_options: main_models.CreateRoutineWithAssetsCodeVersionRequestConfOptions = None,
        extra_info: str = None,
        name: str = None,
    ):
        self.build_id = build_id
        self.code_description = code_description
        self.conf_options = conf_options
        self.extra_info = extra_info
        # This parameter is required.
        self.name = name

    def validate(self):
        if self.conf_options:
            self.conf_options.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.build_id is not None:
            result['BuildId'] = self.build_id

        if self.code_description is not None:
            result['CodeDescription'] = self.code_description

        if self.conf_options is not None:
            result['ConfOptions'] = self.conf_options.to_map()

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BuildId') is not None:
            self.build_id = m.get('BuildId')

        if m.get('CodeDescription') is not None:
            self.code_description = m.get('CodeDescription')

        if m.get('ConfOptions') is not None:
            temp_model = main_models.CreateRoutineWithAssetsCodeVersionRequestConfOptions()
            self.conf_options = temp_model.from_map(m.get('ConfOptions'))

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class CreateRoutineWithAssetsCodeVersionRequestConfOptions(DaraModel):
    def __init__(
        self,
        not_found_strategy: str = None,
    ):
        self.not_found_strategy = not_found_strategy

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.not_found_strategy is not None:
            result['NotFoundStrategy'] = self.not_found_strategy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NotFoundStrategy') is not None:
            self.not_found_strategy = m.get('NotFoundStrategy')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_paistudio20220112 import models as main_models
from darabonba.model import DaraModel

class UpdateResourceGroupRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        name: str = None,
        unbind: bool = None,
        user_vpc: main_models.UserVpc = None,
    ):
        self.description = description
        self.name = name
        self.unbind = unbind
        self.user_vpc = user_vpc

    def validate(self):
        if self.user_vpc:
            self.user_vpc.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.name is not None:
            result['Name'] = self.name

        if self.unbind is not None:
            result['Unbind'] = self.unbind

        if self.user_vpc is not None:
            result['UserVpc'] = self.user_vpc.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Unbind') is not None:
            self.unbind = m.get('Unbind')

        if m.get('UserVpc') is not None:
            temp_model = main_models.UserVpc()
            self.user_vpc = temp_model.from_map(m.get('UserVpc'))

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateInstanceImageRequest(DaraModel):
    def __init__(
        self,
        ignore_param_validation: bool = None,
        image_id: str = None,
        instance_id_list: List[str] = None,
        reset: bool = None,
    ):
        self.ignore_param_validation = ignore_param_validation
        self.image_id = image_id
        self.instance_id_list = instance_id_list
        self.reset = reset

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ignore_param_validation is not None:
            result['IgnoreParamValidation'] = self.ignore_param_validation

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.instance_id_list is not None:
            result['InstanceIdList'] = self.instance_id_list

        if self.reset is not None:
            result['Reset'] = self.reset

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IgnoreParamValidation') is not None:
            self.ignore_param_validation = m.get('IgnoreParamValidation')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('InstanceIdList') is not None:
            self.instance_id_list = m.get('InstanceIdList')

        if m.get('Reset') is not None:
            self.reset = m.get('Reset')

        return self


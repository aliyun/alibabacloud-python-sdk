# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict

from alibabacloud_dlfnext20250310 import models as main_models
from darabonba.model import DaraModel

class UpdateVpcConfigRequest(DaraModel):
    def __init__(
        self,
        removals: List[str] = None,
        updates: List[main_models.UpdateVpcConfigRequestUpdates] = None,
    ):
        # The list of VPC IDs to delete.
        self.removals = removals
        # The list of VPCs to update.
        self.updates = updates

    def validate(self):
        if self.updates:
            for v1 in self.updates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.removals is not None:
            result['removals'] = self.removals

        result['updates'] = []
        if self.updates is not None:
            for k1 in self.updates:
                result['updates'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('removals') is not None:
            self.removals = m.get('removals')

        self.updates = []
        if m.get('updates') is not None:
            for k1 in m.get('updates'):
                temp_model = main_models.UpdateVpcConfigRequestUpdates()
                self.updates.append(temp_model.from_map(k1))

        return self

class UpdateVpcConfigRequestUpdates(DaraModel):
    def __init__(
        self,
        extended_options: Dict[str, str] = None,
        vpc_id: str = None,
    ):
        # The list of configuration items.
        self.extended_options = extended_options
        # VPC ID。
        self.vpc_id = vpc_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extended_options is not None:
            result['extendedOptions'] = self.extended_options

        if self.vpc_id is not None:
            result['vpcId'] = self.vpc_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('extendedOptions') is not None:
            self.extended_options = m.get('extendedOptions')

        if m.get('vpcId') is not None:
            self.vpc_id = m.get('vpcId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_bdrc20230808 import models as main_models
from darabonba.model import DaraModel

class UpdateCrossAccountsRequest(DaraModel):
    def __init__(
        self,
        create_targets: List[main_models.UpdateCrossAccountsRequestCreateTargets] = None,
        delete_targets: List[main_models.UpdateCrossAccountsRequestDeleteTargets] = None,
    ):
        self.create_targets = create_targets
        self.delete_targets = delete_targets

    def validate(self):
        if self.create_targets:
            for v1 in self.create_targets:
                 if v1:
                    v1.validate()
        if self.delete_targets:
            for v1 in self.delete_targets:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CreateTargets'] = []
        if self.create_targets is not None:
            for k1 in self.create_targets:
                result['CreateTargets'].append(k1.to_map() if k1 else None)

        result['DeleteTargets'] = []
        if self.delete_targets is not None:
            for k1 in self.delete_targets:
                result['DeleteTargets'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.create_targets = []
        if m.get('CreateTargets') is not None:
            for k1 in m.get('CreateTargets'):
                temp_model = main_models.UpdateCrossAccountsRequestCreateTargets()
                self.create_targets.append(temp_model.from_map(k1))

        self.delete_targets = []
        if m.get('DeleteTargets') is not None:
            for k1 in m.get('DeleteTargets'):
                temp_model = main_models.UpdateCrossAccountsRequestDeleteTargets()
                self.delete_targets.append(temp_model.from_map(k1))

        return self

class UpdateCrossAccountsRequestDeleteTargets(DaraModel):
    def __init__(
        self,
        target_id: str = None,
        target_type: str = None,
    ):
        # This parameter is required.
        self.target_id = target_id
        # This parameter is required.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self

class UpdateCrossAccountsRequestCreateTargets(DaraModel):
    def __init__(
        self,
        target_id: str = None,
        target_type: str = None,
    ):
        # This parameter is required.
        self.target_id = target_id
        # This parameter is required.
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.target_id is not None:
            result['TargetId'] = self.target_id

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self


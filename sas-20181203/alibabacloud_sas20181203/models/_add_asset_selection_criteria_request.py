# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class AddAssetSelectionCriteriaRequest(DaraModel):
    def __init__(
        self,
        criteria: str = None,
        criteria_operation: str = None,
        selection_key: str = None,
        target_operation_list: List[main_models.AddAssetSelectionCriteriaRequestTargetOperationList] = None,
    ):
        # The search conditions that are used to query assets. The value of this parameter is in the JSON format and is case-sensitive.
        # 
        # > A search condition can be an instance ID, instance name, virtual private cloud (VPC) ID, region, or public IP address. You can call the [DescribeCriteria](~~DescribeCriteria~~) operation to query the supported search conditions.
        self.criteria = criteria
        # The type of the operation on search conditions. Valid values:
        # 
        # *   **add**: adds assets.
        # *   **del**: deletes assets.
        self.criteria_operation = criteria_operation
        # The unique ID of the asset.
        # 
        # This parameter is required.
        self.selection_key = selection_key
        # The list of assets.
        self.target_operation_list = target_operation_list

    def validate(self):
        if self.target_operation_list:
            for v1 in self.target_operation_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.criteria is not None:
            result['Criteria'] = self.criteria

        if self.criteria_operation is not None:
            result['CriteriaOperation'] = self.criteria_operation

        if self.selection_key is not None:
            result['SelectionKey'] = self.selection_key

        result['TargetOperationList'] = []
        if self.target_operation_list is not None:
            for k1 in self.target_operation_list:
                result['TargetOperationList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Criteria') is not None:
            self.criteria = m.get('Criteria')

        if m.get('CriteriaOperation') is not None:
            self.criteria_operation = m.get('CriteriaOperation')

        if m.get('SelectionKey') is not None:
            self.selection_key = m.get('SelectionKey')

        self.target_operation_list = []
        if m.get('TargetOperationList') is not None:
            for k1 in m.get('TargetOperationList'):
                temp_model = main_models.AddAssetSelectionCriteriaRequestTargetOperationList()
                self.target_operation_list.append(temp_model.from_map(k1))

        return self



class AddAssetSelectionCriteriaRequestTargetOperationList(DaraModel):
    def __init__(
        self,
        operation: str = None,
        target: str = None,
    ):
        # The type of the operation. Valid values:
        # 
        # *   **add**
        # *   **del**
        self.operation = operation
        # The ID of the asset.
        self.target = target

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.operation is not None:
            result['Operation'] = self.operation

        if self.target is not None:
            result['Target'] = self.target

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('Target') is not None:
            self.target = m.get('Target')

        return self


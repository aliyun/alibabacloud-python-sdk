# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class PrecheckDuckDBDependencyResponseBody(DaraModel):
    def __init__(
        self,
        failed_check_items: List[main_models.PrecheckDuckDBDependencyResponseBodyFailedCheckItems] = None,
        result: bool = None,
    ):
        # The check items that do not meet the requirements for creating DuckDB-based analytical instances.
        self.failed_check_items = failed_check_items
        # Indicates whether the primary instance meet the requirements for creating DuckDB-based analytical instances. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.result = result

    def validate(self):
        if self.failed_check_items:
            for v1 in self.failed_check_items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FailedCheckItems'] = []
        if self.failed_check_items is not None:
            for k1 in self.failed_check_items:
                result['FailedCheckItems'].append(k1.to_map() if k1 else None)

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.failed_check_items = []
        if m.get('FailedCheckItems') is not None:
            for k1 in m.get('FailedCheckItems'):
                temp_model = main_models.PrecheckDuckDBDependencyResponseBodyFailedCheckItems()
                self.failed_check_items.append(temp_model.from_map(k1))

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class PrecheckDuckDBDependencyResponseBodyFailedCheckItems(DaraModel):
    def __init__(
        self,
        allow_auto_modify: bool = None,
        current_value: str = None,
        name: str = None,
        required_value: str = None,
        type: str = None,
    ):
        # Indicates whether the item can be changed with one click to meet the requirements.
        # 
        # *   **true**: Yes. You can call the [ModifyDBInstanceConfig](https://help.aliyun.com/document_detail/2623684.html) operation to change the item with one click.
        # *   **false**: No.
        # 
        # >  If the major engine version of the primary does not meet the requirements, you must manually upgrade it.
        self.allow_auto_modify = allow_auto_modify
        # The current value of the check item.
        self.current_value = current_value
        # The name of the check item.
        self.name = name
        # The value or value range that meets the requirements.
        self.required_value = required_value
        # The check item. Valid values:
        # 
        # *   **Parameter**: The parameters of the primary instance.
        # *   **MinorVersion**: The minor engine version of the primary instance.
        # *   **MajorVersion**: The major engine version of the primary instance.
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_auto_modify is not None:
            result['AllowAutoModify'] = self.allow_auto_modify

        if self.current_value is not None:
            result['CurrentValue'] = self.current_value

        if self.name is not None:
            result['Name'] = self.name

        if self.required_value is not None:
            result['RequiredValue'] = self.required_value

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllowAutoModify') is not None:
            self.allow_auto_modify = m.get('AllowAutoModify')

        if m.get('CurrentValue') is not None:
            self.current_value = m.get('CurrentValue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RequiredValue') is not None:
            self.required_value = m.get('RequiredValue')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


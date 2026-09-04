# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Dict

from darabonba.model import DaraModel

class FieldSpec(DaraModel):
    def __init__(
        self,
        analysable: bool = None,
        data_format: str = None,
        description: str = None,
        display_name: str = None,
        filterable: bool = None,
        launch_stage: str = None,
        name: str = None,
        orderable: bool = None,
        short_description: str = None,
        type: str = None,
        unit: str = None,
        value_mapping: Dict[str, str] = None,
    ):
        # Specifies whether the field can be analyzed, that is, whether it can be used as a dimension column in a GROUP BY clause.
        self.analysable = analysable
        # The formatting method for numeric or display values, such as KMB (thousand/million/billion), percent, ms, or dthms (hours:minutes:seconds).
        self.data_format = data_format
        # The business description of the field.
        self.description = description
        # The display name used in the console. The value can contain Chinese characters.
        self.display_name = display_name
        # Specifies whether the field can be filtered, that is, whether index-based filter queries are supported.
        self.filterable = filterable
        # The launch stage of the field. Valid values: preview, beta, ga, and deprecated.
        self.launch_stage = launch_stage
        # The field name. The value must consist of lowercase letters, digits, hyphens (-), underscores (_), and periods (.).
        self.name = name
        # Specifies whether the field can be sorted.
        self.orderable = orderable
        # The short description (one sentence) used in compact display scenarios such as lists.
        self.short_description = short_description
        # The field type. Valid values: string, integer, float, boolean, time, json_object, and json_array.
        self.type = type
        # The unit of the field. The unit is used only for display purposes and is not automatically converted. For example, ms is not automatically converted to s.
        self.unit = unit
        # The value mapping for enumerated values. The key is the raw value and the value is the mapped semantic name. This is used to display the business meaning of enumerated values. For example, the value 1 of the status field is mapped to running.
        self.value_mapping = value_mapping

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.analysable is not None:
            result['analysable'] = self.analysable

        if self.data_format is not None:
            result['data_format'] = self.data_format

        if self.description is not None:
            result['description'] = self.description

        if self.display_name is not None:
            result['display_name'] = self.display_name

        if self.filterable is not None:
            result['filterable'] = self.filterable

        if self.launch_stage is not None:
            result['launch_stage'] = self.launch_stage

        if self.name is not None:
            result['name'] = self.name

        if self.orderable is not None:
            result['orderable'] = self.orderable

        if self.short_description is not None:
            result['short_description'] = self.short_description

        if self.type is not None:
            result['type'] = self.type

        if self.unit is not None:
            result['unit'] = self.unit

        if self.value_mapping is not None:
            result['value_mapping'] = self.value_mapping

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('analysable') is not None:
            self.analysable = m.get('analysable')

        if m.get('data_format') is not None:
            self.data_format = m.get('data_format')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('display_name') is not None:
            self.display_name = m.get('display_name')

        if m.get('filterable') is not None:
            self.filterable = m.get('filterable')

        if m.get('launch_stage') is not None:
            self.launch_stage = m.get('launch_stage')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('orderable') is not None:
            self.orderable = m.get('orderable')

        if m.get('short_description') is not None:
            self.short_description = m.get('short_description')

        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('unit') is not None:
            self.unit = m.get('unit')

        if m.get('value_mapping') is not None:
            self.value_mapping = m.get('value_mapping')

        return self


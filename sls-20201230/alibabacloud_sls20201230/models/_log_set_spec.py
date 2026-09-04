# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sls20201230 import models as main_models
from darabonba.model import DaraModel

class LogSetSpec(DaraModel):
    def __init__(
        self,
        default_order: str = None,
        fields: List[main_models.FieldSpec] = None,
        hidden_fields: List[str] = None,
        name_fields: List[str] = None,
        ordered_fields: List[str] = None,
        tag_fields: List[str] = None,
        time_field: str = None,
    ):
        # The default sort direction. Valid values:
        # - asc: ascending order.
        # - desc: descending order.
        # 
        # Default value: asc.
        self.default_order = default_order
        # The list of fields.
        self.fields = fields
        # The list of hidden fields. These fields are not displayed in the interface by default.
        self.hidden_fields = hidden_fields
        # The list of Displayed Fields, in sorting order by display priority.
        self.name_fields = name_fields
        # The list of sort fields, used for default sorting.
        self.ordered_fields = ordered_fields
        # The list of tag fields. Tag fields are aggregated together for display and analysis by default.
        self.tag_fields = tag_fields
        # The name of the time field. The field must be of the timestamp type and supports seconds, milliseconds, microseconds, and nanoseconds.
        self.time_field = time_field

    def validate(self):
        if self.fields:
            for v1 in self.fields:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_order is not None:
            result['default_order'] = self.default_order

        result['fields'] = []
        if self.fields is not None:
            for k1 in self.fields:
                result['fields'].append(k1.to_map() if k1 else None)

        if self.hidden_fields is not None:
            result['hidden_fields'] = self.hidden_fields

        if self.name_fields is not None:
            result['name_fields'] = self.name_fields

        if self.ordered_fields is not None:
            result['ordered_fields'] = self.ordered_fields

        if self.tag_fields is not None:
            result['tag_fields'] = self.tag_fields

        if self.time_field is not None:
            result['time_field'] = self.time_field

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('default_order') is not None:
            self.default_order = m.get('default_order')

        self.fields = []
        if m.get('fields') is not None:
            for k1 in m.get('fields'):
                temp_model = main_models.FieldSpec()
                self.fields.append(temp_model.from_map(k1))

        if m.get('hidden_fields') is not None:
            self.hidden_fields = m.get('hidden_fields')

        if m.get('name_fields') is not None:
            self.name_fields = m.get('name_fields')

        if m.get('ordered_fields') is not None:
            self.ordered_fields = m.get('ordered_fields')

        if m.get('tag_fields') is not None:
            self.tag_fields = m.get('tag_fields')

        if m.get('time_field') is not None:
            self.time_field = m.get('time_field')

        return self


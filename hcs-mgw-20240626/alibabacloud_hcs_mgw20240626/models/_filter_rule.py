# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_hcs_mgw20240626 import models as main_models
from darabonba.model import DaraModel

class FilterRule(DaraModel):
    def __init__(
        self,
        file_type_filters: main_models.FileTypeFilters = None,
        key_filters: main_models.KeyFilters = None,
        last_modified_filters: main_models.LastModifiedFilters = None,
    ):
        self.file_type_filters = file_type_filters
        self.key_filters = key_filters
        self.last_modified_filters = last_modified_filters

    def validate(self):
        if self.file_type_filters:
            self.file_type_filters.validate()
        if self.key_filters:
            self.key_filters.validate()
        if self.last_modified_filters:
            self.last_modified_filters.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_type_filters is not None:
            result['FileTypeFilters'] = self.file_type_filters.to_map()

        if self.key_filters is not None:
            result['KeyFilters'] = self.key_filters.to_map()

        if self.last_modified_filters is not None:
            result['LastModifiedFilters'] = self.last_modified_filters.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileTypeFilters') is not None:
            temp_model = main_models.FileTypeFilters()
            self.file_type_filters = temp_model.from_map(m.get('FileTypeFilters'))

        if m.get('KeyFilters') is not None:
            temp_model = main_models.KeyFilters()
            self.key_filters = temp_model.from_map(m.get('KeyFilters'))

        if m.get('LastModifiedFilters') is not None:
            temp_model = main_models.LastModifiedFilters()
            self.last_modified_filters = temp_model.from_map(m.get('LastModifiedFilters'))

        return self


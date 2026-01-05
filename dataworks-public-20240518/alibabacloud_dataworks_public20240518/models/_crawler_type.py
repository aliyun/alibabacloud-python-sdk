# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20240518 import models as main_models
from darabonba.model import DaraModel

class CrawlerType(DaraModel):
    def __init__(
        self,
        display_name: str = None,
        supported_entity_types: List[main_models.CrawlerTypeSupportedEntityTypes] = None,
        type: str = None,
    ):
        self.display_name = display_name
        self.supported_entity_types = supported_entity_types
        self.type = type

    def validate(self):
        if self.supported_entity_types:
            for v1 in self.supported_entity_types:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.display_name is not None:
            result['DisplayName'] = self.display_name

        result['SupportedEntityTypes'] = []
        if self.supported_entity_types is not None:
            for k1 in self.supported_entity_types:
                result['SupportedEntityTypes'].append(k1.to_map() if k1 else None)

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')

        self.supported_entity_types = []
        if m.get('SupportedEntityTypes') is not None:
            for k1 in m.get('SupportedEntityTypes'):
                temp_model = main_models.CrawlerTypeSupportedEntityTypes()
                self.supported_entity_types.append(temp_model.from_map(k1))

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class CrawlerTypeSupportedEntityTypes(DaraModel):
    def __init__(
        self,
        optional: bool = None,
        parent_sub_type: str = None,
        sub_type: str = None,
        type: str = None,
    ):
        self.optional = optional
        self.parent_sub_type = parent_sub_type
        self.sub_type = sub_type
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.optional is not None:
            result['Optional'] = self.optional

        if self.parent_sub_type is not None:
            result['ParentSubType'] = self.parent_sub_type

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Optional') is not None:
            self.optional = m.get('Optional')

        if m.get('ParentSubType') is not None:
            self.parent_sub_type = m.get('ParentSubType')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


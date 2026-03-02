# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ververica20220718 import models as main_models
from darabonba.model import DaraModel

class Connector(DaraModel):
    def __init__(
        self,
        creator: str = None,
        creator_name: str = None,
        dependencies: List[str] = None,
        lookup: bool = None,
        modifier: str = None,
        modifier_name: str = None,
        name: str = None,
        properties: List[main_models.Property] = None,
        sink: bool = None,
        source: bool = None,
        supported_formats: List[str] = None,
        type: str = None,
    ):
        # The ID of the user who creates the connector.
        self.creator = creator
        # The nickname of the user who creates the connector.
        self.creator_name = creator_name
        # The additional dependency files.
        self.dependencies = dependencies
        # Indicates whether the connector can be used as a lookup table.
        self.lookup = lookup
        # The ID of the user who modifies the connector.
        self.modifier = modifier
        # The nickname of the user who modifies the connector.
        self.modifier_name = modifier_name
        # The name of the connector.
        self.name = name
        # The parameter configurations.
        self.properties = properties
        # Indicates whether the connector can be used as the sink.
        self.sink = sink
        # Indicates whether the connector can be used as the source.
        self.source = source
        # The array of formats that are supported by the connector.
        self.supported_formats = supported_formats
        # The type of the connector.
        self.type = type

    def validate(self):
        if self.properties:
            for v1 in self.properties:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['creator'] = self.creator

        if self.creator_name is not None:
            result['creatorName'] = self.creator_name

        if self.dependencies is not None:
            result['dependencies'] = self.dependencies

        if self.lookup is not None:
            result['lookup'] = self.lookup

        if self.modifier is not None:
            result['modifier'] = self.modifier

        if self.modifier_name is not None:
            result['modifierName'] = self.modifier_name

        if self.name is not None:
            result['name'] = self.name

        result['properties'] = []
        if self.properties is not None:
            for k1 in self.properties:
                result['properties'].append(k1.to_map() if k1 else None)

        if self.sink is not None:
            result['sink'] = self.sink

        if self.source is not None:
            result['source'] = self.source

        if self.supported_formats is not None:
            result['supportedFormats'] = self.supported_formats

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('creator') is not None:
            self.creator = m.get('creator')

        if m.get('creatorName') is not None:
            self.creator_name = m.get('creatorName')

        if m.get('dependencies') is not None:
            self.dependencies = m.get('dependencies')

        if m.get('lookup') is not None:
            self.lookup = m.get('lookup')

        if m.get('modifier') is not None:
            self.modifier = m.get('modifier')

        if m.get('modifierName') is not None:
            self.modifier_name = m.get('modifierName')

        if m.get('name') is not None:
            self.name = m.get('name')

        self.properties = []
        if m.get('properties') is not None:
            for k1 in m.get('properties'):
                temp_model = main_models.Property()
                self.properties.append(temp_model.from_map(k1))

        if m.get('sink') is not None:
            self.sink = m.get('sink')

        if m.get('source') is not None:
            self.source = m.get('source')

        if m.get('supportedFormats') is not None:
            self.supported_formats = m.get('supportedFormats')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self


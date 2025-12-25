# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dms_enterprise20181101 import models as main_models
from darabonba.model import DaraModel

class DLFunctionInput(DaraModel):
    def __init__(
        self,
        class_name: str = None,
        create_time: int = None,
        creator_id: int = None,
        function_name: str = None,
        function_type: str = None,
        modifier_id: int = None,
        owner_name: str = None,
        owner_type: str = None,
        resource_uris: List[main_models.DLResourceUri] = None,
    ):
        self.class_name = class_name
        self.create_time = create_time
        self.creator_id = creator_id
        self.function_name = function_name
        self.function_type = function_type
        self.modifier_id = modifier_id
        self.owner_name = owner_name
        self.owner_type = owner_type
        self.resource_uris = resource_uris

    def validate(self):
        if self.resource_uris:
            for v1 in self.resource_uris:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.class_name is not None:
            result['ClassName'] = self.class_name

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator_id is not None:
            result['CreatorId'] = self.creator_id

        if self.function_name is not None:
            result['FunctionName'] = self.function_name

        if self.function_type is not None:
            result['FunctionType'] = self.function_type

        if self.modifier_id is not None:
            result['ModifierId'] = self.modifier_id

        if self.owner_name is not None:
            result['OwnerName'] = self.owner_name

        if self.owner_type is not None:
            result['OwnerType'] = self.owner_type

        result['ResourceUris'] = []
        if self.resource_uris is not None:
            for k1 in self.resource_uris:
                result['ResourceUris'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ClassName') is not None:
            self.class_name = m.get('ClassName')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatorId') is not None:
            self.creator_id = m.get('CreatorId')

        if m.get('FunctionName') is not None:
            self.function_name = m.get('FunctionName')

        if m.get('FunctionType') is not None:
            self.function_type = m.get('FunctionType')

        if m.get('ModifierId') is not None:
            self.modifier_id = m.get('ModifierId')

        if m.get('OwnerName') is not None:
            self.owner_name = m.get('OwnerName')

        if m.get('OwnerType') is not None:
            self.owner_type = m.get('OwnerType')

        self.resource_uris = []
        if m.get('ResourceUris') is not None:
            for k1 in m.get('ResourceUris'):
                temp_model = main_models.DLResourceUri()
                self.resource_uris.append(temp_model.from_map(k1))

        return self


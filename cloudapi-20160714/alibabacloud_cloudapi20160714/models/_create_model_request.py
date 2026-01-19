# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cloudapi20160714 import models as main_models
from darabonba.model import DaraModel

class CreateModelRequest(DaraModel):
    def __init__(
        self,
        description: str = None,
        group_id: str = None,
        model_name: str = None,
        schema: str = None,
        tag: List[main_models.CreateModelRequestTag] = None,
    ):
        # The description of the model definition.
        self.description = description
        # The ID of the API group to which the model belongs.
        # 
        # This parameter is required.
        self.group_id = group_id
        # The name of the model. The name must be unique within the group.
        # 
        # This parameter is required.
        self.model_name = model_name
        # The definition of the model in JSON Schema.
        # 
        # This parameter is required.
        self.schema = schema
        # The object tags that match the lifecycle rule. You can specify multiple tags.
        self.tag = tag

    def validate(self):
        if self.tag:
            for v1 in self.tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.schema is not None:
            result['Schema'] = self.schema

        result['Tag'] = []
        if self.tag is not None:
            for k1 in self.tag:
                result['Tag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        self.tag = []
        if m.get('Tag') is not None:
            for k1 in m.get('Tag'):
                temp_model = main_models.CreateModelRequestTag()
                self.tag.append(temp_model.from_map(k1))

        return self

class CreateModelRequestTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The key of the tag.
        self.key = key
        # The values of the tag.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


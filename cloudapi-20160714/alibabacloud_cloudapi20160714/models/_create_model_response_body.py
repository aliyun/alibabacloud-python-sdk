# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateModelResponseBody(DaraModel):
    def __init__(
        self,
        created_time: str = None,
        description: str = None,
        group_id: str = None,
        model_id: str = None,
        model_name: str = None,
        model_ref: str = None,
        modified_time: str = None,
        region_id: str = None,
        request_id: str = None,
        schema: str = None,
    ):
        # The time when the model was created.
        self.created_time = created_time
        # The description of the created model.
        self.description = description
        # The ID of the API group to which the created model belongs.
        self.group_id = group_id
        # The ID of the created model.
        self.model_id = model_id
        # The name of the created model.
        self.model_name = model_name
        # The URI of the created model.
        self.model_ref = model_ref
        # The time when the model is last modified.
        self.modified_time = modified_time
        # The region to which the created model belongs.
        self.region_id = region_id
        # The ID of the request.
        self.request_id = request_id
        # The definition of the created model.
        self.schema = schema

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.description is not None:
            result['Description'] = self.description

        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.model_ref is not None:
            result['ModelRef'] = self.model_ref

        if self.modified_time is not None:
            result['ModifiedTime'] = self.modified_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.schema is not None:
            result['Schema'] = self.schema

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('ModelRef') is not None:
            self.model_ref = m.get('ModelRef')

        if m.get('ModifiedTime') is not None:
            self.modified_time = m.get('ModifiedTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        return self


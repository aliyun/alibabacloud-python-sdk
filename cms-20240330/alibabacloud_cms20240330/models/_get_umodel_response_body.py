# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_cms20240330 import models as main_models
from darabonba.model import DaraModel

class GetUmodelResponseBody(DaraModel):
    def __init__(
        self,
        common_schema_ref: List[main_models.GetUmodelResponseBodyCommonSchemaRef] = None,
        description: str = None,
        region_id: str = None,
        request_id: str = None,
        workspace: str = None,
    ):
        # This parameter is reserved.
        self.common_schema_ref = common_schema_ref
        # The Umodel description.
        self.description = description
        # The region of the resource.
        self.region_id = region_id
        # The request ID.
        self.request_id = request_id
        # The workspace name.
        self.workspace = workspace

    def validate(self):
        if self.common_schema_ref:
            for v1 in self.common_schema_ref:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['commonSchemaRef'] = []
        if self.common_schema_ref is not None:
            for k1 in self.common_schema_ref:
                result['commonSchemaRef'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['description'] = self.description

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.workspace is not None:
            result['workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.common_schema_ref = []
        if m.get('commonSchemaRef') is not None:
            for k1 in m.get('commonSchemaRef'):
                temp_model = main_models.GetUmodelResponseBodyCommonSchemaRef()
                self.common_schema_ref.append(temp_model.from_map(k1))

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('workspace') is not None:
            self.workspace = m.get('workspace')

        return self

class GetUmodelResponseBodyCommonSchemaRef(DaraModel):
    def __init__(
        self,
        group: str = None,
        version: str = None,
    ):
        # The public Umodel schema group.
        self.group = group
        # The version.
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group is not None:
            result['group'] = self.group

        if self.version is not None:
            result['version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('group') is not None:
            self.group = m.get('group')

        if m.get('version') is not None:
            self.version = m.get('version')

        return self


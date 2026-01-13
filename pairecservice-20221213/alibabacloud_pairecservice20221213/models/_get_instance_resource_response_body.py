# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetInstanceResourceResponseBody(DaraModel):
    def __init__(
        self,
        category: str = None,
        config: str = None,
        gmt_create_time: str = None,
        gmt_modified_time: str = None,
        group: str = None,
        request_id: str = None,
        resource_id: str = None,
        type: str = None,
        uri: str = None,
    ):
        self.category = category
        self.config = config
        self.gmt_create_time = gmt_create_time
        self.gmt_modified_time = gmt_modified_time
        self.group = group
        self.request_id = request_id
        self.resource_id = resource_id
        self.type = type
        self.uri = uri

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.config is not None:
            result['Config'] = self.config

        if self.gmt_create_time is not None:
            result['GmtCreateTime'] = self.gmt_create_time

        if self.gmt_modified_time is not None:
            result['GmtModifiedTime'] = self.gmt_modified_time

        if self.group is not None:
            result['Group'] = self.group

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.type is not None:
            result['Type'] = self.type

        if self.uri is not None:
            result['Uri'] = self.uri

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('Config') is not None:
            self.config = m.get('Config')

        if m.get('GmtCreateTime') is not None:
            self.gmt_create_time = m.get('GmtCreateTime')

        if m.get('GmtModifiedTime') is not None:
            self.gmt_modified_time = m.get('GmtModifiedTime')

        if m.get('Group') is not None:
            self.group = m.get('Group')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        return self


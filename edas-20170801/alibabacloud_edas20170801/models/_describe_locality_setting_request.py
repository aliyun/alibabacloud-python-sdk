# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DescribeLocalitySettingRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        namespace_id: str = None,
        region: str = None,
    ):
        # The ID of the application. To obtain the application ID, call the ListApplication operation. For more information, see [ListApplication](https://help.aliyun.com/document_detail/423162.html).
        # 
        # This parameter is required.
        self.app_id = app_id
        # The ID of the microservices namespace.
        # 
        # This parameter is required.
        self.namespace_id = namespace_id
        # The ID of the region.
        # 
        # This parameter is required.
        self.region = region

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.namespace_id is not None:
            result['NamespaceId'] = self.namespace_id

        if self.region is not None:
            result['Region'] = self.region

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('NamespaceId') is not None:
            self.namespace_id = m.get('NamespaceId')

        if m.get('Region') is not None:
            self.region = m.get('Region')

        return self


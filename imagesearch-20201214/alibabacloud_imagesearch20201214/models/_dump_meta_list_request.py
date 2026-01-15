# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DumpMetaListRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the export task.
        self.id = id
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The number of the page to return. Default value: 1.
        self.page_number = page_number
        # The number of images to return on each page. Default value: 10.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


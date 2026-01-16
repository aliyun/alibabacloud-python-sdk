# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListInstanceIndicesRequest(DaraModel):
    def __init__(
        self,
        all: bool = None,
        is_managed: bool = None,
        is_openstore: bool = None,
        name: str = None,
        page: int = None,
        size: int = None,
    ):
        # false
        self.all = all
        # 15
        self.is_managed = is_managed
        # The ID of the request.
        self.is_openstore = is_openstore
        # 1
        self.name = name
        # The header of the response.
        self.page = page
        # The total size of the index in Cloud Hosting. Unit: bytes.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all is not None:
            result['all'] = self.all

        if self.is_managed is not None:
            result['isManaged'] = self.is_managed

        if self.is_openstore is not None:
            result['isOpenstore'] = self.is_openstore

        if self.name is not None:
            result['name'] = self.name

        if self.page is not None:
            result['page'] = self.page

        if self.size is not None:
            result['size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('all') is not None:
            self.all = m.get('all')

        if m.get('isManaged') is not None:
            self.is_managed = m.get('isManaged')

        if m.get('isOpenstore') is not None:
            self.is_openstore = m.get('isOpenstore')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('page') is not None:
            self.page = m.get('page')

        if m.get('size') is not None:
            self.size = m.get('size')

        return self


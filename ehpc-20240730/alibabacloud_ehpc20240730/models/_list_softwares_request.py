# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ehpc20240730 import models as main_models
from darabonba.model import DaraModel

class ListSoftwaresRequest(DaraModel):
    def __init__(
        self,
        category: str = None,
        cluster_id: str = None,
        name: str = None,
        os_infos: List[main_models.ListSoftwaresRequestOsInfos] = None,
        page_number: str = None,
        page_size: str = None,
    ):
        # The application category.
        self.category = category
        # The cluster ID.
        self.cluster_id = cluster_id
        # The software name.
        self.name = name
        # The operating system (OS) information.
        self.os_infos = os_infos
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size

    def validate(self):
        if self.os_infos:
            for v1 in self.os_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category is not None:
            result['Category'] = self.category

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.name is not None:
            result['Name'] = self.name

        result['OsInfos'] = []
        if self.os_infos is not None:
            for k1 in self.os_infos:
                result['OsInfos'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        self.os_infos = []
        if m.get('OsInfos') is not None:
            for k1 in m.get('OsInfos'):
                temp_model = main_models.ListSoftwaresRequestOsInfos()
                self.os_infos.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self

class ListSoftwaresRequestOsInfos(DaraModel):
    def __init__(
        self,
        architecture: str = None,
        os_tag: str = None,
    ):
        # The OS architecture. Valid values:
        # 
        # *   x86_64
        # *   arm64
        self.architecture = architecture
        # The image tag.
        self.os_tag = os_tag

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.architecture is not None:
            result['Architecture'] = self.architecture

        if self.os_tag is not None:
            result['OsTag'] = self.os_tag

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Architecture') is not None:
            self.architecture = m.get('Architecture')

        if m.get('OsTag') is not None:
            self.os_tag = m.get('OsTag')

        return self


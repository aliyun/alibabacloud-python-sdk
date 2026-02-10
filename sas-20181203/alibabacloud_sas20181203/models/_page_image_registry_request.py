# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class PageImageRegistryRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        registry_name_like: str = None,
        registry_type_in_list: List[str] = None,
        registry_type_not_in_list: List[str] = None,
        source_ip: str = None,
    ):
        # The number of the page to return.
        self.current_page = current_page
        # The number of entries to return on each page. Default value: 20.
        self.page_size = page_size
        # The name of the image repository. Fuzzy match is supported.
        self.registry_name_like = registry_name_like
        # The types of image repositories.
        self.registry_type_in_list = registry_type_in_list
        # The types of excluded image repositories.
        self.registry_type_not_in_list = registry_type_not_in_list
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.registry_name_like is not None:
            result['RegistryNameLike'] = self.registry_name_like

        if self.registry_type_in_list is not None:
            result['RegistryTypeInList'] = self.registry_type_in_list

        if self.registry_type_not_in_list is not None:
            result['RegistryTypeNotInList'] = self.registry_type_not_in_list

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegistryNameLike') is not None:
            self.registry_name_like = m.get('RegistryNameLike')

        if m.get('RegistryTypeInList') is not None:
            self.registry_type_in_list = m.get('RegistryTypeInList')

        if m.get('RegistryTypeNotInList') is not None:
            self.registry_type_not_in_list = m.get('RegistryTypeNotInList')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self


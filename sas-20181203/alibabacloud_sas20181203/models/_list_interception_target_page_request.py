# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListInterceptionTargetPageRequest(DaraModel):
    def __init__(
        self,
        app_name: str = None,
        current_page: int = None,
        image_list: List[str] = None,
        namespace: str = None,
        page_size: int = None,
        tag_list: List[str] = None,
        target_name: str = None,
        target_type: str = None,
    ):
        # The name of the application to which the network object belongs.
        self.app_name = app_name
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The images of the network object.
        self.image_list = image_list
        # The namespace to which the network object belongs.
        self.namespace = namespace
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The labels specified for the network object.
        self.tag_list = tag_list
        # The name of the network object.
        self.target_name = target_name
        # The type of the network object. Valid values:
        # 
        # *   IMAGE
        self.target_type = target_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.image_list is not None:
            result['ImageList'] = self.image_list

        if self.namespace is not None:
            result['Namespace'] = self.namespace

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.tag_list is not None:
            result['TagList'] = self.tag_list

        if self.target_name is not None:
            result['TargetName'] = self.target_name

        if self.target_type is not None:
            result['TargetType'] = self.target_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('ImageList') is not None:
            self.image_list = m.get('ImageList')

        if m.get('Namespace') is not None:
            self.namespace = m.get('Namespace')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TagList') is not None:
            self.tag_list = m.get('TagList')

        if m.get('TargetName') is not None:
            self.target_name = m.get('TargetName')

        if m.get('TargetType') is not None:
            self.target_type = m.get('TargetType')

        return self


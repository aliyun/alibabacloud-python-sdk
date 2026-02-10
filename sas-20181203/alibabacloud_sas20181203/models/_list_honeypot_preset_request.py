# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListHoneypotPresetRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        honeypot_image_name: str = None,
        lang: str = None,
        node_id: str = None,
        node_name: str = None,
        page_size: int = None,
        preset_name: str = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # The name of the honeypot image.
        self.honeypot_image_name = honeypot_image_name
        # The language of the content within the request and response. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # The ID of the management node.
        self.node_id = node_id
        # The name of the management node.
        self.node_name = node_name
        # The number of entries to return on each page. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size
        # The custom name of the honeypot template.
        self.preset_name = preset_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.honeypot_image_name is not None:
            result['HoneypotImageName'] = self.honeypot_image_name

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.node_name is not None:
            result['NodeName'] = self.node_name

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.preset_name is not None:
            result['PresetName'] = self.preset_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('HoneypotImageName') is not None:
            self.honeypot_image_name = m.get('HoneypotImageName')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('NodeName') is not None:
            self.node_name = m.get('NodeName')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('PresetName') is not None:
            self.preset_name = m.get('PresetName')

        return self


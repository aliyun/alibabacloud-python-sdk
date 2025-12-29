# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sae20190506 import models as main_models
from darabonba.model import DaraModel

class Submenu(DaraModel):
    def __init__(
        self,
        items: List[main_models.SubmenuItems] = None,
        submenu_desc: str = None,
        submenu_type: str = None,
        submenus: List[main_models.Submenu] = None,
    ):
        self.items = items
        self.submenu_desc = submenu_desc
        self.submenu_type = submenu_type
        self.submenus = submenus

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.submenus:
            for v1 in self.submenus:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.submenu_desc is not None:
            result['SubmenuDesc'] = self.submenu_desc

        if self.submenu_type is not None:
            result['SubmenuType'] = self.submenu_type

        result['Submenus'] = []
        if self.submenus is not None:
            for k1 in self.submenus:
                result['Submenus'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.SubmenuItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('SubmenuDesc') is not None:
            self.submenu_desc = m.get('SubmenuDesc')

        if m.get('SubmenuType') is not None:
            self.submenu_type = m.get('SubmenuType')

        self.submenus = []
        if m.get('Submenus') is not None:
            for k1 in m.get('Submenus'):
                temp_model = main_models.Submenu()
                self.submenus.append(temp_model.from_map(k1))

        return self

class SubmenuItems(DaraModel):
    def __init__(
        self,
        default_selected: bool = None,
        item_desc: str = None,
        item_type: str = None,
        relating_items: List[str] = None,
    ):
        self.default_selected = default_selected
        self.item_desc = item_desc
        self.item_type = item_type
        self.relating_items = relating_items

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_selected is not None:
            result['DefaultSelected'] = self.default_selected

        if self.item_desc is not None:
            result['ItemDesc'] = self.item_desc

        if self.item_type is not None:
            result['ItemType'] = self.item_type

        if self.relating_items is not None:
            result['RelatingItems'] = self.relating_items

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultSelected') is not None:
            self.default_selected = m.get('DefaultSelected')

        if m.get('ItemDesc') is not None:
            self.item_desc = m.get('ItemDesc')

        if m.get('ItemType') is not None:
            self.item_type = m.get('ItemType')

        if m.get('RelatingItems') is not None:
            self.relating_items = m.get('RelatingItems')

        return self


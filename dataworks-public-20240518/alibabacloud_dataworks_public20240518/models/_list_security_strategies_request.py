# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListSecurityStrategiesRequest(DaraModel):
    def __init__(
        self,
        control_module: str = None,
        control_sub_module: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # **The control module.**
        self.control_module = control_module
        # **The control submodule.**
        self.control_sub_module = control_sub_module
        # The page number. Starts from 1. Default: 1.
        self.page_number = page_number
        # The number of entries per page. Default: 20.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.control_module is not None:
            result['ControlModule'] = self.control_module

        if self.control_sub_module is not None:
            result['ControlSubModule'] = self.control_sub_module

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ControlModule') is not None:
            self.control_module = m.get('ControlModule')

        if m.get('ControlSubModule') is not None:
            self.control_sub_module = m.get('ControlSubModule')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


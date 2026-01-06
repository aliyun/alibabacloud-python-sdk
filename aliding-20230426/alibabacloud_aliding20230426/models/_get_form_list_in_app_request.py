# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetFormListInAppRequest(DaraModel):
    def __init__(
        self,
        app_type: str = None,
        form_types: str = None,
        page_number: int = None,
        page_size: int = None,
        system_token: str = None,
    ):
        # This parameter is required.
        self.app_type = app_type
        self.form_types = form_types
        self.page_number = page_number
        self.page_size = page_size
        # This parameter is required.
        self.system_token = system_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_type is not None:
            result['AppType'] = self.app_type

        if self.form_types is not None:
            result['FormTypes'] = self.form_types

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.system_token is not None:
            result['SystemToken'] = self.system_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppType') is not None:
            self.app_type = m.get('AppType')

        if m.get('FormTypes') is not None:
            self.form_types = m.get('FormTypes')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('SystemToken') is not None:
            self.system_token = m.get('SystemToken')

        return self


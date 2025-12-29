# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListAppServicesPageRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        page_number: int = None,
        page_size: int = None,
        service_type: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The page number of the returned page.
        self.page_number = page_number
        # The number of entries returned on each page. Valid values: 0 to 9999.
        self.page_size = page_size
        # The service type. Valid values:
        # 
        # *   **dubbo**
        # *   **springCloud**
        # 
        # This parameter is required.
        self.service_type = service_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.service_type is not None:
            result['ServiceType'] = self.service_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('ServiceType') is not None:
            self.service_type = m.get('ServiceType')

        return self


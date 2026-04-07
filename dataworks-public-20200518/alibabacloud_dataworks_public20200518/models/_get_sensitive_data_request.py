# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetSensitiveDataRequest(DaraModel):
    def __init__(
        self,
        name: str = None,
        page_no: int = None,
        page_size: int = None,
    ):
        # The parameters that you can configure to query the access records. Valid values:
        # 
        # *   dbType
        # *   instanceName
        # *   databaseName
        # *   projectName
        # *   clusterName
        # 
        # The sample value shows the parameters configured to query the access records of the sensitive data in the abc database of the Hologres instance ABC. You must configure the parameters based on the compute engine that you use in your business.
        # 
        # This parameter is required.
        self.name = name
        # The page number. Pages start from page 1.
        # 
        # This parameter is required.
        self.page_no = page_no
        # The number of entries per page. Maximum value: 1000.
        # 
        # This parameter is required.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.page_no is not None:
            result['PageNo'] = self.page_no

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PageNo') is not None:
            self.page_no = m.get('PageNo')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


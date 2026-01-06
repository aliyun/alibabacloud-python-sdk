# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCertWarehouseRequest(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        instance_id: str = None,
        name: str = None,
        show_size: int = None,
        type: str = None,
    ):
        # The number of the page to return. Default value: 1.
        self.current_page = current_page
        # The instance ID of the certificate application repository.
        self.instance_id = instance_id
        # The name of the certificate application repository. Fuzzy match is supported.
        self.name = name
        # The number of entries to return on each page. Default value: 50.
        self.show_size = show_size
        # The type of the certificate application repository. Valid values:
        # 
        # *   **ssl**: certificate application repository of SSL certificates
        # *   **uploadPCA**: certificate application repository of uploaded private certificates
        # *   **free**: certificate application repository of free certificates, available only on the China site (aliyun.com)
        # *   **aliyunPCA**: certificate application repository of private certificates purchased from Alibaba Cloud Private Certificate Authority (PCA), available only on the China site (aliyun.com)
        # *   **disable**: disabled certificate application repository
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.name is not None:
            result['Name'] = self.name

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


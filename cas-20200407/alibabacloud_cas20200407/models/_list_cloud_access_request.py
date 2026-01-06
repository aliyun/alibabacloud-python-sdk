# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ListCloudAccessRequest(DaraModel):
    def __init__(
        self,
        cloud_name: str = None,
        current_page: int = None,
        secret_id: str = None,
        show_size: int = None,
    ):
        # The cloud service provider. Set the value to **Tencent**, which indicates Tencent Cloud.
        self.cloud_name = cloud_name
        # The page number. Default value: 1.
        self.current_page = current_page
        # The AccessKey ID that is used to access cloud resources.
        self.secret_id = secret_id
        # The number of entries per page. Valid values: **10**, **20**, and **50**.
        self.show_size = show_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_name is not None:
            result['CloudName'] = self.cloud_name

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.secret_id is not None:
            result['SecretId'] = self.secret_id

        if self.show_size is not None:
            result['ShowSize'] = self.show_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudName') is not None:
            self.cloud_name = m.get('CloudName')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('SecretId') is not None:
            self.secret_id = m.get('SecretId')

        if m.get('ShowSize') is not None:
            self.show_size = m.get('ShowSize')

        return self


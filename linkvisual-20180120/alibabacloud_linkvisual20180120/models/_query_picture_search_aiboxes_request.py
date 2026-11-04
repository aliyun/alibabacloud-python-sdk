# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class QueryPictureSearchAiboxesRequest(DaraModel):
    def __init__(
        self,
        app_instance_id: str = None,
        current_page: int = None,
        iot_instance_id: str = None,
        page_size: int = None,
    ):
        # Instance ID of the image search application instance. You can call the [QueryPictureSearchApps](https://help.aliyun.com/document_detail/206608.html) operation to query instance ID.
        # 
        # This parameter is required.
        self.app_instance_id = app_instance_id
        # The page number. Minimum value: 1.
        # 
        # This parameter is required.
        self.current_page = current_page
        # The ID of the instance. 
        # 
        # You can view the instance ID on the **Instance Overview** page in the IoT Platform console.
        # 
        # > If a public instance does not have an ID, see [How to obtain an instance ID](https://help.aliyun.com/document_detail/267533.html).
        self.iot_instance_id = iot_instance_id
        # The number of entries to return on each page. Valid values: 1 to 30. Default value: 10.
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
        if self.app_instance_id is not None:
            result['AppInstanceId'] = self.app_instance_id

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.iot_instance_id is not None:
            result['IotInstanceId'] = self.iot_instance_id

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppInstanceId') is not None:
            self.app_instance_id = m.get('AppInstanceId')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('IotInstanceId') is not None:
            self.iot_instance_id = m.get('IotInstanceId')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


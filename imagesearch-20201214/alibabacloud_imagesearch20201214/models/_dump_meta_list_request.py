# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class DumpMetaListRequest(DaraModel):
    def __init__(
        self,
        id: int = None,
        instance_name: str = None,
        page_number: int = None,
        page_size: int = None,
    ):
        # The ID of the metadata export task.
        # >To obtain the export task ID, call the [metadata export](https://help.aliyun.com/document_detail/377466.html) operation first and retrieve the ID from the response.
        self.id = id
        # The name of the Image Search instance. The name can be up to 20 characters in length.
        # If you have purchased an Image Search instance, log on to the [Image Search console](https://imagesearch.console.aliyun.com/) to view the instance name.
        # If you have not purchased an Image Search instance, refer to [Activate the service](https://help.aliyun.com/document_detail/179178.html) and [Create an instance](https://help.aliyun.com/document_detail/66569.html).
        # >The instance name is not the instance ID. The instance name must be unique within the same region. Make sure you distinguish between the two.
        # 
        # This parameter is required.
        self.instance_name = instance_name
        # The page number of the returned results. Default value: 1. Maximum value: 30.
        self.page_number = page_number
        # The number of entries to return. Default value: 10. Maximum value: 30.
        self.page_size = page_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        return self


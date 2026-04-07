# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataworks_public20200518 import models as main_models
from darabonba.model import DaraModel

class ListExtensionsResponseBody(DaraModel):
    def __init__(
        self,
        paging_info: main_models.ListExtensionsResponseBodyPagingInfo = None,
        request_id: str = None,
    ):
        # The pagination information.
        self.paging_info = paging_info
        # Id of the request
        self.request_id = request_id

    def validate(self):
        if self.paging_info:
            self.paging_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.paging_info is not None:
            result['PagingInfo'] = self.paging_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PagingInfo') is not None:
            temp_model = main_models.ListExtensionsResponseBodyPagingInfo()
            self.paging_info = temp_model.from_map(m.get('PagingInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListExtensionsResponseBodyPagingInfo(DaraModel):
    def __init__(
        self,
        extensions: List[main_models.ListExtensionsResponseBodyPagingInfoExtensions] = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The list of extensions.
        self.extensions = extensions
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.extensions:
            for v1 in self.extensions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Extensions'] = []
        if self.extensions is not None:
            for k1 in self.extensions:
                result['Extensions'].append(k1.to_map() if k1 else None)

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.extensions = []
        if m.get('Extensions') is not None:
            for k1 in m.get('Extensions'):
                temp_model = main_models.ListExtensionsResponseBodyPagingInfoExtensions()
                self.extensions.append(temp_model.from_map(k1))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListExtensionsResponseBodyPagingInfoExtensions(DaraModel):
    def __init__(
        self,
        bind_event_list: List[main_models.ListExtensionsResponseBodyPagingInfoExtensionsBindEventList] = None,
        extension_code: str = None,
        extension_desc: str = None,
        extension_name: str = None,
        owner: str = None,
        status: int = None,
    ):
        # The list of extension point events.
        self.bind_event_list = bind_event_list
        # The unique code of the extension.
        self.extension_code = extension_code
        # The description of the extension.
        self.extension_desc = extension_desc
        # The name of the extension.
        self.extension_name = extension_name
        # The ID of the RAM user.
        self.owner = owner
        # The state of the extension. Valid values: 0: Testing 1: Publishing 3: Disabled 4: Processing 5: Approved 6: Approve Failed
        self.status = status

    def validate(self):
        if self.bind_event_list:
            for v1 in self.bind_event_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BindEventList'] = []
        if self.bind_event_list is not None:
            for k1 in self.bind_event_list:
                result['BindEventList'].append(k1.to_map() if k1 else None)

        if self.extension_code is not None:
            result['ExtensionCode'] = self.extension_code

        if self.extension_desc is not None:
            result['ExtensionDesc'] = self.extension_desc

        if self.extension_name is not None:
            result['ExtensionName'] = self.extension_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.bind_event_list = []
        if m.get('BindEventList') is not None:
            for k1 in m.get('BindEventList'):
                temp_model = main_models.ListExtensionsResponseBodyPagingInfoExtensionsBindEventList()
                self.bind_event_list.append(temp_model.from_map(k1))

        if m.get('ExtensionCode') is not None:
            self.extension_code = m.get('ExtensionCode')

        if m.get('ExtensionDesc') is not None:
            self.extension_desc = m.get('ExtensionDesc')

        if m.get('ExtensionName') is not None:
            self.extension_name = m.get('ExtensionName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self

class ListExtensionsResponseBodyPagingInfoExtensionsBindEventList(DaraModel):
    def __init__(
        self,
        event_code: str = None,
        event_name: str = None,
    ):
        # The code of the event.
        self.event_code = event_code
        # The name of the event.
        self.event_name = event_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event_code is not None:
            result['EventCode'] = self.event_code

        if self.event_name is not None:
            result['EventName'] = self.event_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EventCode') is not None:
            self.event_code = m.get('EventCode')

        if m.get('EventName') is not None:
            self.event_name = m.get('EventName')

        return self


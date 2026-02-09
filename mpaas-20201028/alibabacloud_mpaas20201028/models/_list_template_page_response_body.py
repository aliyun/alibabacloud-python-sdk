# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_mpaas20201028 import models as main_models
from darabonba.model import DaraModel

class ListTemplatePageResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        current_page: int = None,
        data: List[main_models.ListTemplatePageResponseBodyData] = None,
        msg: str = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_size: int = None,
    ):
        self.code = code
        self.current_page = current_page
        self.data = data
        self.msg = msg
        self.page_size = page_size
        # Id of the request
        self.request_id = request_id
        self.success = success
        self.total_size = total_size

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListTemplatePageResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        return self

class ListTemplatePageResponseBodyData(DaraModel):
    def __init__(
        self,
        action: str = None,
        content: str = None,
        desc_info: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        icon_urls: str = None,
        id: str = None,
        image_urls: str = None,
        name: str = None,
        push_style: str = None,
        show_style: str = None,
        title: str = None,
        uri: str = None,
        variables: str = None,
    ):
        self.action = action
        self.content = content
        self.desc_info = desc_info
        self.gmt_create = gmt_create
        self.gmt_modified = gmt_modified
        self.icon_urls = icon_urls
        self.id = id
        self.image_urls = image_urls
        self.name = name
        self.push_style = push_style
        self.show_style = show_style
        self.title = title
        self.uri = uri
        self.variables = variables

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.action is not None:
            result['Action'] = self.action

        if self.content is not None:
            result['Content'] = self.content

        if self.desc_info is not None:
            result['DescInfo'] = self.desc_info

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.icon_urls is not None:
            result['IconUrls'] = self.icon_urls

        if self.id is not None:
            result['Id'] = self.id

        if self.image_urls is not None:
            result['ImageUrls'] = self.image_urls

        if self.name is not None:
            result['Name'] = self.name

        if self.push_style is not None:
            result['PushStyle'] = self.push_style

        if self.show_style is not None:
            result['ShowStyle'] = self.show_style

        if self.title is not None:
            result['Title'] = self.title

        if self.uri is not None:
            result['Uri'] = self.uri

        if self.variables is not None:
            result['Variables'] = self.variables

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Action') is not None:
            self.action = m.get('Action')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DescInfo') is not None:
            self.desc_info = m.get('DescInfo')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('IconUrls') is not None:
            self.icon_urls = m.get('IconUrls')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImageUrls') is not None:
            self.image_urls = m.get('ImageUrls')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PushStyle') is not None:
            self.push_style = m.get('PushStyle')

        if m.get('ShowStyle') is not None:
            self.show_style = m.get('ShowStyle')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Uri') is not None:
            self.uri = m.get('Uri')

        if m.get('Variables') is not None:
            self.variables = m.get('Variables')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class CreateScheduledPreloadJobRequest(DaraModel):
    def __init__(
        self,
        insert_way: str = None,
        name: str = None,
        oss_url: str = None,
        site_id: int = None,
        url_list: str = None,
    ):
        # The method to submit URLs to be prefetched.
        # 
        # Valid values:
        # 
        # *   **textBox**
        # *   **oss**
        # 
        # This parameter is required.
        self.insert_way = insert_way
        # The name of the scheduled prefetch task.
        # 
        # This parameter is required.
        self.name = name
        # The URL of the OSS object that stores the URLs to be prefetched.
        self.oss_url = oss_url
        # The website ID, which can be obtained by calling the [ListSites](https://help.aliyun.com/document_detail/2850189.html) operation.
        # 
        # This parameter is required.
        self.site_id = site_id
        # The URLs to be prefetched. This parameter is required if you set InsertWay to textBox.
        self.url_list = url_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.insert_way is not None:
            result['InsertWay'] = self.insert_way

        if self.name is not None:
            result['Name'] = self.name

        if self.oss_url is not None:
            result['OssUrl'] = self.oss_url

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        if self.url_list is not None:
            result['UrlList'] = self.url_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InsertWay') is not None:
            self.insert_way = m.get('InsertWay')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OssUrl') is not None:
            self.oss_url = m.get('OssUrl')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        if m.get('UrlList') is not None:
            self.url_list = m.get('UrlList')

        return self


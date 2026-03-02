# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sfmmultimodalapp20250909 import models as main_models
from darabonba.model import DaraModel

class ListPublishedMmAppResponseBody(DaraModel):
    def __init__(
        self,
        page_number: int = None,
        page_size: int = None,
        published_version_info_list: List[main_models.ListPublishedMmAppResponseBodyPublishedVersionInfoList] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        self.page_number = page_number
        self.page_size = page_size
        self.published_version_info_list = published_version_info_list
        self.request_id = request_id
        self.total_count = total_count

    def validate(self):
        if self.published_version_info_list:
            for v1 in self.published_version_info_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['PublishedVersionInfoList'] = []
        if self.published_version_info_list is not None:
            for k1 in self.published_version_info_list:
                result['PublishedVersionInfoList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.published_version_info_list = []
        if m.get('PublishedVersionInfoList') is not None:
            for k1 in m.get('PublishedVersionInfoList'):
                temp_model = main_models.ListPublishedMmAppResponseBodyPublishedVersionInfoList()
                self.published_version_info_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListPublishedMmAppResponseBodyPublishedVersionInfoList(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        app_name: str = None,
        create_user_id: str = None,
        create_user_name: str = None,
        description: str = None,
        gmt_create: str = None,
        publish_time: str = None,
        version: int = None,
    ):
        self.app_id = app_id
        self.app_name = app_name
        self.create_user_id = create_user_id
        self.create_user_name = create_user_name
        self.description = description
        self.gmt_create = gmt_create
        self.publish_time = publish_time
        self.version = version

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.app_name is not None:
            result['AppName'] = self.app_name

        if self.create_user_id is not None:
            result['CreateUserId'] = self.create_user_id

        if self.create_user_name is not None:
            result['CreateUserName'] = self.create_user_name

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.publish_time is not None:
            result['PublishTime'] = self.publish_time

        if self.version is not None:
            result['Version'] = self.version

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('AppName') is not None:
            self.app_name = m.get('AppName')

        if m.get('CreateUserId') is not None:
            self.create_user_id = m.get('CreateUserId')

        if m.get('CreateUserName') is not None:
            self.create_user_name = m.get('CreateUserName')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('PublishTime') is not None:
            self.publish_time = m.get('PublishTime')

        if m.get('Version') is not None:
            self.version = m.get('Version')

        return self


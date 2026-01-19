# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_xtee20210910 import models as main_models
from darabonba.model import DaraModel

class DescribeAppKeyPageResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        current_page: int = None,
        page_size: int = None,
        result_object: List[main_models.DescribeAppKeyPageResponseBodyResultObject] = None,
        total_item: int = None,
        total_page: int = None,
    ):
        # Request ID.
        self.request_id = request_id
        # Current page number.
        self.current_page = current_page
        # Number of items per page, default value is 10.
        self.page_size = page_size
        # Returned object.
        self.result_object = result_object
        # Total number of items.
        self.total_item = total_item
        # Total number of pages.
        self.total_page = total_page

    def validate(self):
        if self.result_object:
            for v1 in self.result_object:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.current_page is not None:
            result['currentPage'] = self.current_page

        if self.page_size is not None:
            result['pageSize'] = self.page_size

        result['resultObject'] = []
        if self.result_object is not None:
            for k1 in self.result_object:
                result['resultObject'].append(k1.to_map() if k1 else None)

        if self.total_item is not None:
            result['totalItem'] = self.total_item

        if self.total_page is not None:
            result['totalPage'] = self.total_page

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('currentPage') is not None:
            self.current_page = m.get('currentPage')

        if m.get('pageSize') is not None:
            self.page_size = m.get('pageSize')

        self.result_object = []
        if m.get('resultObject') is not None:
            for k1 in m.get('resultObject'):
                temp_model = main_models.DescribeAppKeyPageResponseBodyResultObject()
                self.result_object.append(temp_model.from_map(k1))

        if m.get('totalItem') is not None:
            self.total_item = m.get('totalItem')

        if m.get('totalPage') is not None:
            self.total_page = m.get('totalPage')

        return self

class DescribeAppKeyPageResponseBodyResultObject(DaraModel):
    def __init__(
        self,
        android_sdk_url: str = None,
        android_sdk_version: str = None,
        app_key: str = None,
        gmt_create: int = None,
        ios_sdk_url: str = None,
        ios_sdk_version: str = None,
        memo: str = None,
        sdk_items: str = None,
        used: str = None,
    ):
        # Android SDK download URL.
        self.android_sdk_url = android_sdk_url
        # Android SDK version number.
        self.android_sdk_version = android_sdk_version
        # Application appkey.
        self.app_key = app_key
        # Creation time.
        self.gmt_create = gmt_create
        # iOS SDK download URL.
        self.ios_sdk_url = ios_sdk_url
        # iOS SDK version number.
        self.ios_sdk_version = ios_sdk_version
        # Memo.
        self.memo = memo
        # Deprecated.
        self.sdk_items = sdk_items
        # Whether this appKey is integrated.
        self.used = used

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.android_sdk_url is not None:
            result['androidSdkUrl'] = self.android_sdk_url

        if self.android_sdk_version is not None:
            result['androidSdkVersion'] = self.android_sdk_version

        if self.app_key is not None:
            result['appKey'] = self.app_key

        if self.gmt_create is not None:
            result['gmtCreate'] = self.gmt_create

        if self.ios_sdk_url is not None:
            result['iosSdkUrl'] = self.ios_sdk_url

        if self.ios_sdk_version is not None:
            result['iosSdkVersion'] = self.ios_sdk_version

        if self.memo is not None:
            result['memo'] = self.memo

        if self.sdk_items is not None:
            result['sdkItems'] = self.sdk_items

        if self.used is not None:
            result['used'] = self.used

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('androidSdkUrl') is not None:
            self.android_sdk_url = m.get('androidSdkUrl')

        if m.get('androidSdkVersion') is not None:
            self.android_sdk_version = m.get('androidSdkVersion')

        if m.get('appKey') is not None:
            self.app_key = m.get('appKey')

        if m.get('gmtCreate') is not None:
            self.gmt_create = m.get('gmtCreate')

        if m.get('iosSdkUrl') is not None:
            self.ios_sdk_url = m.get('iosSdkUrl')

        if m.get('iosSdkVersion') is not None:
            self.ios_sdk_version = m.get('iosSdkVersion')

        if m.get('memo') is not None:
            self.memo = m.get('memo')

        if m.get('sdkItems') is not None:
            self.sdk_items = m.get('sdkItems')

        if m.get('used') is not None:
            self.used = m.get('used')

        return self


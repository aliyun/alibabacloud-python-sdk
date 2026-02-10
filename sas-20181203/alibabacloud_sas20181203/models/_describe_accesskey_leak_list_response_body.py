# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAccesskeyLeakListResponseBody(DaraModel):
    def __init__(
        self,
        access_key_leak_list: List[main_models.DescribeAccesskeyLeakListResponseBodyAccessKeyLeakList] = None,
        ak_leak_count: int = None,
        current_page: int = None,
        gmt_last: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the details about AccessKey pair leaks.
        self.access_key_leak_list = access_key_leak_list
        # The number of AccessKey pair leaks that are unhandled.
        self.ak_leak_count = ak_leak_count
        # The page number of the returned page.
        self.current_page = current_page
        # This parameter is deprecated.
        self.gmt_last = gmt_last
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of AccessKey pair leaks.
        self.total_count = total_count

    def validate(self):
        if self.access_key_leak_list:
            for v1 in self.access_key_leak_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AccessKeyLeakList'] = []
        if self.access_key_leak_list is not None:
            for k1 in self.access_key_leak_list:
                result['AccessKeyLeakList'].append(k1.to_map() if k1 else None)

        if self.ak_leak_count is not None:
            result['AkLeakCount'] = self.ak_leak_count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.gmt_last is not None:
            result['GmtLast'] = self.gmt_last

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.access_key_leak_list = []
        if m.get('AccessKeyLeakList') is not None:
            for k1 in m.get('AccessKeyLeakList'):
                temp_model = main_models.DescribeAccesskeyLeakListResponseBodyAccessKeyLeakList()
                self.access_key_leak_list.append(temp_model.from_map(k1))

        if m.get('AkLeakCount') is not None:
            self.ak_leak_count = m.get('AkLeakCount')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('GmtLast') is not None:
            self.gmt_last = m.get('GmtLast')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeAccesskeyLeakListResponseBodyAccessKeyLeakList(DaraModel):
    def __init__(
        self,
        accesskey_id: str = None,
        ali_user_name: str = None,
        asset: str = None,
        deal_time: str = None,
        deal_type: str = None,
        gmt_modified: int = None,
        id: int = None,
        status: str = None,
        type: str = None,
        url: str = None,
        user_type: str = None,
    ):
        # The ID of the AccessKey pair that is leaked.
        self.accesskey_id = accesskey_id
        # The name of the Alibaba Cloud account that is affected.
        self.ali_user_name = ali_user_name
        # The platform to which the asset belongs. The value is fixed as **Cloud platform**.
        self.asset = asset
        # The time when the AccessKey pair leak is handled.
        self.deal_time = deal_time
        # The method to handle the AccessKey pair leak. Valid values:
        # 
        # *   **pending**: The AccessKey pair leak is unhandled.
        # *   **manual**: The AccessKey pair leak is manually handled.
        # *   **disable**: The AccessKey pair leak is disabled.
        # *   **add-whitelist**: The AccessKey pair leak is added to the whitelist.
        self.deal_type = deal_type
        # The time when the AccessKey pair leak is first detected. The value of this parameter is a UNIX timestamp. Unit: milliseconds.
        self.gmt_modified = gmt_modified
        # The primary key ID of the database.
        self.id = id
        # Indicates whether the AccessKey pair leak is handled. Valid values:
        # 
        # *   **pending**: unhandled
        # *   **dealed**: handled
        self.status = status
        # The type of the leak. The value is fixed as **AccessKey**.
        self.type = type
        # The URL of the platform on which the AccessKey pair leak is detected.
        self.url = url
        # The type of the account to which the leaked AccessKey pair belongs. Valid values:
        # 
        # *   **master**: Alibaba Cloud account
        # *   **ram**: RAM user
        self.user_type = user_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.accesskey_id is not None:
            result['AccesskeyId'] = self.accesskey_id

        if self.ali_user_name is not None:
            result['AliUserName'] = self.ali_user_name

        if self.asset is not None:
            result['Asset'] = self.asset

        if self.deal_time is not None:
            result['DealTime'] = self.deal_time

        if self.deal_type is not None:
            result['DealType'] = self.deal_type

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.url is not None:
            result['Url'] = self.url

        if self.user_type is not None:
            result['UserType'] = self.user_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccesskeyId') is not None:
            self.accesskey_id = m.get('AccesskeyId')

        if m.get('AliUserName') is not None:
            self.ali_user_name = m.get('AliUserName')

        if m.get('Asset') is not None:
            self.asset = m.get('Asset')

        if m.get('DealTime') is not None:
            self.deal_time = m.get('DealTime')

        if m.get('DealType') is not None:
            self.deal_type = m.get('DealType')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('UserType') is not None:
            self.user_type = m.get('UserType')

        return self


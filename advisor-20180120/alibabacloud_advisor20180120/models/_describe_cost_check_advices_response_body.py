# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class DescribeCostCheckAdvicesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.DescribeCostCheckAdvicesResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: str = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeCostCheckAdvicesResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCostCheckAdvicesResponseBodyData(DaraModel):
    def __init__(
        self,
        advice_list: List[main_models.DescribeCostCheckAdvicesResponseBodyDataAdviceList] = None,
        check_id: str = None,
        page_number: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.advice_list = advice_list
        self.check_id = check_id
        self.page_number = page_number
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.advice_list:
            for v1 in self.advice_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AdviceList'] = []
        if self.advice_list is not None:
            for k1 in self.advice_list:
                result['AdviceList'].append(k1.to_map() if k1 else None)

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.advice_list = []
        if m.get('AdviceList') is not None:
            for k1 in m.get('AdviceList'):
                temp_model = main_models.DescribeCostCheckAdvicesResponseBodyDataAdviceList()
                self.advice_list.append(temp_model.from_map(k1))

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeCostCheckAdvicesResponseBodyDataAdviceList(DaraModel):
    def __init__(
        self,
        account_folder_id: str = None,
        account_folder_name: str = None,
        aliyun_id: int = None,
        content: str = None,
        email: str = None,
        end_time: int = None,
        gmt_deleted: int = None,
        product: str = None,
        region_id: str = None,
        resource_id: str = None,
        resource_name: str = None,
        severity: str = None,
        start_time: int = None,
        tags: List[main_models.DescribeCostCheckAdvicesResponseBodyDataAdviceListTags] = None,
        url: str = None,
        user_name: str = None,
        zone_id: str = None,
    ):
        self.account_folder_id = account_folder_id
        self.account_folder_name = account_folder_name
        self.aliyun_id = aliyun_id
        self.content = content
        # Email
        self.email = email
        self.end_time = end_time
        self.gmt_deleted = gmt_deleted
        self.product = product
        self.region_id = region_id
        self.resource_id = resource_id
        self.resource_name = resource_name
        self.severity = severity
        self.start_time = start_time
        self.tags = tags
        self.url = url
        self.user_name = user_name
        self.zone_id = zone_id

    def validate(self):
        if self.tags:
            for v1 in self.tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_folder_id is not None:
            result['AccountFolderId'] = self.account_folder_id

        if self.account_folder_name is not None:
            result['AccountFolderName'] = self.account_folder_name

        if self.aliyun_id is not None:
            result['AliyunId'] = self.aliyun_id

        if self.content is not None:
            result['Content'] = self.content

        if self.email is not None:
            result['Email'] = self.email

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gmt_deleted is not None:
            result['GmtDeleted'] = self.gmt_deleted

        if self.product is not None:
            result['Product'] = self.product

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.resource_name is not None:
            result['ResourceName'] = self.resource_name

        if self.severity is not None:
            result['Severity'] = self.severity

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        result['Tags'] = []
        if self.tags is not None:
            for k1 in self.tags:
                result['Tags'].append(k1.to_map() if k1 else None)

        if self.url is not None:
            result['Url'] = self.url

        if self.user_name is not None:
            result['UserName'] = self.user_name

        if self.zone_id is not None:
            result['ZoneId'] = self.zone_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountFolderId') is not None:
            self.account_folder_id = m.get('AccountFolderId')

        if m.get('AccountFolderName') is not None:
            self.account_folder_name = m.get('AccountFolderName')

        if m.get('AliyunId') is not None:
            self.aliyun_id = m.get('AliyunId')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('Email') is not None:
            self.email = m.get('Email')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GmtDeleted') is not None:
            self.gmt_deleted = m.get('GmtDeleted')

        if m.get('Product') is not None:
            self.product = m.get('Product')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('ResourceName') is not None:
            self.resource_name = m.get('ResourceName')

        if m.get('Severity') is not None:
            self.severity = m.get('Severity')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        self.tags = []
        if m.get('Tags') is not None:
            for k1 in m.get('Tags'):
                temp_model = main_models.DescribeCostCheckAdvicesResponseBodyDataAdviceListTags()
                self.tags.append(temp_model.from_map(k1))

        if m.get('Url') is not None:
            self.url = m.get('Url')

        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')

        if m.get('ZoneId') is not None:
            self.zone_id = m.get('ZoneId')

        return self

class DescribeCostCheckAdvicesResponseBodyDataAdviceListTags(DaraModel):
    def __init__(
        self,
        tag_key: str = None,
        tag_value: str = None,
    ):
        self.tag_key = tag_key
        self.tag_value = tag_value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key

        if self.tag_value is not None:
            result['TagValue'] = self.tag_value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')

        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')

        return self


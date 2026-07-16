# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeOssObjectsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeOssObjectsResponseBodyItems] = None,
        marker: str = None,
        next_marker: str = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
        truncated: bool = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # A list of OSS objects.
        self.items = items
        # This parameter is deprecated.
        self.marker = marker
        # The token that marks the start of the next page of results.
        # 
        # > This parameter is returned only when `Truncated` is `true`.
        self.next_marker = next_marker
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count
        # Indicates whether the results are truncated. The default value is false. Valid values:
        # 
        # - **true**: The results are truncated.
        # 
        # - **false**: The results are not truncated.
        self.truncated = truncated

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.next_marker is not None:
            result['NextMarker'] = self.next_marker

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.truncated is not None:
            result['Truncated'] = self.truncated

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeOssObjectsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('NextMarker') is not None:
            self.next_marker = m.get('NextMarker')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('Truncated') is not None:
            self.truncated = m.get('Truncated')

        return self

class DescribeOssObjectsResponseBodyItems(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        category: int = None,
        category_name: str = None,
        file_category_code: int = None,
        file_category_name: str = None,
        file_id: str = None,
        id: str = None,
        instance_id: int = None,
        last_modified_time: int = None,
        name: str = None,
        region_id: str = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_count: int = None,
        rule_list: List[main_models.DescribeOssObjectsResponseBodyItemsRuleList] = None,
        sensitive_count: int = None,
        size: int = None,
    ):
        # The bucket name.
        self.bucket_name = bucket_name
        # The type of the OSS object, such as **900001** (MP4 video file), **800015** (PDF document), and **800005** (OSS configuration file).
        self.category = category
        # The name of the file type.
        self.category_name = category_name
        # The code of the file category.
        self.file_category_code = file_category_code
        # The name of the file category.
        self.file_category_name = file_category_name
        # The ID of the OSS file.
        self.file_id = file_id
        # The unique ID of the OSS object.
        self.id = id
        # The ID of the asset instance to which the OSS object belongs.
        self.instance_id = instance_id
        # The time when the file was last modified.
        self.last_modified_time = last_modified_time
        # The name of the OSS object.
        self.name = name
        # The region ID of the OSS object owner.
        self.region_id = region_id
        # The risk level ID of the OSS object. Valid values:
        # 
        # - **1**: N/A. No sensitive data is detected.
        # 
        # - **2**: S1. Level 1 sensitive data.
        # 
        # - **3**: S2. Level 2 sensitive data.
        # 
        # - **4**: S3. Level 3 sensitive data.
        # 
        # - **5**: S4. Level 4 sensitive data.
        self.risk_level_id = risk_level_id
        # The name of the risk level for the OSS object.
        self.risk_level_name = risk_level_name
        # The number of matched rules.
        self.rule_count = rule_count
        # A list of rules.
        self.rule_list = rule_list
        # The number of matched fields.
        self.sensitive_count = sensitive_count
        # The file size. Unit: bytes.
        self.size = size

    def validate(self):
        if self.rule_list:
            for v1 in self.rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bucket_name is not None:
            result['BucketName'] = self.bucket_name

        if self.category is not None:
            result['Category'] = self.category

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.file_category_code is not None:
            result['FileCategoryCode'] = self.file_category_code

        if self.file_category_name is not None:
            result['FileCategoryName'] = self.file_category_name

        if self.file_id is not None:
            result['FileId'] = self.file_id

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('Category') is not None:
            self.category = m.get('Category')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('FileCategoryCode') is not None:
            self.file_category_code = m.get('FileCategoryCode')

        if m.get('FileCategoryName') is not None:
            self.file_category_name = m.get('FileCategoryName')

        if m.get('FileId') is not None:
            self.file_id = m.get('FileId')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.DescribeOssObjectsResponseBodyItemsRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self

class DescribeOssObjectsResponseBodyItemsRuleList(DaraModel):
    def __init__(
        self,
        count: int = None,
        name: str = None,
        risk_level_id: int = None,
    ):
        # The number of times the rule is matched.
        self.count = count
        # The name of the rule.
        self.name = name
        # The risk level ID of the rule. Valid values:
        # 
        # - **1**: N/A. No sensitive data is detected.
        # 
        # - **2**: S1. Level 1 sensitive data.
        # 
        # - **3**: S2. Level 2 sensitive data.
        # 
        # - **4**: S3. Level 3 sensitive data.
        # 
        # - **5**: S4. Level 4 sensitive data.
        self.risk_level_id = risk_level_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.name is not None:
            result['Name'] = self.name

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        return self


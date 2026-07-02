# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeOssObjectDetailResponseBody(DaraModel):
    def __init__(
        self,
        oss_object_detail: main_models.DescribeOssObjectDetailResponseBodyOssObjectDetail = None,
        request_id: str = None,
    ):
        # The details of the OSS object.
        self.oss_object_detail = oss_object_detail
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.oss_object_detail:
            self.oss_object_detail.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.oss_object_detail is not None:
            result['OssObjectDetail'] = self.oss_object_detail.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OssObjectDetail') is not None:
            temp_model = main_models.DescribeOssObjectDetailResponseBodyOssObjectDetail()
            self.oss_object_detail = temp_model.from_map(m.get('OssObjectDetail'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeOssObjectDetailResponseBodyOssObjectDetail(DaraModel):
    def __init__(
        self,
        bucket_name: str = None,
        category_name: str = None,
        name: str = None,
        region_id: str = None,
        risk_level_name: str = None,
        rule_list: List[main_models.DescribeOssObjectDetailResponseBodyOssObjectDetailRuleList] = None,
    ):
        # The name of the bucket to which the OSS object belongs.
        self.bucket_name = bucket_name
        # The name of the OSS object type.
        self.category_name = category_name
        # The name of the OSS object.
        self.name = name
        # The ID of the region where the OSS object is stored.
        self.region_id = region_id
        # The name of the risk level for the OSS object.
        self.risk_level_name = risk_level_name
        # A list of sensitive data detection rules that the OSS object hits.
        self.rule_list = rule_list

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

        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.name is not None:
            result['Name'] = self.name

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        result['RuleList'] = []
        if self.rule_list is not None:
            for k1 in self.rule_list:
                result['RuleList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BucketName') is not None:
            self.bucket_name = m.get('BucketName')

        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.DescribeOssObjectDetailResponseBodyOssObjectDetailRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        return self

class DescribeOssObjectDetailResponseBodyOssObjectDetailRuleList(DaraModel):
    def __init__(
        self,
        category_name: str = None,
        count: int = None,
        model_tags: List[main_models.DescribeOssObjectDetailResponseBodyOssObjectDetailRuleListModelTags] = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_name: str = None,
    ):
        # The name of the OSS object type.
        self.category_name = category_name
        # The number of times the sensitive data detection rule was hit.
        self.count = count
        # A list of data tags that are hit by the detection model.
        self.model_tags = model_tags
        # The ID of the risk level for the OSS object.
        # 
        # - **1**: No sensitive data is detected.
        # 
        # - **2**: Level 1 sensitive data.
        # 
        # - **3**: Level 2 sensitive data.
        # 
        # - **4**: Level 3 sensitive data.
        # 
        # - **5**: Level 4 sensitive data.
        self.risk_level_id = risk_level_id
        # The name of the risk level for the OSS object.
        self.risk_level_name = risk_level_name
        # The name of the sensitive data detection rule that was hit.
        self.rule_name = rule_name

    def validate(self):
        if self.model_tags:
            for v1 in self.model_tags:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.category_name is not None:
            result['CategoryName'] = self.category_name

        if self.count is not None:
            result['Count'] = self.count

        result['ModelTags'] = []
        if self.model_tags is not None:
            for k1 in self.model_tags:
                result['ModelTags'].append(k1.to_map() if k1 else None)

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CategoryName') is not None:
            self.category_name = m.get('CategoryName')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k1 in m.get('ModelTags'):
                temp_model = main_models.DescribeOssObjectDetailResponseBodyOssObjectDetailRuleListModelTags()
                self.model_tags.append(temp_model.from_map(k1))

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        return self

class DescribeOssObjectDetailResponseBodyOssObjectDetailRuleListModelTags(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the data tag for the detection model.
        # 
        # - **101**: Personal sensitive information.
        # 
        # - **102**: Personal information.
        # 
        # - **103**: Important data.
        self.id = id
        # The name of the data tag for the detection model.
        # 
        # - Personal sensitive information.
        # 
        # - Personal information.
        # 
        # - Important data.
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self


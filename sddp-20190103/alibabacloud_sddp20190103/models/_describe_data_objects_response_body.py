# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeDataObjectsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeDataObjectsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The number of the page to return. Default value: **1**.
        self.current_page = current_page
        # A list of data objects.
        self.items = items
        # The number of data asset instances to return on each page. Default value: **10**.
        self.page_size = page_size
        # The unique ID of the request. Alibaba Cloud generates this ID to help you troubleshoot issues.
        self.request_id = request_id
        # The total number of entries that match the query.
        self.total_count = total_count

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

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeDataObjectsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDataObjectsResponseBodyItems(DaraModel):
    def __init__(
        self,
        categories: List[str] = None,
        cluster_type: str = None,
        comment: str = None,
        data_type: str = None,
        db_name: str = None,
        file_category_code: int = None,
        id: str = None,
        instance_description: str = None,
        instance_id: str = None,
        is_revision: int = None,
        last_modified_time: int = None,
        last_scan_time: int = None,
        log_store: str = None,
        mask_status: int = None,
        member_account: int = None,
        model_tags: List[main_models.DescribeDataObjectsResponseBodyItemsModelTags] = None,
        name: str = None,
        object_file_category: str = None,
        object_type: str = None,
        path: str = None,
        product_code: str = None,
        product_id: int = None,
        project: str = None,
        region_id: str = None,
        region_name: str = None,
        risk_level_id: int = None,
        rule_count: int = None,
        rule_list: List[main_models.DescribeDataObjectsResponseBodyItemsRuleList] = None,
        sensitive_count: int = None,
        size: int = None,
        sx: str = None,
        table_name: str = None,
        task_id: int = None,
        task_name: str = None,
        task_number: int = None,
        template_id: int = None,
        template_name: str = None,
    ):
        # An array of industry categories to which the sensitive data belongs.
        self.categories = categories
        self.cluster_type = cluster_type
        # The comment on the column.
        self.comment = comment
        # The data type of the database column.
        self.data_type = data_type
        # The name of the database.
        self.db_name = db_name
        # The code for the file category.
        self.file_category_code = file_category_code
        # The unique ID of the data object.
        self.id = id
        # The description of the data asset instance.
        self.instance_description = instance_description
        # The ID of the data asset instance.
        self.instance_id = instance_id
        # The revision status.
        self.is_revision = is_revision
        # The last modification time of the file, in milliseconds.
        self.last_modified_time = last_modified_time
        # The timestamp of the last scan, in milliseconds.
        self.last_scan_time = last_scan_time
        # The name of the Logstore in SLS.
        self.log_store = log_store
        # The column encryption status.
        self.mask_status = mask_status
        # The ID of the member account.
        self.member_account = member_account
        # A list of data tags.
        self.model_tags = model_tags
        # The name of the data object.
        self.name = name
        # The name of the file category.
        self.object_file_category = object_file_category
        # The type of the data object.
        self.object_type = object_type
        # The path of the data object.
        self.path = path
        # The name of the product to which the data object belongs. Valid values:
        # 
        # - **MaxCompute**
        # 
        # - **OSS**
        # 
        # - **ADB-MYSQL**
        # 
        # - **Table Store**
        # 
        # - **RDS**
        # 
        # - **SELF_DB**
        # 
        # - **PolarDB-X**
        # 
        # - **PolarDB**
        # 
        # - **ADB-PG**
        # 
        # - **OceanBase**
        # 
        # - **MongoDB**
        # 
        # - **Redis**
        self.product_code = product_code
        # The ID of the product to which the data object belongs. Valid values:
        # 
        # - **1**: MaxCompute
        # 
        # - **2**: OSS
        # 
        # - **3**: ADB-MYSQL
        # 
        # - **4**: Table Store
        # 
        # - **5**: RDS
        # 
        # - **6**: SELF_DB
        # 
        # - **7**: PolarDB-X
        # 
        # - **8**: PolarDB
        # 
        # - **9**: ADB-PG
        # 
        # - **10**: OceanBase
        # 
        # - **11**: MongoDB
        # 
        # - **25**: Redis
        self.product_id = product_id
        # The name of the Simple Log Service (SLS) project.
        self.project = project
        # The ID of the region where the data object is located.
        self.region_id = region_id
        # The name of the region.
        self.region_name = region_name
        # The risk level.
        self.risk_level_id = risk_level_id
        # The number of matched rules.
        self.rule_count = rule_count
        # A list of matched detection models.
        self.rule_list = rule_list
        # The number of sensitive data fields.
        self.sensitive_count = sensitive_count
        # The size of the file in bytes.
        self.size = size
        # A comma-separated string that specifies the count of matched rules for each risk level. The string follows the format `S1,S2...S10`, where the value at each position represents the count for the corresponding risk level.
        self.sx = sx
        # The name of the table.
        self.table_name = table_name
        # The ID of the task.
        self.task_id = task_id
        # The name of the task.
        self.task_name = task_name
        # The task number.
        self.task_number = task_number
        # The ID of the industry template.
        self.template_id = template_id
        # The name of the template.
        self.template_name = template_name

    def validate(self):
        if self.model_tags:
            for v1 in self.model_tags:
                 if v1:
                    v1.validate()
        if self.rule_list:
            for v1 in self.rule_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.categories is not None:
            result['Categories'] = self.categories

        if self.cluster_type is not None:
            result['ClusterType'] = self.cluster_type

        if self.comment is not None:
            result['Comment'] = self.comment

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.db_name is not None:
            result['DbName'] = self.db_name

        if self.file_category_code is not None:
            result['FileCategoryCode'] = self.file_category_code

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.is_revision is not None:
            result['IsRevision'] = self.is_revision

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.last_scan_time is not None:
            result['LastScanTime'] = self.last_scan_time

        if self.log_store is not None:
            result['LogStore'] = self.log_store

        if self.mask_status is not None:
            result['MaskStatus'] = self.mask_status

        if self.member_account is not None:
            result['MemberAccount'] = self.member_account

        result['ModelTags'] = []
        if self.model_tags is not None:
            for k1 in self.model_tags:
                result['ModelTags'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.object_file_category is not None:
            result['ObjectFileCategory'] = self.object_file_category

        if self.object_type is not None:
            result['ObjectType'] = self.object_type

        if self.path is not None:
            result['Path'] = self.path

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.project is not None:
            result['Project'] = self.project

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.region_name is not None:
            result['RegionName'] = self.region_name

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

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

        if self.sx is not None:
            result['Sx'] = self.sx

        if self.table_name is not None:
            result['TableName'] = self.table_name

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.task_name is not None:
            result['TaskName'] = self.task_name

        if self.task_number is not None:
            result['TaskNumber'] = self.task_number

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        if m.get('ClusterType') is not None:
            self.cluster_type = m.get('ClusterType')

        if m.get('Comment') is not None:
            self.comment = m.get('Comment')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('DbName') is not None:
            self.db_name = m.get('DbName')

        if m.get('FileCategoryCode') is not None:
            self.file_category_code = m.get('FileCategoryCode')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('IsRevision') is not None:
            self.is_revision = m.get('IsRevision')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('LastScanTime') is not None:
            self.last_scan_time = m.get('LastScanTime')

        if m.get('LogStore') is not None:
            self.log_store = m.get('LogStore')

        if m.get('MaskStatus') is not None:
            self.mask_status = m.get('MaskStatus')

        if m.get('MemberAccount') is not None:
            self.member_account = m.get('MemberAccount')

        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k1 in m.get('ModelTags'):
                temp_model = main_models.DescribeDataObjectsResponseBodyItemsModelTags()
                self.model_tags.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectFileCategory') is not None:
            self.object_file_category = m.get('ObjectFileCategory')

        if m.get('ObjectType') is not None:
            self.object_type = m.get('ObjectType')

        if m.get('Path') is not None:
            self.path = m.get('Path')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('Project') is not None:
            self.project = m.get('Project')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RegionName') is not None:
            self.region_name = m.get('RegionName')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        self.rule_list = []
        if m.get('RuleList') is not None:
            for k1 in m.get('RuleList'):
                temp_model = main_models.DescribeDataObjectsResponseBodyItemsRuleList()
                self.rule_list.append(temp_model.from_map(k1))

        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Sx') is not None:
            self.sx = m.get('Sx')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TaskName') is not None:
            self.task_name = m.get('TaskName')

        if m.get('TaskNumber') is not None:
            self.task_number = m.get('TaskNumber')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        return self

class DescribeDataObjectsResponseBodyItemsRuleList(DaraModel):
    def __init__(
        self,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_category_name_list: str = None,
        rule_count: int = None,
        rule_id: int = None,
        rule_name: str = None,
        sample_list: str = None,
    ):
        # The ID of the risk level. Valid values:
        # 
        # - **1**: N/A - No sensitive data is detected
        # 
        # - **2**: S1 - Level-1 sensitive data
        # 
        # - **3**: S2 - Level-2 sensitive data
        # 
        # - **4**: S3 - Level-3 sensitive data
        # 
        # - **5**: S4 - Level-4 sensitive data
        self.risk_level_id = risk_level_id
        # The name of the risk level. Valid values:
        # 
        # - **N/A**: No sensitive data is detected
        # 
        # - **S1**: Level-1 sensitive data
        # 
        # - **S2**: Level-2 sensitive data
        # 
        # - **S3**: Level-3 sensitive data
        # 
        # - **S4**: Level-4 sensitive data
        self.risk_level_name = risk_level_name
        # The hierarchical category of the rule, from the top-level to the leaf-level category in the template.
        self.rule_category_name_list = rule_category_name_list
        # The number of matched detection models.
        self.rule_count = rule_count
        # The ID of the detection model.
        self.rule_id = rule_id
        # The name of the detection model.
        self.rule_name = rule_name
        # The sample data.
        self.sample_list = sample_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        if self.rule_category_name_list is not None:
            result['RuleCategoryNameList'] = self.rule_category_name_list

        if self.rule_count is not None:
            result['RuleCount'] = self.rule_count

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sample_list is not None:
            result['SampleList'] = self.sample_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        if m.get('RuleCategoryNameList') is not None:
            self.rule_category_name_list = m.get('RuleCategoryNameList')

        if m.get('RuleCount') is not None:
            self.rule_count = m.get('RuleCount')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SampleList') is not None:
            self.sample_list = m.get('SampleList')

        return self

class DescribeDataObjectsResponseBodyItemsModelTags(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the data tag. Valid values:
        # 
        # - **101**: Personal sensitive information
        # 
        # - **102**: Personal information
        # 
        # - **107**: General information
        self.id = id
        # The name of the data tag. Valid values:
        # 
        # - **Personal sensitive information**
        # 
        # - **Personal information**
        # 
        # - **General information**
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


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeDataObjectColumnDetailResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeDataObjectColumnDetailResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The details of the columns.
        self.items = items
        # The number of entries returned on each page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries.
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
                temp_model = main_models.DescribeDataObjectColumnDetailResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDataObjectColumnDetailResponseBodyItems(DaraModel):
    def __init__(
        self,
        categories: List[str] = None,
        column_comment: str = None,
        column_name: str = None,
        data_type: str = None,
        engine_type: str = None,
        id: str = None,
        instance_name: str = None,
        masking_status: int = None,
        model_tags: List[main_models.DescribeDataObjectColumnDetailResponseBodyItemsModelTags] = None,
        primary_key: bool = None,
        product_id: int = None,
        region_id: str = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_id: int = None,
        rule_name: str = None,
        table_name: str = None,
    ):
        # The industry-specific data classifications.
        self.categories = categories
        # The comment on the column.
        self.column_comment = column_comment
        # The name of the column.
        self.column_name = column_name
        # The data type of the column.
        self.data_type = data_type
        # The type of the database engine. Valid values:
        # 
        # - **MySQL**
        # 
        # - **MariaDB**
        # 
        # - **Oracle**
        # 
        # - **PostgreSQL**
        # 
        # - **SQLServer**
        self.engine_type = engine_type
        # The ID of the column.
        self.id = id
        # The name of the instance where the table is located.
        self.instance_name = instance_name
        # The data masking status of the column. Valid values:
        # 
        # - **-1**: Not masked
        # 
        # - **1**: Masked
        # 
        # - **2**: Masking failed
        self.masking_status = masking_status
        # The data labels.
        self.model_tags = model_tags
        # Indicates whether the column is a primary key. Valid values:
        # 
        # - **true**: The column is a primary key.
        # 
        # - **false**: The column is not a primary key.
        self.primary_key = primary_key
        # The ID of the service to which the data object belongs. Valid values:
        # 
        # - **1**: MaxCompute
        # 
        # - **2**: OSS
        # 
        # - **3**: ADB-MYSQL
        # 
        # - **4**: Tablestore
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
        # The ID of the region where the data asset is located.
        self.region_id = region_id
        # The ID of the sensitivity level. Valid values:
        # 
        # - **1**: N/A
        # 
        # - **2**: S1
        # 
        # - **3**: S2
        # 
        # - **4**: S3
        # 
        # - **5**: S4
        self.risk_level_id = risk_level_id
        # The name of the sensitivity level. Valid values:
        # 
        # - **N/A**
        # 
        # - **S1**
        # 
        # - **S2**
        # 
        # - **S3**
        # 
        # - **S4**
        self.risk_level_name = risk_level_name
        # The ID of the sensitive data detection rule that was matched.
        self.rule_id = rule_id
        # The name of the sensitive data detection rule that was matched.
        self.rule_name = rule_name
        # The name of the table.
        self.table_name = table_name

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
        if self.categories is not None:
            result['Categories'] = self.categories

        if self.column_comment is not None:
            result['ColumnComment'] = self.column_comment

        if self.column_name is not None:
            result['ColumnName'] = self.column_name

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.masking_status is not None:
            result['MaskingStatus'] = self.masking_status

        result['ModelTags'] = []
        if self.model_tags is not None:
            for k1 in self.model_tags:
                result['ModelTags'].append(k1.to_map() if k1 else None)

        if self.primary_key is not None:
            result['PrimaryKey'] = self.primary_key

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Categories') is not None:
            self.categories = m.get('Categories')

        if m.get('ColumnComment') is not None:
            self.column_comment = m.get('ColumnComment')

        if m.get('ColumnName') is not None:
            self.column_name = m.get('ColumnName')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MaskingStatus') is not None:
            self.masking_status = m.get('MaskingStatus')

        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k1 in m.get('ModelTags'):
                temp_model = main_models.DescribeDataObjectColumnDetailResponseBodyItemsModelTags()
                self.model_tags.append(temp_model.from_map(k1))

        if m.get('PrimaryKey') is not None:
            self.primary_key = m.get('PrimaryKey')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DescribeDataObjectColumnDetailResponseBodyItemsModelTags(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the data label. Valid values:
        # 
        # - **101**: Personal sensitive information
        # 
        # - **102**: Personal information
        # 
        # - **107**: General information
        self.id = id
        # The name of the data label. Valid values:
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


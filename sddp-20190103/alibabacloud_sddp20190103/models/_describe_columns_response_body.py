# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeColumnsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeColumnsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The data in the columns of the table.
        self.items = items
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of entries returned.
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
                temp_model = main_models.DescribeColumnsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeColumnsResponseBodyItems(DaraModel):
    def __init__(
        self,
        creation_time: int = None,
        data_type: str = None,
        engine_type: str = None,
        id: str = None,
        instance_id: int = None,
        instance_name: str = None,
        masking_status: int = None,
        model_tags: List[main_models.DescribeColumnsResponseBodyItemsModelTags] = None,
        name: str = None,
        odps_risk_level_name: str = None,
        odps_risk_level_value: int = None,
        product_code: str = None,
        product_id: int = None,
        region_id: str = None,
        revision_id: int = None,
        revision_status: int = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_id: int = None,
        rule_name: str = None,
        sens_level_name: str = None,
        sensitive: bool = None,
        table_id: int = None,
        table_name: str = None,
    ):
        # The time when the data in the column of the table is created. Unit: milliseconds.
        self.creation_time = creation_time
        # The type of data in the column of the table.
        self.data_type = data_type
        # The type of the database engine.
        self.engine_type = engine_type
        # The ID of the column of the table.
        self.id = id
        # The ID of the instance to which data in the column of the table belongs.
        self.instance_id = instance_id
        # The name of the instance to which data in the column of the table belongs.
        self.instance_name = instance_name
        # The column encryption status. Valid values:
        # 
        # *   **-1**: unencrypted
        # *   **1**: encrypted
        # *   **2**: encryption failed
        self.masking_status = masking_status
        # A list of tags for data that hits the recognition model.
        self.model_tags = model_tags
        # The name of the column of the table.
        self.name = name
        # The name of the sensitivity level for asset. Valid values:
        # 
        # *   **N/A**: indicates that no sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.odps_risk_level_name = odps_risk_level_name
        # The ID of the sensitivity level of the asset. Valid values:
        # 
        # *   **1**: N/A
        # *   **2**: S1
        # *   **3**: S2
        # *   **4**: S3
        # *   **5**: S4
        self.odps_risk_level_value = odps_risk_level_value
        # The name of the service to which data in the column of the table belongs. Valid values include **MaxCompute, OSS, ADS, OTS, and RDS**.
        self.product_code = product_code
        # The ID of the service to which the data object belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: Object Storage Service (OSS)
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore (OTS)
        # *   **5**: ApsaraDB RDS
        # *   **6**: self-managed database
        # *   **7**: PolarDB for Xscale (PolarDB-X)
        # *   **8**: PolarDB
        # *   **9**: AnalyticDB for PostgreSQL
        # *   **10**: ApsaraDB for OceanBase
        # *   **11**: ApsaraDB for MongoDB
        # *   **25**: ApsaraDB for Redis
        self.product_id = product_id
        # The region in which the asset resides.
        self.region_id = region_id
        # The ID of the revision record.
        self.revision_id = revision_id
        # Indicates whether the column is revised. Valid values:
        # 
        # *   1: yes
        # *   0: no
        self.revision_status = revision_status
        # The ID of the sensitivity level of data in the column of the table. Valid values:
        # 
        # *   **1**: N/A
        # *   **2**: S1
        # *   **3**: S2
        # *   **4**: S3
        # *   **5**: S4
        self.risk_level_id = risk_level_id
        # The name of the sensitivity level for data in the column of the table. Valid values:
        # 
        # *   **N/A**: indicates that no sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.risk_level_name = risk_level_name
        # The ID of the sensitive data detection rule that data in the column of the table hits.
        self.rule_id = rule_id
        # The name of the sensitive data detection rule that data in the column of the table hits.
        self.rule_name = rule_name
        # The name of the sensitivity level. Valid values:
        # 
        # *   **N/A**: indicates that no sensitive data is detected.
        # *   **S1**: indicates the low sensitivity level.
        # *   **S2**: indicates the medium sensitivity level.
        # *   **S3**: indicates the high sensitivity level.
        # *   **S4**: indicates the highest sensitivity level.
        self.sens_level_name = sens_level_name
        # Indicates whether the column contains sensitive data. Valid values:
        # 
        # *   true
        # *   false
        self.sensitive = sensitive
        # The ID of the table.
        self.table_id = table_id
        # The name of the table to which the revised column belongs.
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
        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.engine_type is not None:
            result['EngineType'] = self.engine_type

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.masking_status is not None:
            result['MaskingStatus'] = self.masking_status

        result['ModelTags'] = []
        if self.model_tags is not None:
            for k1 in self.model_tags:
                result['ModelTags'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.odps_risk_level_name is not None:
            result['OdpsRiskLevelName'] = self.odps_risk_level_name

        if self.odps_risk_level_value is not None:
            result['OdpsRiskLevelValue'] = self.odps_risk_level_value

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.revision_id is not None:
            result['RevisionId'] = self.revision_id

        if self.revision_status is not None:
            result['RevisionStatus'] = self.revision_status

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sens_level_name is not None:
            result['SensLevelName'] = self.sens_level_name

        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive

        if self.table_id is not None:
            result['TableId'] = self.table_id

        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('EngineType') is not None:
            self.engine_type = m.get('EngineType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('MaskingStatus') is not None:
            self.masking_status = m.get('MaskingStatus')

        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k1 in m.get('ModelTags'):
                temp_model = main_models.DescribeColumnsResponseBodyItemsModelTags()
                self.model_tags.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OdpsRiskLevelName') is not None:
            self.odps_risk_level_name = m.get('OdpsRiskLevelName')

        if m.get('OdpsRiskLevelValue') is not None:
            self.odps_risk_level_value = m.get('OdpsRiskLevelValue')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RevisionId') is not None:
            self.revision_id = m.get('RevisionId')

        if m.get('RevisionStatus') is not None:
            self.revision_status = m.get('RevisionStatus')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('SensLevelName') is not None:
            self.sens_level_name = m.get('SensLevelName')

        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')

        if m.get('TableId') is not None:
            self.table_id = m.get('TableId')

        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DescribeColumnsResponseBodyItemsModelTags(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The tag ID.
        # 
        # *   **101**: sensitive personal information
        # *   **102**: personal information
        # *   **103**: important information
        self.id = id
        # The tag name.
        # 
        # *   Sensitive personal information
        # *   Personal information
        # *   Important information
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


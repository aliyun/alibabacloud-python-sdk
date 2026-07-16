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
        # The page number of the current page displayed in the results.
        self.current_page = current_page
        # Column data in the data asset table.
        self.items = items
        # The number of data entries displayed per page in the results.
        self.page_size = page_size
        # The request ID of the result.
        self.request_id = request_id
        # The total number of data entries in the results.
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
        # The creation time of the column data in the data asset table, in milliseconds.
        self.creation_time = creation_time
        # The data type of the column data in the data asset table.
        self.data_type = data_type
        # Database engine type.
        self.engine_type = engine_type
        # The unique ID of the column in the data asset table.
        self.id = id
        # The ID of the asset instance to which the column data in the data asset table belongs.
        self.instance_id = instance_id
        # The name of the asset instance to which the column data in the data asset table belongs.
        self.instance_name = instance_name
        # Column encryption status. Valid values:
        # 
        # - **-1**: Not encrypted
        # 
        # - **1**: Encryption successful
        # 
        # - **2**: Encryption failed
        self.masking_status = masking_status
        # The list of data tags hit by the detection model.
        self.model_tags = model_tags
        # The name of the column in the data asset table.
        self.name = name
        # The risk level name of the asset. Valid values:
        # 
        # - **N/A**: No sensitive data detected.
        # 
        # - **S1**: Level 1 sensitive data.
        # 
        # - **S2**: Level 2 sensitive data.
        # 
        # - **S3**: Level 3 sensitive data.
        # 
        # - **S4**: Level 4 sensitive data.
        self.odps_risk_level_name = odps_risk_level_name
        # The risk level code of the asset. Valid values:
        # 
        # - **1**: N/A.
        # 
        # - **2**: S1.
        # 
        # - **3**: S2.
        # 
        # - **4**: S3.
        # 
        # - **5**: S4.
        self.odps_risk_level_value = odps_risk_level_value
        # The product name to which the column data in the data asset table belongs. Valid values: **MaxCompute, OSS, ADS, OTS, RDS**, and others.
        self.product_code = product_code
        # The ID corresponding to the product name to which the data object belongs. Valid values:
        # 
        # - **1**: MaxCompute
        # 
        # - **2**: OSS
        # 
        # - **3**: ADB-MYSQL
        # 
        # - **4**: TableStore
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
        # The region where the asset is located.
        self.region_id = region_id
        # Correction record ID.
        self.revision_id = revision_id
        # Correction status. Valid values:
        # 
        # - 1: Corrected.
        # 
        # - 0: Not corrected.
        self.revision_status = revision_status
        # The risk level ID of the column data in the data asset table. Valid values:
        # 
        # - **1**: N/A.
        # 
        # - **2**: S1.
        # 
        # - **3**: S2.
        # 
        # - **4**: S3.
        # 
        # - **5**: S4.
        self.risk_level_id = risk_level_id
        # The risk level name of the column data in the data asset table. Valid values:
        # 
        # - **N/A**: No sensitive data detected.
        # 
        # - **S1**: Level 1 sensitive data.
        # 
        # - **S2**: Level 2 sensitive data.
        # 
        # - **S3**: Level 3 sensitive data.
        # 
        # - **S4**: Level 4 sensitive data.
        self.risk_level_name = risk_level_name
        # The ID of the sensitive data detection rule hit by the column data in the data asset table.
        self.rule_id = rule_id
        # The name of the sensitive data detection rule hit by the column data in the data asset table.
        self.rule_name = rule_name
        # Sensitivity level name. Valid values:
        # 
        # - **N/A**: No sensitive data detected.
        # 
        # - **S1**: Level 1 sensitive data.
        # 
        # - **S2**: Level 2 sensitive data.
        # 
        # - **S3**: Level 3 sensitive data.
        # 
        # - **S4**: Level 4 sensitive data.
        self.sens_level_name = sens_level_name
        # Indicates whether the column data in the data asset table contains sensitive data. Valid values:
        # 
        # - true: The column data in the data asset table contains sensitive data.
        # 
        # - false: The column data in the data asset table does not contain sensitive data.
        self.sensitive = sensitive
        # The ID of the asset table to which the column data in the data asset table belongs.
        self.table_id = table_id
        # The name of the table to which the target column for correction belongs.
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
        # The data tag ID of the detection model.
        # 
        # - **101**: Personal sensitive information.
        # 
        # - **102**: Personal information.
        # 
        # - **103**: Important data.
        self.id = id
        # The data tag name of the detection model.
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


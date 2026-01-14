# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeDataAssetsResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeDataAssetsResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # An array that consists of data assets.
        self.items = items
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of queried data assets that contain sensitive data.
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
                temp_model = main_models.DescribeDataAssetsResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeDataAssetsResponseBodyItems(DaraModel):
    def __init__(
        self,
        acl: str = None,
        creation_time: int = None,
        data_type: str = None,
        id: str = None,
        labelsec: bool = None,
        name: str = None,
        object_key: str = None,
        odps_risk_level_name: str = None,
        owner: str = None,
        product_code: str = None,
        product_id: str = None,
        protection: bool = None,
        risk_level_id: int = None,
        risk_level_name: str = None,
        rule_name: str = None,
        sensitive: bool = None,
        sensitive_count: int = None,
        sensitive_ratio: str = None,
        total_count: int = None,
    ):
        # The access control list (ACL) that controls the access permissions on the OSS bucket.
        # 
        # > This parameter is returned only when you set the parameter **RangeId** to **21**.
        self.acl = acl
        # The time when the data asset was created. Unit: milliseconds.
        self.creation_time = creation_time
        # The data type of the data asset.
        self.data_type = data_type
        # The ID of the data asset.
        self.id = id
        # The sensitivity tag of the data. The value is fixed as **0**. **0**, **1**, **2**, or **3** is returned for this parameter only when you set the parameter **RangeId** to **1**.
        # 
        # *   **0**: unclassified
        # *   **1**: confidential
        # *   **2**: sensitive
        # *   **3**: highly sensitive
        self.labelsec = labelsec
        # The name of the data asset.
        self.name = name
        # The key value of the OSS object.
        # 
        # > This parameter is returned only when you set the parameter **RangeId** to **22**.
        self.object_key = object_key
        # The sensitivity level of the MaxCompute data asset. Valid values:
        # 
        # *   **S1**: low sensitivity level
        # *   **S2**: medium sensitivity level
        # *   **S3**: high sensitivity level
        # *   **S4**: highest sensitivity level
        # 
        # > This parameter is returned only when you set the parameter **RangeId** to **1**.
        self.odps_risk_level_name = odps_risk_level_name
        # The account that owns the data asset.
        self.owner = owner
        # The name of the service to which the data asset belongs.
        self.product_code = product_code
        # The ID of the service to which the data asset belongs. Valid values:
        # 
        # *   **1**: MaxCompute
        # *   **2**: OSS
        # *   **3**: AnalyticDB for MySQL
        # *   **4**: Tablestore
        # *   **5**: ApsaraDB RDS
        self.product_id = product_id
        # Indicates whether the data protection mechanism is enabled for the data asset. The value is fixed as **false**. **true** or **false** is returned for this parameter only when you set the parameter **RangeId** to **1**.
        # 
        # *   **false**: The data protection mechanism is disabled.
        # *   **true**: The data protection mechanism is enabled. Only data inbound is supported. Data outbound is not supported.
        self.protection = protection
        # The sensitivity level of the data asset. A higher sensitivity level indicates that the identified data is more sensitive. Valid values:
        # 
        # *   **1**: No sensitive data is identified.
        # *   **2**: sensitive data at level 1.
        # *   **3**: sensitive data at level 2.
        # *   **3**: sensitive data at level 3.
        # *   **5**: sensitive data at level 4.
        # *   **6**: sensitive data at level 5.
        # *   **7**: sensitive data at level 6.
        # *   **8**: sensitive data at level 7.
        # *   **9**: sensitive data at level 8.
        # *   **10**: sensitive data at level 9.
        # *   **11**: sensitive data at level 10.
        self.risk_level_id = risk_level_id
        # The name of the sensitivity level for the data asset.
        self.risk_level_name = risk_level_name
        # The name of the sensitive data detection rule that the data asset hits.
        self.rule_name = rule_name
        # Indicates whether the data asset contains sensitive data. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.sensitive = sensitive
        # The total number of sensitive data assets. For example, the value can be the total number of sensitive MaxCompute projects, packages, or tables, the total number of sensitive ApsaraDB RDS databases or tables, or the total number of sensitive OSS buckets or objects.
        self.sensitive_count = sensitive_count
        # The percentage of sensitive data in all data assets.
        self.sensitive_ratio = sensitive_ratio
        # The total number of data assets. For example, the value can be the total number of MaxCompute projects, packages, or tables, the total number of ApsaraDB RDS databases or tables, or the total number of OSS buckets or objects.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.acl is not None:
            result['Acl'] = self.acl

        if self.creation_time is not None:
            result['CreationTime'] = self.creation_time

        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.id is not None:
            result['Id'] = self.id

        if self.labelsec is not None:
            result['Labelsec'] = self.labelsec

        if self.name is not None:
            result['Name'] = self.name

        if self.object_key is not None:
            result['ObjectKey'] = self.object_key

        if self.odps_risk_level_name is not None:
            result['OdpsRiskLevelName'] = self.odps_risk_level_name

        if self.owner is not None:
            result['Owner'] = self.owner

        if self.product_code is not None:
            result['ProductCode'] = self.product_code

        if self.product_id is not None:
            result['ProductId'] = self.product_id

        if self.protection is not None:
            result['Protection'] = self.protection

        if self.risk_level_id is not None:
            result['RiskLevelId'] = self.risk_level_id

        if self.risk_level_name is not None:
            result['RiskLevelName'] = self.risk_level_name

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.sensitive is not None:
            result['Sensitive'] = self.sensitive

        if self.sensitive_count is not None:
            result['SensitiveCount'] = self.sensitive_count

        if self.sensitive_ratio is not None:
            result['SensitiveRatio'] = self.sensitive_ratio

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Acl') is not None:
            self.acl = m.get('Acl')

        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Labelsec') is not None:
            self.labelsec = m.get('Labelsec')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ObjectKey') is not None:
            self.object_key = m.get('ObjectKey')

        if m.get('OdpsRiskLevelName') is not None:
            self.odps_risk_level_name = m.get('OdpsRiskLevelName')

        if m.get('Owner') is not None:
            self.owner = m.get('Owner')

        if m.get('ProductCode') is not None:
            self.product_code = m.get('ProductCode')

        if m.get('ProductId') is not None:
            self.product_id = m.get('ProductId')

        if m.get('Protection') is not None:
            self.protection = m.get('Protection')

        if m.get('RiskLevelId') is not None:
            self.risk_level_id = m.get('RiskLevelId')

        if m.get('RiskLevelName') is not None:
            self.risk_level_name = m.get('RiskLevelName')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Sensitive') is not None:
            self.sensitive = m.get('Sensitive')

        if m.get('SensitiveCount') is not None:
            self.sensitive_count = m.get('SensitiveCount')

        if m.get('SensitiveRatio') is not None:
            self.sensitive_ratio = m.get('SensitiveRatio')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self


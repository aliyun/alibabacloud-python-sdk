# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sddp20190103 import models as main_models
from darabonba.model import DaraModel

class DescribeInstancesResponseBody(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        items: List[main_models.DescribeInstancesResponseBodyItems] = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The page number of the returned page.
        self.current_page = current_page
        # The data assets.
        self.items = items
        # The number of entries returned per page.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # The total number of data assets.
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
                temp_model = main_models.DescribeInstancesResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesResponseBodyItems(DaraModel):
    def __init__(
        self,
        creation_time: int = None,
        depart_name: str = None,
        id: int = None,
        instance_description: str = None,
        labelsec: bool = None,
        last_finish_time: int = None,
        member_ali_uid: str = None,
        model_tags: List[main_models.DescribeInstancesResponseBodyItemsModelTags] = None,
        name: str = None,
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
        tenant_name: str = None,
        total_count: int = None,
    ):
        # The time when the data asset was created. The value is a UNIX timestamp. Unit: milliseconds.
        self.creation_time = creation_time
        # The name of the department to which the data asset belongs.
        self.depart_name = depart_name
        # The unique ID of the data asset in DSC.
        self.id = id
        # The description of the data asset.
        self.instance_description = instance_description
        # The security status of the data asset. Valid values:
        # 
        # *   **true**: The data asset is secure.
        # *   **false**: The data asset is insecure.
        self.labelsec = labelsec
        # The time when the data asset was last scanned. The value is a UNIX timestamp. Unit: milliseconds.
        self.last_finish_time = last_finish_time
        # If the management account has opened multiple accounts and the asset belongs to other member accounts, this field displays the UID of the member accounts.
        self.member_ali_uid = member_ali_uid
        # A list of tags.
        self.model_tags = model_tags
        # The name of the data asset.
        self.name = name
        # This parameter is deprecated.
        self.odps_risk_level_name = odps_risk_level_name
        # The Alibaba Cloud account to which the data asset belongs.
        self.owner = owner
        # The name of the service to which the data asset belongs, such as MaxCompute, OSS, and ApsaraDB RDS. For more information about the types of data assets that DSC can scan to detect sensitive data, see [Supported data assets](https://help.aliyun.com/document_detail/212906.html).
        self.product_code = product_code
        # The ID of the service to which the data asset belongs.
        self.product_id = product_id
        # The protection status of the data asset. Valid values:
        # 
        # *   **true**: The data asset is being protected.
        # *   **false**: The data asset is not protected.
        self.protection = protection
        # The ID of the sensitivity level for the data asset. A higher sensitivity level ID indicates that the identified data is more sensitive.
        # 
        # *   **1**: No sensitive data is detected.
        # *   **2**: sensitive data at level 1.
        # *   **3**: sensitive data at level 2.
        # *   **4**: sensitive data at level 3.
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
        # *   **true**
        # *   **false**
        self.sensitive = sensitive
        # The number of sensitive data objects in the data asset. For example, if the data asset is an ApsaraDB RDS instance, the value indicates the number of sensitive tables in all databases of the instance.
        self.sensitive_count = sensitive_count
        # The name of the tenant.
        self.tenant_name = tenant_name
        # The total number of data objects in the data asset. For example, if the data asset is an ApsaraDB RDS instance, the value indicates the total number of tables in all databases of the instance.
        self.total_count = total_count

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

        if self.depart_name is not None:
            result['DepartName'] = self.depart_name

        if self.id is not None:
            result['Id'] = self.id

        if self.instance_description is not None:
            result['InstanceDescription'] = self.instance_description

        if self.labelsec is not None:
            result['Labelsec'] = self.labelsec

        if self.last_finish_time is not None:
            result['LastFinishTime'] = self.last_finish_time

        if self.member_ali_uid is not None:
            result['MemberAliUid'] = self.member_ali_uid

        result['ModelTags'] = []
        if self.model_tags is not None:
            for k1 in self.model_tags:
                result['ModelTags'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

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

        if self.tenant_name is not None:
            result['TenantName'] = self.tenant_name

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreationTime') is not None:
            self.creation_time = m.get('CreationTime')

        if m.get('DepartName') is not None:
            self.depart_name = m.get('DepartName')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('InstanceDescription') is not None:
            self.instance_description = m.get('InstanceDescription')

        if m.get('Labelsec') is not None:
            self.labelsec = m.get('Labelsec')

        if m.get('LastFinishTime') is not None:
            self.last_finish_time = m.get('LastFinishTime')

        if m.get('MemberAliUid') is not None:
            self.member_ali_uid = m.get('MemberAliUid')

        self.model_tags = []
        if m.get('ModelTags') is not None:
            for k1 in m.get('ModelTags'):
                temp_model = main_models.DescribeInstancesResponseBodyItemsModelTags()
                self.model_tags.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

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

        if m.get('TenantName') is not None:
            self.tenant_name = m.get('TenantName')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstancesResponseBodyItemsModelTags(DaraModel):
    def __init__(
        self,
        id: int = None,
        name: str = None,
    ):
        # The ID of the tag. Valid values:
        # 
        # *   **101**: personal sensitive information
        # *   **102**: personal information
        # *   **107**: general information
        self.id = id
        # The name of the tag. Valid values:
        # 
        # *   Personal sensitive information
        # *   Personal information
        # *   General information
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


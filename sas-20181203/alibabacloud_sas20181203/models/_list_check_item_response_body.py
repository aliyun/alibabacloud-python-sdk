# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCheckItemResponseBody(DaraModel):
    def __init__(
        self,
        check_items: List[main_models.ListCheckItemResponseBodyCheckItems] = None,
        page_info: main_models.ListCheckItemResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The check items.
        self.check_items = check_items
        # The pagination information.
        self.page_info = page_info
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.check_items:
            for v1 in self.check_items:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckItems'] = []
        if self.check_items is not None:
            for k1 in self.check_items:
                result['CheckItems'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_items = []
        if m.get('CheckItems') is not None:
            for k1 in m.get('CheckItems'):
                temp_model = main_models.ListCheckItemResponseBodyCheckItems()
                self.check_items.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListCheckItemResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCheckItemResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number of the returned page.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCheckItemResponseBodyCheckItems(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        check_show_name: str = None,
        check_type: str = None,
        custom_configs: List[main_models.ListCheckItemResponseBodyCheckItemsCustomConfigs] = None,
        description: main_models.ListCheckItemResponseBodyCheckItemsDescription = None,
        estimated_count: int = None,
        instance_sub_type: str = None,
        instance_type: str = None,
        risk_level: str = None,
        section_ids: List[int] = None,
        vendor: str = None,
    ):
        # The ID of the check item.
        self.check_id = check_id
        # The name of the check item.
        self.check_show_name = check_show_name
        # The source type of the Situation Awareness check item: 
        # - **CUSTOM**: User-defined 
        # - **SYSTEM**: Predefined by the Situation Awareness platform
        self.check_type = check_type
        # The check items.
        self.custom_configs = custom_configs
        # The description of the check item.
        self.description = description
        # The estimated quota that will be consumed by this check item.
        self.estimated_count = estimated_count
        # The asset subtype of the cloud service. Valid values:
        # 
        # *   If **InstanceType** is set to **ECS**, this parameter supports the following valid values:
        # 
        #     *   **INSTANCE**
        #     *   **DISK**
        #     *   **SECURITY_GROUP**
        # 
        # *   If **InstanceType** is set to **ACR**, this parameter supports the following valid values:
        # 
        #     *   **REPOSITORY_ENTERPRISE**
        #     *   **REPOSITORY_PERSON**
        # 
        # *   If **InstanceType** is set to **RAM**, this parameter supports the following valid values:
        # 
        #     *   **ALIAS**
        #     *   **USER**
        #     *   **POLICY**
        #     *   **GROUP**
        # 
        # *   If **InstanceType** is set to **WAF**, this parameter supports the following valid value:
        # 
        #     *   **DOMAIN**
        # 
        # *   If **InstanceType** is set to other values, this parameter supports the following valid values:
        # 
        #     *   **INSTANCE**
        self.instance_sub_type = instance_sub_type
        # The asset type of the cloud service. Valid values:
        # 
        # *   **ECS**: Elastic Compute Service (ECS).
        # *   **SLB**: Server Load Balancer (SLB).
        # *   **RDS**: ApsaraDB RDS.
        # *   **MONGODB**: ApsaraDB for MongoDB (MongoDB).
        # *   **KVSTORE**: ApsaraDB for Redis (Redis).
        # *   **ACR**: Container Registry.
        # *   **CSK**: Container Service for Kubernetes (ACK).
        # *   **VPC**: Virtual Private Cloud (VPC).
        # *   **ACTIONTRAIL**: ActionTrail.
        # *   **CDN**: Alibaba Cloud CDN (CDN).
        # *   **CAS**: Certificate Management Service (formerly SSL Certificates Service).
        # *   **RDC**: Apsara Devops.
        # *   **RAM**: Resource Access Management (RAM).
        # *   **DDOS**: Anti-DDoS.
        # *   **WAF**: Web Application Firewall (WAF).
        # *   **OSS**: Object Storage Service (OSS).
        # *   **POLARDB**: PolarDB.
        # *   **POSTGRESQL**: ApsaraDB RDS for PostgreSQL.
        # *   **MSE**: Microservices Engine (MSE).
        # *   **NAS**: File Storage NAS (NAS).
        # *   **SDDP**: Sensitive Data Discovery and Protection (SDDP).
        # *   **EIP**: Elastic IP Address (EIP).
        self.instance_type = instance_type
        # The risk level of the check item. Valid values:
        # 
        # *   **HIGH**
        # *   **MEDIUM**
        # *   **LOW**
        self.risk_level = risk_level
        # The IDs of the sections associated with the check items.
        self.section_ids = section_ids
        # The type of the cloud asset. Valid values:
        # 
        # *   **0**: an asset provided by Alibaba Cloud.
        # *   **1**: an asset outside Alibaba Cloud.
        # *   **2**: an asset in a data center.
        # *   **3**, **4**, **5**, and **7**: other cloud asset.
        # *   **8**: a simple application server.
        self.vendor = vendor

    def validate(self):
        if self.custom_configs:
            for v1 in self.custom_configs:
                 if v1:
                    v1.validate()
        if self.description:
            self.description.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_show_name is not None:
            result['CheckShowName'] = self.check_show_name

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        result['CustomConfigs'] = []
        if self.custom_configs is not None:
            for k1 in self.custom_configs:
                result['CustomConfigs'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description.to_map()

        if self.estimated_count is not None:
            result['EstimatedCount'] = self.estimated_count

        if self.instance_sub_type is not None:
            result['InstanceSubType'] = self.instance_sub_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.section_ids is not None:
            result['SectionIds'] = self.section_ids

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckShowName') is not None:
            self.check_show_name = m.get('CheckShowName')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        self.custom_configs = []
        if m.get('CustomConfigs') is not None:
            for k1 in m.get('CustomConfigs'):
                temp_model = main_models.ListCheckItemResponseBodyCheckItemsCustomConfigs()
                self.custom_configs.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            temp_model = main_models.ListCheckItemResponseBodyCheckItemsDescription()
            self.description = temp_model.from_map(m.get('Description'))

        if m.get('EstimatedCount') is not None:
            self.estimated_count = m.get('EstimatedCount')

        if m.get('InstanceSubType') is not None:
            self.instance_sub_type = m.get('InstanceSubType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('SectionIds') is not None:
            self.section_ids = m.get('SectionIds')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class ListCheckItemResponseBodyCheckItemsDescription(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The type of the description of the check item. Valid value:
        # 
        # *   **text**
        self.type = type
        # The content of the description for the check item when the Type parameter is text.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListCheckItemResponseBodyCheckItemsCustomConfigs(DaraModel):
    def __init__(
        self,
        default_value: str = None,
        name: str = None,
        show_name: str = None,
        type_define: str = None,
        value: str = None,
    ):
        # The default value of the check item. The value is a string.
        self.default_value = default_value
        # The name of the check item.
        self.name = name
        # The display name of the check item.
        self.show_name = show_name
        # The type of the check item. The value is a JSON string.
        self.type_define = type_define
        # The specified value of the check item. The value is a string.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.default_value is not None:
            result['DefaultValue'] = self.default_value

        if self.name is not None:
            result['Name'] = self.name

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.type_define is not None:
            result['TypeDefine'] = self.type_define

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DefaultValue') is not None:
            self.default_value = m.get('DefaultValue')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('TypeDefine') is not None:
            self.type_define = m.get('TypeDefine')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


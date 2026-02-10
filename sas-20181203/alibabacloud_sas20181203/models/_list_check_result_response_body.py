# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCheckResultResponseBody(DaraModel):
    def __init__(
        self,
        checks: List[main_models.ListCheckResultResponseBodyChecks] = None,
        page_info: main_models.ListCheckResultResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # The check items.
        self.checks = checks
        # The pagination information.
        self.page_info = page_info
        # The ID of the request.
        self.request_id = request_id

    def validate(self):
        if self.checks:
            for v1 in self.checks:
                 if v1:
                    v1.validate()
        if self.page_info:
            self.page_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Checks'] = []
        if self.checks is not None:
            for k1 in self.checks:
                result['Checks'].append(k1.to_map() if k1 else None)

        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.checks = []
        if m.get('Checks') is not None:
            for k1 in m.get('Checks'):
                temp_model = main_models.ListCheckResultResponseBodyChecks()
                self.checks.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListCheckResultResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListCheckResultResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of entries returned on the current page.
        self.count = count
        # The page number.
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

class ListCheckResultResponseBodyChecks(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        asset_vendor: int = None,
        check_id: int = None,
        check_policies: List[main_models.ListCheckResultResponseBodyChecksCheckPolicies] = None,
        check_sale_type: int = None,
        check_show_name: str = None,
        check_type: str = None,
        instance_sub_type: str = None,
        instance_type: str = None,
        last_check_time: int = None,
        operation_type: str = None,
        risk_level: str = None,
        status: str = None,
        status_message: str = None,
        task_id: str = None,
        trial_permission: bool = None,
        trial_permission_type: int = None,
        vendor: str = None,
        vendor_show_name: str = None,
    ):
        # The subtype of the cloud service.
        self.asset_sub_type = asset_sub_type
        # The type of the asset. Valid values:
        # 
        # *   **0**: an ECS instance
        # *   **1**: a SLB instance
        # *   **2**: a NAT gateway
        # *   **3**: an ApsaraDB RDS instance
        # *   **4**: an ApsaraDB for MongoDB instance
        # *   **5**: an ApsaraDB for Redis instance
        # *   **6**: a container image
        # *   **7**: a container
        self.asset_type = asset_type
        # The service provider of the asset. Valid values:
        # 
        # *   **0**: Alibaba Cloud
        # *   **3**: Huawei Cloud
        # *   **4**: Microsoft Azure
        # *   **5**: AWS
        # *   **7**: Tencent Cloud
        self.asset_vendor = asset_vendor
        # The ID of the check item.
        self.check_id = check_id
        # The check policies.
        self.check_policies = check_policies
        # The type of the check item. Valid values:
        # 
        # *   **0**: paid
        # *   **1**: free
        self.check_sale_type = check_sale_type
        # The name of the check item.
        self.check_show_name = check_show_name
        # The source type of the situation awareness check item: 
        # - **CUSTOM**: User-defined 
        # - **SYSTEM**: Predefined by the situation awareness platform
        self.check_type = check_type
        # The asset subtype of the cloud service. Valid values:
        # 
        # *   If the **InstanceType** parameter is set to **ECS**, this parameter supports the following valid values:
        # 
        #     *   **INSTANCE**
        #     *   **DISK**
        #     *   **SECURITY_GROUP**
        # 
        # *   If the **InstanceType** parameter is set to **ACR**, this parameter supports the following valid values:
        # 
        #     *   **REPOSITORY_ENTERPRISE**
        #     *   **REPOSITORY_PERSON**
        # 
        # *   If the **InstanceType** parameter is set to **RAM**, this parameter supports the following valid values:
        # 
        #     *   **ALIAS**
        #     *   **USER**
        #     *   **POLICY**
        #     *   **GROUP**
        # 
        # *   If the **InstanceType** parameter is set to **WAF**, this parameter supports the following valid values:
        # 
        #     *   **DOMAIN**
        # 
        # *   If the **InstanceType** parameter is set to other values, this parameter supports the following valid values:
        # 
        #     *   **INSTANCE**
        self.instance_sub_type = instance_sub_type
        # The asset type of the cloud service. Valid values:
        # 
        # *   **ECS**: ECS
        # *   **SLB**: SLB
        # *   **RDS**: ApsaraDB RDS
        # *   **MONGODB**: MongoDB
        # *   **KVSTORE**: Redis
        # *   **ACR**: Container Registry
        # *   **CSK**: ACK
        # *   **VPC**: VPC
        # *   **ACTIONTRAIL**: ActionTrail
        # *   **CDN**: CDN
        # *   **CAS**: Certificate Management Service (formerly SSL Certificates Service)
        # *   **RDC**: Apsara Devops
        # *   **RAM**: RAM
        # *   **DDOS**: Anti-DDoS
        # *   **WAF**: WAF
        # *   **OSS**: OSS
        # *   **POLARDB**: PolarDB
        # *   **POSTGRESQL**: ApsaraDB RDS for PostgreSQL
        # *   **MSE**: MSE
        # *   **NAS**: NAS
        # *   **SDDP**: SDDP
        # *   **EIP**: EIP
        self.instance_type = instance_type
        # The timestamp when the last check was performed. Unit: milliseconds.
        self.last_check_time = last_check_time
        # Indicates whether fixing is supported. Valid values:
        # 
        # *   **SUPPORT_REPAIR**
        # *   **NOT_SUPPORT_REPAIR**
        self.operation_type = operation_type
        # The risk level of the check item. Valid values:
        # 
        # *   **HIGH**
        # *   **MEDIUM**
        # *   **LOW**
        self.risk_level = risk_level
        # The status of the check item. Valid values:
        # 
        # *   **PASS**: passed
        # *   **NOT_PASS**: failed
        # *   **CHECKING**: being checked
        # *   **NOT_CHECK**: not checked
        # *   **WHITELIST**: added to the whitelist
        self.status = status
        # The message returned if the status of the check item is abnormal.
        self.status_message = status_message
        # The ID of the check task.
        self.task_id = task_id
        # Indicates whether the TRIAL permission is required.
        self.trial_permission = trial_permission
        # Check whether the data delivery period for ActionTrail is enabled for more than 30 days to establish a baseline of behaviour.
        # *   **0**: REQUIRED
        # *   **1**: NOT REQUIRED
        self.trial_permission_type = trial_permission_type
        # The cloud service provider.
        self.vendor = vendor
        # The name of the cloud service provider.
        self.vendor_show_name = vendor_show_name

    def validate(self):
        if self.check_policies:
            for v1 in self.check_policies:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asset_sub_type is not None:
            result['AssetSubType'] = self.asset_sub_type

        if self.asset_type is not None:
            result['AssetType'] = self.asset_type

        if self.asset_vendor is not None:
            result['AssetVendor'] = self.asset_vendor

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        result['CheckPolicies'] = []
        if self.check_policies is not None:
            for k1 in self.check_policies:
                result['CheckPolicies'].append(k1.to_map() if k1 else None)

        if self.check_sale_type is not None:
            result['CheckSaleType'] = self.check_sale_type

        if self.check_show_name is not None:
            result['CheckShowName'] = self.check_show_name

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.instance_sub_type is not None:
            result['InstanceSubType'] = self.instance_sub_type

        if self.instance_type is not None:
            result['InstanceType'] = self.instance_type

        if self.last_check_time is not None:
            result['LastCheckTime'] = self.last_check_time

        if self.operation_type is not None:
            result['OperationType'] = self.operation_type

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.status is not None:
            result['Status'] = self.status

        if self.status_message is not None:
            result['StatusMessage'] = self.status_message

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trial_permission is not None:
            result['TrialPermission'] = self.trial_permission

        if self.trial_permission_type is not None:
            result['TrialPermissionType'] = self.trial_permission_type

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        if self.vendor_show_name is not None:
            result['VendorShowName'] = self.vendor_show_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSubType') is not None:
            self.asset_sub_type = m.get('AssetSubType')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('AssetVendor') is not None:
            self.asset_vendor = m.get('AssetVendor')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        self.check_policies = []
        if m.get('CheckPolicies') is not None:
            for k1 in m.get('CheckPolicies'):
                temp_model = main_models.ListCheckResultResponseBodyChecksCheckPolicies()
                self.check_policies.append(temp_model.from_map(k1))

        if m.get('CheckSaleType') is not None:
            self.check_sale_type = m.get('CheckSaleType')

        if m.get('CheckShowName') is not None:
            self.check_show_name = m.get('CheckShowName')

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('InstanceSubType') is not None:
            self.instance_sub_type = m.get('InstanceSubType')

        if m.get('InstanceType') is not None:
            self.instance_type = m.get('InstanceType')

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('OperationType') is not None:
            self.operation_type = m.get('OperationType')

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TrialPermission') is not None:
            self.trial_permission = m.get('TrialPermission')

        if m.get('TrialPermissionType') is not None:
            self.trial_permission_type = m.get('TrialPermissionType')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        if m.get('VendorShowName') is not None:
            self.vendor_show_name = m.get('VendorShowName')

        return self

class ListCheckResultResponseBodyChecksCheckPolicies(DaraModel):
    def __init__(
        self,
        requirement_id: int = None,
        requirement_show_name: str = None,
        section_id: int = None,
        section_show_name: str = None,
        standard_id: int = None,
        standard_show_name: str = None,
    ):
        # The ID of the requirement item for the check item.
        self.requirement_id = requirement_id
        # The display name of the requirement item for the check item.
        self.requirement_show_name = requirement_show_name
        # The ID of the section for the check item.
        self.section_id = section_id
        # The display name of the section for the check item.
        self.section_show_name = section_show_name
        # The standard ID of the check item.
        self.standard_id = standard_id
        # The standard display name of the check item.
        self.standard_show_name = standard_show_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.requirement_id is not None:
            result['RequirementId'] = self.requirement_id

        if self.requirement_show_name is not None:
            result['RequirementShowName'] = self.requirement_show_name

        if self.section_id is not None:
            result['SectionId'] = self.section_id

        if self.section_show_name is not None:
            result['SectionShowName'] = self.section_show_name

        if self.standard_id is not None:
            result['StandardId'] = self.standard_id

        if self.standard_show_name is not None:
            result['StandardShowName'] = self.standard_show_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequirementId') is not None:
            self.requirement_id = m.get('RequirementId')

        if m.get('RequirementShowName') is not None:
            self.requirement_show_name = m.get('RequirementShowName')

        if m.get('SectionId') is not None:
            self.section_id = m.get('SectionId')

        if m.get('SectionShowName') is not None:
            self.section_show_name = m.get('SectionShowName')

        if m.get('StandardId') is not None:
            self.standard_id = m.get('StandardId')

        if m.get('StandardShowName') is not None:
            self.standard_show_name = m.get('StandardShowName')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListClusterCheckResultResponseBody(DaraModel):
    def __init__(
        self,
        checks: List[main_models.ListClusterCheckResultResponseBodyChecks] = None,
        page_info: main_models.ListClusterCheckResultResponseBodyPageInfo = None,
        request_id: str = None,
    ):
        # Information on check results.
        self.checks = checks
        # Pagination information.
        self.page_info = page_info
        # The ID of the current request.
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
                temp_model = main_models.ListClusterCheckResultResponseBodyChecks()
                self.checks.append(temp_model.from_map(k1))

        if m.get('PageInfo') is not None:
            temp_model = main_models.ListClusterCheckResultResponseBodyPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListClusterCheckResultResponseBodyPageInfo(DaraModel):
    def __init__(
        self,
        count: int = None,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The number of data entries displayed on the current page during pagination.
        self.count = count
        # Page number in the pagination query.
        self.current_page = current_page
        # Number of items per page in the pagination query. The default value is **20**, indicating that 20 items are displayed per page.
        self.page_size = page_size
        # The total number of data entries.
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

class ListClusterCheckResultResponseBodyChecks(DaraModel):
    def __init__(
        self,
        asset_sub_type: int = None,
        asset_type: int = None,
        check_id: int = None,
        check_policies: List[main_models.ListClusterCheckResultResponseBodyChecksCheckPolicies] = None,
        check_show_name: str = None,
        check_type: str = None,
        instance_sub_type: str = None,
        instance_type: str = None,
        last_check_time: int = None,
        risk_level: str = None,
        status: str = None,
        trial_permission: bool = None,
        trial_permission_type: int = None,
        vendor: str = None,
    ):
        # Subtype of the cloud product.
        self.asset_sub_type = asset_sub_type
        # Asset type.
        self.asset_type = asset_type
        # ID of the check item.
        self.check_id = check_id
        # Information about the standards, requirements, and sections associated with the check result.
        self.check_policies = check_policies
        # Name of the check item.
        self.check_show_name = check_show_name
        # Source type of the security check item:
        #  - **CUSTOM**：User-defined
        #  - **SYSTEM**：Predefined by the Security Platform
        self.check_type = check_type
        # Subtype of the cloud product asset. Values:
        # 
        # - When **InstanceType** is **ECS**, this parameter can take the following values:
        #     - **INSTANCE**
        #     - **DISK**
        #     - **SECURITY_GROUP**
        # - When **InstanceType** is **ACR**, this parameter can take the following values:
        #     - **REPOSITORY_ENTERPRISE**
        #     - **REPOSITORY_PERSON**
        # - When **InstanceType** is **RAM**, this parameter can take the following values:
        #     - **ALIAS**
        #     - **USER**
        #     - **POLICY**
        #     - **GROUP**
        # - When **InstanceType** is **WAF**, this parameter can take the following values:
        #     - **DOMAIN**
        # - For other **InstanceType** values, this parameter can take the following value:
        #     - **INSTANCE**
        self.instance_sub_type = instance_sub_type
        # Asset type of the cloud product.
        self.instance_type = instance_type
        # Timestamp of the latest check, in milliseconds.
        self.last_check_time = last_check_time
        # Risk level of the check item. Possible values:
        # 
        # - **HIGH**：High
        # - **MEDIUM**：Medium
        # - **LOW**：Low
        self.risk_level = risk_level
        # Status of the check item. Values:
        # 
        # - **PASS**: Passed
        # - **NOT_PASS**: Not passed
        # - **CHECKING**: Checking
        # - **NOT_CHECK**: Not checked
        # - **WHITELIST**: Whitelisted
        self.status = status
        # Whether the check depends on TRIAL permissions.
        self.trial_permission = trial_permission
        # Whether the check item requires enabling data delivery of operation audit for more than 30 days to build a behavior baseline.
        # - **1**：Required
        # - **0**：Not Required
        self.trial_permission_type = trial_permission_type
        # Vendor of the asset. Values:
        # 
        # 0: Alibaba Cloud
        # 3: Other cloud
        # 4: Other cloud
        # 5: Other cloud
        # 7: Other cloud
        self.vendor = vendor

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

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        result['CheckPolicies'] = []
        if self.check_policies is not None:
            for k1 in self.check_policies:
                result['CheckPolicies'].append(k1.to_map() if k1 else None)

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

        if self.risk_level is not None:
            result['RiskLevel'] = self.risk_level

        if self.status is not None:
            result['Status'] = self.status

        if self.trial_permission is not None:
            result['TrialPermission'] = self.trial_permission

        if self.trial_permission_type is not None:
            result['TrialPermissionType'] = self.trial_permission_type

        if self.vendor is not None:
            result['Vendor'] = self.vendor

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssetSubType') is not None:
            self.asset_sub_type = m.get('AssetSubType')

        if m.get('AssetType') is not None:
            self.asset_type = m.get('AssetType')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        self.check_policies = []
        if m.get('CheckPolicies') is not None:
            for k1 in m.get('CheckPolicies'):
                temp_model = main_models.ListClusterCheckResultResponseBodyChecksCheckPolicies()
                self.check_policies.append(temp_model.from_map(k1))

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

        if m.get('RiskLevel') is not None:
            self.risk_level = m.get('RiskLevel')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TrialPermission') is not None:
            self.trial_permission = m.get('TrialPermission')

        if m.get('TrialPermissionType') is not None:
            self.trial_permission_type = m.get('TrialPermissionType')

        if m.get('Vendor') is not None:
            self.vendor = m.get('Vendor')

        return self

class ListClusterCheckResultResponseBodyChecksCheckPolicies(DaraModel):
    def __init__(
        self,
        requirement_id: int = None,
        requirement_show_name: str = None,
        section_id: int = None,
        section_show_name: str = None,
        standard_id: int = None,
        standard_show_name: str = None,
    ):
        # Requirement ID of the check item.
        self.requirement_id = requirement_id
        # Display name of the requirement for the check item.
        self.requirement_show_name = requirement_show_name
        # Section ID of the check item.
        self.section_id = section_id
        # Display name of the section for the check item.
        self.section_show_name = section_show_name
        # Standard ID of the check item.
        self.standard_id = standard_id
        # Display name of the standard for the check item.
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


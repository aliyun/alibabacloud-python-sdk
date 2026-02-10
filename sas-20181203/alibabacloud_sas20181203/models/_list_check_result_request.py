# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class ListCheckResultRequest(DaraModel):
    def __init__(
        self,
        check_ids: List[int] = None,
        check_key: str = None,
        check_types: List[str] = None,
        current_page: int = None,
        custom_param: bool = None,
        instance_ids: List[str] = None,
        instance_types: List[str] = None,
        lang: str = None,
        operation_types: List[str] = None,
        page_size: int = None,
        region_id: str = None,
        requirement_ids: List[int] = None,
        resource_directory_account_id: int = None,
        risk_levels: List[str] = None,
        sort_types: List[str] = None,
        standard_ids: List[int] = None,
        statuses: List[str] = None,
        task_sources: List[str] = None,
        types: List[str] = None,
        vendors: List[str] = None,
    ):
        # The IDs of the check items.
        self.check_ids = check_ids
        # The key that you want to use to search for check items in fuzzy match mode.
        self.check_key = check_key
        # Source type of the situation awareness check item.
        self.check_types = check_types
        # The page number.
        self.current_page = current_page
        # Specifies whether the check item supports custom parameters. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.custom_param = custom_param
        # The instance IDs of the cloud services that you want to query. Separate multiple IDs with commas (,).
        self.instance_ids = instance_ids
        # The asset type of the cloud services. Valid values:
        # 
        # *   **ECS**: Elastic Compute Service (ECS)
        # *   **SLB**: Server Load Balancer (SLB)
        # *   **RDS**: ApsaraDB RDS
        # *   **MONGODB**: ApsaraDB for MongoDB (MongoDB)
        # *   **KVSTORE**: ApsaraDB for Redis (Redis)
        # *   **ACR**: Container Registry
        # *   **CSK**: Container Service for Kubernetes (ACK)
        # *   **VPC**: Virtual Private Cloud (VPC)
        # *   **ACTIONTRAIL**: ActionTrail
        # *   **CDN**: Alibaba Cloud CDN (CDN)
        # *   **CAS**: Certificate Management Service (formerly SSL Certificates Service)
        # *   **RDC**: Apsara Devops
        # *   **RAM**: Resource Access Management (RAM)
        # *   **DDOS**: Anti-DDoS
        # *   **WAF**: Web Application Firewall (WAF)
        # *   **OSS**: Object Storage Service (OSS)
        # *   **POLARDB**: PolarDB
        # *   **POSTGRESQL**: ApsaraDB RDS for PostgreSQL
        # *   **MSE**: Microservices Engine (MSE)
        # *   **NAS**: File Storage NAS (NAS)
        # *   **SDDP**: Sensitive Data Discovery and Protection (SDDP)
        # *   **EIP**: Elastic IP Address (EIP)
        self.instance_types = instance_types
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang
        # Specifies whether fixing is supported. Valid values:
        # 
        # *   **SUPPORT_REPAIR**
        # *   **NOT_SUPPORT_REPAIR**
        self.operation_types = operation_types
        # The number of entries per page. Maximum value: 100.
        self.page_size = page_size
        # The region ID of the instance. Valid values:
        # 
        # *   **cn-hangzhou**: International
        # *   **ap-southeast-1**: Singapore
        self.region_id = region_id
        # The IDs of the requirements.
        self.requirement_ids = requirement_ids
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the IDs.
        self.resource_directory_account_id = resource_directory_account_id
        # The risk levels of check items. Separate multiple risk levels with commas (,). Valid values:
        # 
        # *   **HIGH**
        # *   **MEDIUM**
        # *   **LOW**
        self.risk_levels = risk_levels
        # The types of the conditions based on which check items are sorted. Valid values:
        # 
        # *   **RISK_LEVEL**: risk level
        # *   **STATUS**: status
        self.sort_types = sort_types
        # The standard IDs.
        self.standard_ids = standard_ids
        # The statuses of check items. Separate multiple statuses with commas (,). Valid values:
        # 
        # *   **PASS**
        # *   **NOT_PASS**
        # *   **CHECKING**
        # *   **NOT_CHECK**
        # *   **WHITELIST**
        self.statuses = statuses
        # Delete the custom category in a custom inspection item.
        self.task_sources = task_sources
        # The types of check standards.
        self.types = types
        # The cloud service providers. Valid values:
        # 
        # *   **ALIYUN**: Alibaba Cloud
        # *   **TENCENT**: Tencent Cloud
        # *   **AWS**: Amazon Web Services (AWS)
        # *   **MICROSOFT**: Microsoft Azure
        self.vendors = vendors

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_ids is not None:
            result['CheckIds'] = self.check_ids

        if self.check_key is not None:
            result['CheckKey'] = self.check_key

        if self.check_types is not None:
            result['CheckTypes'] = self.check_types

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.custom_param is not None:
            result['CustomParam'] = self.custom_param

        if self.instance_ids is not None:
            result['InstanceIds'] = self.instance_ids

        if self.instance_types is not None:
            result['InstanceTypes'] = self.instance_types

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.operation_types is not None:
            result['OperationTypes'] = self.operation_types

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.requirement_ids is not None:
            result['RequirementIds'] = self.requirement_ids

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.risk_levels is not None:
            result['RiskLevels'] = self.risk_levels

        if self.sort_types is not None:
            result['SortTypes'] = self.sort_types

        if self.standard_ids is not None:
            result['StandardIds'] = self.standard_ids

        if self.statuses is not None:
            result['Statuses'] = self.statuses

        if self.task_sources is not None:
            result['TaskSources'] = self.task_sources

        if self.types is not None:
            result['Types'] = self.types

        if self.vendors is not None:
            result['Vendors'] = self.vendors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckIds') is not None:
            self.check_ids = m.get('CheckIds')

        if m.get('CheckKey') is not None:
            self.check_key = m.get('CheckKey')

        if m.get('CheckTypes') is not None:
            self.check_types = m.get('CheckTypes')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('CustomParam') is not None:
            self.custom_param = m.get('CustomParam')

        if m.get('InstanceIds') is not None:
            self.instance_ids = m.get('InstanceIds')

        if m.get('InstanceTypes') is not None:
            self.instance_types = m.get('InstanceTypes')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('OperationTypes') is not None:
            self.operation_types = m.get('OperationTypes')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RequirementIds') is not None:
            self.requirement_ids = m.get('RequirementIds')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('RiskLevels') is not None:
            self.risk_levels = m.get('RiskLevels')

        if m.get('SortTypes') is not None:
            self.sort_types = m.get('SortTypes')

        if m.get('StandardIds') is not None:
            self.standard_ids = m.get('StandardIds')

        if m.get('Statuses') is not None:
            self.statuses = m.get('Statuses')

        if m.get('TaskSources') is not None:
            self.task_sources = m.get('TaskSources')

        if m.get('Types') is not None:
            self.types = m.get('Types')

        if m.get('Vendors') is not None:
            self.vendors = m.get('Vendors')

        return self


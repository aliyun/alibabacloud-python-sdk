# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class ListProjectsResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.ListProjectsResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned results.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.ListProjectsResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class ListProjectsResponseBodyData(DaraModel):
    def __init__(
        self,
        next_token: str = None,
        marker: str = None,
        max_item: int = None,
        projects: List[main_models.ListProjectsResponseBodyDataProjects] = None,
    ):
        # The pagination token. The current operation only supports sequential pagination. A non-empty nextToken value indicates that more data is available. You can use the nextToken value as a parameter to query the next page.
        self.next_token = next_token
        # The marker used to specify the starting point of the returned results. The results are sorted in alphabetical order and returned starting from the first item after the marker.
        self.marker = marker
        # The maximum number of results to return per page.
        self.max_item = max_item
        # The list of projects.
        self.projects = projects

    def validate(self):
        if self.projects:
            for v1 in self.projects:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.marker is not None:
            result['marker'] = self.marker

        if self.max_item is not None:
            result['maxItem'] = self.max_item

        result['projects'] = []
        if self.projects is not None:
            for k1 in self.projects:
                result['projects'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('marker') is not None:
            self.marker = m.get('marker')

        if m.get('maxItem') is not None:
            self.max_item = m.get('maxItem')

        self.projects = []
        if m.get('projects') is not None:
            for k1 in m.get('projects'):
                temp_model = main_models.ListProjectsResponseBodyDataProjects()
                self.projects.append(temp_model.from_map(k1))

        return self

class ListProjectsResponseBodyDataProjects(DaraModel):
    def __init__(
        self,
        comment: str = None,
        cost_storage: str = None,
        created_time: int = None,
        default_quota: str = None,
        ip_white_list: main_models.ListProjectsResponseBodyDataProjectsIpWhiteList = None,
        name: str = None,
        owner: str = None,
        properties: main_models.ListProjectsResponseBodyDataProjectsProperties = None,
        region_id: str = None,
        sale_tag: main_models.ListProjectsResponseBodyDataProjectsSaleTag = None,
        security_properties: main_models.ListProjectsResponseBodyDataProjectsSecurityProperties = None,
        status: str = None,
        three_tier_model: bool = None,
        type: str = None,
    ):
        # The project description.
        self.comment = comment
        # The total storage size. This value indicates the current storage size of the project and is consistent with the billing metric. It represents the logical storage size after data compression at the project level.
        self.cost_storage = cost_storage
        # The creation time. The time is a UNIX timestamp in milliseconds.
        self.created_time = created_time
        # The default compute quota.
        # This is used to allocate compute resources. If no compute quota is specified, jobs initiated in the project consume resources from the default quota. For more information about how to use compute resources, see <props="china">[Use of computing resources](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/use-of-computing-resources)
        # <props="intl">[Use of computing resources](https://www.alibabacloud.com/help/en/maxcompute/user-guide/use-of-computing-resources).
        self.default_quota = default_quota
        # The IP address whitelist.
        self.ip_white_list = ip_white_list
        # The project names.
        self.name = name
        # The account information of the project owner.
        self.owner = owner
        # The basic properties of the project.
        self.properties = properties
        # The region ID.
        self.region_id = region_id
        # The instance ID and billing method of the default compute quota.
        self.sale_tag = sale_tag
        # The security properties.
        self.security_properties = security_properties
        # The project status. Valid values:
        # - **AVAILABLE**: normal
        # - **READONLY**: read-only
        # - **FROZEN**: frozen
        # - **DELETING**: deleting
        self.status = status
        # Specifies whether to support schema-based storage.
        # MaxCompute supports schemas, which are located under projects and used to classify objects such as tables, resources, and UDFs. A project can contain multiple schemas. For more information, see <props="china">[Schema-related operations](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/schema-related-operations)
        # <props="intl">[Schema-related operations](https://www.alibabacloud.com/help/en/maxcompute/user-guide/schema-related-operations).
        self.three_tier_model = three_tier_model
        # The project type. Valid values:
        # - **managed**: internal project
        # - **external**: external project
        self.type = type

    def validate(self):
        if self.ip_white_list:
            self.ip_white_list.validate()
        if self.properties:
            self.properties.validate()
        if self.sale_tag:
            self.sale_tag.validate()
        if self.security_properties:
            self.security_properties.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.comment is not None:
            result['comment'] = self.comment

        if self.cost_storage is not None:
            result['costStorage'] = self.cost_storage

        if self.created_time is not None:
            result['createdTime'] = self.created_time

        if self.default_quota is not None:
            result['defaultQuota'] = self.default_quota

        if self.ip_white_list is not None:
            result['ipWhiteList'] = self.ip_white_list.to_map()

        if self.name is not None:
            result['name'] = self.name

        if self.owner is not None:
            result['owner'] = self.owner

        if self.properties is not None:
            result['properties'] = self.properties.to_map()

        if self.region_id is not None:
            result['regionId'] = self.region_id

        if self.sale_tag is not None:
            result['saleTag'] = self.sale_tag.to_map()

        if self.security_properties is not None:
            result['securityProperties'] = self.security_properties.to_map()

        if self.status is not None:
            result['status'] = self.status

        if self.three_tier_model is not None:
            result['threeTierModel'] = self.three_tier_model

        if self.type is not None:
            result['type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('comment') is not None:
            self.comment = m.get('comment')

        if m.get('costStorage') is not None:
            self.cost_storage = m.get('costStorage')

        if m.get('createdTime') is not None:
            self.created_time = m.get('createdTime')

        if m.get('defaultQuota') is not None:
            self.default_quota = m.get('defaultQuota')

        if m.get('ipWhiteList') is not None:
            temp_model = main_models.ListProjectsResponseBodyDataProjectsIpWhiteList()
            self.ip_white_list = temp_model.from_map(m.get('ipWhiteList'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('properties') is not None:
            temp_model = main_models.ListProjectsResponseBodyDataProjectsProperties()
            self.properties = temp_model.from_map(m.get('properties'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('saleTag') is not None:
            temp_model = main_models.ListProjectsResponseBodyDataProjectsSaleTag()
            self.sale_tag = temp_model.from_map(m.get('saleTag'))

        if m.get('securityProperties') is not None:
            temp_model = main_models.ListProjectsResponseBodyDataProjectsSecurityProperties()
            self.security_properties = temp_model.from_map(m.get('securityProperties'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('threeTierModel') is not None:
            self.three_tier_model = m.get('threeTierModel')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class ListProjectsResponseBodyDataProjectsSecurityProperties(DaraModel):
    def __init__(
        self,
        enable_download_privilege: bool = None,
        label_security: bool = None,
        object_creator_has_access_permission: bool = None,
        object_creator_has_grant_permission: bool = None,
        project_protection: main_models.ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection = None,
        using_acl: bool = None,
        using_policy: bool = None,
    ):
        # Specifies whether to use the <props="china">[download control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/download-control)
        # <props="intl">[download control](https://www.alibabacloud.com/help/en/maxcompute/user-guide/label-based-access-control) feature. By default, this feature is disabled.
        self.enable_download_privilege = enable_download_privilege
        # Specifies whether to use the <props="china">[label-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/label-based-access-control)
        # <props="intl">[label-based access control](https://www.alibabacloud.com/help/en/maxcompute/user-guide/label-based-access-control) feature. By default, this feature is disabled.
        self.label_security = label_security
        # Specifies whether to allow object creators to have access permissions on the objects. By default, this is allowed.
        self.object_creator_has_access_permission = object_creator_has_access_permission
        # Specifies whether to allow object creators to have authorization permissions on the objects. By default, this is allowed.
        self.object_creator_has_grant_permission = object_creator_has_grant_permission
        # The <props="china">[data protection mechanism](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/project-data-protection)
        # <props="intl">[data protection mechanism](https://www.alibabacloud.com/help/en/maxcompute/security-and-compliance/project-data-protection) properties.
        self.project_protection = project_protection
        # Specifies whether to use the <props="china">[ACL-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/acl-based-access-control)
        # <props="intl">[ACL-based access control](https://www.alibabacloud.com/help/en/maxcompute/user-guide/acl-based-access-control) feature. By default, this feature is enabled.
        self.using_acl = using_acl
        # Specifies whether to use the <props="china">[policy-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/policy-based-access-control-1)
        # <props="intl">[policy-based access control](https://www.alibabacloud.com/help/en/maxcompute/user-guide/policy-based-access-control-1) feature. By default, this feature is enabled.
        self.using_policy = using_policy

    def validate(self):
        if self.project_protection:
            self.project_protection.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.enable_download_privilege is not None:
            result['enableDownloadPrivilege'] = self.enable_download_privilege

        if self.label_security is not None:
            result['labelSecurity'] = self.label_security

        if self.object_creator_has_access_permission is not None:
            result['objectCreatorHasAccessPermission'] = self.object_creator_has_access_permission

        if self.object_creator_has_grant_permission is not None:
            result['objectCreatorHasGrantPermission'] = self.object_creator_has_grant_permission

        if self.project_protection is not None:
            result['projectProtection'] = self.project_protection.to_map()

        if self.using_acl is not None:
            result['usingAcl'] = self.using_acl

        if self.using_policy is not None:
            result['usingPolicy'] = self.using_policy

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('enableDownloadPrivilege') is not None:
            self.enable_download_privilege = m.get('enableDownloadPrivilege')

        if m.get('labelSecurity') is not None:
            self.label_security = m.get('labelSecurity')

        if m.get('objectCreatorHasAccessPermission') is not None:
            self.object_creator_has_access_permission = m.get('objectCreatorHasAccessPermission')

        if m.get('objectCreatorHasGrantPermission') is not None:
            self.object_creator_has_grant_permission = m.get('objectCreatorHasGrantPermission')

        if m.get('projectProtection') is not None:
            temp_model = main_models.ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection()
            self.project_protection = temp_model.from_map(m.get('projectProtection'))

        if m.get('usingAcl') is not None:
            self.using_acl = m.get('usingAcl')

        if m.get('usingPolicy') is not None:
            self.using_policy = m.get('usingPolicy')

        return self

class ListProjectsResponseBodyDataProjectsSecurityPropertiesProjectProtection(DaraModel):
    def __init__(
        self,
        exception_policy: str = None,
        protected: bool = None,
    ):
        # If you enable data protection for the project, you can configure exceptions or trusted projects to allow specified users to transfer data of specified objects to specified projects. All scenarios described in the exception policy can bypass the data protection mechanism.
        self.exception_policy = exception_policy
        # Specifies whether to enable the <props="china">[data protection mechanism](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/project-data-protection)
        # <props="intl">[data protection mechanism](https://www.alibabacloud.com/help/en/maxcompute/security-and-compliance/project-data-protection) for the project to prohibit or allow data stream out of the project. The default enabling status is disabled.
        self.protected = protected

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_policy is not None:
            result['exceptionPolicy'] = self.exception_policy

        if self.protected is not None:
            result['protected'] = self.protected

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('exceptionPolicy') is not None:
            self.exception_policy = m.get('exceptionPolicy')

        if m.get('protected') is not None:
            self.protected = m.get('protected')

        return self

class ListProjectsResponseBodyDataProjectsSaleTag(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The instance ID of the default compute quota.
        self.resource_id = resource_id
        # The billing method of the default compute quota.
        self.resource_type = resource_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.resource_id is not None:
            result['resourceId'] = self.resource_id

        if self.resource_type is not None:
            result['resourceType'] = self.resource_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('resourceId') is not None:
            self.resource_id = m.get('resourceId')

        if m.get('resourceType') is not None:
            self.resource_type = m.get('resourceType')

        return self

class ListProjectsResponseBodyDataProjectsProperties(DaraModel):
    def __init__(
        self,
        allow_full_scan: bool = None,
        enable_decimal_2: bool = None,
        enable_tunnel_quota_route: bool = None,
        encryption: main_models.ListProjectsResponseBodyDataProjectsPropertiesEncryption = None,
        external_project_properties: main_models.ListProjectsResponseBodyDataProjectsPropertiesExternalProjectProperties = None,
        retention_days: int = None,
        sql_metering_max: str = None,
        table_lifecycle: main_models.ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle = None,
        timezone: str = None,
        tunnel_quota: str = None,
        type_system: str = None,
    ):
        # Specifies whether to allow full table scans in the project. Full table scans consume a large amount of resources. To improve processing efficiency, this feature is disabled by default.
        self.allow_full_scan = allow_full_scan
        # Specifies whether to enable the DECIMAL data type of MaxCompute V2.0 for the project.
        self.enable_decimal_2 = enable_decimal_2
        # Specifies whether to enable EPS resource group routing for the data transfer service.
        # - true: Data transfer tasks submitted by default in the project use the bound EPS resource group for the data transfer service.
        # - false: Data transfer tasks submitted by default in the project use the shared EPS resource group for the data transfer service.
        self.enable_tunnel_quota_route = enable_tunnel_quota_route
        # The storage encryption properties.
        self.encryption = encryption
        # The properties of the external project.
        self.external_project_properties = external_project_properties
        # The retention period of backup data in days. During this period, you can restore the current version to any backed-up data version. Valid values: 0 to 30. Default value: 1. A value of 0 indicates that the backup feature is disabled.
        self.retention_days = retention_days
        # The maximum threshold for the consumption of a single SQL statement. Unit: scanned data volume (GB) × complexity.
        self.sql_metering_max = sql_metering_max
        # The lifecycle properties of tables.
        self.table_lifecycle = table_lifecycle
        # The time zone of the project, which is the odps.sql.timezone property.
        self.timezone = timezone
        # The EPS resource group of the <props="china">[data transfer service](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/overview-of-dts)
        # <props="intl">[data transfer service](https://www.alibabacloud.com/help/en/maxcompute/user-guide/overview-of-dts) bound to the project.
        # 
        # - Default (shared EPS resource group for the data transfer service): The project is not allowed to use the subscription EPS resource group for the data transfer service. Regardless of the default EPS resource group setting, data transfer tasks submitted by default in this project automatically use the Default EPS resource group.
        # 
        # - Subscription EPS resource group for the data transfer service: The project is allowed to use the subscription EPS resource group for the data transfer service.
        self.tunnel_quota = tunnel_quota
        # The data type edition. Valid values:
        # - **1**: MaxCompute V1.0 data type edition
        # - **2**: MaxCompute V2.0 data type edition
        # - **hive**: Hive-compatible data type edition
        # 
        # For more information about the differences among the three data type editions, see <props="china">[Data type editions](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/data-type-editions)
        # <props="intl">[Data type editions](https://www.alibabacloud.com/help/en/maxcompute/user-guide/data-type-editions).
        self.type_system = type_system

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.external_project_properties:
            self.external_project_properties.validate()
        if self.table_lifecycle:
            self.table_lifecycle.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_full_scan is not None:
            result['allowFullScan'] = self.allow_full_scan

        if self.enable_decimal_2 is not None:
            result['enableDecimal2'] = self.enable_decimal_2

        if self.enable_tunnel_quota_route is not None:
            result['enableTunnelQuotaRoute'] = self.enable_tunnel_quota_route

        if self.encryption is not None:
            result['encryption'] = self.encryption.to_map()

        if self.external_project_properties is not None:
            result['externalProjectProperties'] = self.external_project_properties.to_map()

        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days

        if self.sql_metering_max is not None:
            result['sqlMeteringMax'] = self.sql_metering_max

        if self.table_lifecycle is not None:
            result['tableLifecycle'] = self.table_lifecycle.to_map()

        if self.timezone is not None:
            result['timezone'] = self.timezone

        if self.tunnel_quota is not None:
            result['tunnelQuota'] = self.tunnel_quota

        if self.type_system is not None:
            result['typeSystem'] = self.type_system

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('allowFullScan') is not None:
            self.allow_full_scan = m.get('allowFullScan')

        if m.get('enableDecimal2') is not None:
            self.enable_decimal_2 = m.get('enableDecimal2')

        if m.get('enableTunnelQuotaRoute') is not None:
            self.enable_tunnel_quota_route = m.get('enableTunnelQuotaRoute')

        if m.get('encryption') is not None:
            temp_model = main_models.ListProjectsResponseBodyDataProjectsPropertiesEncryption()
            self.encryption = temp_model.from_map(m.get('encryption'))

        if m.get('externalProjectProperties') is not None:
            temp_model = main_models.ListProjectsResponseBodyDataProjectsPropertiesExternalProjectProperties()
            self.external_project_properties = temp_model.from_map(m.get('externalProjectProperties'))

        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')

        if m.get('sqlMeteringMax') is not None:
            self.sql_metering_max = m.get('sqlMeteringMax')

        if m.get('tableLifecycle') is not None:
            temp_model = main_models.ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle()
            self.table_lifecycle = temp_model.from_map(m.get('tableLifecycle'))

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')

        if m.get('typeSystem') is not None:
            self.type_system = m.get('typeSystem')

        return self

class ListProjectsResponseBodyDataProjectsPropertiesTableLifecycle(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The lifecycle type. Valid values:
        # - **mandatory**: The LIFECYCLE clause is required. You must specify a lifecycle for the table.
        # - **optional**: The LIFECYCLE clause is optional when you create a table. If you do not specify a lifecycle for the table, the table never expires.
        # - **inherit**: If you do not specify a lifecycle for a table when you create the table, the lifecycle of the table is the value of the odps.table.lifecycle.value parameter.
        self.type = type
        # The lifecycle of the table. Unit: days. Valid values: 1 to 37231. Default value: 37231.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.type is not None:
            result['type'] = self.type

        if self.value is not None:
            result['value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('type') is not None:
            self.type = m.get('type')

        if m.get('value') is not None:
            self.value = m.get('value')

        return self

class ListProjectsResponseBodyDataProjectsPropertiesExternalProjectProperties(DaraModel):
    def __init__(
        self,
        is_external_catalog_bound: str = None,
    ):
        # Specifies whether the project is an external project of <props="china">[Data Lakehouse Solution 2.0](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/lake-warehouse-integrated-2-0-use-guide)
        # <props="intl">[Data Lakehouse Solution 2.0](https://www.alibabacloud.com/help/en/maxcompute/user-guide/lake-warehouse-integrated-2-0-use-guide).
        self.is_external_catalog_bound = is_external_catalog_bound

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_external_catalog_bound is not None:
            result['isExternalCatalogBound'] = self.is_external_catalog_bound

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('isExternalCatalogBound') is not None:
            self.is_external_catalog_bound = m.get('isExternalCatalogBound')

        return self

class ListProjectsResponseBodyDataProjectsPropertiesEncryption(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        enable: bool = None,
        key: str = None,
    ):
        # The data encryption algorithm. The encryption algorithms supported by the key include AES256, AESCTR, and RC4.
        self.algorithm = algorithm
        # Specifies whether to enable data encryption for the project. For more information about data encryption, see 
        # <props="china">[Storage encryption](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/storage-encryption)
        # <props="intl">[Storage encryption](https://www.alibabacloud.com/help/en/maxcompute/security-and-compliance/storage-encryption).
        self.enable = enable
        # The type of the key used for data encryption. Valid values include the default key (MaxCompute Default Key) and Bring Your Own Key (BYOK). The default key is a default key created internally by MaxCompute.
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.algorithm is not None:
            result['algorithm'] = self.algorithm

        if self.enable is not None:
            result['enable'] = self.enable

        if self.key is not None:
            result['key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('algorithm') is not None:
            self.algorithm = m.get('algorithm')

        if m.get('enable') is not None:
            self.enable = m.get('enable')

        if m.get('key') is not None:
            self.key = m.get('key')

        return self

class ListProjectsResponseBodyDataProjectsIpWhiteList(DaraModel):
    def __init__(
        self,
        ip_list: str = None,
        vpc_ip_list: str = None,
    ):
        # The IP address whitelist for the Internet and cloud service interconnection network.
        # 
        # > If you configure only the IP address whitelist for the Internet and cloud service interconnection network, access from the Internet and cloud service interconnection network is restricted by the configuration, and all access from VPCs is prohibited.
        self.ip_list = ip_list
        # The IP address whitelist for VPCs.
        # > If you configure only the IP address whitelist for VPCs, access from VPCs is restricted by the configuration, and all access from the Internet and cloud service interconnection network is prohibited.
        self.vpc_ip_list = vpc_ip_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ip_list is not None:
            result['ipList'] = self.ip_list

        if self.vpc_ip_list is not None:
            result['vpcIpList'] = self.vpc_ip_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ipList') is not None:
            self.ip_list = m.get('ipList')

        if m.get('vpcIpList') is not None:
            self.vpc_ip_list = m.get('vpcIpList')

        return self


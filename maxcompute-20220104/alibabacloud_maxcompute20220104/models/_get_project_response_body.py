# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_maxcompute20220104 import models as main_models
from darabonba.model import DaraModel

class GetProjectResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetProjectResponseBodyData = None,
        error_code: str = None,
        error_msg: str = None,
        http_code: int = None,
        request_id: str = None,
    ):
        # The response result.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # - 1xx: Informational response - The request has been received and is being processed.
        # - 2xx: Success - The request has been successfully received, understood, and accepted by the server.
        # - 3xx: Redirection - The request has been redirected. Further action is required to complete the request.
        # - 4xx: Client error - The request contains incorrect parameters, syntax errors, or specific request conditions cannot be met.
        # - 5xx: Server error - The server is unable to fulfill the request due to other reasons.
        self.http_code = http_code
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

        if self.error_code is not None:
            result['errorCode'] = self.error_code

        if self.error_msg is not None:
            result['errorMsg'] = self.error_msg

        if self.http_code is not None:
            result['httpCode'] = self.http_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('data') is not None:
            temp_model = main_models.GetProjectResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('errorCode') is not None:
            self.error_code = m.get('errorCode')

        if m.get('errorMsg') is not None:
            self.error_msg = m.get('errorMsg')

        if m.get('httpCode') is not None:
            self.http_code = m.get('httpCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        return self

class GetProjectResponseBodyData(DaraModel):
    def __init__(
        self,
        comment: str = None,
        cost_storage: str = None,
        created_time: int = None,
        default_quota: str = None,
        ip_white_list: main_models.GetProjectResponseBodyDataIpWhiteList = None,
        name: str = None,
        owner: str = None,
        product_type: str = None,
        properties: main_models.GetProjectResponseBodyDataProperties = None,
        region_id: str = None,
        sale_tag: main_models.GetProjectResponseBodyDataSaleTag = None,
        security_properties: main_models.GetProjectResponseBodyDataSecurityProperties = None,
        status: str = None,
        super_admins: List[str] = None,
        three_tier_model: bool = None,
        type: str = None,
    ):
        # The project description.
        self.comment = comment
        # The total storage size.
        # Views the current storage size of the project. This storage size is consistent with the metering caliber, which is the logical storage size after compression at the Project level.
        self.cost_storage = cost_storage
        # The creation time.
        self.created_time = created_time
        # The default computing quota.
        # Used to allocate computing resources. If no computing quota is specified, jobs initiated by this project will consume resources from the default quota. For more information about computing resource usage, see <props="china">[Computing Resources - Quota Usage](https://help.aliyun.com/zh/maxcompute/user-guide/use-of-computing-resources)
        # <props="intl">[Computing Resources - Quota Usage](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/use-of-computing-resources).
        self.default_quota = default_quota
        # The IP whitelist.
        self.ip_white_list = ip_white_list
        # The project name.
        self.name = name
        # The account information of the project owner.
        self.owner = owner
        # The billing mode of the default computing quota.
        self.product_type = product_type
        # The basic properties of the project.
        self.properties = properties
        # The region ID.
        self.region_id = region_id
        # The instance ID and billing type of the default computing quota.
        self.sale_tag = sale_tag
        # The permission properties.
        self.security_properties = security_properties
        # The project status. Valid values:
        # - **AVAILABLE**: normal.
        # - **READONLY**: read-only.
        # - **FROZEN**: frozen.
        # - **DELETING**: being deleted.
        self.status = status
        # The list of members with the `Super_Administrator` role in the project.
        self.super_admins = super_admins
        # Whether schema-based storage is supported.
        # MaxCompute supports Schema, which is an object between Project and Table/Resource/UDF for categorizing Tables, Resources, and UDFs. A Project can contain multiple Schemas. For more information, see <props="china">[Schema Operations](https://help.aliyun.com/zh/maxcompute/user-guide/schema-related-operations)
        # <props="intl">[Schema Operations](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/schema-related-operations).
        self.three_tier_model = three_tier_model
        # The project type. Valid values:
        # - **managed**: internal project.
        # - **external**: external project.
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

        if self.product_type is not None:
            result['productType'] = self.product_type

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

        if self.super_admins is not None:
            result['superAdmins'] = self.super_admins

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
            temp_model = main_models.GetProjectResponseBodyDataIpWhiteList()
            self.ip_white_list = temp_model.from_map(m.get('ipWhiteList'))

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('owner') is not None:
            self.owner = m.get('owner')

        if m.get('productType') is not None:
            self.product_type = m.get('productType')

        if m.get('properties') is not None:
            temp_model = main_models.GetProjectResponseBodyDataProperties()
            self.properties = temp_model.from_map(m.get('properties'))

        if m.get('regionId') is not None:
            self.region_id = m.get('regionId')

        if m.get('saleTag') is not None:
            temp_model = main_models.GetProjectResponseBodyDataSaleTag()
            self.sale_tag = temp_model.from_map(m.get('saleTag'))

        if m.get('securityProperties') is not None:
            temp_model = main_models.GetProjectResponseBodyDataSecurityProperties()
            self.security_properties = temp_model.from_map(m.get('securityProperties'))

        if m.get('status') is not None:
            self.status = m.get('status')

        if m.get('superAdmins') is not None:
            self.super_admins = m.get('superAdmins')

        if m.get('threeTierModel') is not None:
            self.three_tier_model = m.get('threeTierModel')

        if m.get('type') is not None:
            self.type = m.get('type')

        return self

class GetProjectResponseBodyDataSecurityProperties(DaraModel):
    def __init__(
        self,
        enable_download_privilege: bool = None,
        label_security: bool = None,
        object_creator_has_access_permission: bool = None,
        object_creator_has_grant_permission: bool = None,
        project_protection: main_models.GetProjectResponseBodyDataSecurityPropertiesProjectProtection = None,
        using_acl: bool = None,
        using_policy: bool = None,
    ):
        # Whether the <props="china">[download control](https://help.aliyun.com/zh/maxcompute/user-guide/download-control)
        # <props="intl">[download control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/label-based-access-control) feature is enabled. It is disabled by default.
        self.enable_download_privilege = enable_download_privilege
        # Whether the <props="china">[label-based access control](https://help.aliyun.com/zh/maxcompute/user-guide/label-based-access-control)
        # <props="intl">[label-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/label-based-access-control) feature is enabled. It is disabled by default.
        self.label_security = label_security
        # Whether the object creator is allowed to have access permissions on the object. This is allowed by default.
        self.object_creator_has_access_permission = object_creator_has_access_permission
        # Whether the object creator is allowed to have grant permissions on the object. This is allowed by default.
        self.object_creator_has_grant_permission = object_creator_has_grant_permission
        # The <props="china">[data protection](https://help.aliyun.com/zh/maxcompute/security-and-compliance/project-data-protection)
        # <props="intl">[data protection](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/project-data-protection) properties.
        self.project_protection = project_protection
        # Whether the <props="china">[ACL-based access control](https://help.aliyun.com/zh/maxcompute/user-guide/acl-based-access-control)
        # <props="intl">[ACL-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/acl-based-access-control) feature is enabled. It is enabled by default.
        self.using_acl = using_acl
        # Whether the <props="china">[policy-based access control](https://help.aliyun.com/zh/maxcompute/user-guide/policy-based-access-control-1)
        # <props="intl">[policy-based access control](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/policy-based-access-control-1) feature is enabled. It is enabled by default.
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
            temp_model = main_models.GetProjectResponseBodyDataSecurityPropertiesProjectProtection()
            self.project_protection = temp_model.from_map(m.get('projectProtection'))

        if m.get('usingAcl') is not None:
            self.using_acl = m.get('usingAcl')

        if m.get('usingPolicy') is not None:
            self.using_policy = m.get('usingPolicy')

        return self

class GetProjectResponseBodyDataSecurityPropertiesProjectProtection(DaraModel):
    def __init__(
        self,
        exception_policy: str = None,
        protected: bool = None,
    ):
        # If project data protection is enabled, you can set exceptions or trusted projects to allow specified users to export data of specified objects to specified projects. All scenarios described in the Exception Policy can override the data protection mechanism.
        self.exception_policy = exception_policy
        # Whether the project <props="china">[data protection mechanism](https://help.aliyun.com/zh/maxcompute/security-and-compliance/project-data-protection)
        # <props="intl">[data protection mechanism](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/project-data-protection) is enabled to prohibit or allow data to flow out of the project. It is disabled by default.
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

class GetProjectResponseBodyDataSaleTag(DaraModel):
    def __init__(
        self,
        resource_id: str = None,
        resource_type: str = None,
    ):
        # The instance ID of the default computing quota.
        self.resource_id = resource_id
        # The billing type of the default computing quota.
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

class GetProjectResponseBodyDataProperties(DaraModel):
    def __init__(
        self,
        allow_full_scan: bool = None,
        auto_mv_quota_gb: int = None,
        elder_tunnel_quota: str = None,
        enable_auto_mv: bool = None,
        enable_data_masking: bool = None,
        enable_decimal_2: bool = None,
        enable_dr: bool = None,
        enable_fdc_cache_force: bool = None,
        enable_tiered_storage: bool = None,
        enable_tunnel_quota_route: bool = None,
        encryption: main_models.GetProjectResponseBodyDataPropertiesEncryption = None,
        external_project_properties: main_models.GetProjectResponseBodyDataPropertiesExternalProjectProperties = None,
        fdc_quota: str = None,
        retention_days: int = None,
        sql_metering_max: str = None,
        storage_tier_info: main_models.GetProjectResponseBodyDataPropertiesStorageTierInfo = None,
        table_lifecycle: main_models.GetProjectResponseBodyDataPropertiesTableLifecycle = None,
        table_lifecycle_config: main_models.GetProjectResponseBodyDataPropertiesTableLifecycleConfig = None,
        timezone: str = None,
        tunnel_quota: str = None,
        type_system: str = None,
    ):
        # Whether full table scans are allowed in the project. Full table scans consume significant resources, so this feature is disabled by default to improve processing efficiency.
        self.allow_full_scan = allow_full_scan
        self.auto_mv_quota_gb = auto_mv_quota_gb
        # The parent group of the Data Transfer Service resource group bound to the project (can be ignored).
        self.elder_tunnel_quota = elder_tunnel_quota
        self.enable_auto_mv = enable_auto_mv
        self.enable_data_masking = enable_data_masking
        # Whether the MaxCompute 2.0 Decimal data type is enabled for the project.
        self.enable_decimal_2 = enable_decimal_2
        self.enable_dr = enable_dr
        # Whether to force enable external table caching.
        self.enable_fdc_cache_force = enable_fdc_cache_force
        # Whether <props="china">[tiered storage](https://help.aliyun.com/zh/maxcompute/user-guide/tiered-storage)
        # <props="intl">[tiered storage](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/tiered-storage) is enabled.
        self.enable_tiered_storage = enable_tiered_storage
        # Whether the Data Transfer Service resource group routing is enabled.
        # - true: Data Transfer Service tasks submitted by this project will use the bound Data Transfer Service resource group by default.
        # - false: Data Transfer Service tasks submitted by this project will use the Data Transfer Service shared resource group by default.
        self.enable_tunnel_quota_route = enable_tunnel_quota_route
        # The storage encryption properties.
        self.encryption = encryption
        # The external project properties.
        self.external_project_properties = external_project_properties
        # The external table cache quota.
        self.fdc_quota = fdc_quota
        # The number of days to retain backup data. During this period, you can restore the current version to any backed-up data version.
        # Valid values: [0, 30]. Default value: 1. A value of 0 indicates that the backup feature is disabled.
        self.retention_days = retention_days
        # The maximum threshold for single SQL consumption.
        # Unit: scan volume (GB) × complexity.
        self.sql_metering_max = sql_metering_max
        # The <props="china">[tiered storage](https://help.aliyun.com/zh/maxcompute/user-guide/tiered-storage)
        # <props="intl">[tiered storage](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/tiered-storage) information.
        self.storage_tier_info = storage_tier_info
        # The lifecycle properties of tables.
        self.table_lifecycle = table_lifecycle
        # The <props="china">[tiered storage lifecycle rules](https://help.aliyun.com/zh/maxcompute/user-guide/tiered-storage#f61fc9db76nna)
        # <props="intl">[tiered storage lifecycle rules](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/tiered-storage#f61fc9db76nna) properties. After configuration, the system will trigger automatic storage tier conversion based on these rules.
        self.table_lifecycle_config = table_lifecycle_config
        # The project timezone, which is the `odps.sql.timezone` property.
        self.timezone = timezone
        # The <props="china">[Data Transfer Service](https://help.aliyun.com/zh/maxcompute/user-guide/overview-of-dts)
        # <props="intl">[Data Transfer Service](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/overview-of-dts) resource group bound to the project.
        # 
        # - Default (Data Transfer Service shared resource group): This project is not allowed to use the Data Transfer Service (subscription) resource group. Regardless of the default Data Transfer Service resource group setting, Data Transfer Service tasks submitted by this project will automatically use the Default resource group.
        # 
        # - Data Transfer Service (subscription) resource group: This project is allowed to use the Data Transfer Service (subscription) resource group.
        self.tunnel_quota = tunnel_quota
        # The data type edition. Valid values:
        # - **1**: Edition 1.0.
        # - **2**: Edition 2.0.
        # - **hive**: Hive-compatible type.
        # 
        # For differences among the three data type editions, see <props="china">[Data Type Editions](https://help.aliyun.com/zh/maxcompute/user-guide/data-type-editions)
        # <props="intl">[Data Type Editions](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/data-type-editions).
        self.type_system = type_system

    def validate(self):
        if self.encryption:
            self.encryption.validate()
        if self.external_project_properties:
            self.external_project_properties.validate()
        if self.storage_tier_info:
            self.storage_tier_info.validate()
        if self.table_lifecycle:
            self.table_lifecycle.validate()
        if self.table_lifecycle_config:
            self.table_lifecycle_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.allow_full_scan is not None:
            result['allowFullScan'] = self.allow_full_scan

        if self.auto_mv_quota_gb is not None:
            result['autoMvQuotaGb'] = self.auto_mv_quota_gb

        if self.elder_tunnel_quota is not None:
            result['elderTunnelQuota'] = self.elder_tunnel_quota

        if self.enable_auto_mv is not None:
            result['enableAutoMv'] = self.enable_auto_mv

        if self.enable_data_masking is not None:
            result['enableDataMasking'] = self.enable_data_masking

        if self.enable_decimal_2 is not None:
            result['enableDecimal2'] = self.enable_decimal_2

        if self.enable_dr is not None:
            result['enableDr'] = self.enable_dr

        if self.enable_fdc_cache_force is not None:
            result['enableFdcCacheForce'] = self.enable_fdc_cache_force

        if self.enable_tiered_storage is not None:
            result['enableTieredStorage'] = self.enable_tiered_storage

        if self.enable_tunnel_quota_route is not None:
            result['enableTunnelQuotaRoute'] = self.enable_tunnel_quota_route

        if self.encryption is not None:
            result['encryption'] = self.encryption.to_map()

        if self.external_project_properties is not None:
            result['externalProjectProperties'] = self.external_project_properties.to_map()

        if self.fdc_quota is not None:
            result['fdcQuota'] = self.fdc_quota

        if self.retention_days is not None:
            result['retentionDays'] = self.retention_days

        if self.sql_metering_max is not None:
            result['sqlMeteringMax'] = self.sql_metering_max

        if self.storage_tier_info is not None:
            result['storageTierInfo'] = self.storage_tier_info.to_map()

        if self.table_lifecycle is not None:
            result['tableLifecycle'] = self.table_lifecycle.to_map()

        if self.table_lifecycle_config is not None:
            result['tableLifecycleConfig'] = self.table_lifecycle_config.to_map()

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

        if m.get('autoMvQuotaGb') is not None:
            self.auto_mv_quota_gb = m.get('autoMvQuotaGb')

        if m.get('elderTunnelQuota') is not None:
            self.elder_tunnel_quota = m.get('elderTunnelQuota')

        if m.get('enableAutoMv') is not None:
            self.enable_auto_mv = m.get('enableAutoMv')

        if m.get('enableDataMasking') is not None:
            self.enable_data_masking = m.get('enableDataMasking')

        if m.get('enableDecimal2') is not None:
            self.enable_decimal_2 = m.get('enableDecimal2')

        if m.get('enableDr') is not None:
            self.enable_dr = m.get('enableDr')

        if m.get('enableFdcCacheForce') is not None:
            self.enable_fdc_cache_force = m.get('enableFdcCacheForce')

        if m.get('enableTieredStorage') is not None:
            self.enable_tiered_storage = m.get('enableTieredStorage')

        if m.get('enableTunnelQuotaRoute') is not None:
            self.enable_tunnel_quota_route = m.get('enableTunnelQuotaRoute')

        if m.get('encryption') is not None:
            temp_model = main_models.GetProjectResponseBodyDataPropertiesEncryption()
            self.encryption = temp_model.from_map(m.get('encryption'))

        if m.get('externalProjectProperties') is not None:
            temp_model = main_models.GetProjectResponseBodyDataPropertiesExternalProjectProperties()
            self.external_project_properties = temp_model.from_map(m.get('externalProjectProperties'))

        if m.get('fdcQuota') is not None:
            self.fdc_quota = m.get('fdcQuota')

        if m.get('retentionDays') is not None:
            self.retention_days = m.get('retentionDays')

        if m.get('sqlMeteringMax') is not None:
            self.sql_metering_max = m.get('sqlMeteringMax')

        if m.get('storageTierInfo') is not None:
            temp_model = main_models.GetProjectResponseBodyDataPropertiesStorageTierInfo()
            self.storage_tier_info = temp_model.from_map(m.get('storageTierInfo'))

        if m.get('tableLifecycle') is not None:
            temp_model = main_models.GetProjectResponseBodyDataPropertiesTableLifecycle()
            self.table_lifecycle = temp_model.from_map(m.get('tableLifecycle'))

        if m.get('tableLifecycleConfig') is not None:
            temp_model = main_models.GetProjectResponseBodyDataPropertiesTableLifecycleConfig()
            self.table_lifecycle_config = temp_model.from_map(m.get('tableLifecycleConfig'))

        if m.get('timezone') is not None:
            self.timezone = m.get('timezone')

        if m.get('tunnelQuota') is not None:
            self.tunnel_quota = m.get('tunnelQuota')

        if m.get('typeSystem') is not None:
            self.type_system = m.get('typeSystem')

        return self

class GetProjectResponseBodyDataPropertiesTableLifecycleConfig(DaraModel):
    def __init__(
        self,
        tier_to_longterm: main_models.GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongterm = None,
        tier_to_low_frequency: main_models.GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequency = None,
    ):
        # The long-term storage identifier.
        self.tier_to_longterm = tier_to_longterm
        # The infrequent access storage identifier.
        self.tier_to_low_frequency = tier_to_low_frequency

    def validate(self):
        if self.tier_to_longterm:
            self.tier_to_longterm.validate()
        if self.tier_to_low_frequency:
            self.tier_to_low_frequency.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.tier_to_longterm is not None:
            result['TierToLongterm'] = self.tier_to_longterm.to_map()

        if self.tier_to_low_frequency is not None:
            result['TierToLowFrequency'] = self.tier_to_low_frequency.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TierToLongterm') is not None:
            temp_model = main_models.GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongterm()
            self.tier_to_longterm = temp_model.from_map(m.get('TierToLongterm'))

        if m.get('TierToLowFrequency') is not None:
            temp_model = main_models.GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequency()
            self.tier_to_low_frequency = temp_model.from_map(m.get('TierToLowFrequency'))

        return self

class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLowFrequency(DaraModel):
    def __init__(
        self,
        days_after_last_access_greater_than: int = None,
        days_after_last_modification_greater_than: int = None,
        days_after_last_tier_modification_greater_than: int = None,
    ):
        # The number of days after the last data access before automatic conversion, corresponding to the `LastAccessTime` of the table or partition.
        # 
        # > If the LastAccessTime of the table or partition is empty:
        # > - For tables or partitions created before October 1, 2023, the default time is 2023.10.01 00:00:00 in the UTC+0 timezone.
        # > - For tables or partitions created after October 1, 2023, if the data has not been accessed, the CreateTime is used for calculation.
        self.days_after_last_access_greater_than = days_after_last_access_greater_than
        # The number of days after the last data modification before automatic conversion, corresponding to the `LastModifiedTime` of the table or partition.
        self.days_after_last_modification_greater_than = days_after_last_modification_greater_than
        # The number of days since the last storage tier conversion.
        self.days_after_last_tier_modification_greater_than = days_after_last_tier_modification_greater_than

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days_after_last_access_greater_than is not None:
            result['DaysAfterLastAccessGreaterThan'] = self.days_after_last_access_greater_than

        if self.days_after_last_modification_greater_than is not None:
            result['DaysAfterLastModificationGreaterThan'] = self.days_after_last_modification_greater_than

        if self.days_after_last_tier_modification_greater_than is not None:
            result['DaysAfterLastTierModificationGreaterThan'] = self.days_after_last_tier_modification_greater_than

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysAfterLastAccessGreaterThan') is not None:
            self.days_after_last_access_greater_than = m.get('DaysAfterLastAccessGreaterThan')

        if m.get('DaysAfterLastModificationGreaterThan') is not None:
            self.days_after_last_modification_greater_than = m.get('DaysAfterLastModificationGreaterThan')

        if m.get('DaysAfterLastTierModificationGreaterThan') is not None:
            self.days_after_last_tier_modification_greater_than = m.get('DaysAfterLastTierModificationGreaterThan')

        return self

class GetProjectResponseBodyDataPropertiesTableLifecycleConfigTierToLongterm(DaraModel):
    def __init__(
        self,
        days_after_last_access_greater_than: int = None,
        days_after_last_modification_greater_than: int = None,
        days_after_last_tier_modification_greater_than: int = None,
    ):
        # The number of days after the last data access before automatic conversion, corresponding to the `LastAccessTime` of the table or partition.
        # 
        # > If the LastAccessTime of the table or partition is empty:
        # > - For tables or partitions created before October 1, 2023, the default time is 2023.10.01 00:00:00 in the UTC+0 timezone.
        # > - For tables or partitions created after October 1, 2023, if the data has not been accessed, the CreateTime is used for calculation.
        self.days_after_last_access_greater_than = days_after_last_access_greater_than
        # The number of days after the last data modification before automatic conversion, corresponding to the `LastModifiedTime` of the table or partition.
        self.days_after_last_modification_greater_than = days_after_last_modification_greater_than
        # The number of days since the last storage tier conversion.
        self.days_after_last_tier_modification_greater_than = days_after_last_tier_modification_greater_than

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.days_after_last_access_greater_than is not None:
            result['DaysAfterLastAccessGreaterThan'] = self.days_after_last_access_greater_than

        if self.days_after_last_modification_greater_than is not None:
            result['DaysAfterLastModificationGreaterThan'] = self.days_after_last_modification_greater_than

        if self.days_after_last_tier_modification_greater_than is not None:
            result['DaysAfterLastTierModificationGreaterThan'] = self.days_after_last_tier_modification_greater_than

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DaysAfterLastAccessGreaterThan') is not None:
            self.days_after_last_access_greater_than = m.get('DaysAfterLastAccessGreaterThan')

        if m.get('DaysAfterLastModificationGreaterThan') is not None:
            self.days_after_last_modification_greater_than = m.get('DaysAfterLastModificationGreaterThan')

        if m.get('DaysAfterLastTierModificationGreaterThan') is not None:
            self.days_after_last_tier_modification_greater_than = m.get('DaysAfterLastTierModificationGreaterThan')

        return self

class GetProjectResponseBodyDataPropertiesTableLifecycle(DaraModel):
    def __init__(
        self,
        type: str = None,
        value: str = None,
    ):
        # The lifecycle type. Valid values:
        # - **mandatory**: The Lifecycle clause is mandatory. Users must set the table lifecycle.
        # - **optional**: The Lifecycle clause is optional when creating a table. If the table lifecycle is not set, the table is permanently valid.
        # - **inherit**: If the table lifecycle is not set when creating a table, the table lifecycle defaults to the value of odps.table.lifecycle.value.
        self.type = type
        # The table lifecycle in days. Valid values: 1 to 37231. Default value: 37231.
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

class GetProjectResponseBodyDataPropertiesStorageTierInfo(DaraModel):
    def __init__(
        self,
        project_backup_size: int = None,
        project_total_size: int = None,
        storage_tier_size: main_models.GetProjectResponseBodyDataPropertiesStorageTierInfoStorageTierSize = None,
    ):
        # The backup storage size.
        self.project_backup_size = project_backup_size
        # The total storage usage.
        self.project_total_size = project_total_size
        # The <props="china">[tiered storage](https://help.aliyun.com/zh/maxcompute/user-guide/tiered-storage)
        # <props="intl">[tiered storage](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/tiered-storage) information.
        self.storage_tier_size = storage_tier_size

    def validate(self):
        if self.storage_tier_size:
            self.storage_tier_size.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.project_backup_size is not None:
            result['projectBackupSize'] = self.project_backup_size

        if self.project_total_size is not None:
            result['projectTotalSize'] = self.project_total_size

        if self.storage_tier_size is not None:
            result['storageTierSize'] = self.storage_tier_size.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('projectBackupSize') is not None:
            self.project_backup_size = m.get('projectBackupSize')

        if m.get('projectTotalSize') is not None:
            self.project_total_size = m.get('projectTotalSize')

        if m.get('storageTierSize') is not None:
            temp_model = main_models.GetProjectResponseBodyDataPropertiesStorageTierInfoStorageTierSize()
            self.storage_tier_size = temp_model.from_map(m.get('storageTierSize'))

        return self

class GetProjectResponseBodyDataPropertiesStorageTierInfoStorageTierSize(DaraModel):
    def __init__(
        self,
        long_term_size: int = None,
        low_frequency_size: int = None,
        standard_size: int = None,
    ):
        # The long-term storage usage.
        self.long_term_size = long_term_size
        # The infrequent access storage usage.
        self.low_frequency_size = low_frequency_size
        # The standard storage usage.
        self.standard_size = standard_size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.long_term_size is not None:
            result['longTermSize'] = self.long_term_size

        if self.low_frequency_size is not None:
            result['lowFrequencySize'] = self.low_frequency_size

        if self.standard_size is not None:
            result['standardSize'] = self.standard_size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('longTermSize') is not None:
            self.long_term_size = m.get('longTermSize')

        if m.get('lowFrequencySize') is not None:
            self.low_frequency_size = m.get('lowFrequencySize')

        if m.get('standardSize') is not None:
            self.standard_size = m.get('standardSize')

        return self

class GetProjectResponseBodyDataPropertiesExternalProjectProperties(DaraModel):
    def __init__(
        self,
        external_catalog_id: str = None,
        foreign_server_name: str = None,
        foreign_server_type: str = None,
        is_external_catalog_bound: str = None,
        table_format: str = None,
        warehouse: str = None,
    ):
        self.external_catalog_id = external_catalog_id
        self.foreign_server_name = foreign_server_name
        self.foreign_server_type = foreign_server_type
        # Whether this is a <props="china">[Lakehouse 2.0](https://help.aliyun.com/zh/maxcompute/user-guide/lake-warehouse-integrated-2-0-use-guide)
        # <props="intl">[Lakehouse 2.0](https://www.alibabacloud.com/help/zh/maxcompute/user-guide/lake-warehouse-integrated-2-0-use-guide) external project.
        self.is_external_catalog_bound = is_external_catalog_bound
        self.table_format = table_format
        self.warehouse = warehouse

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.external_catalog_id is not None:
            result['externalCatalogId'] = self.external_catalog_id

        if self.foreign_server_name is not None:
            result['foreignServerName'] = self.foreign_server_name

        if self.foreign_server_type is not None:
            result['foreignServerType'] = self.foreign_server_type

        if self.is_external_catalog_bound is not None:
            result['isExternalCatalogBound'] = self.is_external_catalog_bound

        if self.table_format is not None:
            result['tableFormat'] = self.table_format

        if self.warehouse is not None:
            result['warehouse'] = self.warehouse

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('externalCatalogId') is not None:
            self.external_catalog_id = m.get('externalCatalogId')

        if m.get('foreignServerName') is not None:
            self.foreign_server_name = m.get('foreignServerName')

        if m.get('foreignServerType') is not None:
            self.foreign_server_type = m.get('foreignServerType')

        if m.get('isExternalCatalogBound') is not None:
            self.is_external_catalog_bound = m.get('isExternalCatalogBound')

        if m.get('tableFormat') is not None:
            self.table_format = m.get('tableFormat')

        if m.get('warehouse') is not None:
            self.warehouse = m.get('warehouse')

        return self

class GetProjectResponseBodyDataPropertiesEncryption(DaraModel):
    def __init__(
        self,
        algorithm: str = None,
        enable: bool = None,
        key: str = None,
    ):
        # The data encryption algorithm. Supported encryption algorithms include AES256, AESCTR, and RC4.
        self.algorithm = algorithm
        # Whether data encryption is enabled for the project. For more information about data encryption, see
        # <props="china">[Storage Encryption](https://help.aliyun.com/zh/maxcompute/security-and-compliance/storage-encryption)
        # <props="intl">[Storage Encryption](https://www.alibabacloud.com/help/zh/maxcompute/security-and-compliance/storage-encryption).
        self.enable = enable
        # The key type used for data encryption, including the default key (MaxCompute Default Key) and Bring Your Own Key (BYOK). The default key (MaxCompute Default Key) is created internally by MaxCompute.
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

class GetProjectResponseBodyDataIpWhiteList(DaraModel):
    def __init__(
        self,
        ip_list: str = None,
        vpc_ip_list: str = None,
    ):
        # The IP whitelist for public network and cloud product interconnection network.
        # 
        # > If only the public network and cloud product interconnection network IP whitelist is configured, access through the public network and cloud product interconnection network is restricted by the configuration, and all VPC network access is prohibited.
        self.ip_list = ip_list
        # The VPC network IP whitelist.
        # > If only the VPC network IP whitelist is configured, VPC network access is restricted by the configuration, and all public network and cloud product interconnection network access is prohibited.
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


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
        # The data returned.
        self.data = data
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_msg = error_msg
        # The HTTP status code.
        # 
        # - 1xx: Informational response. The request is received and is being processed.
        # 
        # - 2xx: Success. The request is successfully received, understood, and accepted by the server.
        # 
        # - 3xx: Redirection. The request is redirected, and further actions are required to complete the request.
        # 
        # - 4xx: Client error. The request contains invalid request parameters or syntax, or specific request conditions cannot be met.
        # 
        # - 5xx: Server error. The server cannot fulfill the request for other reasons.
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
        # The total storage usage. This value indicates the logical storage size after data is collected and compressed for the project. The storage usage is the same as the usage for billing.
        self.cost_storage = cost_storage
        # The time when the project was created.
        self.created_time = created_time
        # The default computing quota. Quotas are used for resource allocation. If you do not specify a computing quota, jobs that are initiated in the project consume resources from the default quota. For more information, see <props="intl">[Use of computing resources](https://www.alibabacloud.com/help/en/maxcompute/user-guide/use-of-computing-resources).
        self.default_quota = default_quota
        # The IP address whitelist.
        self.ip_white_list = ip_white_list
        # The project name.
        self.name = name
        # The account information of the project owner.
        self.owner = owner
        # The billing method of the default computing quota.
        self.product_type = product_type
        # The basic properties of the project.
        self.properties = properties
        # The region ID.
        self.region_id = region_id
        # The instance ID and billing method of the default computing quota.
        self.sale_tag = sale_tag
        # The permission properties.
        self.security_properties = security_properties
        # The project status. Valid values:
        # 
        # - **AVAILABLE**: Normal
        # 
        # - **READONLY**: read-only
        # 
        # - **FROZEN**: frozen
        # 
        # - **DELETING**: being deleted
        self.status = status
        # The list of members that are assigned the `Super_Administrator` role in the project.
        self.super_admins = super_admins
        # Specifies whether data storage by schema is supported. MaxCompute supports schemas. A schema is an object in a project. It is used to classify objects such as tables, resources, and user-defined functions (UDFs). You can create multiple schemas in a project. For more information, see <props="intl">[Schema operations](https://www.alibabacloud.com/help/en/maxcompute/user-guide/schema-related-operations).
        self.three_tier_model = three_tier_model
        # The project type. Valid values:
        # 
        # - **managed**: an internal project.
        # 
        # - **external**: an external project.
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
        # Specifies whether to use the <props="intl">[download control](https://www.alibabacloud.com/help/en/maxcompute/user-guide/download-control) feature. By default, this feature is disabled.
        self.enable_download_privilege = enable_download_privilege
        # Specifies whether to use the <props="intl">[label-based access control](https://www.alibabacloud.com/help/en/maxcompute/user-guide/label-based-access-control) feature. By default, this feature is disabled.
        self.label_security = label_security
        # Specifies whether the creator of an object has access permissions on the object. Default value: true.
        self.object_creator_has_access_permission = object_creator_has_access_permission
        # Specifies whether the creator of an object has grant permissions on the object. Default value: true.
        self.object_creator_has_grant_permission = object_creator_has_grant_permission
        # The properties of the <props="intl">[data protection mechanism](https://www.alibabacloud.com/help/en/maxcompute/security-and-compliance/project-data-protection).
        self.project_protection = project_protection
        # Specifies whether to use the <props="intl">[ACL-based access control](https://www.alibabacloud.com/help/en/maxcompute/user-guide/acl-based-access-control) feature. By default, this feature is enabled.
        self.using_acl = using_acl
        # Specifies whether to use the <props="intl">[policy-based access control](https://www.alibabacloud.com/help/en/maxcompute/user-guide/policy-based-access-control-1) feature. By default, this feature is enabled.
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
        # If data protection is enabled for a project, you can configure an exception policy to specify exception or trusted projects. This policy allows specified users to transfer data from a specified object to a specified project. The data protection mechanism does not apply to the scenarios described in the exception policy.
        self.exception_policy = exception_policy
        # Specifies whether to enable the <props="intl">[data protection mechanism](https://www.alibabacloud.com/help/en/maxcompute/security-and-compliance/project-data-protection) for the project to prohibit or allow data to flow out of the project. By default, this mechanism is disabled.
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
        # The billing method of the default computing quota.
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
        # Specifies whether to allow a full table scan in the project. A full table scan consumes a large amount of resources and reduces processing efficiency. By default, this feature is disabled.
        self.allow_full_scan = allow_full_scan
        self.auto_mv_quota_gb = auto_mv_quota_gb
        # The parent resource group of the Data Transmission Service resource group that is bound to the project. This parameter is for internal use.
        self.elder_tunnel_quota = elder_tunnel_quota
        self.enable_auto_mv = enable_auto_mv
        # Specifies whether to enable the DECIMAL data type of MaxCompute V2.0 for the project.
        self.enable_decimal_2 = enable_decimal_2
        self.enable_dr = enable_dr
        # Specifies whether to forcefully enable external table caching.
        self.enable_fdc_cache_force = enable_fdc_cache_force
        # Specifies whether to enable <props="intl">[tiered storage](https://www.alibabacloud.com/help/en/maxcompute/user-guide/tiered-storage).
        self.enable_tiered_storage = enable_tiered_storage
        # Specifies whether to enable routing for the Data Transmission Service resource group.
        # 
        # - true: The data transmission tasks that are submitted by default in the project use the Data Transmission Service resource group that is bound to the project.
        # 
        # - false: The data transmission tasks that are submitted by default in the project use the shared Data Transmission Service resource group.
        self.enable_tunnel_quota_route = enable_tunnel_quota_route
        # The storage encryption properties.
        self.encryption = encryption
        # The properties of the external project.
        self.external_project_properties = external_project_properties
        # The quota for external table caching.
        self.fdc_quota = fdc_quota
        # The retention period of backup data. Unit: days. During this period, you can restore the current data version to any backup version. The value can be an integer from 0 to 30. The default value is 1. A value of 0 indicates that the backup feature is disabled.
        self.retention_days = retention_days
        # The maximum consumption threshold of a single SQL statement. Formula: Amount of scanned data (GB) × Complexity.
        self.sql_metering_max = sql_metering_max
        # The <props="intl">[tiered storage](https://www.alibabacloud.com/help/en/maxcompute/user-guide/tiered-storage) information.
        self.storage_tier_info = storage_tier_info
        # The lifecycle properties of the table.
        self.table_lifecycle = table_lifecycle
        # The properties of the <props="intl">[tiered storage lifecycle rule](https://www.alibabacloud.com/help/en/maxcompute/user-guide/tiered-storage#f61fc9db76nna). After you set these properties, the system automatically triggers the conversion of storage classes based on the rule.
        self.table_lifecycle_config = table_lifecycle_config
        # The time zone of the project. This parameter corresponds to the `odps.sql.timezone` property.
        self.timezone = timezone
        # The <props="intl">[Data Transmission Service](https://www.alibabacloud.com/help/en/maxcompute/user-guide/overview-of-dts) resource group that is bound to the project.
        # 
        # - Default (shared Data Transmission Service resource group): The project cannot use a subscription Data Transmission Service resource group. Regardless of the value of the default Data Transmission Service resource group, the Data Transmission Service automatically uses the Default resource group for data transmission tasks that are submitted by default in the project.
        # 
        # - Subscription Data Transmission Service resource group: The project can use a subscription Data Transmission Service resource group.
        self.tunnel_quota = tunnel_quota
        # The data type edition. Valid values:
        # 
        # - **1**: V1.0
        # 
        # - **2**: V2.0
        # 
        # - **hive**: Hive-compatible
        # 
        # For more information, see <props="intl">[Data type editions](https://www.alibabacloud.com/help/en/maxcompute/user-guide/data-type-editions).
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
        # The identifier for the long-term storage class.
        self.tier_to_longterm = tier_to_longterm
        # The identifier for the IA storage class.
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
        # The number of days after the data was last accessed. After this period, the storage class is automatically changed. This corresponds to the `LastAccessTime` of the table or partition.
        # 
        # > If the LastAccessTime of the table or partition is empty:
        # >
        # > - For tables or partitions that were created before October 1, 2023, the last access time is considered 00:00:00 on October 1, 2023 (UTC+0).
        # >
        # > - For tables or partitions that were created on or after October 1, 2023, if the data has not been accessed, the creation time of the table or partition is considered the last access time.
        self.days_after_last_access_greater_than = days_after_last_access_greater_than
        # The number of days after the data was last modified. After this period, the storage class is automatically changed. This corresponds to the `LastModifiedTime` of the table or partition.
        self.days_after_last_modification_greater_than = days_after_last_modification_greater_than
        # The number of days after the storage class was last changed.
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
        # The number of days after the data was last accessed. After this period, the storage class is automatically changed. This corresponds to the `LastAccessTime` of the table or partition.
        # 
        # > If the LastAccessTime of the table or partition is empty:
        # >
        # > - For tables or partitions that were created before October 1, 2023, the last access time is considered 00:00:00 on October 1, 2023 (UTC+0).
        # >
        # > - For tables or partitions that were created on or after October 1, 2023, if the data has not been accessed, the creation time of the table or partition is considered the last access time.
        self.days_after_last_access_greater_than = days_after_last_access_greater_than
        # The number of days after the data was last modified. After this period, the storage class is automatically changed. This corresponds to the `LastModifiedTime` of the table or partition.
        self.days_after_last_modification_greater_than = days_after_last_modification_greater_than
        # The number of days after the storage class was last changed.
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
        # 
        # - **mandatory**: The Lifecycle clause is required. You must set a lifecycle for the table.
        # 
        # - **optional**: The Lifecycle clause is optional when you create a table. If you do not set a lifecycle for the table, the table is permanently valid.
        # 
        # - **inherit**: If you do not set a lifecycle for a table when you create it, the lifecycle of the table is the value of odps.table.lifecycle.value.
        self.type = type
        # The lifecycle of the table. Unit: days. The value can be an integer from 1 to 37231. The default value is 37231.
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
        # The <props="intl">[tiered storage](https://www.alibabacloud.com/help/en/maxcompute/user-guide/tiered-storage) information.
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
        # The IA storage class usage.
        self.low_frequency_size = low_frequency_size
        # The Standard storage usage.
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
        # Specifies whether the project is an external project of <props="intl">[data lakehouse 2.0](https://www.alibabacloud.com/help/en/maxcompute/user-guide/lake-warehouse-integrated-2-0-use-guide).
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
        # The data encryption algorithm. Supported algorithms include AES256, AESCTR, and RC4.
        self.algorithm = algorithm
        # Specifies whether to enable data encryption for the project. For more information, see <props="intl">[Storage encryption](https://www.alibabacloud.com/help/en/maxcompute/security-and-compliance/storage-encryption).
        self.enable = enable
        # The type of key used for data encryption. Valid values include MaxCompute Default Key and Bring-Your-Own-Key (BYOK). MaxCompute Default Key is a default key created within MaxCompute.
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
        # The IP address whitelist for access over the Internet or a network that is used to interconnect with other Alibaba Cloud services.
        # 
        # > If you configure only this IP address whitelist, access over the Internet or the network that is used to interconnect with other Alibaba Cloud services is restricted based on the configuration, and access over a VPC is prohibited.
        self.ip_list = ip_list
        # The IP address whitelist for access over a VPC.
        # 
        # > If you configure only this IP address whitelist, access over a VPC is restricted based on the configuration, and access over the Internet or a network that is used to interconnect with other Alibaba Cloud services is prohibited.
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


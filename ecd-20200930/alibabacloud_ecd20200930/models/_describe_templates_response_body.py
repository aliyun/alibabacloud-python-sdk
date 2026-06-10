# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class DescribeTemplatesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.DescribeTemplatesResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # Operation result. Returns `success` if successful. Otherwise, returns an error message.
        self.code = code
        # List of template information.
        self.data = data
        # HTTP status code.
        self.http_status_code = http_status_code
        # Error message. This parameter is not returned when Code is `success`.
        self.message = message
        # Current page number.
        self.page_number = page_number
        # Entries per page.
        self.page_size = page_size
        # Request ID.
        self.request_id = request_id
        # Indicates whether the operation succeeded.
        self.success = success
        # Total count.
        self.total_count = total_count

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.DescribeTemplatesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeTemplatesResponseBodyData(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        charge_type: str = None,
        data_disk_list: List[main_models.DescribeTemplatesResponseBodyDataDataDiskList] = None,
        default_language: str = None,
        description: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        image_id: str = None,
        image_type: str = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        post_paid_after_used_up: bool = None,
        product_type: str = None,
        region_config_list: List[main_models.DescribeTemplatesResponseBodyDataRegionConfigList] = None,
        request_id: str = None,
        resource_group_id: str = None,
        resource_tag_list: List[main_models.DescribeTemplatesResponseBodyDataResourceTagList] = None,
        site_config_list: List[main_models.DescribeTemplatesResponseBodyDataSiteConfigList] = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
        template_id: str = None,
        template_name: str = None,
        template_type: str = None,
        timer_group_id: str = None,
        user_duration: str = None,
    ):
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.charge_type = charge_type
        # Data disk size and specification configuration.
        self.data_disk_list = data_disk_list
        # Default startup language for the template.
        self.default_language = default_language
        # Template description.
        self.description = description
        # Template creation time in UTC.
        self.gmt_create = gmt_create
        # Template modification time in UTC.
        self.gmt_modified = gmt_modified
        # Image ID.
        self.image_id = image_id
        # Image type.
        self.image_type = image_type
        self.period = period
        self.period_unit = period_unit
        # Policy ID.
        self.policy_group_id = policy_group_id
        self.post_paid_after_used_up = post_paid_after_used_up
        # Product type.
        self.product_type = product_type
        # Region-specific configuration parameters.
        self.region_config_list = region_config_list
        # Request ID.
        self.request_id = request_id
        # Resource group ID.
        self.resource_group_id = resource_group_id
        # Cloud Desktop tags in key-value format.
        self.resource_tag_list = resource_tag_list
        # Site configuration management.
        self.site_config_list = site_config_list
        # System disk type.
        self.system_disk_performance_level = system_disk_performance_level
        # System disk size in GiB.
        self.system_disk_size = system_disk_size
        # Template ID.
        self.template_id = template_id
        # Template name.
        self.template_name = template_name
        # Template type.
        self.template_type = template_type
        # Scheduled task group ID.
        self.timer_group_id = timer_group_id
        self.user_duration = user_duration

    def validate(self):
        if self.data_disk_list:
            for v1 in self.data_disk_list:
                 if v1:
                    v1.validate()
        if self.region_config_list:
            for v1 in self.region_config_list:
                 if v1:
                    v1.validate()
        if self.resource_tag_list:
            for v1 in self.resource_tag_list:
                 if v1:
                    v1.validate()
        if self.site_config_list:
            for v1 in self.site_config_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_pay is not None:
            result['AutoPay'] = self.auto_pay

        if self.auto_renew is not None:
            result['AutoRenew'] = self.auto_renew

        if self.charge_type is not None:
            result['ChargeType'] = self.charge_type

        result['DataDiskList'] = []
        if self.data_disk_list is not None:
            for k1 in self.data_disk_list:
                result['DataDiskList'].append(k1.to_map() if k1 else None)

        if self.default_language is not None:
            result['DefaultLanguage'] = self.default_language

        if self.description is not None:
            result['Description'] = self.description

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.image_type is not None:
            result['ImageType'] = self.image_type

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.post_paid_after_used_up is not None:
            result['PostPaidAfterUsedUp'] = self.post_paid_after_used_up

        if self.product_type is not None:
            result['ProductType'] = self.product_type

        result['RegionConfigList'] = []
        if self.region_config_list is not None:
            for k1 in self.region_config_list:
                result['RegionConfigList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        result['ResourceTagList'] = []
        if self.resource_tag_list is not None:
            for k1 in self.resource_tag_list:
                result['ResourceTagList'].append(k1.to_map() if k1 else None)

        result['SiteConfigList'] = []
        if self.site_config_list is not None:
            for k1 in self.site_config_list:
                result['SiteConfigList'].append(k1.to_map() if k1 else None)

        if self.system_disk_performance_level is not None:
            result['SystemDiskPerformanceLevel'] = self.system_disk_performance_level

        if self.system_disk_size is not None:
            result['SystemDiskSize'] = self.system_disk_size

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        if self.template_name is not None:
            result['TemplateName'] = self.template_name

        if self.template_type is not None:
            result['TemplateType'] = self.template_type

        if self.timer_group_id is not None:
            result['TimerGroupId'] = self.timer_group_id

        if self.user_duration is not None:
            result['UserDuration'] = self.user_duration

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoPay') is not None:
            self.auto_pay = m.get('AutoPay')

        if m.get('AutoRenew') is not None:
            self.auto_renew = m.get('AutoRenew')

        if m.get('ChargeType') is not None:
            self.charge_type = m.get('ChargeType')

        self.data_disk_list = []
        if m.get('DataDiskList') is not None:
            for k1 in m.get('DataDiskList'):
                temp_model = main_models.DescribeTemplatesResponseBodyDataDataDiskList()
                self.data_disk_list.append(temp_model.from_map(k1))

        if m.get('DefaultLanguage') is not None:
            self.default_language = m.get('DefaultLanguage')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('ImageType') is not None:
            self.image_type = m.get('ImageType')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PostPaidAfterUsedUp') is not None:
            self.post_paid_after_used_up = m.get('PostPaidAfterUsedUp')

        if m.get('ProductType') is not None:
            self.product_type = m.get('ProductType')

        self.region_config_list = []
        if m.get('RegionConfigList') is not None:
            for k1 in m.get('RegionConfigList'):
                temp_model = main_models.DescribeTemplatesResponseBodyDataRegionConfigList()
                self.region_config_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.resource_tag_list = []
        if m.get('ResourceTagList') is not None:
            for k1 in m.get('ResourceTagList'):
                temp_model = main_models.DescribeTemplatesResponseBodyDataResourceTagList()
                self.resource_tag_list.append(temp_model.from_map(k1))

        self.site_config_list = []
        if m.get('SiteConfigList') is not None:
            for k1 in m.get('SiteConfigList'):
                temp_model = main_models.DescribeTemplatesResponseBodyDataSiteConfigList()
                self.site_config_list.append(temp_model.from_map(k1))

        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TemplateType') is not None:
            self.template_type = m.get('TemplateType')

        if m.get('TimerGroupId') is not None:
            self.timer_group_id = m.get('TimerGroupId')

        if m.get('UserDuration') is not None:
            self.user_duration = m.get('UserDuration')

        return self

class DescribeTemplatesResponseBodyDataSiteConfigList(DaraModel):
    def __init__(
        self,
        app_rule_id: str = None,
        site_id: str = None,
    ):
        # Application control policy ID.
        self.app_rule_id = app_rule_id
        # Site name.
        self.site_id = site_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_rule_id is not None:
            result['AppRuleId'] = self.app_rule_id

        if self.site_id is not None:
            result['SiteId'] = self.site_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppRuleId') is not None:
            self.app_rule_id = m.get('AppRuleId')

        if m.get('SiteId') is not None:
            self.site_id = m.get('SiteId')

        return self

class DescribeTemplatesResponseBodyDataResourceTagList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # Tag key.
        self.key = key
        # Tag value.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.key is not None:
            result['Key'] = self.key

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class DescribeTemplatesResponseBodyDataRegionConfigList(DaraModel):
    def __init__(
        self,
        cpu_count: int = None,
        gpu_spec: str = None,
        memory_size: int = None,
        office_site_id: str = None,
        region_id: str = None,
        resource_instance_type: str = None,
        snapshot_policy_id: str = None,
        subnet_id: str = None,
        volume_encryption_enable: bool = None,
        volume_encryption_key: str = None,
    ):
        # Number of vCPUs in the Cloud Desktop instance type.
        self.cpu_count = cpu_count
        # GPU memory size. This field appears only for graphics instance types.
        self.gpu_spec = gpu_spec
        # Memory size in MiB.
        self.memory_size = memory_size
        # Office site ID.
        self.office_site_id = office_site_id
        # Region ID.
        self.region_id = region_id
        # Cloud Desktop instance type ID.
        self.resource_instance_type = resource_instance_type
        # Snapshot policy ID.
        self.snapshot_policy_id = snapshot_policy_id
        # Subnet ID.
        self.subnet_id = subnet_id
        # Whether disk encryption is enabled.
        self.volume_encryption_enable = volume_encryption_enable
        # KMS key ID used when disk encryption is enabled.
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cpu_count is not None:
            result['CpuCount'] = self.cpu_count

        if self.gpu_spec is not None:
            result['GpuSpec'] = self.gpu_spec

        if self.memory_size is not None:
            result['MemorySize'] = self.memory_size

        if self.office_site_id is not None:
            result['OfficeSiteId'] = self.office_site_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_instance_type is not None:
            result['ResourceInstanceType'] = self.resource_instance_type

        if self.snapshot_policy_id is not None:
            result['SnapshotPolicyId'] = self.snapshot_policy_id

        if self.subnet_id is not None:
            result['SubnetId'] = self.subnet_id

        if self.volume_encryption_enable is not None:
            result['VolumeEncryptionEnable'] = self.volume_encryption_enable

        if self.volume_encryption_key is not None:
            result['VolumeEncryptionKey'] = self.volume_encryption_key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CpuCount') is not None:
            self.cpu_count = m.get('CpuCount')

        if m.get('GpuSpec') is not None:
            self.gpu_spec = m.get('GpuSpec')

        if m.get('MemorySize') is not None:
            self.memory_size = m.get('MemorySize')

        if m.get('OfficeSiteId') is not None:
            self.office_site_id = m.get('OfficeSiteId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceInstanceType') is not None:
            self.resource_instance_type = m.get('ResourceInstanceType')

        if m.get('SnapshotPolicyId') is not None:
            self.snapshot_policy_id = m.get('SnapshotPolicyId')

        if m.get('SubnetId') is not None:
            self.subnet_id = m.get('SubnetId')

        if m.get('VolumeEncryptionEnable') is not None:
            self.volume_encryption_enable = m.get('VolumeEncryptionEnable')

        if m.get('VolumeEncryptionKey') is not None:
            self.volume_encryption_key = m.get('VolumeEncryptionKey')

        return self

class DescribeTemplatesResponseBodyDataDataDiskList(DaraModel):
    def __init__(
        self,
        performance_level: str = None,
        size: str = None,
    ):
        # Data disk performance level.
        self.performance_level = performance_level
        # Data disk size in GiB.
        self.size = size

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.performance_level is not None:
            result['PerformanceLevel'] = self.performance_level

        if self.size is not None:
            result['Size'] = self.size

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PerformanceLevel') is not None:
            self.performance_level = m.get('PerformanceLevel')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        return self


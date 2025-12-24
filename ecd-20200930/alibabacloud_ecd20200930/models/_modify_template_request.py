# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class ModifyTemplateRequest(DaraModel):
    def __init__(
        self,
        auto_pay: bool = None,
        auto_renew: bool = None,
        charge_type: str = None,
        data_disk_list: List[main_models.ModifyTemplateRequestDataDiskList] = None,
        default_language: str = None,
        description: str = None,
        image_id: str = None,
        period: int = None,
        period_unit: str = None,
        policy_group_id: str = None,
        post_paid_after_used_up: bool = None,
        region_config_list: List[main_models.ModifyTemplateRequestRegionConfigList] = None,
        resource_group_id: str = None,
        resource_tag_list: List[main_models.ModifyTemplateRequestResourceTagList] = None,
        site_config_list: List[main_models.ModifyTemplateRequestSiteConfigList] = None,
        system_disk_performance_level: str = None,
        system_disk_size: int = None,
        template_id: str = None,
        template_name: str = None,
        timer_group_id: str = None,
        user_duration: int = None,
    ):
        self.auto_pay = auto_pay
        self.auto_renew = auto_renew
        self.charge_type = charge_type
        self.data_disk_list = data_disk_list
        # The default language of the cloud computer during startup. This parameter takes effect only when the cloud computer is created from a system image.
        # 
        # Valid values:
        # 
        # *   en-US: English.
        # *   zh-HK: Chinese, Traditional (Hong Kong, China).
        # *   zh-CN: Simplified Chinese.
        # *   ja-JP: Japanese.
        self.default_language = default_language
        # The template description. It must meet the following criteria:
        # 
        # *   It can be 2 to 256 characters in length and cannot start with `http://` or `https://`.
        # *   It can contain letters, digits, and special characters, including spaces. Note: You can use carriage returns to break lines.
        self.description = description
        # The ID of the cloud computer image. You can query image IDs on the Images page. System images and custom images are supported.
        self.image_id = image_id
        self.period = period
        self.period_unit = period_unit
        # The ID of the policy group.
        self.policy_group_id = policy_group_id
        self.post_paid_after_used_up = post_paid_after_used_up
        # The regions by which you can search for cloud computer templates. When this parameter takes effect, cloud computer templates are matched based on the specified regions.
        # 
        # >  You can specify up to 20 regions.
        self.region_config_list = region_config_list
        # The ID of the resource group.
        self.resource_group_id = resource_group_id
        # The tags added to cloud computers. Specify tags in key-value pairs. You can specify up to 20 tags.
        self.resource_tag_list = resource_tag_list
        self.site_config_list = site_config_list
        # The performance level (PL) of the system disk.
        # 
        # >  Only cloud computers of the Graphics or High Frequency type support Enterprise SSDs (ESSDs).
        # 
        # Valid values:
        # 
        # *   PL1: a PL1 ESSD.
        # *   PL0: a PL0 ESSD.
        # *   AutoPL: an AutoPL ESSD.
        self.system_disk_performance_level = system_disk_performance_level
        # The size of the system disk. Unit: GiB. Valid values: 40 to 500. Increments: 10 GiB.
        # 
        # >  The system disk size must be at least as large as the configured image size.
        self.system_disk_size = system_disk_size
        # The template ID.
        # 
        # This parameter is required.
        self.template_id = template_id
        # The template name. It must meet the following criteria:
        # 
        # *   It can be 2 to 126 characters in length.
        # *   It must begin with a letter and cannot start with `http://` or `https://`.
        # *   It can contain letters, digits, colons (:), underscores (_), and hyphens (-). Note: Periods (.) are not supported in the name.
        self.template_name = template_name
        # The ID of the scheduled task group.
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

        if self.image_id is not None:
            result['ImageId'] = self.image_id

        if self.period is not None:
            result['Period'] = self.period

        if self.period_unit is not None:
            result['PeriodUnit'] = self.period_unit

        if self.policy_group_id is not None:
            result['PolicyGroupId'] = self.policy_group_id

        if self.post_paid_after_used_up is not None:
            result['PostPaidAfterUsedUp'] = self.post_paid_after_used_up

        result['RegionConfigList'] = []
        if self.region_config_list is not None:
            for k1 in self.region_config_list:
                result['RegionConfigList'].append(k1.to_map() if k1 else None)

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
                temp_model = main_models.ModifyTemplateRequestDataDiskList()
                self.data_disk_list.append(temp_model.from_map(k1))

        if m.get('DefaultLanguage') is not None:
            self.default_language = m.get('DefaultLanguage')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('ImageId') is not None:
            self.image_id = m.get('ImageId')

        if m.get('Period') is not None:
            self.period = m.get('Period')

        if m.get('PeriodUnit') is not None:
            self.period_unit = m.get('PeriodUnit')

        if m.get('PolicyGroupId') is not None:
            self.policy_group_id = m.get('PolicyGroupId')

        if m.get('PostPaidAfterUsedUp') is not None:
            self.post_paid_after_used_up = m.get('PostPaidAfterUsedUp')

        self.region_config_list = []
        if m.get('RegionConfigList') is not None:
            for k1 in m.get('RegionConfigList'):
                temp_model = main_models.ModifyTemplateRequestRegionConfigList()
                self.region_config_list.append(temp_model.from_map(k1))

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        self.resource_tag_list = []
        if m.get('ResourceTagList') is not None:
            for k1 in m.get('ResourceTagList'):
                temp_model = main_models.ModifyTemplateRequestResourceTagList()
                self.resource_tag_list.append(temp_model.from_map(k1))

        self.site_config_list = []
        if m.get('SiteConfigList') is not None:
            for k1 in m.get('SiteConfigList'):
                temp_model = main_models.ModifyTemplateRequestSiteConfigList()
                self.site_config_list.append(temp_model.from_map(k1))

        if m.get('SystemDiskPerformanceLevel') is not None:
            self.system_disk_performance_level = m.get('SystemDiskPerformanceLevel')

        if m.get('SystemDiskSize') is not None:
            self.system_disk_size = m.get('SystemDiskSize')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        if m.get('TemplateName') is not None:
            self.template_name = m.get('TemplateName')

        if m.get('TimerGroupId') is not None:
            self.timer_group_id = m.get('TimerGroupId')

        if m.get('UserDuration') is not None:
            self.user_duration = m.get('UserDuration')

        return self

class ModifyTemplateRequestSiteConfigList(DaraModel):
    def __init__(
        self,
        app_rule_id: str = None,
        site_id: str = None,
    ):
        self.app_rule_id = app_rule_id
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

class ModifyTemplateRequestResourceTagList(DaraModel):
    def __init__(
        self,
        key: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag value.
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

class ModifyTemplateRequestRegionConfigList(DaraModel):
    def __init__(
        self,
        office_site_id: str = None,
        region_id: str = None,
        resource_instance_type: str = None,
        snapshot_policy_id: str = None,
        subnet_id: str = None,
        volume_encryption_enable: bool = None,
        volume_encryption_key: str = None,
    ):
        # The office network ID.
        self.office_site_id = office_site_id
        # The region ID. You can call the [DescribeRegions](~~DescribeRegions~~) operation to query the list of regions where Elastic Desktop Service (EDS) Enterprise is available.
        self.region_id = region_id
        # The ID of the cloud computer type.
        self.resource_instance_type = resource_instance_type
        # The ID of the automatic snapshot policy.
        self.snapshot_policy_id = snapshot_policy_id
        # The subnet ID.
        self.subnet_id = subnet_id
        # Specifies whether to enable disk encryption.
        # 
        # Valid values:
        # 
        # *   false (default): disables disk encryption.
        # *   true: enables disk encryption.
        self.volume_encryption_enable = volume_encryption_enable
        # The ID of the Key Management Service (KMS) key that you want to use to encrypt disks.
        self.volume_encryption_key = volume_encryption_key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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

class ModifyTemplateRequestDataDiskList(DaraModel):
    def __init__(
        self,
        performance_level: str = None,
        size: int = None,
    ):
        # The PL of the data disk. Default value: `AutoPL`.
        # Valid values:
        # *   PL1: a PL1 ESSD
        # *   PL0: a PL0 ESSD
        # *   AutoPL: an AutoPL ESSD
        self.performance_level = performance_level
        # The size of the data disk. Unit: GiB.Valid range: 40 to 2040 GiB with an increment of 10 GiB.
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


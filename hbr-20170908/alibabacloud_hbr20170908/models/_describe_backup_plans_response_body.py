# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_hbr20170908 import models as main_models
from darabonba.model import DaraModel

class DescribeBackupPlansResponseBody(DaraModel):
    def __init__(
        self,
        backup_plans: main_models.DescribeBackupPlansResponseBodyBackupPlans = None,
        code: str = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        # The queried backup plans.
        self.backup_plans = backup_plans
        # The HTTP status code. The status code 200 indicates that the call is successful.
        self.code = code
        # The message that is returned. If the call is successful, "successful" is returned. If the call fails, an error message is returned.
        self.message = message
        # The page number of the returned page. Pages start from page 1. Default value: 1.
        self.page_number = page_number
        # The number of entries returned on each page. Valid values: 1 to 99. Default value: 10.
        self.page_size = page_size
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call is successful. Valid values:
        # 
        # *   true: The call is successful.
        # *   false: The call fails.
        self.success = success
        # The total number of returned backup plans that meet the specified conditions.
        self.total_count = total_count

    def validate(self):
        if self.backup_plans:
            self.backup_plans.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_plans is not None:
            result['BackupPlans'] = self.backup_plans.to_map()

        if self.code is not None:
            result['Code'] = self.code

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
        if m.get('BackupPlans') is not None:
            temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlans()
            self.backup_plans = temp_model.from_map(m.get('BackupPlans'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

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

class DescribeBackupPlansResponseBodyBackupPlans(DaraModel):
    def __init__(
        self,
        backup_plan: List[main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlan] = None,
    ):
        self.backup_plan = backup_plan

    def validate(self):
        if self.backup_plan:
            for v1 in self.backup_plan:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BackupPlan'] = []
        if self.backup_plan is not None:
            for k1 in self.backup_plan:
                result['BackupPlan'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.backup_plan = []
        if m.get('BackupPlan') is not None:
            for k1 in m.get('BackupPlan'):
                temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlan()
                self.backup_plan.append(temp_model.from_map(k1))

        return self

class DescribeBackupPlansResponseBodyBackupPlansBackupPlan(DaraModel):
    def __init__(
        self,
        backup_source_group_id: str = None,
        backup_type: str = None,
        bucket: str = None,
        business_status: str = None,
        change_list_path: str = None,
        client_id: str = None,
        cluster_id: str = None,
        create_time: int = None,
        created_by_tag: bool = None,
        created_time: int = None,
        cross_account_role_name: str = None,
        cross_account_type: str = None,
        cross_account_user_id: int = None,
        data_source_id: str = None,
        dest_data_source_detail: str = None,
        dest_data_source_id: str = None,
        dest_source_type: str = None,
        detail: str = None,
        disabled: bool = None,
        exclude: str = None,
        file_system_id: str = None,
        hit_tags: main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTags = None,
        include: str = None,
        instance_group_id: str = None,
        instance_id: str = None,
        instance_name: str = None,
        keep_latest_snapshots: int = None,
        latest_execute_job_id: str = None,
        latest_finish_job_id: str = None,
        options: str = None,
        ots_detail: main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetail = None,
        paths: main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanPaths = None,
        plan_id: str = None,
        plan_name: str = None,
        prefix: str = None,
        resources: main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanResources = None,
        retention: int = None,
        rules: main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanRules = None,
        schedule: str = None,
        source_type: str = None,
        speed_limit: str = None,
        trial_info: main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanTrialInfo = None,
        updated_time: int = None,
        vault_id: str = None,
    ):
        # The ID of the data source group.
        self.backup_source_group_id = backup_source_group_id
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # This parameter is valid only when **SourceType** is set to **OSS**. This parameter indicates the name of the OSS bucket.
        self.bucket = bucket
        self.business_status = business_status
        # The configurations of the incremental file synchronization. This parameter is returned only for data synchronization.
        self.change_list_path = change_list_path
        # The ID of the backup client.
        self.client_id = client_id
        # The ID of the client group.
        self.cluster_id = cluster_id
        # This parameter is valid only when **SourceType** is set to **NAS**. This parameter indicates the time when the file system was created. This value is a UNIX timestamp. Unit: seconds.
        self.create_time = create_time
        # Indicates whether a backup plan is automatically created based on tags.
        self.created_by_tag = created_by_tag
        # The time when the backup plan was created. This value is a UNIX timestamp. Unit: seconds.
        self.created_time = created_time
        # The name of the Resource Access Management (RAM) role that is created within the source Alibaba Cloud account and assigned to the current Alibaba Cloud account to authorize the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_role_name = cross_account_role_name
        # Indicates whether data is backed up within the same Alibaba Cloud account or across Alibaba Cloud accounts. Valid values:
        # 
        # *   SELF_ACCOUNT
        # *   CROSS_ACCOUNT
        self.cross_account_type = cross_account_type
        # The ID of the source Alibaba Cloud account that authorizes the current Alibaba Cloud account to back up data across Alibaba Cloud accounts.
        self.cross_account_user_id = cross_account_user_id
        # The ID of the data source.
        self.data_source_id = data_source_id
        # The data source details at the destination. This parameter is returned only for data synchronization.
        self.dest_data_source_detail = dest_data_source_detail
        # The data source ID at the destination. This parameter is returned only for data synchronization.
        self.dest_data_source_id = dest_data_source_id
        # The data source type at the destination. This parameter is returned only for data synchronization.
        self.dest_source_type = dest_source_type
        # The details about ECS instance backup.
        self.detail = detail
        # Indicates whether the backup plan is disabled. Valid values:
        # 
        # *   true: The backup plan is disabled.
        # *   false: The backup plan is enabled.
        self.disabled = disabled
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the paths to the files that are excluded from the backup job.
        self.exclude = exclude
        # This parameter is valid only when **SourceType** is set to **NAS**. This parameter indicates the ID of the NAS file system.
        self.file_system_id = file_system_id
        # The matched tag rules.
        self.hit_tags = hit_tags
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the paths to the files that are backed up.
        self.include = include
        # The ID of the instance group.
        self.instance_group_id = instance_group_id
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the ID of the ECS instance.
        self.instance_id = instance_id
        # The name of the Tablestore instance.
        self.instance_name = instance_name
        # Indicates whether the feature of keeping at least one backup version is enabled. Valid values:
        # 
        # *   0: The feature is disabled.
        # *   1: The feature is enabled.
        self.keep_latest_snapshots = keep_latest_snapshots
        # The latest execution job id of plan.
        self.latest_execute_job_id = latest_execute_job_id
        self.latest_finish_job_id = latest_finish_job_id
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates whether Windows Volume Shadow Copy Service (VSS) is used to define a source path.
        self.options = options
        # The details about the Tablestore instance.
        self.ots_detail = ots_detail
        # The source paths. This parameter is valid only when **SourceType** is set to **ECS_FILE**.
        self.paths = paths
        # The ID of the backup plan.
        self.plan_id = plan_id
        # The name of the backup plan.
        self.plan_name = plan_name
        # This parameter is valid only when **SourceType** is set to **OSS**. This parameter indicates the prefix of the objects that are backed up.
        self.prefix = prefix
        # The backup resources. This parameter is valid only for disk backup.
        self.resources = resources
        # The retention period of the backup data. Unit: days.
        self.retention = retention
        # The backup policies. This parameter is valid only for disk backup.
        self.rules = rules
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified by `{startTime}` and the subsequent backup jobs at an interval that is specified by `{interval}`. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   **startTime**: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   **interval**: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule
        # The type of the data source. Valid values:
        # 
        # *   **ECS_FILE**: ECS files
        # *   **OSS**: OSS buckets
        # *   **NAS**: NAS file systems
        # *   **OTS**: Tablestore instances
        # *   **UDM_ECS**: ECS instances
        # *   **SYNC**: data synchronization
        self.source_type = source_type
        # This parameter is valid only when **SourceType** is set to **ECS_FILE**. This parameter indicates the throttling rules. Format: `{start}|{end}|{bandwidth}`. Multiple throttling rules are separated with vertical bars (`|`). A time range cannot overlap with another one.
        # 
        # *   start: the start hour.
        # *   end: the end hour.
        # *   bandwidth: the bandwidth. Unit: KB.
        self.speed_limit = speed_limit
        # The free trial information.
        self.trial_info = trial_info
        # The time when the backup plan was updated. This value is a UNIX timestamp. Unit: seconds.
        self.updated_time = updated_time
        # The ID of the backup vault.
        self.vault_id = vault_id

    def validate(self):
        if self.hit_tags:
            self.hit_tags.validate()
        if self.ots_detail:
            self.ots_detail.validate()
        if self.paths:
            self.paths.validate()
        if self.resources:
            self.resources.validate()
        if self.rules:
            self.rules.validate()
        if self.trial_info:
            self.trial_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_source_group_id is not None:
            result['BackupSourceGroupId'] = self.backup_source_group_id

        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.bucket is not None:
            result['Bucket'] = self.bucket

        if self.business_status is not None:
            result['BusinessStatus'] = self.business_status

        if self.change_list_path is not None:
            result['ChangeListPath'] = self.change_list_path

        if self.client_id is not None:
            result['ClientId'] = self.client_id

        if self.cluster_id is not None:
            result['ClusterId'] = self.cluster_id

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.created_by_tag is not None:
            result['CreatedByTag'] = self.created_by_tag

        if self.created_time is not None:
            result['CreatedTime'] = self.created_time

        if self.cross_account_role_name is not None:
            result['CrossAccountRoleName'] = self.cross_account_role_name

        if self.cross_account_type is not None:
            result['CrossAccountType'] = self.cross_account_type

        if self.cross_account_user_id is not None:
            result['CrossAccountUserId'] = self.cross_account_user_id

        if self.data_source_id is not None:
            result['DataSourceId'] = self.data_source_id

        if self.dest_data_source_detail is not None:
            result['DestDataSourceDetail'] = self.dest_data_source_detail

        if self.dest_data_source_id is not None:
            result['DestDataSourceId'] = self.dest_data_source_id

        if self.dest_source_type is not None:
            result['DestSourceType'] = self.dest_source_type

        if self.detail is not None:
            result['Detail'] = self.detail

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.exclude is not None:
            result['Exclude'] = self.exclude

        if self.file_system_id is not None:
            result['FileSystemId'] = self.file_system_id

        if self.hit_tags is not None:
            result['HitTags'] = self.hit_tags.to_map()

        if self.include is not None:
            result['Include'] = self.include

        if self.instance_group_id is not None:
            result['InstanceGroupId'] = self.instance_group_id

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.keep_latest_snapshots is not None:
            result['KeepLatestSnapshots'] = self.keep_latest_snapshots

        if self.latest_execute_job_id is not None:
            result['LatestExecuteJobId'] = self.latest_execute_job_id

        if self.latest_finish_job_id is not None:
            result['LatestFinishJobId'] = self.latest_finish_job_id

        if self.options is not None:
            result['Options'] = self.options

        if self.ots_detail is not None:
            result['OtsDetail'] = self.ots_detail.to_map()

        if self.paths is not None:
            result['Paths'] = self.paths.to_map()

        if self.plan_id is not None:
            result['PlanId'] = self.plan_id

        if self.plan_name is not None:
            result['PlanName'] = self.plan_name

        if self.prefix is not None:
            result['Prefix'] = self.prefix

        if self.resources is not None:
            result['Resources'] = self.resources.to_map()

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.rules is not None:
            result['Rules'] = self.rules.to_map()

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        if self.speed_limit is not None:
            result['SpeedLimit'] = self.speed_limit

        if self.trial_info is not None:
            result['TrialInfo'] = self.trial_info.to_map()

        if self.updated_time is not None:
            result['UpdatedTime'] = self.updated_time

        if self.vault_id is not None:
            result['VaultId'] = self.vault_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupSourceGroupId') is not None:
            self.backup_source_group_id = m.get('BackupSourceGroupId')

        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('Bucket') is not None:
            self.bucket = m.get('Bucket')

        if m.get('BusinessStatus') is not None:
            self.business_status = m.get('BusinessStatus')

        if m.get('ChangeListPath') is not None:
            self.change_list_path = m.get('ChangeListPath')

        if m.get('ClientId') is not None:
            self.client_id = m.get('ClientId')

        if m.get('ClusterId') is not None:
            self.cluster_id = m.get('ClusterId')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreatedByTag') is not None:
            self.created_by_tag = m.get('CreatedByTag')

        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')

        if m.get('CrossAccountRoleName') is not None:
            self.cross_account_role_name = m.get('CrossAccountRoleName')

        if m.get('CrossAccountType') is not None:
            self.cross_account_type = m.get('CrossAccountType')

        if m.get('CrossAccountUserId') is not None:
            self.cross_account_user_id = m.get('CrossAccountUserId')

        if m.get('DataSourceId') is not None:
            self.data_source_id = m.get('DataSourceId')

        if m.get('DestDataSourceDetail') is not None:
            self.dest_data_source_detail = m.get('DestDataSourceDetail')

        if m.get('DestDataSourceId') is not None:
            self.dest_data_source_id = m.get('DestDataSourceId')

        if m.get('DestSourceType') is not None:
            self.dest_source_type = m.get('DestSourceType')

        if m.get('Detail') is not None:
            self.detail = m.get('Detail')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('Exclude') is not None:
            self.exclude = m.get('Exclude')

        if m.get('FileSystemId') is not None:
            self.file_system_id = m.get('FileSystemId')

        if m.get('HitTags') is not None:
            temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTags()
            self.hit_tags = temp_model.from_map(m.get('HitTags'))

        if m.get('Include') is not None:
            self.include = m.get('Include')

        if m.get('InstanceGroupId') is not None:
            self.instance_group_id = m.get('InstanceGroupId')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('KeepLatestSnapshots') is not None:
            self.keep_latest_snapshots = m.get('KeepLatestSnapshots')

        if m.get('LatestExecuteJobId') is not None:
            self.latest_execute_job_id = m.get('LatestExecuteJobId')

        if m.get('LatestFinishJobId') is not None:
            self.latest_finish_job_id = m.get('LatestFinishJobId')

        if m.get('Options') is not None:
            self.options = m.get('Options')

        if m.get('OtsDetail') is not None:
            temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetail()
            self.ots_detail = temp_model.from_map(m.get('OtsDetail'))

        if m.get('Paths') is not None:
            temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanPaths()
            self.paths = temp_model.from_map(m.get('Paths'))

        if m.get('PlanId') is not None:
            self.plan_id = m.get('PlanId')

        if m.get('PlanName') is not None:
            self.plan_name = m.get('PlanName')

        if m.get('Prefix') is not None:
            self.prefix = m.get('Prefix')

        if m.get('Resources') is not None:
            temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanResources()
            self.resources = temp_model.from_map(m.get('Resources'))

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('Rules') is not None:
            temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanRules()
            self.rules = temp_model.from_map(m.get('Rules'))

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        if m.get('SpeedLimit') is not None:
            self.speed_limit = m.get('SpeedLimit')

        if m.get('TrialInfo') is not None:
            temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanTrialInfo()
            self.trial_info = temp_model.from_map(m.get('TrialInfo'))

        if m.get('UpdatedTime') is not None:
            self.updated_time = m.get('UpdatedTime')

        if m.get('VaultId') is not None:
            self.vault_id = m.get('VaultId')

        return self

class DescribeBackupPlansResponseBodyBackupPlansBackupPlanTrialInfo(DaraModel):
    def __init__(
        self,
        keep_after_trial_expiration: bool = None,
        trial_expire_time: int = None,
        trial_start_time: int = None,
        trial_vault_release_time: int = None,
    ):
        # Indicates whether you are billed based on the pay-as-you-go method after the free trial ends.
        self.keep_after_trial_expiration = keep_after_trial_expiration
        # The expiration time of the free trial.
        self.trial_expire_time = trial_expire_time
        # The start time of the free trial.
        self.trial_start_time = trial_start_time
        # The time when the free-trial backup vault is released.
        self.trial_vault_release_time = trial_vault_release_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.keep_after_trial_expiration is not None:
            result['KeepAfterTrialExpiration'] = self.keep_after_trial_expiration

        if self.trial_expire_time is not None:
            result['TrialExpireTime'] = self.trial_expire_time

        if self.trial_start_time is not None:
            result['TrialStartTime'] = self.trial_start_time

        if self.trial_vault_release_time is not None:
            result['TrialVaultReleaseTime'] = self.trial_vault_release_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('KeepAfterTrialExpiration') is not None:
            self.keep_after_trial_expiration = m.get('KeepAfterTrialExpiration')

        if m.get('TrialExpireTime') is not None:
            self.trial_expire_time = m.get('TrialExpireTime')

        if m.get('TrialStartTime') is not None:
            self.trial_start_time = m.get('TrialStartTime')

        if m.get('TrialVaultReleaseTime') is not None:
            self.trial_vault_release_time = m.get('TrialVaultReleaseTime')

        return self

class DescribeBackupPlansResponseBodyBackupPlansBackupPlanRules(DaraModel):
    def __init__(
        self,
        rule: List[main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanRulesRule] = None,
    ):
        self.rule = rule

    def validate(self):
        if self.rule:
            for v1 in self.rule:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Rule'] = []
        if self.rule is not None:
            for k1 in self.rule:
                result['Rule'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.rule = []
        if m.get('Rule') is not None:
            for k1 in m.get('Rule'):
                temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanRulesRule()
                self.rule.append(temp_model.from_map(k1))

        return self

class DescribeBackupPlansResponseBodyBackupPlansBackupPlanRulesRule(DaraModel):
    def __init__(
        self,
        backup_type: str = None,
        destination_region_id: str = None,
        destination_retention: int = None,
        disabled: bool = None,
        do_copy: bool = None,
        retention: int = None,
        rule_id: str = None,
        rule_name: str = None,
        schedule: str = None,
    ):
        # The backup type. Valid value: **COMPLETE**, which indicates full backup.
        self.backup_type = backup_type
        # The ID of the region in which the remote backup vault resides.
        self.destination_region_id = destination_region_id
        # The retention period of the backup data in remote backup mode. Unit: days.
        self.destination_retention = destination_retention
        # Indicates whether the policy is disabled.
        self.disabled = disabled
        # Indicates whether the snapshot data is backed up to the backup vault.
        self.do_copy = do_copy
        # The retention period of the backup data. Unit: days.
        self.retention = retention
        # The policy ID.
        self.rule_id = rule_id
        # The policy name.
        self.rule_name = rule_name
        # The backup policy. Format: `I|{startTime}|{interval}`. The system runs the first backup job at a point in time that is specified by `{startTime}` and the subsequent backup jobs at an interval that is specified by `{interval}`. The system does not run a backup job before the specified point in time. Each backup job, except the first one, starts only after the previous backup job is completed. For example, `I|1631685600|P1D` indicates that the system runs the first backup job at 14:00:00 on September 15, 2021 and the subsequent backup jobs once a day.
        # 
        # *   `startTime`: the time at which the system starts to run a backup job. The time follows the UNIX time format. Unit: seconds.
        # *   `interval`: the interval at which the system runs a backup job. The interval follows the ISO 8601 standard. For example, PT1H indicates an interval of 1 hour. P1D indicates an interval of one day.
        self.schedule = schedule

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.backup_type is not None:
            result['BackupType'] = self.backup_type

        if self.destination_region_id is not None:
            result['DestinationRegionId'] = self.destination_region_id

        if self.destination_retention is not None:
            result['DestinationRetention'] = self.destination_retention

        if self.disabled is not None:
            result['Disabled'] = self.disabled

        if self.do_copy is not None:
            result['DoCopy'] = self.do_copy

        if self.retention is not None:
            result['Retention'] = self.retention

        if self.rule_id is not None:
            result['RuleId'] = self.rule_id

        if self.rule_name is not None:
            result['RuleName'] = self.rule_name

        if self.schedule is not None:
            result['Schedule'] = self.schedule

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BackupType') is not None:
            self.backup_type = m.get('BackupType')

        if m.get('DestinationRegionId') is not None:
            self.destination_region_id = m.get('DestinationRegionId')

        if m.get('DestinationRetention') is not None:
            self.destination_retention = m.get('DestinationRetention')

        if m.get('Disabled') is not None:
            self.disabled = m.get('Disabled')

        if m.get('DoCopy') is not None:
            self.do_copy = m.get('DoCopy')

        if m.get('Retention') is not None:
            self.retention = m.get('Retention')

        if m.get('RuleId') is not None:
            self.rule_id = m.get('RuleId')

        if m.get('RuleName') is not None:
            self.rule_name = m.get('RuleName')

        if m.get('Schedule') is not None:
            self.schedule = m.get('Schedule')

        return self

class DescribeBackupPlansResponseBodyBackupPlansBackupPlanResources(DaraModel):
    def __init__(
        self,
        resource: List[main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanResourcesResource] = None,
    ):
        self.resource = resource

    def validate(self):
        if self.resource:
            for v1 in self.resource:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Resource'] = []
        if self.resource is not None:
            for k1 in self.resource:
                result['Resource'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.resource = []
        if m.get('Resource') is not None:
            for k1 in m.get('Resource'):
                temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanResourcesResource()
                self.resource.append(temp_model.from_map(k1))

        return self

class DescribeBackupPlansResponseBodyBackupPlansBackupPlanResourcesResource(DaraModel):
    def __init__(
        self,
        extra: str = None,
        resource_id: str = None,
        source_type: str = None,
    ):
        # Additional information about the data source.
        self.extra = extra
        # The ID of the data source.
        self.resource_id = resource_id
        # The type of the data source. Valid value: **UDM_DISK**.
        self.source_type = source_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.extra is not None:
            result['Extra'] = self.extra

        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id

        if self.source_type is not None:
            result['SourceType'] = self.source_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Extra') is not None:
            self.extra = m.get('Extra')

        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')

        if m.get('SourceType') is not None:
            self.source_type = m.get('SourceType')

        return self

class DescribeBackupPlansResponseBodyBackupPlansBackupPlanPaths(DaraModel):
    def __init__(
        self,
        path: List[str] = None,
    ):
        self.path = path

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.path is not None:
            result['Path'] = self.path

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Path') is not None:
            self.path = m.get('Path')

        return self

class DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetail(DaraModel):
    def __init__(
        self,
        table_names: main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetailTableNames = None,
    ):
        # The names of the tables in the Tablestore instance.
        self.table_names = table_names

    def validate(self):
        if self.table_names:
            self.table_names.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_names is not None:
            result['TableNames'] = self.table_names.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableNames') is not None:
            temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetailTableNames()
            self.table_names = temp_model.from_map(m.get('TableNames'))

        return self

class DescribeBackupPlansResponseBodyBackupPlansBackupPlanOtsDetailTableNames(DaraModel):
    def __init__(
        self,
        table_name: List[str] = None,
    ):
        self.table_name = table_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.table_name is not None:
            result['TableName'] = self.table_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('TableName') is not None:
            self.table_name = m.get('TableName')

        return self

class DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTags(DaraModel):
    def __init__(
        self,
        hit_tag: List[main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTagsHitTag] = None,
    ):
        self.hit_tag = hit_tag

    def validate(self):
        if self.hit_tag:
            for v1 in self.hit_tag:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['HitTag'] = []
        if self.hit_tag is not None:
            for k1 in self.hit_tag:
                result['HitTag'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.hit_tag = []
        if m.get('HitTag') is not None:
            for k1 in m.get('HitTag'):
                temp_model = main_models.DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTagsHitTag()
                self.hit_tag.append(temp_model.from_map(k1))

        return self

class DescribeBackupPlansResponseBodyBackupPlansBackupPlanHitTagsHitTag(DaraModel):
    def __init__(
        self,
        key: str = None,
        operator: str = None,
        value: str = None,
    ):
        # The tag key.
        self.key = key
        # The tag-based matching rule. Valid values:
        # 
        # *   **EQUAL**: Both the tag key and tag value are matched.
        # *   **NOT**: The tag key is matched and the tag value is not matched.
        self.operator = operator
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

        if self.operator is not None:
            result['Operator'] = self.operator

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')

        if m.get('Operator') is not None:
            self.operator = m.get('Operator')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


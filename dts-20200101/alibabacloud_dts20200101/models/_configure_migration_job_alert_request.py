# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ConfigureMigrationJobAlertRequest(DaraModel):
    def __init__(
        self,
        account_id: str = None,
        delay_alert_phone: str = None,
        delay_alert_status: str = None,
        delay_over_seconds: str = None,
        error_alert_phone: str = None,
        error_alert_status: str = None,
        migration_job_id: str = None,
        owner_id: str = None,
        region_id: str = None,
        resource_group_id: str = None,
    ):
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter because this parameter will be removed in the future.
        self.account_id = account_id
        # The mobile phone numbers that receive latency-related alerts. Separate mobile phone numbers with commas (,).
        # 
        # > 
        # 
        # *   This parameter is available only for China site (aliyun.com) users. Only mobile phone numbers in the Chinese mainland are supported. Up to 10 mobile phone numbers can be specified.
        # *   International site (alibabacloud.com) users cannot receive alerts by using mobile phones, but can [set alert rules for DTS tasks in the Cloud Monitor console](https://help.aliyun.com/document_detail/175876.html).
        self.delay_alert_phone = delay_alert_phone
        # Specifies whether to monitor task latency. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        # 
        # > 
        # 
        # *   The default value is **enable**.
        # *   You must specify at least one of the DelayAlertStatus and **ErrorAlertStatus** parameters.
        self.delay_alert_status = delay_alert_status
        # The threshold for triggering latency alerts. The unit is seconds and the value must be an integer. You can set the threshold based on your business needs. To avoid delay fluctuations caused by network and database loads, we recommend that you set the threshold to more than 10 seconds.
        # 
        # >  If the **DelayAlertStatus** parameter is set to **enable**, this parameter must be specified.
        self.delay_over_seconds = delay_over_seconds
        # The mobile phone numbers that receive status-related alerts. Separate mobile phone numbers with commas (,).
        # 
        # > 
        # 
        # *   This parameter is available only for China site (aliyun.com) users. Only mobile phone numbers in the Chinese mainland are supported. Up to 10 mobile phone numbers can be specified.
        # *   International site (alibabacloud.com) users cannot receive alerts by using mobile phones, but can [set alert rules for DTS tasks in the Cloud Monitor console](https://help.aliyun.com/document_detail/175876.html).
        self.error_alert_phone = error_alert_phone
        # Specifies whether to monitor task status. Valid values:
        # 
        # *   **enable**: yes
        # *   **disable**: no
        # 
        # > 
        # 
        # *   The default value is **enable**.
        # *   You must specify at least one of the **DelayAlertStatus** and ErrorAlertStatus parameters.
        # *   If the task that you monitor enters an abnormal state, an alert is triggered.
        self.error_alert_status = error_alert_status
        # The ID of the data migration instance. You can call the **DescribeMigrationJobs** operation to query the instance ID.
        # 
        # This parameter is required.
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        # The ID of the region where the data migration instance resides. For more information, see [List of supported regions](https://help.aliyun.com/document_detail/141033.html).
        self.region_id = region_id
        # Resource group ID.
        self.resource_group_id = resource_group_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.account_id is not None:
            result['AccountId'] = self.account_id

        if self.delay_alert_phone is not None:
            result['DelayAlertPhone'] = self.delay_alert_phone

        if self.delay_alert_status is not None:
            result['DelayAlertStatus'] = self.delay_alert_status

        if self.delay_over_seconds is not None:
            result['DelayOverSeconds'] = self.delay_over_seconds

        if self.error_alert_phone is not None:
            result['ErrorAlertPhone'] = self.error_alert_phone

        if self.error_alert_status is not None:
            result['ErrorAlertStatus'] = self.error_alert_status

        if self.migration_job_id is not None:
            result['MigrationJobId'] = self.migration_job_id

        if self.owner_id is not None:
            result['OwnerId'] = self.owner_id

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccountId') is not None:
            self.account_id = m.get('AccountId')

        if m.get('DelayAlertPhone') is not None:
            self.delay_alert_phone = m.get('DelayAlertPhone')

        if m.get('DelayAlertStatus') is not None:
            self.delay_alert_status = m.get('DelayAlertStatus')

        if m.get('DelayOverSeconds') is not None:
            self.delay_over_seconds = m.get('DelayOverSeconds')

        if m.get('ErrorAlertPhone') is not None:
            self.error_alert_phone = m.get('ErrorAlertPhone')

        if m.get('ErrorAlertStatus') is not None:
            self.error_alert_status = m.get('ErrorAlertStatus')

        if m.get('MigrationJobId') is not None:
            self.migration_job_id = m.get('MigrationJobId')

        if m.get('OwnerId') is not None:
            self.owner_id = m.get('OwnerId')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')

        return self


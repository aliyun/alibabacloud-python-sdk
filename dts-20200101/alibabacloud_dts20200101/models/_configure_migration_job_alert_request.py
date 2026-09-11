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
        # The ID of the Alibaba Cloud account. You do not need to specify this parameter. This parameter will be deprecated.
        self.account_id = account_id
        # The mobile phone numbers of contacts for latency alerts. Separate multiple mobile phone numbers with commas (,).
        # 
        # This parameter is supported only on the China site (aliyun.com) and supports only Chinese mainland mobile phone numbers. You can specify up to 10 mobile phone numbers.
        # The China site does not support phone alerts. You can configure alert rules for DTS tasks only in the CloudMonitor console.
        self.delay_alert_phone = delay_alert_phone
        # Specifies whether to monitor the latency status. Valid values:
        # 
        # - **enable**: yes.
        # - **disable**: no.
        # 
        # > - Default value: **enable**.
        # - You must specify at least one of this parameter and the **ErrorAlertStatus** parameter.
        self.delay_alert_status = delay_alert_status
        # The threshold for triggering a latency alert. Unit: seconds. The value must be an integer. Set the threshold based on your business requirements. To avoid latency fluctuations caused by network conditions or database loads, set the threshold to 10 seconds or more.
        # > This parameter is required when **DelayAlertStatus** is set to **enable**.
        self.delay_over_seconds = delay_over_seconds
        # The mobile phone numbers of contacts for exception alerts. Separate multiple mobile phone numbers with commas (,).
        # 
        # This parameter is supported only on the China site (aliyun.com) and supports only Chinese mainland mobile phone numbers. You can specify up to 10 mobile phone numbers.
        # The international site does not support phone alerts. You can configure alert rules for DTS tasks only in the CloudMonitor console.
        self.error_alert_phone = error_alert_phone
        # Specifies whether to monitor the exception status. Valid values:
        # 
        # - **enable**: yes.
        # - **disable**: no.
        # 
        # > - Default value: **enable**.
        # - You must specify at least one of this parameter and the **DelayAlertStatus** parameter.
        # - After you enable the exception status monitoring feature, an alert is triggered when an exception is detected.
        self.error_alert_status = error_alert_status
        # Instance ID of the data migration instance. You can call the **DescribeMigrationJobs** operation to query instance ID.
        # 
        # This parameter is required.
        self.migration_job_id = migration_job_id
        self.owner_id = owner_id
        # The ID of the region where the data migration instance resides. For more information, see the supported region list.
        self.region_id = region_id
        # The resource group ID.
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


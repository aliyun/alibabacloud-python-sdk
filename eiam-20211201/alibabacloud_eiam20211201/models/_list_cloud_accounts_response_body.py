# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_eiam20211201 import models as main_models
from darabonba.model import DaraModel

class ListCloudAccountsResponseBody(DaraModel):
    def __init__(
        self,
        cloud_accounts: List[main_models.ListCloudAccountsResponseBodyCloudAccounts] = None,
        max_results: int = None,
        next_token: str = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The list of cloud accounts.
        self.cloud_accounts = cloud_accounts
        # The number of rows per page for paging.
        self.max_results = max_results
        # The token returned for the current call.
        self.next_token = next_token
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.cloud_accounts:
            for v1 in self.cloud_accounts:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CloudAccounts'] = []
        if self.cloud_accounts is not None:
            for k1 in self.cloud_accounts:
                result['CloudAccounts'].append(k1.to_map() if k1 else None)

        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cloud_accounts = []
        if m.get('CloudAccounts') is not None:
            for k1 in m.get('CloudAccounts'):
                temp_model = main_models.ListCloudAccountsResponseBodyCloudAccounts()
                self.cloud_accounts.append(temp_model.from_map(k1))

        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListCloudAccountsResponseBodyCloudAccounts(DaraModel):
    def __init__(
        self,
        cloud_account_external_id: str = None,
        cloud_account_health: str = None,
        cloud_account_health_check_result: main_models.ListCloudAccountsResponseBodyCloudAccountsCloudAccountHealthCheckResult = None,
        cloud_account_id: str = None,
        cloud_account_name: str = None,
        cloud_account_provider_name: str = None,
        cloud_account_site: str = None,
        cloud_account_vendor_type: str = None,
        create_time: int = None,
        description: str = None,
        instance_id: str = None,
        update_time: int = None,
    ):
        # The external unique identifier of the cloud account.
        self.cloud_account_external_id = cloud_account_external_id
        # The health status of the cloud account. Valid values:
        # - healthy: Healthy.
        # - unhealthy: Unhealthy.
        # - unknown: Unknown.
        self.cloud_account_health = cloud_account_health
        # The health check result of the cloud account.
        self.cloud_account_health_check_result = cloud_account_health_check_result
        # The cloud account ID.
        self.cloud_account_id = cloud_account_id
        # The cloud account name.
        self.cloud_account_name = cloud_account_name
        # The identity provider name.
        self.cloud_account_provider_name = cloud_account_provider_name
        self.cloud_account_site = cloud_account_site
        # The cloud account type. Valid values:
        # 
        # - alibaba_cloud: Alibaba Cloud.
        self.cloud_account_vendor_type = cloud_account_vendor_type
        # The time when the cloud account was created. The value is a UNIX timestamp in milliseconds.
        self.create_time = create_time
        # The description of the cloud account.
        self.description = description
        # The instance ID.
        self.instance_id = instance_id
        # The time when the cloud account was last updated. The value is a UNIX timestamp in milliseconds.
        self.update_time = update_time

    def validate(self):
        if self.cloud_account_health_check_result:
            self.cloud_account_health_check_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cloud_account_external_id is not None:
            result['CloudAccountExternalId'] = self.cloud_account_external_id

        if self.cloud_account_health is not None:
            result['CloudAccountHealth'] = self.cloud_account_health

        if self.cloud_account_health_check_result is not None:
            result['CloudAccountHealthCheckResult'] = self.cloud_account_health_check_result.to_map()

        if self.cloud_account_id is not None:
            result['CloudAccountId'] = self.cloud_account_id

        if self.cloud_account_name is not None:
            result['CloudAccountName'] = self.cloud_account_name

        if self.cloud_account_provider_name is not None:
            result['CloudAccountProviderName'] = self.cloud_account_provider_name

        if self.cloud_account_site is not None:
            result['CloudAccountSite'] = self.cloud_account_site

        if self.cloud_account_vendor_type is not None:
            result['CloudAccountVendorType'] = self.cloud_account_vendor_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CloudAccountExternalId') is not None:
            self.cloud_account_external_id = m.get('CloudAccountExternalId')

        if m.get('CloudAccountHealth') is not None:
            self.cloud_account_health = m.get('CloudAccountHealth')

        if m.get('CloudAccountHealthCheckResult') is not None:
            temp_model = main_models.ListCloudAccountsResponseBodyCloudAccountsCloudAccountHealthCheckResult()
            self.cloud_account_health_check_result = temp_model.from_map(m.get('CloudAccountHealthCheckResult'))

        if m.get('CloudAccountId') is not None:
            self.cloud_account_id = m.get('CloudAccountId')

        if m.get('CloudAccountName') is not None:
            self.cloud_account_name = m.get('CloudAccountName')

        if m.get('CloudAccountProviderName') is not None:
            self.cloud_account_provider_name = m.get('CloudAccountProviderName')

        if m.get('CloudAccountSite') is not None:
            self.cloud_account_site = m.get('CloudAccountSite')

        if m.get('CloudAccountVendorType') is not None:
            self.cloud_account_vendor_type = m.get('CloudAccountVendorType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class ListCloudAccountsResponseBodyCloudAccountsCloudAccountHealthCheckResult(DaraModel):
    def __init__(
        self,
        error_reason: main_models.ListCloudAccountsResponseBodyCloudAccountsCloudAccountHealthCheckResultErrorReason = None,
        last_check_time: int = None,
        result: str = None,
    ):
        # The error reason. This field is returned when the health check status is unhealthy.
        self.error_reason = error_reason
        # The time of the last health check. The value is a UNIX timestamp in milliseconds.
        self.last_check_time = last_check_time
        # The health check result of the cloud account. Valid values:
        # - success: Succeeded.
        # - failed: Failed.
        self.result = result

    def validate(self):
        if self.error_reason:
            self.error_reason.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_reason is not None:
            result['ErrorReason'] = self.error_reason.to_map()

        if self.last_check_time is not None:
            result['LastCheckTime'] = self.last_check_time

        if self.result is not None:
            result['Result'] = self.result

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorReason') is not None:
            temp_model = main_models.ListCloudAccountsResponseBodyCloudAccountsCloudAccountHealthCheckResultErrorReason()
            self.error_reason = temp_model.from_map(m.get('ErrorReason'))

        if m.get('LastCheckTime') is not None:
            self.last_check_time = m.get('LastCheckTime')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        return self

class ListCloudAccountsResponseBodyCloudAccountsCloudAccountHealthCheckResultErrorReason(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
    ):
        # The error code.
        self.error_code = error_code
        # The error message.
        self.error_message = error_message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        return self


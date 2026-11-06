# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class UpdateDataStorageDeliveryRequest(DaraModel):
    def __init__(
        self,
        auto_include_new_accounts: bool = None,
        configuration_version: int = None,
        lang: str = None,
        log_code: str = None,
        log_delivery_status: str = None,
        region_id: str = None,
        role_for: int = None,
        selected_account_ids: List[str] = None,
        sub_user_id: int = None,
        target_project: str = None,
    ):
        # Specifies whether to automatically add subsequent new and available managed members to the account selection for the log type. A value of true indicates that the feature is enabled. A value of false indicates that the feature is disabled. Disabling the feature does not remove selected members. If this parameter is omitted, the original value is retained. You must also specify LogCode, ConfigurationVersion, and TargetProject. You can update this parameter together with SelectedAccountIds. You cannot specify LogDeliveryStatus or the member SubUserId at the same time. The actual delivery is also controlled by the global switch for multi-account delivery and the delivery switch for the log type.
        self.auto_include_new_accounts = auto_include_new_accounts
        # The version of the delivery settings on which the current modification is based. Call GetDataStorage first and pass the original value of Data.DeliverySettings.ConfigurationVersion. Example 1 only shows the format and cannot be used as a fixed version. This parameter is required when you modify the global switch, account selection, auto-inclusion settings, or specified member delivery. If the version is missing or has changed, the OperationDenied.CentralizedDeliveryConfigChanged error is returned. In this case, query the version again before you submit the request.
        self.configuration_version = configuration_version
        # The language of the response message. Valid values:
        # - **zh** (default): Chinese.
        # - **en**: English.
        # This parameter is required. If this parameter is not specified, the API returns a 400 error.
        self.lang = lang
        # The log code.
        # 
        # This parameter is required.
        self.log_code = log_code
        # The log delivery status. Valid values:
        # - enable: Enables delivery.
        # - disable: Disables delivery.
        self.log_delivery_status = log_delivery_status
        # The region where the data management center for threat analysis is located. You must select the region of the management center based on the region where your assets are located. Valid values:
        # - cn-hangzhou: The assets are located in the Chinese mainland.
        # - ap-southeast-1: The assets are located outside the Chinese mainland.
        self.region_id = region_id
        # The ID of the user whose perspective the administrator switches to.
        self.role_for = role_for
        # The complete list of selected accounts for the log type. Each element is a decimal UID string. The list must include Data.DeliverySettings.DaAccountId (the current account) and can contain up to 10,000 items. A new member must be in the Accounts list returned by GetDataStorage and have Authorized set to true. If only the current account is retained, specify the UID of the current account. Do not use an empty string or an empty array. If this parameter is omitted, the original selection is retained. For HTTP requests, use the comma-separated format of array(simple): SelectedAccountIds=1234567890123456,1234567890123457. For a single account, specify only one UID. Do not use SelectedAccountIds.1/.2 or a JSON array string. You must also specify ConfigurationVersion and TargetProject, and omit LogDeliveryStatus and the member SubUserId.
        self.selected_account_ids = selected_account_ids
        # The UID of the source Alibaba Cloud account, which is a decimal integer. If this parameter is omitted or set to the UID of the current account, the delivery settings of the current account are modified. If a member UID is specified, the expected delivery status in the current configuration is applied only to the member. In this case, you must also specify LogDeliveryStatus, ConfigurationVersion, and TargetProject. The member must be within the selection scope of the log type or have existing delivery records. You must omit this parameter when you save the account selection or auto-inclusion settings. You cannot specify the UID of another member.
        self.sub_user_id = sub_user_id
        # The name of the current Simple Log Service project for log delivery. Invoke GetDataStorage first and pass the original value of Data.DeliverySettings.TargetProject. This parameter is used to verify the target of the current modification, not to specify a new project. This parameter is required when you modify the global switch, account selection, auto-inclusion settings, or specified member log delivery. If this parameter is missing or different from the current target, the OperationDenied.CentralizedDeliveryConfigChanged error is returned. Replace the account UID and region in the example with the query results.
        self.target_project = target_project

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auto_include_new_accounts is not None:
            result['AutoIncludeNewAccounts'] = self.auto_include_new_accounts

        if self.configuration_version is not None:
            result['ConfigurationVersion'] = self.configuration_version

        if self.lang is not None:
            result['Lang'] = self.lang

        if self.log_code is not None:
            result['LogCode'] = self.log_code

        if self.log_delivery_status is not None:
            result['LogDeliveryStatus'] = self.log_delivery_status

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.role_for is not None:
            result['RoleFor'] = self.role_for

        if self.selected_account_ids is not None:
            result['SelectedAccountIds'] = self.selected_account_ids

        if self.sub_user_id is not None:
            result['SubUserId'] = self.sub_user_id

        if self.target_project is not None:
            result['TargetProject'] = self.target_project

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AutoIncludeNewAccounts') is not None:
            self.auto_include_new_accounts = m.get('AutoIncludeNewAccounts')

        if m.get('ConfigurationVersion') is not None:
            self.configuration_version = m.get('ConfigurationVersion')

        if m.get('Lang') is not None:
            self.lang = m.get('Lang')

        if m.get('LogCode') is not None:
            self.log_code = m.get('LogCode')

        if m.get('LogDeliveryStatus') is not None:
            self.log_delivery_status = m.get('LogDeliveryStatus')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('RoleFor') is not None:
            self.role_for = m.get('RoleFor')

        if m.get('SelectedAccountIds') is not None:
            self.selected_account_ids = m.get('SelectedAccountIds')

        if m.get('SubUserId') is not None:
            self.sub_user_id = m.get('SubUserId')

        if m.get('TargetProject') is not None:
            self.target_project = m.get('TargetProject')

        return self


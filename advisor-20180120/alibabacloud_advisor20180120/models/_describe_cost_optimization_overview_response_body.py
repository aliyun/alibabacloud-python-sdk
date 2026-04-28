# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_advisor20180120 import models as main_models
from darabonba.model import DaraModel

class DescribeCostOptimizationOverviewResponseBody(DaraModel):
    def __init__(
        self,
        access_denied_detail: main_models.DescribeCostOptimizationOverviewResponseBodyAccessDeniedDetail = None,
        code: str = None,
        data: main_models.DescribeCostOptimizationOverviewResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.access_denied_detail = access_denied_detail
        self.code = code
        self.data = data
        self.message = message
        # Id of the request
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.access_denied_detail:
            self.access_denied_detail.validate()
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.access_denied_detail is not None:
            result['AccessDeniedDetail'] = self.access_denied_detail.to_map()

        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AccessDeniedDetail') is not None:
            temp_model = main_models.DescribeCostOptimizationOverviewResponseBodyAccessDeniedDetail()
            self.access_denied_detail = temp_model.from_map(m.get('AccessDeniedDetail'))

        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.DescribeCostOptimizationOverviewResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class DescribeCostOptimizationOverviewResponseBodyData(DaraModel):
    def __init__(
        self,
        billing_cycle_date: str = None,
        current_billing_cost: str = None,
        expected_saving_cost: str = None,
        gmt_modified: int = None,
        opt_check_item_num: str = None,
        opt_resource_num: str = None,
        processed_resource_count: str = None,
        processed_save_amount: str = None,
        task_id: int = None,
        wait_process_resource_count: str = None,
    ):
        self.billing_cycle_date = billing_cycle_date
        self.current_billing_cost = current_billing_cost
        self.expected_saving_cost = expected_saving_cost
        self.gmt_modified = gmt_modified
        self.opt_check_item_num = opt_check_item_num
        self.opt_resource_num = opt_resource_num
        self.processed_resource_count = processed_resource_count
        self.processed_save_amount = processed_save_amount
        self.task_id = task_id
        self.wait_process_resource_count = wait_process_resource_count

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.billing_cycle_date is not None:
            result['BillingCycleDate'] = self.billing_cycle_date

        if self.current_billing_cost is not None:
            result['CurrentBillingCost'] = self.current_billing_cost

        if self.expected_saving_cost is not None:
            result['ExpectedSavingCost'] = self.expected_saving_cost

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.opt_check_item_num is not None:
            result['OptCheckItemNum'] = self.opt_check_item_num

        if self.opt_resource_num is not None:
            result['OptResourceNum'] = self.opt_resource_num

        if self.processed_resource_count is not None:
            result['ProcessedResourceCount'] = self.processed_resource_count

        if self.processed_save_amount is not None:
            result['ProcessedSaveAmount'] = self.processed_save_amount

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.wait_process_resource_count is not None:
            result['WaitProcessResourceCount'] = self.wait_process_resource_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BillingCycleDate') is not None:
            self.billing_cycle_date = m.get('BillingCycleDate')

        if m.get('CurrentBillingCost') is not None:
            self.current_billing_cost = m.get('CurrentBillingCost')

        if m.get('ExpectedSavingCost') is not None:
            self.expected_saving_cost = m.get('ExpectedSavingCost')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('OptCheckItemNum') is not None:
            self.opt_check_item_num = m.get('OptCheckItemNum')

        if m.get('OptResourceNum') is not None:
            self.opt_resource_num = m.get('OptResourceNum')

        if m.get('ProcessedResourceCount') is not None:
            self.processed_resource_count = m.get('ProcessedResourceCount')

        if m.get('ProcessedSaveAmount') is not None:
            self.processed_save_amount = m.get('ProcessedSaveAmount')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WaitProcessResourceCount') is not None:
            self.wait_process_resource_count = m.get('WaitProcessResourceCount')

        return self

class DescribeCostOptimizationOverviewResponseBodyAccessDeniedDetail(DaraModel):
    def __init__(
        self,
        auth_action: str = None,
        auth_principal_display_name: str = None,
        auth_principal_owner_id: str = None,
        auth_principal_type: str = None,
        encoded_diagnostic_message: str = None,
        no_permission_type: str = None,
        policy_type: str = None,
    ):
        # AuthAction
        self.auth_action = auth_action
        self.auth_principal_display_name = auth_principal_display_name
        self.auth_principal_owner_id = auth_principal_owner_id
        self.auth_principal_type = auth_principal_type
        self.encoded_diagnostic_message = encoded_diagnostic_message
        self.no_permission_type = no_permission_type
        self.policy_type = policy_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_action is not None:
            result['AuthAction'] = self.auth_action

        if self.auth_principal_display_name is not None:
            result['AuthPrincipalDisplayName'] = self.auth_principal_display_name

        if self.auth_principal_owner_id is not None:
            result['AuthPrincipalOwnerId'] = self.auth_principal_owner_id

        if self.auth_principal_type is not None:
            result['AuthPrincipalType'] = self.auth_principal_type

        if self.encoded_diagnostic_message is not None:
            result['EncodedDiagnosticMessage'] = self.encoded_diagnostic_message

        if self.no_permission_type is not None:
            result['NoPermissionType'] = self.no_permission_type

        if self.policy_type is not None:
            result['PolicyType'] = self.policy_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthAction') is not None:
            self.auth_action = m.get('AuthAction')

        if m.get('AuthPrincipalDisplayName') is not None:
            self.auth_principal_display_name = m.get('AuthPrincipalDisplayName')

        if m.get('AuthPrincipalOwnerId') is not None:
            self.auth_principal_owner_id = m.get('AuthPrincipalOwnerId')

        if m.get('AuthPrincipalType') is not None:
            self.auth_principal_type = m.get('AuthPrincipalType')

        if m.get('EncodedDiagnosticMessage') is not None:
            self.encoded_diagnostic_message = m.get('EncodedDiagnosticMessage')

        if m.get('NoPermissionType') is not None:
            self.no_permission_type = m.get('NoPermissionType')

        if m.get('PolicyType') is not None:
            self.policy_type = m.get('PolicyType')

        return self


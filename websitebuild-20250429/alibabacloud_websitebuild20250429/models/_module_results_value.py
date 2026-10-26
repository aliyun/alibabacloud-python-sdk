# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class ModuleResultsValue(DaraModel):
    def __init__(
        self,
        desired_total: int = None,
        error_code: str = None,
        error_message: str = None,
        limit: int = None,
        passed: bool = None,
        resource_code: str = None,
        upgrade_available: bool = None,
    ):
        # Returned only for APP_WORKSPACE: the target total amount for this check, which is the used amount in the saved configuration plus the ResourceValue. If a compatible DesiredTotal is provided, this total amount is used directly. The used amount for issues is the sum of regular and reputation issues in the saved configuration, and the used amount for competitors is the number of competitors. This field is empty for APP and USER checks.
        self.desired_total = desired_total
        # The error code when the check fails. This field is null when the check passes.
        self.error_code = error_code
        # The error message when the check fails. This field is null when the check passes.
        self.error_message = error_message
        # Returned only for APP_WORKSPACE quantity pre-checks: the maximum number of issues or competitors allowed by the current product edition, which is not the remaining quota. This field is empty for APP and USER checks or when the edition benefits cannot be determined.
        self.limit = limit
        # Indicates whether the check passed.
        self.passed = passed
        # The resource code.
        self.resource_code = resource_code
        # Indicates whether a purchasable higher edition exists that can accommodate the DesiredTotal. This field is true only when the capacity of the current edition is insufficient and a higher edition meets the requirement. Otherwise, it is false. This field may be empty for APP and USER checks. This field does not indicate that an upgrade has been performed or an upgrade order has been created.
        self.upgrade_available = upgrade_available

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.desired_total is not None:
            result['DesiredTotal'] = self.desired_total

        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.limit is not None:
            result['Limit'] = self.limit

        if self.passed is not None:
            result['Passed'] = self.passed

        if self.resource_code is not None:
            result['ResourceCode'] = self.resource_code

        if self.upgrade_available is not None:
            result['UpgradeAvailable'] = self.upgrade_available

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DesiredTotal') is not None:
            self.desired_total = m.get('DesiredTotal')

        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Limit') is not None:
            self.limit = m.get('Limit')

        if m.get('Passed') is not None:
            self.passed = m.get('Passed')

        if m.get('ResourceCode') is not None:
            self.resource_code = m.get('ResourceCode')

        if m.get('UpgradeAvailable') is not None:
            self.upgrade_available = m.get('UpgradeAvailable')

        return self


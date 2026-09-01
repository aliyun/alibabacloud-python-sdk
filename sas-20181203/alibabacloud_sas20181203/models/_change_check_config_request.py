# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ChangeCheckConfigRequest(DaraModel):
    def __init__(
        self,
        added_check: List[main_models.ChangeCheckConfigRequestAddedCheck] = None,
        client_token: str = None,
        config_requirement_ids: main_models.ChangeCheckConfigRequestConfigRequirementIds = None,
        config_standard_ids: main_models.ChangeCheckConfigRequestConfigStandardIds = None,
        configure: str = None,
        cycle_days: List[int] = None,
        enable_add_check: bool = None,
        enable_auto_check: bool = None,
        end_time: int = None,
        region_id: str = None,
        removed_check: List[main_models.ChangeCheckConfigRequestRemovedCheck] = None,
        resource_directory_account_id: int = None,
        standard_ids: List[int] = None,
        start_time: int = None,
        system_config: bool = None,
        vendors: List[str] = None,
    ):
        # The list of check items to add to the policy.
        # <notice> If ConfigStandardIds or ConfigRequirementIds is specified, this parameter does not take effect.
        self.added_check = added_check
        # The client token used to ensure request idempotency. Use a different token for each request. Only ASCII characters are supported. The token can be up to 64 characters in length.
        self.client_token = client_token
        # Configures the check policy by specifying requirement IDs.
        # 
        # > Call [ListCheckResult](~~ListCheckResult~~) to obtain requirement IDs. If ConfigStandardIds is specified, this parameter does not take effect.
        self.config_requirement_ids = config_requirement_ids
        # Configures the check policy by specifying standard IDs.
        # 
        # > Call [ListCheckResult](~~ListCheckResult~~) to obtain standard IDs.
        self.config_standard_ids = config_standard_ids
        # The field configuration. Valid values:
        # 
        # - **all:** Adds all check items.
        self.configure = configure
        # The scheduled check days.
        self.cycle_days = cycle_days
        # Specifies whether to automatically include newly added check items from the selected requirements. Valid values:
        # 
        # - **true:** Enabled.
        # - **false:** Disabled.
        self.enable_add_check = enable_add_check
        # Specifies whether to enable automatic scheduled checks. Valid values:
        # 
        # - **true:** Enabled.
        # - **false:** Disabled.
        self.enable_auto_check = enable_auto_check
        # The end hour of the check time window, expressed as an hour of the day. The start and end times must fall within one of the following time ranges. Valid values: 6, 12, 18, 24.
        # 
        # - **0~6:** If the start time is 0, set the end time to 6.
        # - **6~12:** If the start time is 6, set the end time to 12.
        # - **12~18:** If the start time is 12, set the end time to 18.
        # - **18~24:** If the start time is 18, set the end time to 24.
        self.end_time = end_time
        # The region of the Security Center instance. Valid values:
        # 
        # - **cn-hangzhou:** China (Hangzhou)
        # - **ap-southeast-1:** Singapore
        self.region_id = region_id
        # The list of check items to remove from the policy.
        # <notice> If ConfigStandardIds or ConfigRequirementIds is specified, this parameter does not take effect.
        self.removed_check = removed_check
        # The ID of the resource directory member accounts (Alibaba Cloud account).
        # > Call [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) to obtain this parameter.
        self.resource_directory_account_id = resource_directory_account_id
        # This parameter is deprecated. You do not need to configure it.
        self.standard_ids = standard_ids
        # The start hour of the check time window, expressed as an hour of the day. The start and end times must fall within one of the following time ranges. Valid values: 0, 6, 12, 18.
        # 
        # - **0~6:** If the start time is 0, set the end time to 6.
        # - **6~12:** If the start time is 6, set the end time to 12.
        # - **12~18:** If the start time is 12, set the end time to 18.
        # - **18~24:** If the start time is 18, set the end time to 24.
        self.start_time = start_time
        # Specifies whether to use the system-generated configuration. Valid values:
        # - **true:** Yes.
        # - **false:** No.
        self.system_config = system_config
        # The list of cloud vendors.
        self.vendors = vendors

    def validate(self):
        if self.added_check:
            for v1 in self.added_check:
                 if v1:
                    v1.validate()
        if self.config_requirement_ids:
            self.config_requirement_ids.validate()
        if self.config_standard_ids:
            self.config_standard_ids.validate()
        if self.removed_check:
            for v1 in self.removed_check:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AddedCheck'] = []
        if self.added_check is not None:
            for k1 in self.added_check:
                result['AddedCheck'].append(k1.to_map() if k1 else None)

        if self.client_token is not None:
            result['ClientToken'] = self.client_token

        if self.config_requirement_ids is not None:
            result['ConfigRequirementIds'] = self.config_requirement_ids.to_map()

        if self.config_standard_ids is not None:
            result['ConfigStandardIds'] = self.config_standard_ids.to_map()

        if self.configure is not None:
            result['Configure'] = self.configure

        if self.cycle_days is not None:
            result['CycleDays'] = self.cycle_days

        if self.enable_add_check is not None:
            result['EnableAddCheck'] = self.enable_add_check

        if self.enable_auto_check is not None:
            result['EnableAutoCheck'] = self.enable_auto_check

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        result['RemovedCheck'] = []
        if self.removed_check is not None:
            for k1 in self.removed_check:
                result['RemovedCheck'].append(k1.to_map() if k1 else None)

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.standard_ids is not None:
            result['StandardIds'] = self.standard_ids

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.system_config is not None:
            result['SystemConfig'] = self.system_config

        if self.vendors is not None:
            result['Vendors'] = self.vendors

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.added_check = []
        if m.get('AddedCheck') is not None:
            for k1 in m.get('AddedCheck'):
                temp_model = main_models.ChangeCheckConfigRequestAddedCheck()
                self.added_check.append(temp_model.from_map(k1))

        if m.get('ClientToken') is not None:
            self.client_token = m.get('ClientToken')

        if m.get('ConfigRequirementIds') is not None:
            temp_model = main_models.ChangeCheckConfigRequestConfigRequirementIds()
            self.config_requirement_ids = temp_model.from_map(m.get('ConfigRequirementIds'))

        if m.get('ConfigStandardIds') is not None:
            temp_model = main_models.ChangeCheckConfigRequestConfigStandardIds()
            self.config_standard_ids = temp_model.from_map(m.get('ConfigStandardIds'))

        if m.get('Configure') is not None:
            self.configure = m.get('Configure')

        if m.get('CycleDays') is not None:
            self.cycle_days = m.get('CycleDays')

        if m.get('EnableAddCheck') is not None:
            self.enable_add_check = m.get('EnableAddCheck')

        if m.get('EnableAutoCheck') is not None:
            self.enable_auto_check = m.get('EnableAutoCheck')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        self.removed_check = []
        if m.get('RemovedCheck') is not None:
            for k1 in m.get('RemovedCheck'):
                temp_model = main_models.ChangeCheckConfigRequestRemovedCheck()
                self.removed_check.append(temp_model.from_map(k1))

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('StandardIds') is not None:
            self.standard_ids = m.get('StandardIds')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('SystemConfig') is not None:
            self.system_config = m.get('SystemConfig')

        if m.get('Vendors') is not None:
            self.vendors = m.get('Vendors')

        return self

class ChangeCheckConfigRequestRemovedCheck(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        section_id: int = None,
    ):
        # The ID of the check item.
        # 
        # > Call [ListCheckResult](~~ListCheckResult~~) to obtain check item IDs.
        self.check_id = check_id
        # The section ID of the check item.
        self.section_id = section_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.section_id is not None:
            result['SectionId'] = self.section_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('SectionId') is not None:
            self.section_id = m.get('SectionId')

        return self

class ChangeCheckConfigRequestConfigStandardIds(DaraModel):
    def __init__(
        self,
        add_ids: List[int] = None,
        remove_ids: List[int] = None,
    ):
        # The list of standard IDs to add to the policy.
        self.add_ids = add_ids
        # The list of standard IDs to remove from the policy.
        self.remove_ids = remove_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_ids is not None:
            result['AddIds'] = self.add_ids

        if self.remove_ids is not None:
            result['RemoveIds'] = self.remove_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddIds') is not None:
            self.add_ids = m.get('AddIds')

        if m.get('RemoveIds') is not None:
            self.remove_ids = m.get('RemoveIds')

        return self

class ChangeCheckConfigRequestConfigRequirementIds(DaraModel):
    def __init__(
        self,
        add_ids: List[int] = None,
        remove_ids: List[int] = None,
    ):
        # The list of requirement IDs to add to the policy.
        self.add_ids = add_ids
        # The list of requirement IDs to remove from the policy.
        self.remove_ids = remove_ids

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.add_ids is not None:
            result['AddIds'] = self.add_ids

        if self.remove_ids is not None:
            result['RemoveIds'] = self.remove_ids

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AddIds') is not None:
            self.add_ids = m.get('AddIds')

        if m.get('RemoveIds') is not None:
            self.remove_ids = m.get('RemoveIds')

        return self

class ChangeCheckConfigRequestAddedCheck(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        section_id: int = None,
    ):
        # The ID of the check item.
        # 
        # > Call [ListCheckResult](~~ListCheckResult~~) to obtain check item IDs.
        self.check_id = check_id
        # The section ID of the check item.
        self.section_id = section_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.section_id is not None:
            result['SectionId'] = self.section_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('SectionId') is not None:
            self.section_id = m.get('SectionId')

        return self


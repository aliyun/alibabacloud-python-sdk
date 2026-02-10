# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetCheckConfigResponseBody(DaraModel):
    def __init__(
        self,
        cycle_days: List[int] = None,
        enable_add_check: bool = None,
        enable_auto_check: bool = None,
        end_time: int = None,
        request_id: str = None,
        selected_checks: List[main_models.GetCheckConfigResponseBodySelectedChecks] = None,
        standards: List[main_models.GetCheckConfigResponseBodyStandards] = None,
        start_time: int = None,
    ):
        # The days in a week on which an automatic check is performed.
        self.cycle_days = cycle_days
        # Indicates whether the check for new check items in the selected requirement item is enabled by default. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_add_check = enable_add_check
        # Indicates whether the automatic check is enabled. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.enable_auto_check = enable_auto_check
        # The end time of the check. The value indicates a point in time. The time period that is specified by the start time and end time must be one of the following time periods:
        # 
        # *   **00:00 to 06:00**: If StartTime is set to 00:00, EndTime must be set to 06:00.
        # *   **06:00 to 12:00**: If StartTime is set to 06:00, EndTime must be set to 12:00.
        # *   **12:00 to 18:00**: If StartTime is set to 12:00, EndTime must be set to 18:00.
        # *   **18:00 to 24:00**: If StartTime is set to 18:00, EndTime must be set to 24:00.
        self.end_time = end_time
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The check items selected in the policy.
        self.selected_checks = selected_checks
        # The information about the check items.
        self.standards = standards
        # The start time of the check. The value indicates a point in time.
        self.start_time = start_time

    def validate(self):
        if self.selected_checks:
            for v1 in self.selected_checks:
                 if v1:
                    v1.validate()
        if self.standards:
            for v1 in self.standards:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cycle_days is not None:
            result['CycleDays'] = self.cycle_days

        if self.enable_add_check is not None:
            result['EnableAddCheck'] = self.enable_add_check

        if self.enable_auto_check is not None:
            result['EnableAutoCheck'] = self.enable_auto_check

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['SelectedChecks'] = []
        if self.selected_checks is not None:
            for k1 in self.selected_checks:
                result['SelectedChecks'].append(k1.to_map() if k1 else None)

        result['Standards'] = []
        if self.standards is not None:
            for k1 in self.standards:
                result['Standards'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CycleDays') is not None:
            self.cycle_days = m.get('CycleDays')

        if m.get('EnableAddCheck') is not None:
            self.enable_add_check = m.get('EnableAddCheck')

        if m.get('EnableAutoCheck') is not None:
            self.enable_auto_check = m.get('EnableAutoCheck')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.selected_checks = []
        if m.get('SelectedChecks') is not None:
            for k1 in m.get('SelectedChecks'):
                temp_model = main_models.GetCheckConfigResponseBodySelectedChecks()
                self.selected_checks.append(temp_model.from_map(k1))

        self.standards = []
        if m.get('Standards') is not None:
            for k1 in m.get('Standards'):
                temp_model = main_models.GetCheckConfigResponseBodyStandards()
                self.standards.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class GetCheckConfigResponseBodyStandards(DaraModel):
    def __init__(
        self,
        id: int = None,
        show_name: str = None,
        status: str = None,
        type: str = None,
    ):
        # The ID of the check item.
        self.id = id
        # The name of the check item.
        self.show_name = show_name
        # The status of the check item. Valid values:
        # 
        # *   **ON**: The check item is enabled.
        # *   **OFF**: The check item is disabled.
        self.status = status
        # The type of the check item. Valid values:
        # 
        # *   **RISK**: cloud service configuration management
        # *   **IDENTITY_PERMISSION**: identity and permission management
        # *   **COMPLIANCE**: compliance
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.show_name is not None:
            result['ShowName'] = self.show_name

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ShowName') is not None:
            self.show_name = m.get('ShowName')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class GetCheckConfigResponseBodySelectedChecks(DaraModel):
    def __init__(
        self,
        check_id: int = None,
        section_id: int = None,
    ):
        # The ID of the check item.
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


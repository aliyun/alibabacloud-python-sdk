# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class GetModuleTrialAuthInfoResponseBody(DaraModel):
    def __init__(
        self,
        data: main_models.GetModuleTrialAuthInfoResponseBodyData = None,
        request_id: str = None,
    ):
        # The returned data.
        self.data = data
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Data') is not None:
            temp_model = main_models.GetModuleTrialAuthInfoResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class GetModuleTrialAuthInfoResponseBodyData(DaraModel):
    def __init__(
        self,
        can_try: bool = None,
        module_code: str = None,
        trial_record_list: List[main_models.GetModuleTrialAuthInfoResponseBodyDataTrialRecordList] = None,
    ):
        # Indicates whether the user is qualified for the trial use. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.can_try = can_try
        # The code of the feature. Valid values:
        # 
        # *   **vulFix**: vulnerability fixing.
        # *   **cloudSiem**: threat analysis and response.
        self.module_code = module_code
        # The trial use record.
        self.trial_record_list = trial_record_list

    def validate(self):
        if self.trial_record_list:
            for v1 in self.trial_record_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.can_try is not None:
            result['CanTry'] = self.can_try

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        result['TrialRecordList'] = []
        if self.trial_record_list is not None:
            for k1 in self.trial_record_list:
                result['TrialRecordList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CanTry') is not None:
            self.can_try = m.get('CanTry')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        self.trial_record_list = []
        if m.get('TrialRecordList') is not None:
            for k1 in m.get('TrialRecordList'):
                temp_model = main_models.GetModuleTrialAuthInfoResponseBodyDataTrialRecordList()
                self.trial_record_list.append(temp_model.from_map(k1))

        return self

class GetModuleTrialAuthInfoResponseBodyDataTrialRecordList(DaraModel):
    def __init__(
        self,
        auth_limit: int = None,
        auth_limit_list: str = None,
        gmt_end: int = None,
        gmt_start: int = None,
        module_code: str = None,
        status: int = None,
    ):
        # The quota.
        self.auth_limit = auth_limit
        # The list of quotas. This parameter is available if the value of the ModuleCode parameter is cloudSiem. The value of this parameter consists of the log storage capacity for the threat analysis and response feature and the log data to add. Units: GB and GB-day.
        self.auth_limit_list = auth_limit_list
        # The end time of the trial use.
        self.gmt_end = gmt_end
        # The start time of the trial use.
        self.gmt_start = gmt_start
        # The code of the feature. Valid values:
        # 
        # *   **vulFix**: vulnerability fixing.
        # *   **cloudSiem**: threat analysis and response.
        self.module_code = module_code
        # The status of the trial use. Valid values:
        # 
        # *   **1**: The feature is in trial use.
        # *   **0**: The trial use ends.
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.auth_limit is not None:
            result['AuthLimit'] = self.auth_limit

        if self.auth_limit_list is not None:
            result['AuthLimitList'] = self.auth_limit_list

        if self.gmt_end is not None:
            result['GmtEnd'] = self.gmt_end

        if self.gmt_start is not None:
            result['GmtStart'] = self.gmt_start

        if self.module_code is not None:
            result['ModuleCode'] = self.module_code

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AuthLimit') is not None:
            self.auth_limit = m.get('AuthLimit')

        if m.get('AuthLimitList') is not None:
            self.auth_limit_list = m.get('AuthLimitList')

        if m.get('GmtEnd') is not None:
            self.gmt_end = m.get('GmtEnd')

        if m.get('GmtStart') is not None:
            self.gmt_start = m.get('GmtStart')

        if m.get('ModuleCode') is not None:
            self.module_code = m.get('ModuleCode')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


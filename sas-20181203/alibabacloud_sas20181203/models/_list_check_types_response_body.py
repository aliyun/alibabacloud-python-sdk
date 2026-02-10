# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class ListCheckTypesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[main_models.ListCheckTypesResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code.
        self.code = code
        # The total number of entries returned.
        self.count = count
        # The data returned.
        self.data = data
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   **true**
        # *   **false**
        self.success = success

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListCheckTypesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListCheckTypesResponseBodyData(DaraModel):
    def __init__(
        self,
        check_details: List[main_models.ListCheckTypesResponseBodyDataCheckDetails] = None,
        check_type: str = None,
        check_type_dis_name: str = None,
    ):
        # The detail of check items.
        self.check_details = check_details
        # The type of the check item.
        self.check_type = check_type
        # The display name of the check item type.
        self.check_type_dis_name = check_type_dis_name

    def validate(self):
        if self.check_details:
            for v1 in self.check_details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CheckDetails'] = []
        if self.check_details is not None:
            for k1 in self.check_details:
                result['CheckDetails'].append(k1.to_map() if k1 else None)

        if self.check_type is not None:
            result['CheckType'] = self.check_type

        if self.check_type_dis_name is not None:
            result['CheckTypeDisName'] = self.check_type_dis_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.check_details = []
        if m.get('CheckDetails') is not None:
            for k1 in m.get('CheckDetails'):
                temp_model = main_models.ListCheckTypesResponseBodyDataCheckDetails()
                self.check_details.append(temp_model.from_map(k1))

        if m.get('CheckType') is not None:
            self.check_type = m.get('CheckType')

        if m.get('CheckTypeDisName') is not None:
            self.check_type_dis_name = m.get('CheckTypeDisName')

        return self

class ListCheckTypesResponseBodyDataCheckDetails(DaraModel):
    def __init__(
        self,
        affiliated_risk_types: List[str] = None,
        affiliated_risks: List[str] = None,
        check_id: int = None,
        check_item: str = None,
    ):
        # The list of the baseline categories of attribution.
        self.affiliated_risk_types = affiliated_risk_types
        # The list of baselines attribution.
        self.affiliated_risks = affiliated_risks
        # The ID of the check item.
        self.check_id = check_id
        # The description of the check item.
        self.check_item = check_item

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.affiliated_risk_types is not None:
            result['AffiliatedRiskTypes'] = self.affiliated_risk_types

        if self.affiliated_risks is not None:
            result['AffiliatedRisks'] = self.affiliated_risks

        if self.check_id is not None:
            result['CheckId'] = self.check_id

        if self.check_item is not None:
            result['CheckItem'] = self.check_item

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AffiliatedRiskTypes') is not None:
            self.affiliated_risk_types = m.get('AffiliatedRiskTypes')

        if m.get('AffiliatedRisks') is not None:
            self.affiliated_risks = m.get('AffiliatedRisks')

        if m.get('CheckId') is not None:
            self.check_id = m.get('CheckId')

        if m.get('CheckItem') is not None:
            self.check_item = m.get('CheckItem')

        return self


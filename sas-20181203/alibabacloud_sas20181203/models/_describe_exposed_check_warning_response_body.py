# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeExposedCheckWarningResponseBody(DaraModel):
    def __init__(
        self,
        count: int = None,
        request_id: str = None,
        warning_list: List[main_models.DescribeExposedCheckWarningResponseBodyWarningList] = None,
    ):
        # The total number of entries returned.
        self.count = count
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # An array that consists of the baseline risk items of the exposed server.
        self.warning_list = warning_list

    def validate(self):
        if self.warning_list:
            for v1 in self.warning_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.count is not None:
            result['Count'] = self.count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['WarningList'] = []
        if self.warning_list is not None:
            for k1 in self.warning_list:
                result['WarningList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.warning_list = []
        if m.get('WarningList') is not None:
            for k1 in m.get('WarningList'):
                temp_model = main_models.DescribeExposedCheckWarningResponseBodyWarningList()
                self.warning_list.append(temp_model.from_map(k1))

        return self

class DescribeExposedCheckWarningResponseBodyWarningList(DaraModel):
    def __init__(
        self,
        risk_id: int = None,
        risk_name: str = None,
        sub_type_alias: str = None,
        type_alias: str = None,
        uuid: str = None,
    ):
        # The ID of the baseline.
        # 
        # >  You can call the [DescribeCheckWarningSummary](https://help.aliyun.com/document_detail/116179.html) operation to query the IDs of baselines.
        self.risk_id = risk_id
        # The name of the baseline.
        self.risk_name = risk_name
        # The display name of the baseline sub type.
        self.sub_type_alias = sub_type_alias
        # The display name of the baseline type.
        self.type_alias = type_alias
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.risk_id is not None:
            result['RiskId'] = self.risk_id

        if self.risk_name is not None:
            result['RiskName'] = self.risk_name

        if self.sub_type_alias is not None:
            result['SubTypeAlias'] = self.sub_type_alias

        if self.type_alias is not None:
            result['TypeAlias'] = self.type_alias

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RiskId') is not None:
            self.risk_id = m.get('RiskId')

        if m.get('RiskName') is not None:
            self.risk_name = m.get('RiskName')

        if m.get('SubTypeAlias') is not None:
            self.sub_type_alias = m.get('SubTypeAlias')

        if m.get('TypeAlias') is not None:
            self.type_alias = m.get('TypeAlias')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self


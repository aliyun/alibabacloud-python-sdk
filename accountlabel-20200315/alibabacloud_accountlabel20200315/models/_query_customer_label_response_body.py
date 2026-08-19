# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_accountlabel20200315 import models as main_models
from darabonba.model import DaraModel

class QueryCustomerLabelResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryCustomerLabelResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
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
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.QueryCustomerLabelResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryCustomerLabelResponseBodyData(DaraModel):
    def __init__(
        self,
        customer_label: List[main_models.QueryCustomerLabelResponseBodyDataCustomerLabel] = None,
    ):
        self.customer_label = customer_label

    def validate(self):
        if self.customer_label:
            for v1 in self.customer_label:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['CustomerLabel'] = []
        if self.customer_label is not None:
            for k1 in self.customer_label:
                result['CustomerLabel'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.customer_label = []
        if m.get('CustomerLabel') is not None:
            for k1 in m.get('CustomerLabel'):
                temp_model = main_models.QueryCustomerLabelResponseBodyDataCustomerLabel()
                self.customer_label.append(temp_model.from_map(k1))

        return self

class QueryCustomerLabelResponseBodyDataCustomerLabel(DaraModel):
    def __init__(
        self,
        creator: str = None,
        end_time_str: str = None,
        gmt_created_str: str = None,
        gmt_modified_str: str = None,
        id: str = None,
        label: str = None,
        label_series: str = None,
        start_time_str: str = None,
    ):
        self.creator = creator
        self.end_time_str = end_time_str
        self.gmt_created_str = gmt_created_str
        self.gmt_modified_str = gmt_modified_str
        self.id = id
        self.label = label
        self.label_series = label_series
        self.start_time_str = start_time_str

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.end_time_str is not None:
            result['EndTimeStr'] = self.end_time_str

        if self.gmt_created_str is not None:
            result['GmtCreatedStr'] = self.gmt_created_str

        if self.gmt_modified_str is not None:
            result['GmtModifiedStr'] = self.gmt_modified_str

        if self.id is not None:
            result['Id'] = self.id

        if self.label is not None:
            result['Label'] = self.label

        if self.label_series is not None:
            result['LabelSeries'] = self.label_series

        if self.start_time_str is not None:
            result['StartTimeStr'] = self.start_time_str

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('EndTimeStr') is not None:
            self.end_time_str = m.get('EndTimeStr')

        if m.get('GmtCreatedStr') is not None:
            self.gmt_created_str = m.get('GmtCreatedStr')

        if m.get('GmtModifiedStr') is not None:
            self.gmt_modified_str = m.get('GmtModifiedStr')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LabelSeries') is not None:
            self.label_series = m.get('LabelSeries')

        if m.get('StartTimeStr') is not None:
            self.start_time_str = m.get('StartTimeStr')

        return self


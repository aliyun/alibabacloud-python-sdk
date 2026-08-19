# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_accountlabel20200315 import models as main_models
from darabonba.model import DaraModel

class BatchFetchAccountLabelResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        data: List[main_models.BatchFetchAccountLabelResponseBodyData] = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.data = data
        self.message = message
        self.request_id = request_id
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
                temp_model = main_models.BatchFetchAccountLabelResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self



class BatchFetchAccountLabelResponseBodyData(DaraModel):
    def __init__(
        self,
        creator: str = None,
        end_time: str = None,
        gmt_created: str = None,
        gmt_modified: str = None,
        kp: int = None,
        label: str = None,
        label_series: str = None,
        start_time: str = None,
    ):
        self.creator = creator
        self.end_time = end_time
        self.gmt_created = gmt_created
        self.gmt_modified = gmt_modified
        self.kp = kp
        self.label = label
        self.label_series = label_series
        self.start_time = start_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.creator is not None:
            result['Creator'] = self.creator

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.gmt_created is not None:
            result['GmtCreated'] = self.gmt_created

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.kp is not None:
            result['Kp'] = self.kp

        if self.label is not None:
            result['Label'] = self.label

        if self.label_series is not None:
            result['LabelSeries'] = self.label_series

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Creator') is not None:
            self.creator = m.get('Creator')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('GmtCreated') is not None:
            self.gmt_created = m.get('GmtCreated')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Kp') is not None:
            self.kp = m.get('Kp')

        if m.get('Label') is not None:
            self.label = m.get('Label')

        if m.get('LabelSeries') is not None:
            self.label_series = m.get('LabelSeries')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self


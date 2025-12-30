# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetSupplementDagrunResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        dagrun_list: List[main_models.GetSupplementDagrunResponseBodyDagrunList] = None,
        http_status_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.dagrun_list = dagrun_list
        self.http_status_code = http_status_code
        self.message = message
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.dagrun_list:
            for v1 in self.dagrun_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        result['DagrunList'] = []
        if self.dagrun_list is not None:
            for k1 in self.dagrun_list:
                result['DagrunList'].append(k1.to_map() if k1 else None)

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

        self.dagrun_list = []
        if m.get('DagrunList') is not None:
            for k1 in m.get('DagrunList'):
                temp_model = main_models.GetSupplementDagrunResponseBodyDagrunList()
                self.dagrun_list.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetSupplementDagrunResponseBodyDagrunList(DaraModel):
    def __init__(
        self,
        biz_date: str = None,
        duration: str = None,
        end_execute_time: int = None,
        id: str = None,
        start_execute_time: int = None,
        status: str = None,
        supplement_id: str = None,
    ):
        self.biz_date = biz_date
        self.duration = duration
        self.end_execute_time = end_execute_time
        # Dagrun ID
        self.id = id
        self.start_execute_time = start_execute_time
        self.status = status
        self.supplement_id = supplement_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_date is not None:
            result['BizDate'] = self.biz_date

        if self.duration is not None:
            result['Duration'] = self.duration

        if self.end_execute_time is not None:
            result['EndExecuteTime'] = self.end_execute_time

        if self.id is not None:
            result['Id'] = self.id

        if self.start_execute_time is not None:
            result['StartExecuteTime'] = self.start_execute_time

        if self.status is not None:
            result['Status'] = self.status

        if self.supplement_id is not None:
            result['SupplementId'] = self.supplement_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizDate') is not None:
            self.biz_date = m.get('BizDate')

        if m.get('Duration') is not None:
            self.duration = m.get('Duration')

        if m.get('EndExecuteTime') is not None:
            self.end_execute_time = m.get('EndExecuteTime')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('StartExecuteTime') is not None:
            self.start_execute_time = m.get('StartExecuteTime')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SupplementId') is not None:
            self.supplement_id = m.get('SupplementId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class InsertAiOutboundPhoneNumsRequest(DaraModel):
    def __init__(
        self,
        batch_version: int = None,
        details: List[main_models.InsertAiOutboundPhoneNumsRequestDetails] = None,
        instance_id: str = None,
        task_id: int = None,
    ):
        self.batch_version = batch_version
        # This parameter is required.
        self.details = details
        # This parameter is required.
        self.instance_id = instance_id
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        if self.details:
            for v1 in self.details:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_version is not None:
            result['BatchVersion'] = self.batch_version

        result['Details'] = []
        if self.details is not None:
            for k1 in self.details:
                result['Details'].append(k1.to_map() if k1 else None)

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchVersion') is not None:
            self.batch_version = m.get('BatchVersion')

        self.details = []
        if m.get('Details') is not None:
            for k1 in m.get('Details'):
                temp_model = main_models.InsertAiOutboundPhoneNumsRequestDetails()
                self.details.append(temp_model.from_map(k1))

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self

class InsertAiOutboundPhoneNumsRequestDetails(DaraModel):
    def __init__(
        self,
        biz_data: str = None,
        phone_num: str = None,
    ):
        self.biz_data = biz_data
        self.phone_num = phone_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_data is not None:
            result['BizData'] = self.biz_data

        if self.phone_num is not None:
            result['PhoneNum'] = self.phone_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizData') is not None:
            self.biz_data = m.get('BizData')

        if m.get('PhoneNum') is not None:
            self.phone_num = m.get('PhoneNum')

        return self


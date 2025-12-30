# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class PausePhysicalNodeResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        node_operate_result_list: List[main_models.PausePhysicalNodeResponseBodyNodeOperateResultList] = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.node_operate_result_list = node_operate_result_list
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_operate_result_list:
            for v1 in self.node_operate_result_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        result['NodeOperateResultList'] = []
        if self.node_operate_result_list is not None:
            for k1 in self.node_operate_result_list:
                result['NodeOperateResultList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        self.node_operate_result_list = []
        if m.get('NodeOperateResultList') is not None:
            for k1 in m.get('NodeOperateResultList'):
                temp_model = main_models.PausePhysicalNodeResponseBodyNodeOperateResultList()
                self.node_operate_result_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class PausePhysicalNodeResponseBodyNodeOperateResultList(DaraModel):
    def __init__(
        self,
        error_message: str = None,
        node_id: str = None,
        status: str = None,
    ):
        self.error_message = error_message
        self.node_id = node_id
        self.status = status

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.node_id is not None:
            result['NodeId'] = self.node_id

        if self.status is not None:
            result['Status'] = self.status

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('NodeId') is not None:
            self.node_id = m.get('NodeId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetVhostErrorByTaskIdResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetVhostErrorByTaskIdResponseBodyData = None,
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
            temp_model = main_models.GetVhostErrorByTaskIdResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetVhostErrorByTaskIdResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: main_models.GetVhostErrorByTaskIdResponseBodyDataVoList = None,
    ):
        self.current_page = current_page
        self.page_size = page_size
        self.total_count = total_count
        self.vo_list = vo_list

    def validate(self):
        if self.vo_list:
            self.vo_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        if self.vo_list is not None:
            result['VoList'] = self.vo_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        if m.get('VoList') is not None:
            temp_model = main_models.GetVhostErrorByTaskIdResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m.get('VoList'))

        return self

class GetVhostErrorByTaskIdResponseBodyDataVoList(DaraModel):
    def __init__(
        self,
        vhost_error_do: List[main_models.GetVhostErrorByTaskIdResponseBodyDataVoListVhostErrorDO] = None,
    ):
        self.vhost_error_do = vhost_error_do

    def validate(self):
        if self.vhost_error_do:
            for v1 in self.vhost_error_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['VhostErrorDO'] = []
        if self.vhost_error_do is not None:
            for k1 in self.vhost_error_do:
                result['VhostErrorDO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.vhost_error_do = []
        if m.get('VhostErrorDO') is not None:
            for k1 in m.get('VhostErrorDO'):
                temp_model = main_models.GetVhostErrorByTaskIdResponseBodyDataVoListVhostErrorDO()
                self.vhost_error_do.append(temp_model.from_map(k1))

        return self

class GetVhostErrorByTaskIdResponseBodyDataVoListVhostErrorDO(DaraModel):
    def __init__(
        self,
        error_message: int = None,
        task_id: int = None,
        vhost_name: str = None,
    ):
        self.error_message = error_message
        self.task_id = task_id
        self.vhost_name = vhost_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        return self


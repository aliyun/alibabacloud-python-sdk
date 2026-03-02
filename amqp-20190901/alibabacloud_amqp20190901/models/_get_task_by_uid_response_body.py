# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_amqp20190901 import models as main_models
from darabonba.model import DaraModel

class GetTaskByUidResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.GetTaskByUidResponseBodyData = None,
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
            temp_model = main_models.GetTaskByUidResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetTaskByUidResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
        vo_list: main_models.GetTaskByUidResponseBodyDataVoList = None,
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
            temp_model = main_models.GetTaskByUidResponseBodyDataVoList()
            self.vo_list = temp_model.from_map(m.get('VoList'))

        return self

class GetTaskByUidResponseBodyDataVoList(DaraModel):
    def __init__(
        self,
        import_definition_task_do: List[main_models.GetTaskByUidResponseBodyDataVoListImportDefinitionTaskDO] = None,
    ):
        self.import_definition_task_do = import_definition_task_do

    def validate(self):
        if self.import_definition_task_do:
            for v1 in self.import_definition_task_do:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ImportDefinitionTaskDO'] = []
        if self.import_definition_task_do is not None:
            for k1 in self.import_definition_task_do:
                result['ImportDefinitionTaskDO'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.import_definition_task_do = []
        if m.get('ImportDefinitionTaskDO') is not None:
            for k1 in m.get('ImportDefinitionTaskDO'):
                temp_model = main_models.GetTaskByUidResponseBodyDataVoListImportDefinitionTaskDO()
                self.import_definition_task_do.append(temp_model.from_map(k1))

        return self

class GetTaskByUidResponseBodyDataVoListImportDefinitionTaskDO(DaraModel):
    def __init__(
        self,
        binding_num: int = None,
        exchange_num: int = None,
        gmt_create: str = None,
        id: int = None,
        import_type: int = None,
        instance_id: str = None,
        instance_name: str = None,
        queue_num: int = None,
        status: int = None,
        user_id: int = None,
        vhost_name: str = None,
        vhost_num: int = None,
    ):
        self.binding_num = binding_num
        self.exchange_num = exchange_num
        self.gmt_create = gmt_create
        self.id = id
        self.import_type = import_type
        self.instance_id = instance_id
        self.instance_name = instance_name
        self.queue_num = queue_num
        self.status = status
        self.user_id = user_id
        self.vhost_name = vhost_name
        self.vhost_num = vhost_num

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.binding_num is not None:
            result['BindingNum'] = self.binding_num

        if self.exchange_num is not None:
            result['ExchangeNum'] = self.exchange_num

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.id is not None:
            result['Id'] = self.id

        if self.import_type is not None:
            result['ImportType'] = self.import_type

        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id

        if self.instance_name is not None:
            result['InstanceName'] = self.instance_name

        if self.queue_num is not None:
            result['QueueNum'] = self.queue_num

        if self.status is not None:
            result['Status'] = self.status

        if self.user_id is not None:
            result['UserId'] = self.user_id

        if self.vhost_name is not None:
            result['VhostName'] = self.vhost_name

        if self.vhost_num is not None:
            result['VhostNum'] = self.vhost_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BindingNum') is not None:
            self.binding_num = m.get('BindingNum')

        if m.get('ExchangeNum') is not None:
            self.exchange_num = m.get('ExchangeNum')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ImportType') is not None:
            self.import_type = m.get('ImportType')

        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')

        if m.get('InstanceName') is not None:
            self.instance_name = m.get('InstanceName')

        if m.get('QueueNum') is not None:
            self.queue_num = m.get('QueueNum')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')

        if m.get('VhostName') is not None:
            self.vhost_name = m.get('VhostName')

        if m.get('VhostNum') is not None:
            self.vhost_num = m.get('VhostNum')

        return self


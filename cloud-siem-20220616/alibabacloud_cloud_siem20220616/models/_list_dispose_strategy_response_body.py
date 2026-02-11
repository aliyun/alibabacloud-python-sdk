# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_cloud_siem20220616 import models as main_models
from darabonba.model import DaraModel

class ListDisposeStrategyResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.ListDisposeStrategyResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The HTTP status code.
        self.code = code
        # The data returned.
        self.data = data
        # The returned message.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful. Valid values:
        # 
        # *   true
        # *   false
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
            temp_model = main_models.ListDisposeStrategyResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListDisposeStrategyResponseBodyData(DaraModel):
    def __init__(
        self,
        page_info: main_models.ListDisposeStrategyResponseBodyDataPageInfo = None,
        response_data: List[main_models.ListDisposeStrategyResponseBodyDataResponseData] = None,
    ):
        # The pagination information.
        self.page_info = page_info
        # The detailed data.
        self.response_data = response_data

    def validate(self):
        if self.page_info:
            self.page_info.validate()
        if self.response_data:
            for v1 in self.response_data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.page_info is not None:
            result['PageInfo'] = self.page_info.to_map()

        result['ResponseData'] = []
        if self.response_data is not None:
            for k1 in self.response_data:
                result['ResponseData'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('PageInfo') is not None:
            temp_model = main_models.ListDisposeStrategyResponseBodyDataPageInfo()
            self.page_info = temp_model.from_map(m.get('PageInfo'))

        self.response_data = []
        if m.get('ResponseData') is not None:
            for k1 in m.get('ResponseData'):
                temp_model = main_models.ListDisposeStrategyResponseBodyDataResponseData()
                self.response_data.append(temp_model.from_map(k1))

        return self

class ListDisposeStrategyResponseBodyDataResponseData(DaraModel):
    def __init__(
        self,
        alert_uuid: str = None,
        aliuid: int = None,
        effective_status: int = None,
        entity: List[Any] = None,
        entity_id: int = None,
        entity_type: str = None,
        error_message: str = None,
        finish_time: str = None,
        gmt_create: str = None,
        gmt_modified: str = None,
        id: int = None,
        incident_name: str = None,
        incident_uuid: str = None,
        playbook_name: str = None,
        playbook_type: str = None,
        playbook_uuid: str = None,
        scope: List[Any] = None,
        sophon_task_id: str = None,
        status: int = None,
        sub_aliuid: int = None,
        task_param: str = None,
        task_url: str = None,
    ):
        # The UUID of the alert.
        self.alert_uuid = alert_uuid
        # The ID of the Alibaba Cloud account that is associated with the policy in SIEM.
        self.aliuid = aliuid
        # The status of the policy. Valid values:
        # 
        # *   0: invalid
        # *   1: valid
        self.effective_status = effective_status
        # The details of the entity. The value is a JSON array.
        self.entity = entity
        # The ID of the entity.
        self.entity_id = entity_id
        # The type of the entity. Valid values:
        # 
        # *   ip
        # *   process
        # *   file
        self.entity_type = entity_type
        # The summary information about the failed task.
        self.error_message = error_message
        # The end time of the task.
        self.finish_time = finish_time
        # The creation time.
        self.gmt_create = gmt_create
        # The update time.
        self.gmt_modified = gmt_modified
        # The ID of the policy.
        self.id = id
        # The name of the event.
        self.incident_name = incident_name
        # The UUID of the event.
        self.incident_uuid = incident_uuid
        # The name of the playbook, which is the unique identifier of the playbook.
        self.playbook_name = playbook_name
        # The type of the playbook. Valid values:
        # 
        # *   system: user-triggered playbook
        # *   custom: event-triggered playbook
        # *   custom_alert: alert-triggered playbook
        # *   soar-manual: user-run playbook
        # *   soar-mdr: MDR-run playbook
        self.playbook_type = playbook_type
        # The UUID of the playbook.
        self.playbook_uuid = playbook_uuid
        # The scope of the policy.
        self.scope = scope
        # The ID of the SOAR handling policy.
        self.sophon_task_id = sophon_task_id
        # The running status of the playbook. Valid values:
        # 
        # *   200: successful
        # *   10: deleted
        # *   5: failed
        # *   0: initial
        self.status = status
        # The ID of the Alibaba account that is used to configure the policy.
        self.sub_aliuid = sub_aliuid
        # The parameters that are used to trigger the playbook. The value is in the JSON format.
        self.task_param = task_param
        self.task_url = task_url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_uuid is not None:
            result['AlertUuid'] = self.alert_uuid

        if self.aliuid is not None:
            result['Aliuid'] = self.aliuid

        if self.effective_status is not None:
            result['EffectiveStatus'] = self.effective_status

        if self.entity is not None:
            result['Entity'] = self.entity

        if self.entity_id is not None:
            result['EntityId'] = self.entity_id

        if self.entity_type is not None:
            result['EntityType'] = self.entity_type

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.finish_time is not None:
            result['FinishTime'] = self.finish_time

        if self.gmt_create is not None:
            result['GmtCreate'] = self.gmt_create

        if self.gmt_modified is not None:
            result['GmtModified'] = self.gmt_modified

        if self.id is not None:
            result['Id'] = self.id

        if self.incident_name is not None:
            result['IncidentName'] = self.incident_name

        if self.incident_uuid is not None:
            result['IncidentUuid'] = self.incident_uuid

        if self.playbook_name is not None:
            result['PlaybookName'] = self.playbook_name

        if self.playbook_type is not None:
            result['PlaybookType'] = self.playbook_type

        if self.playbook_uuid is not None:
            result['PlaybookUuid'] = self.playbook_uuid

        if self.scope is not None:
            result['Scope'] = self.scope

        if self.sophon_task_id is not None:
            result['SophonTaskId'] = self.sophon_task_id

        if self.status is not None:
            result['Status'] = self.status

        if self.sub_aliuid is not None:
            result['SubAliuid'] = self.sub_aliuid

        if self.task_param is not None:
            result['TaskParam'] = self.task_param

        if self.task_url is not None:
            result['TaskUrl'] = self.task_url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AlertUuid') is not None:
            self.alert_uuid = m.get('AlertUuid')

        if m.get('Aliuid') is not None:
            self.aliuid = m.get('Aliuid')

        if m.get('EffectiveStatus') is not None:
            self.effective_status = m.get('EffectiveStatus')

        if m.get('Entity') is not None:
            self.entity = m.get('Entity')

        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')

        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('FinishTime') is not None:
            self.finish_time = m.get('FinishTime')

        if m.get('GmtCreate') is not None:
            self.gmt_create = m.get('GmtCreate')

        if m.get('GmtModified') is not None:
            self.gmt_modified = m.get('GmtModified')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('IncidentName') is not None:
            self.incident_name = m.get('IncidentName')

        if m.get('IncidentUuid') is not None:
            self.incident_uuid = m.get('IncidentUuid')

        if m.get('PlaybookName') is not None:
            self.playbook_name = m.get('PlaybookName')

        if m.get('PlaybookType') is not None:
            self.playbook_type = m.get('PlaybookType')

        if m.get('PlaybookUuid') is not None:
            self.playbook_uuid = m.get('PlaybookUuid')

        if m.get('Scope') is not None:
            self.scope = m.get('Scope')

        if m.get('SophonTaskId') is not None:
            self.sophon_task_id = m.get('SophonTaskId')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('SubAliuid') is not None:
            self.sub_aliuid = m.get('SubAliuid')

        if m.get('TaskParam') is not None:
            self.task_param = m.get('TaskParam')

        if m.get('TaskUrl') is not None:
            self.task_url = m.get('TaskUrl')

        return self

class ListDisposeStrategyResponseBodyDataPageInfo(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        page_size: int = None,
        total_count: int = None,
    ):
        # The current page number.
        self.current_page = current_page
        # The number of entries per page.
        self.page_size = page_size
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        pass

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self


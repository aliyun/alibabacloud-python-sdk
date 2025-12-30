# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_dataphin_public20230630 import models as main_models
from darabonba.model import DaraModel

class GetPhysicalNodeByOutputNameResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        http_status_code: int = None,
        message: str = None,
        node_info: main_models.GetPhysicalNodeByOutputNameResponseBodyNodeInfo = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.http_status_code = http_status_code
        self.message = message
        self.node_info = node_info
        self.request_id = request_id
        self.success = success

    def validate(self):
        if self.node_info:
            self.node_info.validate()

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

        if self.node_info is not None:
            result['NodeInfo'] = self.node_info.to_map()

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

        if m.get('NodeInfo') is not None:
            temp_model = main_models.GetPhysicalNodeByOutputNameResponseBodyNodeInfo()
            self.node_info = temp_model.from_map(m.get('NodeInfo'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class GetPhysicalNodeByOutputNameResponseBodyNodeInfo(DaraModel):
    def __init__(
        self,
        create_time: int = None,
        creator: main_models.GetPhysicalNodeByOutputNameResponseBodyNodeInfoCreator = None,
        description: str = None,
        from_: str = None,
        id: str = None,
        last_modified_time: int = None,
        modifier: main_models.GetPhysicalNodeByOutputNameResponseBodyNodeInfoModifier = None,
        name: str = None,
        operator_type: str = None,
        owner: main_models.GetPhysicalNodeByOutputNameResponseBodyNodeInfoOwner = None,
        priority: str = None,
        project_info: main_models.GetPhysicalNodeByOutputNameResponseBodyNodeInfoProjectInfo = None,
        schedule_type: str = None,
        status: str = None,
        trigger_config: str = None,
    ):
        self.create_time = create_time
        self.creator = creator
        self.description = description
        self.from_ = from_
        self.id = id
        self.last_modified_time = last_modified_time
        self.modifier = modifier
        self.name = name
        self.operator_type = operator_type
        self.owner = owner
        self.priority = priority
        self.project_info = project_info
        self.schedule_type = schedule_type
        self.status = status
        self.trigger_config = trigger_config

    def validate(self):
        if self.creator:
            self.creator.validate()
        if self.modifier:
            self.modifier.validate()
        if self.owner:
            self.owner.validate()
        if self.project_info:
            self.project_info.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.creator is not None:
            result['Creator'] = self.creator.to_map()

        if self.description is not None:
            result['Description'] = self.description

        if self.from_ is not None:
            result['From'] = self.from_

        if self.id is not None:
            result['Id'] = self.id

        if self.last_modified_time is not None:
            result['LastModifiedTime'] = self.last_modified_time

        if self.modifier is not None:
            result['Modifier'] = self.modifier.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.operator_type is not None:
            result['OperatorType'] = self.operator_type

        if self.owner is not None:
            result['Owner'] = self.owner.to_map()

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.project_info is not None:
            result['ProjectInfo'] = self.project_info.to_map()

        if self.schedule_type is not None:
            result['ScheduleType'] = self.schedule_type

        if self.status is not None:
            result['Status'] = self.status

        if self.trigger_config is not None:
            result['TriggerConfig'] = self.trigger_config

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Creator') is not None:
            temp_model = main_models.GetPhysicalNodeByOutputNameResponseBodyNodeInfoCreator()
            self.creator = temp_model.from_map(m.get('Creator'))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('LastModifiedTime') is not None:
            self.last_modified_time = m.get('LastModifiedTime')

        if m.get('Modifier') is not None:
            temp_model = main_models.GetPhysicalNodeByOutputNameResponseBodyNodeInfoModifier()
            self.modifier = temp_model.from_map(m.get('Modifier'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('OperatorType') is not None:
            self.operator_type = m.get('OperatorType')

        if m.get('Owner') is not None:
            temp_model = main_models.GetPhysicalNodeByOutputNameResponseBodyNodeInfoOwner()
            self.owner = temp_model.from_map(m.get('Owner'))

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('ProjectInfo') is not None:
            temp_model = main_models.GetPhysicalNodeByOutputNameResponseBodyNodeInfoProjectInfo()
            self.project_info = temp_model.from_map(m.get('ProjectInfo'))

        if m.get('ScheduleType') is not None:
            self.schedule_type = m.get('ScheduleType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('TriggerConfig') is not None:
            self.trigger_config = m.get('TriggerConfig')

        return self

class GetPhysicalNodeByOutputNameResponseBodyNodeInfoProjectInfo(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetPhysicalNodeByOutputNameResponseBodyNodeInfoOwner(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetPhysicalNodeByOutputNameResponseBodyNodeInfoModifier(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self

class GetPhysicalNodeByOutputNameResponseBodyNodeInfoCreator(DaraModel):
    def __init__(
        self,
        id: str = None,
        name: str = None,
    ):
        self.id = id
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.id is not None:
            result['Id'] = self.id

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self


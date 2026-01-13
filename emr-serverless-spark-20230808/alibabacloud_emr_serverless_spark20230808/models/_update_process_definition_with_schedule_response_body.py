# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from alibabacloud_emr_serverless_spark20230808 import models as main_models
from darabonba.model import DaraModel

class UpdateProcessDefinitionWithScheduleResponseBody(DaraModel):
    def __init__(
        self,
        code: int = None,
        data: main_models.UpdateProcessDefinitionWithScheduleResponseBodyData = None,
        failed: str = None,
        http_status_code: int = None,
        msg: str = None,
        request_id: str = None,
        success: str = None,
    ):
        # The code that is returned by the backend server.
        self.code = code
        # The data returned.
        self.data = data
        # Indicates whether the request failed.
        self.failed = failed
        # The HTTP status code.
        self.http_status_code = http_status_code
        # The description of the returned code.
        self.msg = msg
        # The request ID.
        self.request_id = request_id
        # Indicates whether the request was successful.
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
            result['code'] = self.code

        if self.data is not None:
            result['data'] = self.data.to_map()

        if self.failed is not None:
            result['failed'] = self.failed

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.msg is not None:
            result['msg'] = self.msg

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('data') is not None:
            temp_model = main_models.UpdateProcessDefinitionWithScheduleResponseBodyData()
            self.data = temp_model.from_map(m.get('data'))

        if m.get('failed') is not None:
            self.failed = m.get('failed')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('msg') is not None:
            self.msg = m.get('msg')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class UpdateProcessDefinitionWithScheduleResponseBodyData(DaraModel):
    def __init__(
        self,
        alert_email_address: str = None,
        biz_id: str = None,
        code: str = None,
        create_time: str = None,
        crontab: str = None,
        description: str = None,
        end_time: str = None,
        execution_type: str = None,
        id: str = None,
        name: str = None,
        project_name: str = None,
        release_state: str = None,
        start_time: str = None,
        timezone_id: str = None,
        update_time: str = None,
        user_id: str = None,
        user_name: str = None,
        version: int = None,
        version_hash_code: str = None,
    ):
        # The email address to receive alerts.
        self.alert_email_address = alert_email_address
        # The workspace ID.
        self.biz_id = biz_id
        # The workflow ID.
        self.code = code
        # The time when the workflow was created.
        self.create_time = create_time
        # The CRON expression that is used for scheduling.
        self.crontab = crontab
        # The node description.
        self.description = description
        # The end of the end time range.
        self.end_time = end_time
        # The execution policy.
        self.execution_type = execution_type
        # The serial number of the workflow.
        self.id = id
        # The name of the workflow.
        self.name = name
        # The name of the project to which the workflow belongs.
        self.project_name = project_name
        # The status of the workflow.
        self.release_state = release_state
        # The start time of the scheduling.
        self.start_time = start_time
        # The ID of the time zone.
        self.timezone_id = timezone_id
        # The time when the workflow was updated.
        self.update_time = update_time
        # The ID of the user that is used to initiate a scheduling.
        self.user_id = user_id
        # The name of the user that is used to initiate a scheduling.
        self.user_name = user_name
        # The version number.
        self.version = version
        # The hash code of the version.
        self.version_hash_code = version_hash_code

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.alert_email_address is not None:
            result['alertEmailAddress'] = self.alert_email_address

        if self.biz_id is not None:
            result['bizId'] = self.biz_id

        if self.code is not None:
            result['code'] = self.code

        if self.create_time is not None:
            result['createTime'] = self.create_time

        if self.crontab is not None:
            result['crontab'] = self.crontab

        if self.description is not None:
            result['description'] = self.description

        if self.end_time is not None:
            result['endTime'] = self.end_time

        if self.execution_type is not None:
            result['executionType'] = self.execution_type

        if self.id is not None:
            result['id'] = self.id

        if self.name is not None:
            result['name'] = self.name

        if self.project_name is not None:
            result['projectName'] = self.project_name

        if self.release_state is not None:
            result['releaseState'] = self.release_state

        if self.start_time is not None:
            result['startTime'] = self.start_time

        if self.timezone_id is not None:
            result['timezoneId'] = self.timezone_id

        if self.update_time is not None:
            result['updateTime'] = self.update_time

        if self.user_id is not None:
            result['userId'] = self.user_id

        if self.user_name is not None:
            result['userName'] = self.user_name

        if self.version is not None:
            result['version'] = self.version

        if self.version_hash_code is not None:
            result['versionHashCode'] = self.version_hash_code

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('alertEmailAddress') is not None:
            self.alert_email_address = m.get('alertEmailAddress')

        if m.get('bizId') is not None:
            self.biz_id = m.get('bizId')

        if m.get('code') is not None:
            self.code = m.get('code')

        if m.get('createTime') is not None:
            self.create_time = m.get('createTime')

        if m.get('crontab') is not None:
            self.crontab = m.get('crontab')

        if m.get('description') is not None:
            self.description = m.get('description')

        if m.get('endTime') is not None:
            self.end_time = m.get('endTime')

        if m.get('executionType') is not None:
            self.execution_type = m.get('executionType')

        if m.get('id') is not None:
            self.id = m.get('id')

        if m.get('name') is not None:
            self.name = m.get('name')

        if m.get('projectName') is not None:
            self.project_name = m.get('projectName')

        if m.get('releaseState') is not None:
            self.release_state = m.get('releaseState')

        if m.get('startTime') is not None:
            self.start_time = m.get('startTime')

        if m.get('timezoneId') is not None:
            self.timezone_id = m.get('timezoneId')

        if m.get('updateTime') is not None:
            self.update_time = m.get('updateTime')

        if m.get('userId') is not None:
            self.user_id = m.get('userId')

        if m.get('userName') is not None:
            self.user_name = m.get('userName')

        if m.get('version') is not None:
            self.version = m.get('version')

        if m.get('versionHashCode') is not None:
            self.version_hash_code = m.get('versionHashCode')

        return self


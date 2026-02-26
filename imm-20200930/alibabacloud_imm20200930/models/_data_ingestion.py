# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Dict, Any

from alibabacloud_imm20200930 import models as main_models
from darabonba.model import DaraModel

class DataIngestion(DaraModel):
    def __init__(
        self,
        actions: List[main_models.DataIngestionActions] = None,
        create_time: str = None,
        error: str = None,
        id: str = None,
        input: main_models.Input = None,
        marker: str = None,
        notification: main_models.DataIngestionNotification = None,
        phase: str = None,
        service_role: str = None,
        state: str = None,
        statistic: main_models.DataIngestionStatistic = None,
        tags: Dict[str, Any] = None,
        update_time: str = None,
    ):
        # The templates.
        self.actions = actions
        # The time when the task was created.
        self.create_time = create_time
        # The error message.
        self.error = error
        # The unique ID of the data ingestion.
        self.id = id
        # The information about the data source.
        self.input = input
        # The task execution location.
        self.marker = marker
        # The notification for task completion.
        self.notification = notification
        # The scanning phase.
        self.phase = phase
        # The service-linked role.
        self.service_role = service_role
        # The status of the batch processing task.
        # 
        # *   Ready: The task is created.
        # *   Running: The task is running.
        # *   Failed: The task fails and cannot be automatically recovered.
        # *   Suspended: The task is suspended.
        # *   Succeeded: The task is successful.
        self.state = state
        # The statistical information.
        self.statistic = statistic
        # The task tags.
        self.tags = tags
        # The time when the task was updated.
        self.update_time = update_time

    def validate(self):
        if self.actions:
            for v1 in self.actions:
                 if v1:
                    v1.validate()
        if self.input:
            self.input.validate()
        if self.notification:
            self.notification.validate()
        if self.statistic:
            self.statistic.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Actions'] = []
        if self.actions is not None:
            for k1 in self.actions:
                result['Actions'].append(k1.to_map() if k1 else None)

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.error is not None:
            result['Error'] = self.error

        if self.id is not None:
            result['Id'] = self.id

        if self.input is not None:
            result['Input'] = self.input.to_map()

        if self.marker is not None:
            result['Marker'] = self.marker

        if self.notification is not None:
            result['Notification'] = self.notification.to_map()

        if self.phase is not None:
            result['Phase'] = self.phase

        if self.service_role is not None:
            result['ServiceRole'] = self.service_role

        if self.state is not None:
            result['State'] = self.state

        if self.statistic is not None:
            result['Statistic'] = self.statistic.to_map()

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.actions = []
        if m.get('Actions') is not None:
            for k1 in m.get('Actions'):
                temp_model = main_models.DataIngestionActions()
                self.actions.append(temp_model.from_map(k1))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Error') is not None:
            self.error = m.get('Error')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('Input') is not None:
            temp_model = main_models.Input()
            self.input = temp_model.from_map(m.get('Input'))

        if m.get('Marker') is not None:
            self.marker = m.get('Marker')

        if m.get('Notification') is not None:
            temp_model = main_models.DataIngestionNotification()
            self.notification = temp_model.from_map(m.get('Notification'))

        if m.get('Phase') is not None:
            self.phase = m.get('Phase')

        if m.get('ServiceRole') is not None:
            self.service_role = m.get('ServiceRole')

        if m.get('State') is not None:
            self.state = m.get('State')

        if m.get('Statistic') is not None:
            temp_model = main_models.DataIngestionStatistic()
            self.statistic = temp_model.from_map(m.get('Statistic'))

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        return self

class DataIngestionStatistic(DaraModel):
    def __init__(
        self,
        skip_files: int = None,
        submit_failure: int = None,
        submit_success: int = None,
    ):
        # The number of files that are skipped.
        self.skip_files = skip_files
        # The number of files that fail to be submitted.
        self.submit_failure = submit_failure
        # The number of files that are submitted.
        self.submit_success = submit_success

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skip_files is not None:
            result['SkipFiles'] = self.skip_files

        if self.submit_failure is not None:
            result['SubmitFailure'] = self.submit_failure

        if self.submit_success is not None:
            result['SubmitSuccess'] = self.submit_success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkipFiles') is not None:
            self.skip_files = m.get('SkipFiles')

        if m.get('SubmitFailure') is not None:
            self.submit_failure = m.get('SubmitFailure')

        if m.get('SubmitSuccess') is not None:
            self.submit_success = m.get('SubmitSuccess')

        return self

class DataIngestionNotification(DaraModel):
    def __init__(
        self,
        endpoint: str = None,
        mns: main_models.MNS = None,
        rocket_mq: main_models.RocketMQ = None,
        topic: str = None,
    ):
        # The Simple Message Queue (SMQ) endpoint.
        self.endpoint = endpoint
        # MNS
        self.mns = mns
        # RocketMQ
        self.rocket_mq = rocket_mq
        # The SMQ topic.
        self.topic = topic

    def validate(self):
        if self.mns:
            self.mns.validate()
        if self.rocket_mq:
            self.rocket_mq.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.endpoint is not None:
            result['Endpoint'] = self.endpoint

        if self.mns is not None:
            result['MNS'] = self.mns.to_map()

        if self.rocket_mq is not None:
            result['RocketMQ'] = self.rocket_mq.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Endpoint') is not None:
            self.endpoint = m.get('Endpoint')

        if m.get('MNS') is not None:
            temp_model = main_models.MNS()
            self.mns = temp_model.from_map(m.get('MNS'))

        if m.get('RocketMQ') is not None:
            temp_model = main_models.RocketMQ()
            self.rocket_mq = temp_model.from_map(m.get('RocketMQ'))

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        return self

class DataIngestionActions(DaraModel):
    def __init__(
        self,
        fast_fail_policy: main_models.FastFailPolicy = None,
        name: str = None,
        parameters: List[str] = None,
    ):
        # The on-error policy that is used to quickly troubleshoot an error.
        self.fast_fail_policy = fast_fail_policy
        # The name of the template.
        self.name = name
        # The template parameters.
        self.parameters = parameters

    def validate(self):
        if self.fast_fail_policy:
            self.fast_fail_policy.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.fast_fail_policy is not None:
            result['FastFailPolicy'] = self.fast_fail_policy.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.parameters is not None:
            result['Parameters'] = self.parameters

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FastFailPolicy') is not None:
            temp_model = main_models.FastFailPolicy()
            self.fast_fail_policy = temp_model.from_map(m.get('FastFailPolicy'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Parameters') is not None:
            self.parameters = m.get('Parameters')

        return self


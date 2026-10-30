# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class RunServiceScheduleRequest(DaraModel):
    def __init__(
        self,
        app_id: str = None,
        client_ip: str = None,
        directorys: str = None,
        pod_config_name: str = None,
        pre_locked_timeout: int = None,
        schedule_strategy: str = None,
        service_action: str = None,
        service_commands: str = None,
        uuid: str = None,
    ):
        # The application ID.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The IP address of the client.
        # 
        # This parameter is required.
        self.client_ip = client_ip
        # The list of directories of user data files to be mounted. The directories must be absolute paths, and the \\"/../\\" format is not supported. Example: ["/data/app01", "/data/user"]. Note: The input directory path is relative to the /data directory of the virtual device. The actual path on the virtual device is /data/{input path}.
        self.directorys = directorys
        # Invalid parameter.
        self.pod_config_name = pod_config_name
        # The maximum time to lock an idle device, in seconds. This parameter takes effect only when ServiceAction is set to PreSchedule. Default value: 300.
        self.pre_locked_timeout = pre_locked_timeout
        # The device scheduling policy. The value is a string in JSON format.
        self.schedule_strategy = schedule_strategy
        # The scheduling service operation. Valid values:
        # 
        # Container scenarios:
        # 
        # - Start: Selects and activates a schedulable cloud device and starts the service.
        # - Stop: Stops and releases the cloud device.
        # - Console: Interacts with the device by using commands when the UUID is in the scheduling state.
        # 
        # Bare metal or virtual machine scenarios:
        #   
        # - PreSchedule: Pre-schedules and locks a virtual machine instance.
        # - Confirm: Confirms the scheduling.
        # - Cancel: Cancels the scheduling.
        # - Console: Interacts with the device by using commands when the UUID is in the scheduling state.
        # 
        # This parameter is required.
        self.service_action = service_action
        # The list of container service commands. The value is a string in JSON array format.
        self.service_commands = service_commands
        # The UUID of the device.
        # 
        # This parameter is required.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.app_id is not None:
            result['AppId'] = self.app_id

        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip

        if self.directorys is not None:
            result['Directorys'] = self.directorys

        if self.pod_config_name is not None:
            result['PodConfigName'] = self.pod_config_name

        if self.pre_locked_timeout is not None:
            result['PreLockedTimeout'] = self.pre_locked_timeout

        if self.schedule_strategy is not None:
            result['ScheduleStrategy'] = self.schedule_strategy

        if self.service_action is not None:
            result['ServiceAction'] = self.service_action

        if self.service_commands is not None:
            result['ServiceCommands'] = self.service_commands

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AppId') is not None:
            self.app_id = m.get('AppId')

        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')

        if m.get('Directorys') is not None:
            self.directorys = m.get('Directorys')

        if m.get('PodConfigName') is not None:
            self.pod_config_name = m.get('PodConfigName')

        if m.get('PreLockedTimeout') is not None:
            self.pre_locked_timeout = m.get('PreLockedTimeout')

        if m.get('ScheduleStrategy') is not None:
            self.schedule_strategy = m.get('ScheduleStrategy')

        if m.get('ServiceAction') is not None:
            self.service_action = m.get('ServiceAction')

        if m.get('ServiceCommands') is not None:
            self.service_commands = m.get('ServiceCommands')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self


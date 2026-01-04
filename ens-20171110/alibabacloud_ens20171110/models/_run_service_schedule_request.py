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
        # The ID of the application.
        # 
        # This parameter is required.
        self.app_id = app_id
        # The IP address of the client.
        # 
        # This parameter is required.
        self.client_ip = client_ip
        # The directory to which the data file is mounted. The value must be a full path and cannot be \\"/../\\". Example: ["/data/app01", "/data/user"]. Specify the relative path of the virtual device for this parameter. For example, specify /data for this parameter when the actual path of the virtual device is /data/{input path}.
        self.directorys = directorys
        # The parameter does not take effect.
        self.pod_config_name = pod_config_name
        # The maximum duration for locking an idle device. Unit: seconds. This parameter takes effect only if you set ServiceAction to PreSchedule. Default value: 300.
        self.pre_locked_timeout = pre_locked_timeout
        # The scheduling policy of the device. The value must be a JSON string.
        self.schedule_strategy = schedule_strategy
        # The scheduling operation. The value must be of the enumeration type. Valid values:
        # 
        # Container scenario:
        # 
        # *   Start: selects and activates an idle cloud device.
        # *   Stop: stops and releases the cloud device.
        # *   Console: performs the scheduling operation when the device is in the scheduling state.
        # 
        # Bare metal instance or virtual machine scenario:
        # 
        # *   PreSchedule: locks a virtual machine instance for scheduling.
        # *   Confirm: confirms the scheduling operation.
        # *   Cancel: cancels the scheduling operation.
        # *   Console: performs the scheduling operation when the device is in the scheduling state.
        # 
        # This parameter is required.
        self.service_action = service_action
        # The service commands. The value must be a JSON string.
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


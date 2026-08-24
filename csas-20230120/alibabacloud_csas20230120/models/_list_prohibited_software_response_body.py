# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_csas20230120 import models as main_models
from darabonba.model import DaraModel

class ListProhibitedSoftwareResponseBody(DaraModel):
    def __init__(
        self,
        request_id: str = None,
        software: List[main_models.ListProhibitedSoftwareResponseBodySoftware] = None,
        total_num: int = None,
    ):
        # Id of the request
        self.request_id = request_id
        # The list of prohibited software.
        self.software = software
        # The total number of prohibited software entries.
        self.total_num = total_num

    def validate(self):
        if self.software:
            for v1 in self.software:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.request_id is not None:
            result['RequestId'] = self.request_id

        result['Software'] = []
        if self.software is not None:
            for k1 in self.software:
                result['Software'].append(k1.to_map() if k1 else None)

        if self.total_num is not None:
            result['TotalNum'] = self.total_num

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        self.software = []
        if m.get('Software') is not None:
            for k1 in m.get('Software'):
                temp_model = main_models.ListProhibitedSoftwareResponseBodySoftware()
                self.software.append(temp_model.from_map(k1))

        if m.get('TotalNum') is not None:
            self.total_num = m.get('TotalNum')

        return self

class ListProhibitedSoftwareResponseBodySoftware(DaraModel):
    def __init__(
        self,
        create_time: str = None,
        description: str = None,
        dynamic_policy_ids: List[str] = None,
        is_default: bool = None,
        linux_processes: List[main_models.ListProhibitedSoftwareResponseBodySoftwareLinuxProcesses] = None,
        mac_osprocesses: List[main_models.ListProhibitedSoftwareResponseBodySoftwareMacOSProcesses] = None,
        name: str = None,
        policy_ids: List[str] = None,
        software_id: str = None,
        tag_ids: List[str] = None,
        windows_processes: List[main_models.ListProhibitedSoftwareResponseBodySoftwareWindowsProcesses] = None,
    ):
        # The time when the prohibited software was created, in the yyyy-MM-dd HH:mm:ss format. The time is in the UTC+8 time zone.
        self.create_time = create_time
        # The description of the prohibited software.
        self.description = description
        # The collection of dynamic policy IDs that reference the prohibited software as a disposal action.
        self.dynamic_policy_ids = dynamic_policy_ids
        # Indicates whether the software is a system built-in prohibited software. Valid values:
        # - **true**: A system built-in prohibited software that is shared across all Alibaba Cloud accounts and cannot be modified or deleted.
        # - **false**: Custom prohibited software under the current Alibaba Cloud account.
        self.is_default = is_default
        # The list of process configurations for the Linux operating system.
        self.linux_processes = linux_processes
        # The list of process configurations for the macOS operating system.
        self.mac_osprocesses = mac_osprocesses
        # The name of the prohibited software.
        self.name = name
        # The collection of software prohibition policy IDs that directly reference the prohibited software.
        self.policy_ids = policy_ids
        # The ID of the prohibited software.
        self.software_id = software_id
        # The collection of prohibited software tag IDs associated with the prohibited software.
        self.tag_ids = tag_ids
        # The list of process configurations for the Windows operating system.
        self.windows_processes = windows_processes

    def validate(self):
        if self.linux_processes:
            for v1 in self.linux_processes:
                 if v1:
                    v1.validate()
        if self.mac_osprocesses:
            for v1 in self.mac_osprocesses:
                 if v1:
                    v1.validate()
        if self.windows_processes:
            for v1 in self.windows_processes:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.description is not None:
            result['Description'] = self.description

        if self.dynamic_policy_ids is not None:
            result['DynamicPolicyIds'] = self.dynamic_policy_ids

        if self.is_default is not None:
            result['IsDefault'] = self.is_default

        result['LinuxProcesses'] = []
        if self.linux_processes is not None:
            for k1 in self.linux_processes:
                result['LinuxProcesses'].append(k1.to_map() if k1 else None)

        result['MacOSProcesses'] = []
        if self.mac_osprocesses is not None:
            for k1 in self.mac_osprocesses:
                result['MacOSProcesses'].append(k1.to_map() if k1 else None)

        if self.name is not None:
            result['Name'] = self.name

        if self.policy_ids is not None:
            result['PolicyIds'] = self.policy_ids

        if self.software_id is not None:
            result['SoftwareId'] = self.software_id

        if self.tag_ids is not None:
            result['TagIds'] = self.tag_ids

        result['WindowsProcesses'] = []
        if self.windows_processes is not None:
            for k1 in self.windows_processes:
                result['WindowsProcesses'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('DynamicPolicyIds') is not None:
            self.dynamic_policy_ids = m.get('DynamicPolicyIds')

        if m.get('IsDefault') is not None:
            self.is_default = m.get('IsDefault')

        self.linux_processes = []
        if m.get('LinuxProcesses') is not None:
            for k1 in m.get('LinuxProcesses'):
                temp_model = main_models.ListProhibitedSoftwareResponseBodySoftwareLinuxProcesses()
                self.linux_processes.append(temp_model.from_map(k1))

        self.mac_osprocesses = []
        if m.get('MacOSProcesses') is not None:
            for k1 in m.get('MacOSProcesses'):
                temp_model = main_models.ListProhibitedSoftwareResponseBodySoftwareMacOSProcesses()
                self.mac_osprocesses.append(temp_model.from_map(k1))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('PolicyIds') is not None:
            self.policy_ids = m.get('PolicyIds')

        if m.get('SoftwareId') is not None:
            self.software_id = m.get('SoftwareId')

        if m.get('TagIds') is not None:
            self.tag_ids = m.get('TagIds')

        self.windows_processes = []
        if m.get('WindowsProcesses') is not None:
            for k1 in m.get('WindowsProcesses'):
                temp_model = main_models.ListProhibitedSoftwareResponseBodySoftwareWindowsProcesses()
                self.windows_processes.append(temp_model.from_map(k1))

        return self

class ListProhibitedSoftwareResponseBodySoftwareWindowsProcesses(DaraModel):
    def __init__(
        self,
        bundle_id: str = None,
        cmdline: str = None,
        directory: str = None,
        process: str = None,
    ):
        # The application bundle identifier (Bundle ID). This parameter is required only for macOS processes.
        self.bundle_id = bundle_id
        # The command-line parameters for starting the process.
        self.cmdline = cmdline
        # The directory where the process is located.
        self.directory = directory
        # The process name.
        self.process = process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.process is not None:
            result['Process'] = self.process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        return self

class ListProhibitedSoftwareResponseBodySoftwareMacOSProcesses(DaraModel):
    def __init__(
        self,
        bundle_id: str = None,
        cmdline: str = None,
        directory: str = None,
        process: str = None,
    ):
        # The application bundle identifier (Bundle ID). This parameter is required only for macOS processes.
        self.bundle_id = bundle_id
        # The command-line parameters for starting the process.
        self.cmdline = cmdline
        # The directory where the process is located.
        self.directory = directory
        # The process name.
        self.process = process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.process is not None:
            result['Process'] = self.process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        return self

class ListProhibitedSoftwareResponseBodySoftwareLinuxProcesses(DaraModel):
    def __init__(
        self,
        bundle_id: str = None,
        cmdline: str = None,
        directory: str = None,
        process: str = None,
    ):
        # The application bundle identifier (Bundle ID). This parameter is required only for macOS processes.
        self.bundle_id = bundle_id
        # The command-line parameters for starting the process.
        self.cmdline = cmdline
        # The directory where the process is located.
        self.directory = directory
        # The process name.
        self.process = process

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.bundle_id is not None:
            result['BundleId'] = self.bundle_id

        if self.cmdline is not None:
            result['Cmdline'] = self.cmdline

        if self.directory is not None:
            result['Directory'] = self.directory

        if self.process is not None:
            result['Process'] = self.process

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BundleId') is not None:
            self.bundle_id = m.get('BundleId')

        if m.get('Cmdline') is not None:
            self.cmdline = m.get('Cmdline')

        if m.get('Directory') is not None:
            self.directory = m.get('Directory')

        if m.get('Process') is not None:
            self.process = m.get('Process')

        return self


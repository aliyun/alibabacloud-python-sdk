# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class GetRumExceptionStackRequest(DaraModel):
    def __init__(
        self,
        exception_binary_images: str = None,
        exception_stack: str = None,
        exception_thread_id: str = None,
        extra_info: str = None,
        pid: str = None,
        region_id: str = None,
        service_id: str = None,
        sourcemap_type: str = None,
        workspace: str = None,
    ):
        # The binary images, which represent all executable files loaded into the process address space when a crash occurs.
        self.exception_binary_images = exception_binary_images
        # The exception stack information. Set the value to a JSON string. call_stack.info represents the stack information, call_stack.thread.name represents the thread name, and call_stack.thread.id represents the thread ID. This parameter is exactly the same as the exception.stack parameter in the logstore-rum Logstore of Simple Log Service.
        self.exception_stack = exception_stack
        # The ID of the exception thread.
        self.exception_thread_id = exception_thread_id
        # Extra information about iOS symbol tables. You can leave this parameter empty.
        self.extra_info = extra_info
        # The application ID.
        self.pid = pid
        # The region ID.
        self.region_id = region_id
        self.service_id = service_id
        # The parsing type. Valid values:
        # 
        # *   js: Parses JavaScript errors.
        # *   sym: Parses PC errors.
        # *   har: Parses HarmonyOS errors.
        # *   dSYM: Parses iOS errors.
        # *   so: Parses Android errors.
        self.sourcemap_type = sourcemap_type
        self.workspace = workspace

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.exception_binary_images is not None:
            result['ExceptionBinaryImages'] = self.exception_binary_images

        if self.exception_stack is not None:
            result['ExceptionStack'] = self.exception_stack

        if self.exception_thread_id is not None:
            result['ExceptionThreadId'] = self.exception_thread_id

        if self.extra_info is not None:
            result['ExtraInfo'] = self.extra_info

        if self.pid is not None:
            result['Pid'] = self.pid

        if self.region_id is not None:
            result['RegionId'] = self.region_id

        if self.service_id is not None:
            result['ServiceId'] = self.service_id

        if self.sourcemap_type is not None:
            result['SourcemapType'] = self.sourcemap_type

        if self.workspace is not None:
            result['Workspace'] = self.workspace

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ExceptionBinaryImages') is not None:
            self.exception_binary_images = m.get('ExceptionBinaryImages')

        if m.get('ExceptionStack') is not None:
            self.exception_stack = m.get('ExceptionStack')

        if m.get('ExceptionThreadId') is not None:
            self.exception_thread_id = m.get('ExceptionThreadId')

        if m.get('ExtraInfo') is not None:
            self.extra_info = m.get('ExtraInfo')

        if m.get('Pid') is not None:
            self.pid = m.get('Pid')

        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')

        if m.get('ServiceId') is not None:
            self.service_id = m.get('ServiceId')

        if m.get('SourcemapType') is not None:
            self.sourcemap_type = m.get('SourcemapType')

        if m.get('Workspace') is not None:
            self.workspace = m.get('Workspace')

        return self


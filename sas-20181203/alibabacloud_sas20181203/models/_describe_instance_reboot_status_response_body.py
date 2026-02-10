# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeInstanceRebootStatusResponseBody(DaraModel):
    def __init__(
        self,
        reboot_statuses: List[main_models.DescribeInstanceRebootStatusResponseBodyRebootStatuses] = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # An array that consists of the status information about the servers that you restart.
        self.reboot_statuses = reboot_statuses
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.reboot_statuses:
            for v1 in self.reboot_statuses:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['RebootStatuses'] = []
        if self.reboot_statuses is not None:
            for k1 in self.reboot_statuses:
                result['RebootStatuses'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.reboot_statuses = []
        if m.get('RebootStatuses') is not None:
            for k1 in m.get('RebootStatuses'):
                temp_model = main_models.DescribeInstanceRebootStatusResponseBodyRebootStatuses()
                self.reboot_statuses.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeInstanceRebootStatusResponseBodyRebootStatuses(DaraModel):
    def __init__(
        self,
        code: str = None,
        msg: str = None,
        reboot_status: int = None,
        uuid: str = None,
    ):
        # The error code that is returned when the server failed to be restarted. Valid values:
        # 
        # *   **10001**: The restart command failed to be sent.
        # *   **10002**: The restart operation failed.
        # *   **10003**: A timeout error occurs.
        self.code = code
        # The message that is returned when the server failed to be restarted.
        self.msg = msg
        # The status of the server. Valid values:
        # 
        # *   **0**: The server is being restarted.
        # *   **1**: The server is restarted.
        # *   **2**: The server failed to be restarted.
        self.reboot_status = reboot_status
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.msg is not None:
            result['Msg'] = self.msg

        if self.reboot_status is not None:
            result['RebootStatus'] = self.reboot_status

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Msg') is not None:
            self.msg = m.get('Msg')

        if m.get('RebootStatus') is not None:
            self.reboot_status = m.get('RebootStatus')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self


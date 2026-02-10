# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeAgentInstallStatusResponseBody(DaraModel):
    def __init__(
        self,
        aegis_client_invoke_status_response_list: List[main_models.DescribeAgentInstallStatusResponseBodyAegisClientInvokeStatusResponseList] = None,
        request_id: str = None,
    ):
        # The status of servers.
        self.aegis_client_invoke_status_response_list = aegis_client_invoke_status_response_list
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id

    def validate(self):
        if self.aegis_client_invoke_status_response_list:
            for v1 in self.aegis_client_invoke_status_response_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AegisClientInvokeStatusResponseList'] = []
        if self.aegis_client_invoke_status_response_list is not None:
            for k1 in self.aegis_client_invoke_status_response_list:
                result['AegisClientInvokeStatusResponseList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.aegis_client_invoke_status_response_list = []
        if m.get('AegisClientInvokeStatusResponseList') is not None:
            for k1 in m.get('AegisClientInvokeStatusResponseList'):
                temp_model = main_models.DescribeAgentInstallStatusResponseBodyAegisClientInvokeStatusResponseList()
                self.aegis_client_invoke_status_response_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeAgentInstallStatusResponseBodyAegisClientInvokeStatusResponseList(DaraModel):
    def __init__(
        self,
        message: str = None,
        resule_code: str = None,
        result: int = None,
        uuid: str = None,
    ):
        # The returned message.
        self.message = message
        # The installation status. Valid value:
        # 
        # *   **-1**: The agent is not installed.
        # *   **0**: The agent is installed.
        # *   **1**: Failed to create a directory in the client.
        # *   **2**: Failed to download the installation package.
        # *   **3**: The installation file does not exist.
        # *   **4**: The verification information of the installation file does not exist.
        # *   **5**: Failed to verify the installation file.
        # *   **6**: Failed to execute the installation file.
        # *   **7**: You do not have the required permissions. The installation failed.
        # *   **8**: No client process is detected.
        # *   **100**: The installation failed due to an unknown error.
        # *   **1001**: The installation failed. One-click installation is not supported in this region.
        # *   **1002**: The installation failed. Servers that are not provided by Alibaba Cloud are not supported. Install the agent by executing a script on the server.
        # *   **1003**: The installation failed. The operating system is not supported.
        # *   **1004**: An internal error occurred. Try again later.
        # *   **1005**: The Elastic Compute Service (ECS) instance is not started. Start the ECS instance and try again.
        # *   **1006**: One-click installation is not supported for ECS instances of the classic network type.
        # *   **1007**: The running command is manually stopped.
        # *   **1008**: Cloud Assistant is not installed. You cannot install the client.
        # *   **1009**: The command execution timed out. Try again later.
        # *   **1010**: The machine is already online. You do not need to install a client.
        self.resule_code = resule_code
        # The installation result. Valid value:
        # 
        # *   **-1**: The agent is not installed.
        # *   **0**: The agent is being installed.
        # *   **1**: The agent is installed.
        # *   **2**: The installation failed.
        self.result = result
        # The UUID of the server.
        self.uuid = uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        if self.resule_code is not None:
            result['ResuleCode'] = self.resule_code

        if self.result is not None:
            result['Result'] = self.result

        if self.uuid is not None:
            result['Uuid'] = self.uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('ResuleCode') is not None:
            self.resule_code = m.get('ResuleCode')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('Uuid') is not None:
            self.uuid = m.get('Uuid')

        return self


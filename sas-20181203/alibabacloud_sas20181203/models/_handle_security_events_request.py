# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HandleSecurityEventsRequest(DaraModel):
    def __init__(
        self,
        mark_batch: str = None,
        mark_miss_param: str = None,
        operation_code: str = None,
        operation_params: str = None,
        remark: str = None,
        resource_directory_account_id: int = None,
        security_event_ids: List[str] = None,
        source_ip: str = None,
    ):
        # Specifies whether to add multiple alert events to the whitelist at a time. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.mark_batch = mark_batch
        # The whitelist rule. The value of this parameter is in the JSON format and contains the following fields:
        # 
        # *   **field**: The field based on which alert events are added to the whitelist.
        # 
        # *   **operate**: The method that is used to added alert events to the whitelist. Valid values:
        # 
        #     *   **notContains**: does not contain
        #     *   **contains**: contains
        #     *   **regex**: matches by regular expression
        #     *   **strEqual**: equals
        #     *   **strNotEqual**: does not equal
        # 
        # *   **fieldValue**: The value of the field based on which alert events are added to the whitelist.
        # 
        # *   **uuid**: The application scope of the whitelist rule. Valid values:
        # 
        #     *   **part**: the current asset
        #     *   **ALL**: all assets
        # 
        # >  You can call the [DescribeSecurityEventOperations](~~DescribeSecurityEventOperations~~) operation to obtain the fields that you can specify for **field**.
        self.mark_miss_param = mark_miss_param
        # The operation that you want to perform to handle the alert events. Valid values:
        # 
        # *   **block_ip**: blocks the source IP address.
        # *   **advance_mark_mis_info**: adds the alert events to the whitelist.
        # *   **ignore**: ignores the alert events.
        # *   **manual_handled**: marks the alert events as manually handled.
        # *   **kill_process**: terminates the malicious process.
        # *   **cleanup**: performs in-depth virus detection and removal.
        # *   **kill_and_quara**: kills the malicious processes and quarantines the source file.
        # *   **disable_malicious_defense**: stops the container on which the alerting files or processes exist.
        # *   **client_problem_check**: performs troubleshooting.
        # *   **quara**: quarantines the source file of the malicious process.
        # 
        # This parameter is required.
        self.operation_code = operation_code
        # The configuration of the operation that you want to perform to handle the alert events.
        # 
        # >  If you set OperationCode to `kill_and_quara` or `block_ip`, you must specify OperationParams. If you set OperationCode to other values, you can leave OperationParams empty.
        self.operation_params = operation_params
        # The remarks of the handling operation.
        self.remark = remark
        # The Alibaba Cloud account ID of the member in the resource directory.
        # 
        # >  You can call the [DescribeMonitorAccounts](~~DescribeMonitorAccounts~~) operation to obtain the IDs.
        self.resource_directory_account_id = resource_directory_account_id
        # The IDs of the alert events.
        # 
        # This parameter is required.
        self.security_event_ids = security_event_ids
        # The source IP address of the request.
        self.source_ip = source_ip

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mark_batch is not None:
            result['MarkBatch'] = self.mark_batch

        if self.mark_miss_param is not None:
            result['MarkMissParam'] = self.mark_miss_param

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_directory_account_id is not None:
            result['ResourceDirectoryAccountId'] = self.resource_directory_account_id

        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarkBatch') is not None:
            self.mark_batch = m.get('MarkBatch')

        if m.get('MarkMissParam') is not None:
            self.mark_miss_param = m.get('MarkMissParam')

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceDirectoryAccountId') is not None:
            self.resource_directory_account_id = m.get('ResourceDirectoryAccountId')

        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        return self


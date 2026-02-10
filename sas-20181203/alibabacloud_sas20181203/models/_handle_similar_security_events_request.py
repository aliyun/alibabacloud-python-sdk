# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from darabonba.model import DaraModel

class HandleSimilarSecurityEventsRequest(DaraModel):
    def __init__(
        self,
        mark_miss_param: str = None,
        operation_code: str = None,
        operation_params: str = None,
        remark: str = None,
        resource_owner_id: int = None,
        source_ip: str = None,
        task_id: int = None,
    ):
        # The whitelist rule. For example, if you want to add a file that contains the string a to the whitelist based on the MD5 hash value, set this parameter to {"field":"md5","operate":"contains","fieldValue":"aa"}.
        self.mark_miss_param = mark_miss_param
        # The operation that you want to perform to handle the alert events.
        # 
        # >  You can call the [DescribeSecurityEventOperations](~~DescribeSecurityEventOperations~~) operation to query the operations.
        # 
        # This parameter is required.
        self.operation_code = operation_code
        # The configuration of the operation that you want to perform to handle the alert events. The value of this parameter is in the JSON format.
        # 
        # >  If you set **OperationCode** to **kill_and_quara**, **block_ip**, or **virus_quara**, you must specify OperationParams. If you set **OperationCode** to other values, you can leave OperationParams empty. If you set **OperationCode** to **block_ip**, the value of OperationParams must consist of the following fields:
        # 
        # > *   **expireTime**: the end time of locking. Unit: milliseconds.
        # 
        # >  If you set **OperationCode** to **kill_and_quara**, the value of OperationParams must consist of the following fields:
        # 
        # > *   **subOperation**: the method of detection and removal. Valid values:
        # 
        # >     *   **killAndQuaraFileByMd5andPath**: terminates the process and quarantines the source file of the process.
        # >     *   **killByMd5andPath**: terminates the running process.
        # 
        # >  If you set **OperationCode** to **virus_quara**, the value of OperationParams consists of the following fields:
        # 
        # > *   **subOperation**: the method of detection and removal. Valid values:
        # 
        # >     *   **quaraFileByMd5andPath**: quarantines the source file of the process.
        self.operation_params = operation_params
        # The remark of the operation.
        self.remark = remark
        self.resource_owner_id = resource_owner_id
        # The source IP address of the request.
        self.source_ip = source_ip
        # The ID of the task that handles the alert events at a time.
        # 
        # >  You can call the [CreateSimilarSecurityEventsQueryTask](~~CreateSimilarSecurityEventsQueryTask~~) operation to query the IDs of tasks.
        # 
        # This parameter is required.
        self.task_id = task_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.mark_miss_param is not None:
            result['MarkMissParam'] = self.mark_miss_param

        if self.operation_code is not None:
            result['OperationCode'] = self.operation_code

        if self.operation_params is not None:
            result['OperationParams'] = self.operation_params

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.resource_owner_id is not None:
            result['ResourceOwnerId'] = self.resource_owner_id

        if self.source_ip is not None:
            result['SourceIp'] = self.source_ip

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MarkMissParam') is not None:
            self.mark_miss_param = m.get('MarkMissParam')

        if m.get('OperationCode') is not None:
            self.operation_code = m.get('OperationCode')

        if m.get('OperationParams') is not None:
            self.operation_params = m.get('OperationParams')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('ResourceOwnerId') is not None:
            self.resource_owner_id = m.get('ResourceOwnerId')

        if m.get('SourceIp') is not None:
            self.source_ip = m.get('SourceIp')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self


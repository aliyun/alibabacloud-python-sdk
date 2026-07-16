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
        # The rule for adding items to the whitelist. For example, to add a whitelist rule based on file MD5 where the file contains the string "a", set this parameter to {"field":"md5","operate":"contains","fieldValue":"aa"}.
        self.mark_miss_param = mark_miss_param
        # The type of operation for batch processing alert events of the same type.
        # >Call the [DescribeSecurityEventOperations](~~DescribeSecurityEventOperations~~) operation to obtain this parameter.
        # 
        # This parameter is required.
        self.operation_code = operation_code
        # The configuration of the sub-operation for handling alerting events. The value is in JSON format.
        # 
        # > This parameter is required when **OperationCode** is set to **kill_and_quara**, **block_ip**, or **virus_quara**. For other values of **OperationCode**, this parameter can be left empty.
        # 
        # > When **OperationCode** is set to **block_ip**, the following field is included:
        # > - **expireTime**: the lock expiration time. Unit: milliseconds.
        # >
        # > When **OperationCode** is set to **kill_and_quara**, the following field is included:
        # > - **subOperation**: the method used to scan and remove threats. Valid values:
        # >     - **killAndQuaraFileByMd5andPath**: terminates the process and moves the file to the quarantined file.
        # >     - **killByMd5andPath**: terminates the running process.
        # >
        # > When **OperationCode** is set to **virus_quara**, the following field is included:
        # > - **subOperation**: the method used to scan and remove threats. Valid values:
        # >    - **quaraFileByMd5andPath**: moves the source file of the process to the quarantined file.
        self.operation_params = operation_params
        # The remarks for the operation.
        self.remark = remark
        self.resource_owner_id = resource_owner_id
        # The IP address of the access source.
        self.source_ip = source_ip
        # The ID of the task that batch processes all alert events of the same type.
        # >Call the [CreateSimilarSecurityEventsQueryTask](~~CreateSimilarSecurityEventsQueryTask~~) operation to obtain this parameter.
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


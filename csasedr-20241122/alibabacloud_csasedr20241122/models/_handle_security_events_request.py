# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from darabonba.model import DaraModel

class HandleSecurityEventsRequest(DaraModel):
    def __init__(
        self,
        mark_batch: bool = None,
        mark_miss_param: str = None,
        operation_code: str = None,
        operation_params: str = None,
        remark: str = None,
        security_event_ids: List[int] = None,
    ):
        # Specifies whether to add to the whitelist in batches. Valid values:
        # - true: Yes.
        # - false: No.
        self.mark_batch = mark_batch
        # The JSON array string used when adding an advanced whitelist or precise defense whitelist rule. This parameter applies only when OperationCode is set to `advance_mark_mis_info` or `defense_mark_mis_info`. Do not pass this parameter for other operations.
        # 
        # Each rule contains the following fields:
        # - `field`: The matching field, which is obtained from the FiledName in MarkFieldsSource returned by DescribeSecurityEventOperations.
        # - `fieldValue`: The user-defined matching value, which does not need to be equal to the original field value of the current alert.
        # - `operate`: The matching operator, which must belong to the SupportedMisType list returned for the field. Do not use a general fixed enumeration instead of the supported range for the current field.
        # - `assetScope`: The effective scope object of the whitelist rule, which includes matchMode (scope mode) and the corresponding matchTargetIds (scope target list).
        # 
        # The assetScope parameter specifies the effective scope of the rule. If you only handle the alert and do not add a whitelist rule, you can omit this parameter or pass an empty array string `[]`.
        self.mark_miss_param = mark_miss_param
        # The operation code for handling the endpoint alert. Valid values:
        # - advance_mark_mis_info: Adds to the advanced whitelist.
        # - defense_mark_mis_info: Adds to the precise defense whitelist.
        # - mark_mis_info: Marks as a false positive (standard whitelisting).
        # - rm_mark_mis_info: Removes from the standard or advanced whitelist.
        # - rm_defense_mark_mis_info: Removes from the precise defense whitelist.
        # - ignore: Ignores the alert.
        # - manual_handled: Marks as manually handled.
        # - cancle_manual: Cancels the manually handled status.
        # The preceding list is not a fixed set of operations that can be performed on every alert. The actual available operations are also restricted by feature switches, dynamic whitelists, alert operation configurations, and the current status. Before you call this operation, call DescribeSecurityEventOperations to query the currently available operations for the alert and check UserCanOperate. Use only the OperationCode values that are allowed in the query result.
        # 
        # This parameter is required.
        self.operation_code = operation_code
        # The operation parameters, represented as a JSON object string. If this parameter is not passed or an empty string is passed, the backend processes it as `{}`. The specific parameters must correspond to the OperationCode and are subject to the OperationParams returned by DescribeSecurityEventOperations.
        self.operation_params = operation_params
        # The remark for the handling operation.
        self.remark = remark
        # The IDs of the security alert events to handle.
        # 
        # This parameter is required.
        self.security_event_ids = security_event_ids

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

        if self.security_event_ids is not None:
            result['SecurityEventIds'] = self.security_event_ids

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

        if m.get('SecurityEventIds') is not None:
            self.security_event_ids = m.get('SecurityEventIds')

        return self


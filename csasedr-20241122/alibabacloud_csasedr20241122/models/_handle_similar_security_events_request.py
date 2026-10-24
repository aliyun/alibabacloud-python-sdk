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
        task_id: int = None,
    ):
        # The JSON array string used to add advanced whitelist or precise defense whitelist rules. This parameter applies only to scenarios where the OperationCode is `advance_mark_mis_info` or `defense_mark_mis_info`. Do not pass this parameter for other operations.
        # 
        # Each rule includes the following fields:
        # 
        # - `field`: The matching field, which is obtained from the FiledName field in the MarkFieldsSource returned by the DescribeSecurityEventOperations operation.
        # - `fieldValue`: The user-defined matching value, which does not need to equal the original field value of the current alert.
        # - `operate`: The matching operator, which must be included in the list returned by the SupportedMisType corresponding to the field. Do not use a common fixed enumeration to replace the supported scope of the current field.
        # - `assetScope`: The effective scope object of the whitelist rule, which includes matchMode (the scope mode) and the corresponding matchTargetIds (the list of scope targets).
        # 
        # The assetScope field specifies the effective scope of the rule. If you only process alerts and do not add whitelist rules, you can leave this parameter empty or pass an empty array string `[]`.
        self.mark_miss_param = mark_miss_param
        # The operation code for processing endpoint alerts. The allowed operations for the code are as follows:
        # 
        # - `advance_mark_mis_info`: Adds the alert to the advanced whitelist.
        # - `defense_mark_mis_info`: Adds the alert to the precise defense whitelist.
        # - `mark_mis_info`: Marks the alert as a false positive and adds it to the common whitelist.
        # - `rm_mark_mis_info`: Removes the alert from the common or advanced whitelist.
        # - `rm_defense_mark_mis_info`: Removes the alert from the precise defense whitelist.
        # - `ignore`: Ignores the alert.
        # - `manual_handled`: Marks the alert as manually handled.
        # - `cancle_manual`: Cancels the manually handled status of the alert.
        # 
        # The preceding set is not a fixed list of operations that can be performed on every alert. The actual available operations are also restricted by conditions such as feature switches, dynamic whitelists, alert operation configurations, and the current status. Before calling this operation, call the DescribeSecurityEventOperations operation to query the currently available operations for the alert and check UserCanOperate. Use only the OperationCode values that are allowed in the query results.
        # 
        # This parameter is required.
        self.operation_code = operation_code
        # The operation parameters, represented as a JSON object string. If this parameter is not passed or an empty string is passed, the backend processes it as `{}`. The specific parameters must correspond to the OperationCode and are subject to the OperationParams returned by the DescribeSecurityEventOperations operation.
        self.operation_params = operation_params
        # The remark for the operation.
        self.remark = remark
        # The ID of the similar alert query task. You can obtain the ID by calling the CreateSimilarSecurityEventsQueryTask operation. The task must belong to the current calling account and must be a similar alert query task. Before calling this operation, call the DescribeSecurityEventOperationStatus operation to query the TaskStatus. Wait until the status reaches DataRetrieved before initiating the processing. The New or RetrievingData status indicates that data extraction is not complete.
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

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_notifications20241225 import models as main_models
from darabonba.model import DaraModel

class ReadRevisionHistoryListResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.ReadRevisionHistoryListResponseBodyData = None,
        http_code: int = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The error code returned by the system. For more information, see error codes.
        self.code = code
        # The execution result.
        self.data = data
        # The description.
        self.http_code = http_code
        # The message returned when the call failed.
        self.message = message
        # The request ID.
        self.request_id = request_id
        # Indicates whether the call was successful. Valid values:
        # - true: The call was successful.
        # - false: The call failed.
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_code is not None:
            result['HttpCode'] = self.http_code

        if self.message is not None:
            result['Message'] = self.message

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Data') is not None:
            temp_model = main_models.ReadRevisionHistoryListResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpCode') is not None:
            self.http_code = m.get('HttpCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ReadRevisionHistoryListResponseBodyData(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
        rows: List[main_models.ReadRevisionHistoryListResponseBodyDataRows] = None,
        total_count: int = None,
    ):
        # The maximum number of entries.
        self.max_results = max_results
        # The token for the next page of data.
        self.next_token = next_token
        # A single row of returned data.
        self.rows = rows
        # The total number of messages in the category.
        self.total_count = total_count

    def validate(self):
        if self.rows:
            for v1 in self.rows:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        result['Rows'] = []
        if self.rows is not None:
            for k1 in self.rows:
                result['Rows'].append(k1.to_map() if k1 else None)

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        self.rows = []
        if m.get('Rows') is not None:
            for k1 in m.get('Rows'):
                temp_model = main_models.ReadRevisionHistoryListResponseBodyDataRows()
                self.rows.append(temp_model.from_map(k1))

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ReadRevisionHistoryListResponseBodyDataRows(DaraModel):
    def __init__(
        self,
        ali_uid: int = None,
        category_code: str = None,
        channel_group_code: str = None,
        new_value: str = None,
        operation_item_code: str = None,
        operation_item_name: str = None,
        operation_timestamp: int = None,
        operator_ip: str = None,
        operator_name: str = None,
        operator_uid: int = None,
        original_value: str = None,
        page_spec: main_models.ReadRevisionHistoryListResponseBodyDataRowsPageSpec = None,
        remarks: str = None,
    ):
        # The Alibaba Cloud account ID.
        self.ali_uid = ali_uid
        # The event type code.
        self.category_code = category_code
        # The channel group.
        self.channel_group_code = channel_group_code
        # The modified value.
        self.new_value = new_value
        # The revision item code. Valid values:
        self.operation_item_code = operation_item_code
        # The revision item name.
        self.operation_item_name = operation_item_name
        # The timestamp.
        self.operation_timestamp = operation_timestamp
        # The IP address of the operator.
        self.operator_ip = operator_ip
        # The name of the operator.
        self.operator_name = operator_name
        # The UID of the operator.
        self.operator_uid = operator_uid
        # The original value.
        self.original_value = original_value
        # The pagination information.
        self.page_spec = page_spec
        # The remarks.
        self.remarks = remarks

    def validate(self):
        if self.page_spec:
            self.page_spec.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid

        if self.category_code is not None:
            result['CategoryCode'] = self.category_code

        if self.channel_group_code is not None:
            result['ChannelGroupCode'] = self.channel_group_code

        if self.new_value is not None:
            result['NewValue'] = self.new_value

        if self.operation_item_code is not None:
            result['OperationItemCode'] = self.operation_item_code

        if self.operation_item_name is not None:
            result['OperationItemName'] = self.operation_item_name

        if self.operation_timestamp is not None:
            result['OperationTimestamp'] = self.operation_timestamp

        if self.operator_ip is not None:
            result['OperatorIp'] = self.operator_ip

        if self.operator_name is not None:
            result['OperatorName'] = self.operator_name

        if self.operator_uid is not None:
            result['OperatorUid'] = self.operator_uid

        if self.original_value is not None:
            result['OriginalValue'] = self.original_value

        if self.page_spec is not None:
            result['PageSpec'] = self.page_spec.to_map()

        if self.remarks is not None:
            result['Remarks'] = self.remarks

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')

        if m.get('CategoryCode') is not None:
            self.category_code = m.get('CategoryCode')

        if m.get('ChannelGroupCode') is not None:
            self.channel_group_code = m.get('ChannelGroupCode')

        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')

        if m.get('OperationItemCode') is not None:
            self.operation_item_code = m.get('OperationItemCode')

        if m.get('OperationItemName') is not None:
            self.operation_item_name = m.get('OperationItemName')

        if m.get('OperationTimestamp') is not None:
            self.operation_timestamp = m.get('OperationTimestamp')

        if m.get('OperatorIp') is not None:
            self.operator_ip = m.get('OperatorIp')

        if m.get('OperatorName') is not None:
            self.operator_name = m.get('OperatorName')

        if m.get('OperatorUid') is not None:
            self.operator_uid = m.get('OperatorUid')

        if m.get('OriginalValue') is not None:
            self.original_value = m.get('OriginalValue')

        if m.get('PageSpec') is not None:
            temp_model = main_models.ReadRevisionHistoryListResponseBodyDataRowsPageSpec()
            self.page_spec = temp_model.from_map(m.get('PageSpec'))

        if m.get('Remarks') is not None:
            self.remarks = m.get('Remarks')

        return self

class ReadRevisionHistoryListResponseBodyDataRowsPageSpec(DaraModel):
    def __init__(
        self,
        max_results: int = None,
        next_token: str = None,
    ):
        # The maximum number of entries.
        self.max_results = max_results
        # The token for the next page of data.
        self.next_token = next_token

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.max_results is not None:
            result['MaxResults'] = self.max_results

        if self.next_token is not None:
            result['NextToken'] = self.next_token

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')

        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')

        return self


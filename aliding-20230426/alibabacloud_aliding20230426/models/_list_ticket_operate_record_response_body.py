# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aliding20230426 import models as main_models
from darabonba.model import DaraModel

class ListTicketOperateRecordResponseBody(DaraModel):
    def __init__(
        self,
        records: List[main_models.ListTicketOperateRecordResponseBodyRecords] = None,
        request_id: str = None,
        vendor_request_id: str = None,
        vendor_type: str = None,
    ):
        self.records = records
        self.request_id = request_id
        self.vendor_request_id = vendor_request_id
        self.vendor_type = vendor_type

    def validate(self):
        if self.records:
            for v1 in self.records:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['records'] = []
        if self.records is not None:
            for k1 in self.records:
                result['records'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.vendor_request_id is not None:
            result['vendorRequestId'] = self.vendor_request_id

        if self.vendor_type is not None:
            result['vendorType'] = self.vendor_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.records = []
        if m.get('records') is not None:
            for k1 in m.get('records'):
                temp_model = main_models.ListTicketOperateRecordResponseBodyRecords()
                self.records.append(temp_model.from_map(k1))

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('vendorRequestId') is not None:
            self.vendor_request_id = m.get('vendorRequestId')

        if m.get('vendorType') is not None:
            self.vendor_type = m.get('vendorType')

        return self

class ListTicketOperateRecordResponseBodyRecords(DaraModel):
    def __init__(
        self,
        open_ticket_id: str = None,
        operate_data: str = None,
        operate_time: str = None,
        operation: str = None,
        operation_display_name: str = None,
        operator: main_models.ListTicketOperateRecordResponseBodyRecordsOperator = None,
        ticket_memo: main_models.ListTicketOperateRecordResponseBodyRecordsTicketMemo = None,
    ):
        self.open_ticket_id = open_ticket_id
        self.operate_data = operate_data
        self.operate_time = operate_time
        self.operation = operation
        self.operation_display_name = operation_display_name
        self.operator = operator
        self.ticket_memo = ticket_memo

    def validate(self):
        if self.operator:
            self.operator.validate()
        if self.ticket_memo:
            self.ticket_memo.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.open_ticket_id is not None:
            result['OpenTicketId'] = self.open_ticket_id

        if self.operate_data is not None:
            result['OperateData'] = self.operate_data

        if self.operate_time is not None:
            result['OperateTime'] = self.operate_time

        if self.operation is not None:
            result['Operation'] = self.operation

        if self.operation_display_name is not None:
            result['OperationDisplayName'] = self.operation_display_name

        if self.operator is not None:
            result['Operator'] = self.operator.to_map()

        if self.ticket_memo is not None:
            result['TicketMemo'] = self.ticket_memo.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OpenTicketId') is not None:
            self.open_ticket_id = m.get('OpenTicketId')

        if m.get('OperateData') is not None:
            self.operate_data = m.get('OperateData')

        if m.get('OperateTime') is not None:
            self.operate_time = m.get('OperateTime')

        if m.get('Operation') is not None:
            self.operation = m.get('Operation')

        if m.get('OperationDisplayName') is not None:
            self.operation_display_name = m.get('OperationDisplayName')

        if m.get('Operator') is not None:
            temp_model = main_models.ListTicketOperateRecordResponseBodyRecordsOperator()
            self.operator = temp_model.from_map(m.get('Operator'))

        if m.get('TicketMemo') is not None:
            temp_model = main_models.ListTicketOperateRecordResponseBodyRecordsTicketMemo()
            self.ticket_memo = temp_model.from_map(m.get('TicketMemo'))

        return self

class ListTicketOperateRecordResponseBodyRecordsTicketMemo(DaraModel):
    def __init__(
        self,
        attachments: List[main_models.ListTicketOperateRecordResponseBodyRecordsTicketMemoAttachments] = None,
        memo: str = None,
    ):
        self.attachments = attachments
        self.memo = memo

    def validate(self):
        if self.attachments:
            for v1 in self.attachments:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Attachments'] = []
        if self.attachments is not None:
            for k1 in self.attachments:
                result['Attachments'].append(k1.to_map() if k1 else None)

        if self.memo is not None:
            result['Memo'] = self.memo

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.attachments = []
        if m.get('Attachments') is not None:
            for k1 in m.get('Attachments'):
                temp_model = main_models.ListTicketOperateRecordResponseBodyRecordsTicketMemoAttachments()
                self.attachments.append(temp_model.from_map(k1))

        if m.get('Memo') is not None:
            self.memo = m.get('Memo')

        return self

class ListTicketOperateRecordResponseBodyRecordsTicketMemoAttachments(DaraModel):
    def __init__(
        self,
        file_name: str = None,
        key: str = None,
    ):
        self.file_name = file_name
        self.key = key

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_name is not None:
            result['FileName'] = self.file_name

        if self.key is not None:
            result['Key'] = self.key

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileName') is not None:
            self.file_name = m.get('FileName')

        if m.get('Key') is not None:
            self.key = m.get('Key')

        return self

class ListTicketOperateRecordResponseBodyRecordsOperator(DaraModel):
    def __init__(
        self,
        nick_name: str = None,
        union_id: str = None,
    ):
        self.nick_name = nick_name
        self.union_id = union_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.nick_name is not None:
            result['NickName'] = self.nick_name

        if self.union_id is not None:
            result['UnionId'] = self.union_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NickName') is not None:
            self.nick_name = m.get('NickName')

        if m.get('UnionId') is not None:
            self.union_id = m.get('UnionId')

        return self


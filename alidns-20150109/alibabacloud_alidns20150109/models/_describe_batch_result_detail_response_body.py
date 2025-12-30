# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_alidns20150109 import models as main_models
from darabonba.model import DaraModel

class DescribeBatchResultDetailResponseBody(DaraModel):
    def __init__(
        self,
        batch_result_details: main_models.DescribeBatchResultDetailResponseBodyBatchResultDetails = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        total_count: int = None,
    ):
        # The detailed results of the batch operation.
        self.batch_result_details = batch_result_details
        # The page number.
        self.page_number = page_number
        # The number of entries per page.
        self.page_size = page_size
        # The request ID.
        self.request_id = request_id
        # The total number of entries returned.
        self.total_count = total_count

    def validate(self):
        if self.batch_result_details:
            self.batch_result_details.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_result_details is not None:
            result['BatchResultDetails'] = self.batch_result_details.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchResultDetails') is not None:
            temp_model = main_models.DescribeBatchResultDetailResponseBodyBatchResultDetails()
            self.batch_result_details = temp_model.from_map(m.get('BatchResultDetails'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class DescribeBatchResultDetailResponseBodyBatchResultDetails(DaraModel):
    def __init__(
        self,
        batch_result_detail: List[main_models.DescribeBatchResultDetailResponseBodyBatchResultDetailsBatchResultDetail] = None,
    ):
        self.batch_result_detail = batch_result_detail

    def validate(self):
        if self.batch_result_detail:
            for v1 in self.batch_result_detail:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['BatchResultDetail'] = []
        if self.batch_result_detail is not None:
            for k1 in self.batch_result_detail:
                result['BatchResultDetail'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.batch_result_detail = []
        if m.get('BatchResultDetail') is not None:
            for k1 in m.get('BatchResultDetail'):
                temp_model = main_models.DescribeBatchResultDetailResponseBodyBatchResultDetailsBatchResultDetail()
                self.batch_result_detail.append(temp_model.from_map(k1))

        return self

class DescribeBatchResultDetailResponseBodyBatchResultDetailsBatchResultDetail(DaraModel):
    def __init__(
        self,
        batch_type: str = None,
        domain: str = None,
        line: str = None,
        new_rr: str = None,
        new_value: str = None,
        operate_date_str: str = None,
        priority: str = None,
        reason: str = None,
        record_id: str = None,
        remark: str = None,
        rr: str = None,
        rr_status: str = None,
        status: bool = None,
        ttl: str = None,
        type: str = None,
        value: str = None,
    ):
        # The type of the batch operation.
        self.batch_type = batch_type
        # The domain name.
        self.domain = domain
        # The line code.
        self.line = line
        # The new hostname.
        self.new_rr = new_rr
        # The new record value.
        self.new_value = new_value
        # The time when the operation was performed. The time follows the ISO 8601 standard in the YYYY-MM-DDThh:mm:ss format. The time is displayed in UTC.
        self.operate_date_str = operate_date_str
        # The priority of the mail exchanger (MX) record.
        self.priority = priority
        # The cause of the execution failure.
        self.reason = reason
        # The ID of the DNS record.
        self.record_id = record_id
        # The description of the DNS record.
        self.remark = remark
        # The hostname.
        self.rr = rr
        # The status of the DNS record.
        self.rr_status = rr_status
        # The execution result of the batch operation. Valid values: **true**: The operation succeeded. **false**: The operation failed.
        self.status = status
        # The time-to-live (TTL) of the DNS record.
        self.ttl = ttl
        # The type of the DNS record.
        self.type = type
        # The value of the DNS record.
        self.value = value

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.batch_type is not None:
            result['BatchType'] = self.batch_type

        if self.domain is not None:
            result['Domain'] = self.domain

        if self.line is not None:
            result['Line'] = self.line

        if self.new_rr is not None:
            result['NewRr'] = self.new_rr

        if self.new_value is not None:
            result['NewValue'] = self.new_value

        if self.operate_date_str is not None:
            result['OperateDateStr'] = self.operate_date_str

        if self.priority is not None:
            result['Priority'] = self.priority

        if self.reason is not None:
            result['Reason'] = self.reason

        if self.record_id is not None:
            result['RecordId'] = self.record_id

        if self.remark is not None:
            result['Remark'] = self.remark

        if self.rr is not None:
            result['Rr'] = self.rr

        if self.rr_status is not None:
            result['RrStatus'] = self.rr_status

        if self.status is not None:
            result['Status'] = self.status

        if self.ttl is not None:
            result['Ttl'] = self.ttl

        if self.type is not None:
            result['Type'] = self.type

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BatchType') is not None:
            self.batch_type = m.get('BatchType')

        if m.get('Domain') is not None:
            self.domain = m.get('Domain')

        if m.get('Line') is not None:
            self.line = m.get('Line')

        if m.get('NewRr') is not None:
            self.new_rr = m.get('NewRr')

        if m.get('NewValue') is not None:
            self.new_value = m.get('NewValue')

        if m.get('OperateDateStr') is not None:
            self.operate_date_str = m.get('OperateDateStr')

        if m.get('Priority') is not None:
            self.priority = m.get('Priority')

        if m.get('Reason') is not None:
            self.reason = m.get('Reason')

        if m.get('RecordId') is not None:
            self.record_id = m.get('RecordId')

        if m.get('Remark') is not None:
            self.remark = m.get('Remark')

        if m.get('Rr') is not None:
            self.rr = m.get('Rr')

        if m.get('RrStatus') is not None:
            self.rr_status = m.get('RrStatus')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Ttl') is not None:
            self.ttl = m.get('Ttl')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_sas20181203 import models as main_models
from darabonba.model import DaraModel

class DescribeReportRecipientStatusResponseBody(DaraModel):
    def __init__(
        self,
        report_recipient_list: List[main_models.DescribeReportRecipientStatusResponseBodyReportRecipientList] = None,
        request_id: str = None,
    ):
        # The report recipients.
        self.report_recipient_list = report_recipient_list
        # The request ID.
        self.request_id = request_id

    def validate(self):
        if self.report_recipient_list:
            for v1 in self.report_recipient_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ReportRecipientList'] = []
        if self.report_recipient_list is not None:
            for k1 in self.report_recipient_list:
                result['ReportRecipientList'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.report_recipient_list = []
        if m.get('ReportRecipientList') is not None:
            for k1 in m.get('ReportRecipientList'):
                temp_model = main_models.DescribeReportRecipientStatusResponseBodyReportRecipientList()
                self.report_recipient_list.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class DescribeReportRecipientStatusResponseBodyReportRecipientList(DaraModel):
    def __init__(
        self,
        is_verify: int = None,
        recipient: str = None,
    ):
        # Indicates whether the email address is verified. Valid values:
        # 
        # *   0: no
        # *   1: yes
        # 
        # >  If no email is specified when you create a report, the value of this parameter is empty.
        self.is_verify = is_verify
        # The email address of the report recipient.
        # 
        # >  If no email is specified when you create a report, the value of this parameter is empty.
        self.recipient = recipient

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.is_verify is not None:
            result['IsVerify'] = self.is_verify

        if self.recipient is not None:
            result['Recipient'] = self.recipient

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('IsVerify') is not None:
            self.is_verify = m.get('IsVerify')

        if m.get('Recipient') is not None:
            self.recipient = m.get('Recipient')

        return self


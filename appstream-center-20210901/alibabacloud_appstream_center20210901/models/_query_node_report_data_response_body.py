# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_appstream_center20210901 import models as main_models
from darabonba.model import DaraModel

class QueryNodeReportDataResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        report_data_model: List[main_models.QueryNodeReportDataResponseBodyReportDataModel] = None,
        request_id: str = None,
    ):
        # The business status code. A value of 200 indicates that the request is successful. Other values indicate that the request failed.
        self.code = code
        # The total number of records that meet the query conditions.
        self.count = count
        # The description of the request processing result. If the request is successful, success is usually returned.
        self.message = message
        # The page number corresponding to the current response.
        self.page_number = page_number
        # The number of entries per page used in the current response.
        self.page_size = page_size
        # The list of node report data.
        self.report_data_model = report_data_model
        # The unique identifier of the request, which can be used to troubleshoot request issues.
        self.request_id = request_id

    def validate(self):
        if self.report_data_model:
            for v1 in self.report_data_model:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        result['ReportDataModel'] = []
        if self.report_data_model is not None:
            for k1 in self.report_data_model:
                result['ReportDataModel'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        self.report_data_model = []
        if m.get('ReportDataModel') is not None:
            for k1 in m.get('ReportDataModel'):
                temp_model = main_models.QueryNodeReportDataResponseBodyReportDataModel()
                self.report_data_model.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class QueryNodeReportDataResponseBodyReportDataModel(DaraModel):
    def __init__(
        self,
        node_count: int = None,
        postpaid_node_count: int = None,
        prepaid_node_count: int = None,
        stat_date: str = None,
    ):
        # The total number of nodes for the record.
        self.node_count = node_count
        # The number of pay-as-you-go nodes in the record.
        self.postpaid_node_count = postpaid_node_count
        # The number of subscription nodes in the record.
        self.prepaid_node_count = prepaid_node_count
        # The statistical time. The 1d granularity returns the time in the yyyy-MM-dd format. The 1m, 30m, and 6h granularities return the time in the yyyy-MM-dd HH:mm format. The string itself does not carry a time zone and is interpreted in the Asia/Shanghai (UTC+8) time zone.
        self.stat_date = stat_date

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.node_count is not None:
            result['NodeCount'] = self.node_count

        if self.postpaid_node_count is not None:
            result['PostpaidNodeCount'] = self.postpaid_node_count

        if self.prepaid_node_count is not None:
            result['PrepaidNodeCount'] = self.prepaid_node_count

        if self.stat_date is not None:
            result['StatDate'] = self.stat_date

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('NodeCount') is not None:
            self.node_count = m.get('NodeCount')

        if m.get('PostpaidNodeCount') is not None:
            self.postpaid_node_count = m.get('PostpaidNodeCount')

        if m.get('PrepaidNodeCount') is not None:
            self.prepaid_node_count = m.get('PrepaidNodeCount')

        if m.get('StatDate') is not None:
            self.stat_date = m.get('StatDate')

        return self


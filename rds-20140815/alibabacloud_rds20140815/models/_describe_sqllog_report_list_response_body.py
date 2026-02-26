# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_rds20140815 import models as main_models
from darabonba.model import DaraModel

class DescribeSQLLogReportListResponseBody(DaraModel):
    def __init__(
        self,
        items: main_models.DescribeSQLLogReportListResponseBodyItems = None,
        page_number: int = None,
        page_record_count: int = None,
        request_id: str = None,
        total_record_count: int = None,
    ):
        self.items = items
        # The page number.
        self.page_number = page_number
        # The number of SQL log reports on the current page.
        self.page_record_count = page_record_count
        # The request ID.
        self.request_id = request_id
        # The total number of entries.
        self.total_record_count = total_record_count

    def validate(self):
        if self.items:
            self.items.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.items is not None:
            result['Items'] = self.items.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_record_count is not None:
            result['PageRecordCount'] = self.page_record_count

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.total_record_count is not None:
            result['TotalRecordCount'] = self.total_record_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Items') is not None:
            temp_model = main_models.DescribeSQLLogReportListResponseBodyItems()
            self.items = temp_model.from_map(m.get('Items'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageRecordCount') is not None:
            self.page_record_count = m.get('PageRecordCount')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('TotalRecordCount') is not None:
            self.total_record_count = m.get('TotalRecordCount')

        return self

class DescribeSQLLogReportListResponseBodyItems(DaraModel):
    def __init__(
        self,
        item: List[main_models.DescribeSQLLogReportListResponseBodyItemsItem] = None,
    ):
        self.item = item

    def validate(self):
        if self.item:
            for v1 in self.item:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Item'] = []
        if self.item is not None:
            for k1 in self.item:
                result['Item'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.item = []
        if m.get('Item') is not None:
            for k1 in m.get('Item'):
                temp_model = main_models.DescribeSQLLogReportListResponseBodyItemsItem()
                self.item.append(temp_model.from_map(k1))

        return self

class DescribeSQLLogReportListResponseBodyItemsItem(DaraModel):
    def __init__(
        self,
        latency_top_nitems: main_models.DescribeSQLLogReportListResponseBodyItemsItemLatencyTopNItems = None,
        qpstop_nitems: main_models.DescribeSQLLogReportListResponseBodyItemsItemQPSTopNItems = None,
        report_time: str = None,
    ):
        self.latency_top_nitems = latency_top_nitems
        self.qpstop_nitems = qpstop_nitems
        self.report_time = report_time

    def validate(self):
        if self.latency_top_nitems:
            self.latency_top_nitems.validate()
        if self.qpstop_nitems:
            self.qpstop_nitems.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.latency_top_nitems is not None:
            result['LatencyTopNItems'] = self.latency_top_nitems.to_map()

        if self.qpstop_nitems is not None:
            result['QPSTopNItems'] = self.qpstop_nitems.to_map()

        if self.report_time is not None:
            result['ReportTime'] = self.report_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('LatencyTopNItems') is not None:
            temp_model = main_models.DescribeSQLLogReportListResponseBodyItemsItemLatencyTopNItems()
            self.latency_top_nitems = temp_model.from_map(m.get('LatencyTopNItems'))

        if m.get('QPSTopNItems') is not None:
            temp_model = main_models.DescribeSQLLogReportListResponseBodyItemsItemQPSTopNItems()
            self.qpstop_nitems = temp_model.from_map(m.get('QPSTopNItems'))

        if m.get('ReportTime') is not None:
            self.report_time = m.get('ReportTime')

        return self

class DescribeSQLLogReportListResponseBodyItemsItemQPSTopNItems(DaraModel):
    def __init__(
        self,
        qpstop_nitem: List[main_models.DescribeSQLLogReportListResponseBodyItemsItemQPSTopNItemsQPSTopNItem] = None,
    ):
        self.qpstop_nitem = qpstop_nitem

    def validate(self):
        if self.qpstop_nitem:
            for v1 in self.qpstop_nitem:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['QPSTopNItem'] = []
        if self.qpstop_nitem is not None:
            for k1 in self.qpstop_nitem:
                result['QPSTopNItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.qpstop_nitem = []
        if m.get('QPSTopNItem') is not None:
            for k1 in m.get('QPSTopNItem'):
                temp_model = main_models.DescribeSQLLogReportListResponseBodyItemsItemQPSTopNItemsQPSTopNItem()
                self.qpstop_nitem.append(temp_model.from_map(k1))

        return self

class DescribeSQLLogReportListResponseBodyItemsItemQPSTopNItemsQPSTopNItem(DaraModel):
    def __init__(
        self,
        sqlexecute_times: int = None,
        sqltext: str = None,
    ):
        self.sqlexecute_times = sqlexecute_times
        self.sqltext = sqltext

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sqlexecute_times is not None:
            result['SQLExecuteTimes'] = self.sqlexecute_times

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SQLExecuteTimes') is not None:
            self.sqlexecute_times = m.get('SQLExecuteTimes')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        return self

class DescribeSQLLogReportListResponseBodyItemsItemLatencyTopNItems(DaraModel):
    def __init__(
        self,
        latency_top_nitem: List[main_models.DescribeSQLLogReportListResponseBodyItemsItemLatencyTopNItemsLatencyTopNItem] = None,
    ):
        self.latency_top_nitem = latency_top_nitem

    def validate(self):
        if self.latency_top_nitem:
            for v1 in self.latency_top_nitem:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['LatencyTopNItem'] = []
        if self.latency_top_nitem is not None:
            for k1 in self.latency_top_nitem:
                result['LatencyTopNItem'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.latency_top_nitem = []
        if m.get('LatencyTopNItem') is not None:
            for k1 in m.get('LatencyTopNItem'):
                temp_model = main_models.DescribeSQLLogReportListResponseBodyItemsItemLatencyTopNItemsLatencyTopNItem()
                self.latency_top_nitem.append(temp_model.from_map(k1))

        return self

class DescribeSQLLogReportListResponseBodyItemsItemLatencyTopNItemsLatencyTopNItem(DaraModel):
    def __init__(
        self,
        avg_latency: int = None,
        sqlexecute_times: int = None,
        sqltext: str = None,
    ):
        self.avg_latency = avg_latency
        self.sqlexecute_times = sqlexecute_times
        self.sqltext = sqltext

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.avg_latency is not None:
            result['AvgLatency'] = self.avg_latency

        if self.sqlexecute_times is not None:
            result['SQLExecuteTimes'] = self.sqlexecute_times

        if self.sqltext is not None:
            result['SQLText'] = self.sqltext

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AvgLatency') is not None:
            self.avg_latency = m.get('AvgLatency')

        if m.get('SQLExecuteTimes') is not None:
            self.sqlexecute_times = m.get('SQLExecuteTimes')

        if m.get('SQLText') is not None:
            self.sqltext = m.get('SQLText')

        return self


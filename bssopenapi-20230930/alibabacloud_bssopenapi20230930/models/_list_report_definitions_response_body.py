# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import Any, List

from alibabacloud_bssopenapi20230930 import models as main_models
from darabonba.model import DaraModel

class ListReportDefinitionsResponseBody(DaraModel):
    def __init__(
        self,
        metadata: Any = None,
        report_definitions: List[main_models.ListReportDefinitionsResponseBodyReportDefinitions] = None,
        request_id: str = None,
    ):
        self.metadata = metadata
        self.report_definitions = report_definitions
        self.request_id = request_id

    def validate(self):
        if self.report_definitions:
            for v1 in self.report_definitions:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.metadata is not None:
            result['Metadata'] = self.metadata

        result['ReportDefinitions'] = []
        if self.report_definitions is not None:
            for k1 in self.report_definitions:
                result['ReportDefinitions'].append(k1.to_map() if k1 else None)

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Metadata') is not None:
            self.metadata = m.get('Metadata')

        self.report_definitions = []
        if m.get('ReportDefinitions') is not None:
            for k1 in m.get('ReportDefinitions'):
                temp_model = main_models.ListReportDefinitionsResponseBodyReportDefinitions()
                self.report_definitions.append(temp_model.from_map(k1))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class ListReportDefinitionsResponseBodyReportDefinitions(DaraModel):
    def __init__(
        self,
        begin_billing_cycle: str = None,
        oss_bucket_name: str = None,
        oss_bucket_owner_account_id: int = None,
        oss_bucket_path: str = None,
        report_source_name: str = None,
        report_source_type: str = None,
        report_task_id: int = None,
        report_type: str = None,
        subscribe_create_time: str = None,
    ):
        self.begin_billing_cycle = begin_billing_cycle
        self.oss_bucket_name = oss_bucket_name
        self.oss_bucket_owner_account_id = oss_bucket_owner_account_id
        self.oss_bucket_path = oss_bucket_path
        self.report_source_name = report_source_name
        self.report_source_type = report_source_type
        self.report_task_id = report_task_id
        self.report_type = report_type
        self.subscribe_create_time = subscribe_create_time

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin_billing_cycle is not None:
            result['BeginBillingCycle'] = self.begin_billing_cycle

        if self.oss_bucket_name is not None:
            result['OssBucketName'] = self.oss_bucket_name

        if self.oss_bucket_owner_account_id is not None:
            result['OssBucketOwnerAccountId'] = self.oss_bucket_owner_account_id

        if self.oss_bucket_path is not None:
            result['OssBucketPath'] = self.oss_bucket_path

        if self.report_source_name is not None:
            result['ReportSourceName'] = self.report_source_name

        if self.report_source_type is not None:
            result['ReportSourceType'] = self.report_source_type

        if self.report_task_id is not None:
            result['ReportTaskId'] = self.report_task_id

        if self.report_type is not None:
            result['ReportType'] = self.report_type

        if self.subscribe_create_time is not None:
            result['SubscribeCreateTime'] = self.subscribe_create_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BeginBillingCycle') is not None:
            self.begin_billing_cycle = m.get('BeginBillingCycle')

        if m.get('OssBucketName') is not None:
            self.oss_bucket_name = m.get('OssBucketName')

        if m.get('OssBucketOwnerAccountId') is not None:
            self.oss_bucket_owner_account_id = m.get('OssBucketOwnerAccountId')

        if m.get('OssBucketPath') is not None:
            self.oss_bucket_path = m.get('OssBucketPath')

        if m.get('ReportSourceName') is not None:
            self.report_source_name = m.get('ReportSourceName')

        if m.get('ReportSourceType') is not None:
            self.report_source_type = m.get('ReportSourceType')

        if m.get('ReportTaskId') is not None:
            self.report_task_id = m.get('ReportTaskId')

        if m.get('ReportType') is not None:
            self.report_type = m.get('ReportType')

        if m.get('SubscribeCreateTime') is not None:
            self.subscribe_create_time = m.get('SubscribeCreateTime')

        return self


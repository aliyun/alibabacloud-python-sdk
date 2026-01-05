# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_polardb20170801 import models as main_models
from darabonba.model import DaraModel

class DescribeUpgradeReportResponseBody(DaraModel):
    def __init__(
        self,
        details: str = None,
        dst_dbtype: str = None,
        items: List[main_models.DescribeUpgradeReportResponseBodyItems] = None,
        items_size: int = None,
        request_id: str = None,
        source_dbcluster_id: str = None,
        src_dbtype: str = None,
        src_deleted: str = None,
        total_size: int = None,
        type: str = None,
        upgrade_report_list: List[main_models.DescribeUpgradeReportResponseBodyUpgradeReportList] = None,
    ):
        self.details = details
        self.dst_dbtype = dst_dbtype
        self.items = items
        self.items_size = items_size
        # Id of the request
        self.request_id = request_id
        self.source_dbcluster_id = source_dbcluster_id
        self.src_dbtype = src_dbtype
        self.src_deleted = src_deleted
        self.total_size = total_size
        self.type = type
        self.upgrade_report_list = upgrade_report_list

    def validate(self):
        if self.items:
            for v1 in self.items:
                 if v1:
                    v1.validate()
        if self.upgrade_report_list:
            for v1 in self.upgrade_report_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.details is not None:
            result['Details'] = self.details

        if self.dst_dbtype is not None:
            result['DstDBType'] = self.dst_dbtype

        result['Items'] = []
        if self.items is not None:
            for k1 in self.items:
                result['Items'].append(k1.to_map() if k1 else None)

        if self.items_size is not None:
            result['ItemsSize'] = self.items_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.source_dbcluster_id is not None:
            result['SourceDBClusterId'] = self.source_dbcluster_id

        if self.src_dbtype is not None:
            result['SrcDBType'] = self.src_dbtype

        if self.src_deleted is not None:
            result['SrcDeleted'] = self.src_deleted

        if self.total_size is not None:
            result['TotalSize'] = self.total_size

        if self.type is not None:
            result['Type'] = self.type

        result['UpgradeReportList'] = []
        if self.upgrade_report_list is not None:
            for k1 in self.upgrade_report_list:
                result['UpgradeReportList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Details') is not None:
            self.details = m.get('Details')

        if m.get('DstDBType') is not None:
            self.dst_dbtype = m.get('DstDBType')

        self.items = []
        if m.get('Items') is not None:
            for k1 in m.get('Items'):
                temp_model = main_models.DescribeUpgradeReportResponseBodyItems()
                self.items.append(temp_model.from_map(k1))

        if m.get('ItemsSize') is not None:
            self.items_size = m.get('ItemsSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('SourceDBClusterId') is not None:
            self.source_dbcluster_id = m.get('SourceDBClusterId')

        if m.get('SrcDBType') is not None:
            self.src_dbtype = m.get('SrcDBType')

        if m.get('SrcDeleted') is not None:
            self.src_deleted = m.get('SrcDeleted')

        if m.get('TotalSize') is not None:
            self.total_size = m.get('TotalSize')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        self.upgrade_report_list = []
        if m.get('UpgradeReportList') is not None:
            for k1 in m.get('UpgradeReportList'):
                temp_model = main_models.DescribeUpgradeReportResponseBodyUpgradeReportList()
                self.upgrade_report_list.append(temp_model.from_map(k1))

        return self

class DescribeUpgradeReportResponseBodyUpgradeReportList(DaraModel):
    def __init__(
        self,
        check_time: str = None,
        dst_version: str = None,
        effective_time: str = None,
        end_time: str = None,
        result: str = None,
        src_ins_name: str = None,
        src_version: str = None,
        start_time: str = None,
        task_id: str = None,
        upgrade_mode: str = None,
    ):
        self.check_time = check_time
        self.dst_version = dst_version
        self.effective_time = effective_time
        self.end_time = end_time
        self.result = result
        self.src_ins_name = src_ins_name
        self.src_version = src_version
        self.start_time = start_time
        self.task_id = task_id
        self.upgrade_mode = upgrade_mode

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.check_time is not None:
            result['CheckTime'] = self.check_time

        if self.dst_version is not None:
            result['DstVersion'] = self.dst_version

        if self.effective_time is not None:
            result['EffectiveTime'] = self.effective_time

        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.result is not None:
            result['Result'] = self.result

        if self.src_ins_name is not None:
            result['SrcInsName'] = self.src_ins_name

        if self.src_version is not None:
            result['SrcVersion'] = self.src_version

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.upgrade_mode is not None:
            result['UpgradeMode'] = self.upgrade_mode

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CheckTime') is not None:
            self.check_time = m.get('CheckTime')

        if m.get('DstVersion') is not None:
            self.dst_version = m.get('DstVersion')

        if m.get('EffectiveTime') is not None:
            self.effective_time = m.get('EffectiveTime')

        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('Result') is not None:
            self.result = m.get('Result')

        if m.get('SrcInsName') is not None:
            self.src_ins_name = m.get('SrcInsName')

        if m.get('SrcVersion') is not None:
            self.src_version = m.get('SrcVersion')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('UpgradeMode') is not None:
            self.upgrade_mode = m.get('UpgradeMode')

        return self

class DescribeUpgradeReportResponseBodyItems(DaraModel):
    def __init__(
        self,
        ddl: str = None,
        name: str = None,
        schema: str = None,
        status: str = None,
        type: str = None,
    ):
        self.ddl = ddl
        self.name = name
        self.schema = schema
        self.status = status
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ddl is not None:
            result['DDL'] = self.ddl

        if self.name is not None:
            result['Name'] = self.name

        if self.schema is not None:
            result['Schema'] = self.schema

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DDL') is not None:
            self.ddl = m.get('DDL')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Schema') is not None:
            self.schema = m.get('Schema')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self


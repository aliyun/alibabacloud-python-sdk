# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class CreateEcdReportTaskRequest(DaraModel):
    def __init__(
        self,
        filter_list: List[main_models.CreateEcdReportTaskRequestFilterList] = None,
        lang_type: str = None,
        report_file_name: str = None,
        sub_type: str = None,
        task_type: str = None,
    ):
        # The filter conditions for filtering query results. The logical relationship between each filter condition is "and" (&). Each filter condition contains FilterKey and FilterValues, which indicate the key and value for the filter condition.
        self.filter_list = filter_list
        # The language of the report. An enumerated type.
        # 
        # Valid values:
        # 
        # *   zh-CN (default): Chinese
        # *   en-GB: English
        self.lang_type = lang_type
        # The name of the report file.
        self.report_file_name = report_file_name
        # The sub-type of the report export task.
        # 
        # Valid value:
        # 
        # *   DESKTOP: cloud computer
        # 
        # This parameter is required.
        self.sub_type = sub_type
        # The type of the report task.
        # 
        # Valid value:
        # 
        # *   RESOURCE_REPORT
        # 
        # This parameter is required.
        self.task_type = task_type

    def validate(self):
        if self.filter_list:
            for v1 in self.filter_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['FilterList'] = []
        if self.filter_list is not None:
            for k1 in self.filter_list:
                result['FilterList'].append(k1.to_map() if k1 else None)

        if self.lang_type is not None:
            result['LangType'] = self.lang_type

        if self.report_file_name is not None:
            result['ReportFileName'] = self.report_file_name

        if self.sub_type is not None:
            result['SubType'] = self.sub_type

        if self.task_type is not None:
            result['TaskType'] = self.task_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.filter_list = []
        if m.get('FilterList') is not None:
            for k1 in m.get('FilterList'):
                temp_model = main_models.CreateEcdReportTaskRequestFilterList()
                self.filter_list.append(temp_model.from_map(k1))

        if m.get('LangType') is not None:
            self.lang_type = m.get('LangType')

        if m.get('ReportFileName') is not None:
            self.report_file_name = m.get('ReportFileName')

        if m.get('SubType') is not None:
            self.sub_type = m.get('SubType')

        if m.get('TaskType') is not None:
            self.task_type = m.get('TaskType')

        return self

class CreateEcdReportTaskRequestFilterList(DaraModel):
    def __init__(
        self,
        filter_key: str = None,
        filter_values: List[str] = None,
    ):
        # The key of the filter condition for filtering query results. When SubType is set to:
        # 
        # 1.  DESKTOP (indicating a cloud computer report), the following filter conditions are available:
        # 
        # *   KeyWord: cloud computer keyword (supports automatic recognition)
        # *   RegionId: region ID
        # *   DesktopId: cloud computer ID
        # *   DesktopName: cloud computer name (supports fuzzy matching)
        # *   OfficeSiteId: office network ID
        # *   OfficeSiteName: office network name (supports fuzzy matching)
        # *   Status: cloud computer status
        # *   DesktopType: desktop type
        # *   DesktopIP: cloud computer IP address
        # *   SubPayType: billing method
        # *   EndUserId: user name (supports fuzzy matching)
        # *   ExpireTime: expiration date and time, in the yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\" format
        # *   IncludeAssignedUser: indicates whether the cloud computer is assigned to users or not
        # *   ResourceGroupId: resource group ID
        # *   PolicyId: policy ID
        # *   Tag:{Tag Key value}: cloud computer tag (To filter data using multiple tags, specify multiple filter condition objects.)
        self.filter_key = filter_key
        # The value of the filter condition. Only the first value of the FilterValues parameter is used, if FilterKey is set to one of the following values:
        # 
        # *   KeyWord
        # *   DesktopName
        # *   OfficeSiteName
        # *   DesktopIP
        # *   EndUserId
        # *   ExpireTime
        # *   IncludeAssignedUser
        self.filter_values = filter_values

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.filter_key is not None:
            result['FilterKey'] = self.filter_key

        if self.filter_values is not None:
            result['FilterValues'] = self.filter_values

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FilterKey') is not None:
            self.filter_key = m.get('FilterKey')

        if m.get('FilterValues') is not None:
            self.filter_values = m.get('FilterValues')

        return self


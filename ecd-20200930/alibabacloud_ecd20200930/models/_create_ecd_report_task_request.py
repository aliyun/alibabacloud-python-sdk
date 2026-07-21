# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_ecd20200930 import models as main_models
from darabonba.model import DaraModel

class CreateEcdReportTaskRequest(DaraModel):
    def __init__(
        self,
        business_channel: str = None,
        filter_list: List[main_models.CreateEcdReportTaskRequestFilterList] = None,
        lang_type: str = None,
        report_file_name: str = None,
        sub_type: str = None,
        task_type: str = None,
    ):
        self.business_channel = business_channel
        # The list of filter conditions for query results. The filter condition objects have a logical AND (&) relationship.
        # Each filter condition contains FilterKey and FilterValues, which represent the filter condition name and specific values.
        self.filter_list = filter_list
        # The report language type. This is an enumerated value.
        self.lang_type = lang_type
        # The report file name.
        self.report_file_name = report_file_name
        # The report task subtype.
        # [_single.params.SubType.enum.  DESKTOP]Cloud computer
        # 
        # This parameter is required.
        self.sub_type = sub_type
        # The report task type.
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
        if self.business_channel is not None:
            result['BusinessChannel'] = self.business_channel

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
        if m.get('BusinessChannel') is not None:
            self.business_channel = m.get('BusinessChannel')

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
        # The report query filter condition. The valid values vary based on the SubType value:
        # 1. Cloud computer report
        # - KeyWord: automatic keyword recognition for cloud computers.
        # - RegionId: the region ID.
        # - DesktopId: the cloud computer ID.
        # - DesktopName: the cloud computer name (fuzzy match).
        # - OfficeSiteId: the office network ID.
        # - OfficeSiteName: the office network name (fuzzy match).
        # - Status: the cloud computer status.
        # - DesktopType: the desktop specifications.
        # - DesktopIP: the cloud computer IP address.
        # - SubPayType: the billing method.
        # - EndUserId: the username (fuzzy match).
        # - ExpireTime: the expiration time in the yyyy-MM-dd\\"T\\"HH:mm:ss\\"Z\\" format.
        # - IncludeAssignedUser: specifies whether users are assigned.
        # - ResourceGroupId: the resource group ID.
        # - PolicyId: the policy ID.
        # - Tag:{Tag Key}: the cloud computer tag. To query by multiple tags, pass in multiple Filter objects.
        self.filter_key = filter_key
        # The values of the filter condition.
        # When FilterKey is set to one of the following values, only the first value in FilterValues is used:
        # - KeyWord
        # - DesktopName
        # - OfficeSiteName
        # - DesktopIP
        # - EndUserId
        # - ExpireTime
        # - IncludeAssignedUser
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


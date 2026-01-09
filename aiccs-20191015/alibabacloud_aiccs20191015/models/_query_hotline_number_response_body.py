# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aiccs20191015 import models as main_models
from darabonba.model import DaraModel

class QueryHotlineNumberResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryHotlineNumberResponseBodyData = None,
        message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.data = data
        self.message = message
        self.request_id = request_id
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
            temp_model = main_models.QueryHotlineNumberResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryHotlineNumberResponseBodyData(DaraModel):
    def __init__(
        self,
        current_page: int = None,
        hotline_num_list: List[main_models.QueryHotlineNumberResponseBodyDataHotlineNumList] = None,
        page_size: int = None,
        total_count: int = None,
    ):
        self.current_page = current_page
        self.hotline_num_list = hotline_num_list
        self.page_size = page_size
        self.total_count = total_count

    def validate(self):
        if self.hotline_num_list:
            for v1 in self.hotline_num_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        result['HotlineNumList'] = []
        if self.hotline_num_list is not None:
            for k1 in self.hotline_num_list:
                result['HotlineNumList'].append(k1.to_map() if k1 else None)

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        self.hotline_num_list = []
        if m.get('HotlineNumList') is not None:
            for k1 in m.get('HotlineNumList'):
                temp_model = main_models.QueryHotlineNumberResponseBodyDataHotlineNumList()
                self.hotline_num_list.append(temp_model.from_map(k1))

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class QueryHotlineNumberResponseBodyDataHotlineNumList(DaraModel):
    def __init__(
        self,
        callout_all_department: bool = None,
        callout_range_list: List[main_models.QueryHotlineNumberResponseBodyDataHotlineNumListCalloutRangeList] = None,
        description: str = None,
        evaluation_status: int = None,
        flow_id: int = None,
        flow_name: str = None,
        hotline_number: str = None,
        in_bound_enabled: bool = None,
        location: str = None,
        outbound_enabled: bool = None,
        sp: str = None,
    ):
        self.callout_all_department = callout_all_department
        self.callout_range_list = callout_range_list
        self.description = description
        self.evaluation_status = evaluation_status
        self.flow_id = flow_id
        self.flow_name = flow_name
        self.hotline_number = hotline_number
        self.in_bound_enabled = in_bound_enabled
        self.location = location
        self.outbound_enabled = outbound_enabled
        self.sp = sp

    def validate(self):
        if self.callout_range_list:
            for v1 in self.callout_range_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.callout_all_department is not None:
            result['CalloutAllDepartment'] = self.callout_all_department

        result['CalloutRangeList'] = []
        if self.callout_range_list is not None:
            for k1 in self.callout_range_list:
                result['CalloutRangeList'].append(k1.to_map() if k1 else None)

        if self.description is not None:
            result['Description'] = self.description

        if self.evaluation_status is not None:
            result['EvaluationStatus'] = self.evaluation_status

        if self.flow_id is not None:
            result['FlowId'] = self.flow_id

        if self.flow_name is not None:
            result['FlowName'] = self.flow_name

        if self.hotline_number is not None:
            result['HotlineNumber'] = self.hotline_number

        if self.in_bound_enabled is not None:
            result['InBoundEnabled'] = self.in_bound_enabled

        if self.location is not None:
            result['Location'] = self.location

        if self.outbound_enabled is not None:
            result['OutboundEnabled'] = self.outbound_enabled

        if self.sp is not None:
            result['Sp'] = self.sp

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CalloutAllDepartment') is not None:
            self.callout_all_department = m.get('CalloutAllDepartment')

        self.callout_range_list = []
        if m.get('CalloutRangeList') is not None:
            for k1 in m.get('CalloutRangeList'):
                temp_model = main_models.QueryHotlineNumberResponseBodyDataHotlineNumListCalloutRangeList()
                self.callout_range_list.append(temp_model.from_map(k1))

        if m.get('Description') is not None:
            self.description = m.get('Description')

        if m.get('EvaluationStatus') is not None:
            self.evaluation_status = m.get('EvaluationStatus')

        if m.get('FlowId') is not None:
            self.flow_id = m.get('FlowId')

        if m.get('FlowName') is not None:
            self.flow_name = m.get('FlowName')

        if m.get('HotlineNumber') is not None:
            self.hotline_number = m.get('HotlineNumber')

        if m.get('InBoundEnabled') is not None:
            self.in_bound_enabled = m.get('InBoundEnabled')

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('OutboundEnabled') is not None:
            self.outbound_enabled = m.get('OutboundEnabled')

        if m.get('Sp') is not None:
            self.sp = m.get('Sp')

        return self

class QueryHotlineNumberResponseBodyDataHotlineNumListCalloutRangeList(DaraModel):
    def __init__(
        self,
        department_id: int = None,
        department_name: str = None,
        group_dolist: List[main_models.QueryHotlineNumberResponseBodyDataHotlineNumListCalloutRangeListGroupDOList] = None,
    ):
        self.department_id = department_id
        self.department_name = department_name
        self.group_dolist = group_dolist

    def validate(self):
        if self.group_dolist:
            for v1 in self.group_dolist:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.department_id is not None:
            result['DepartmentId'] = self.department_id

        if self.department_name is not None:
            result['DepartmentName'] = self.department_name

        result['GroupDOList'] = []
        if self.group_dolist is not None:
            for k1 in self.group_dolist:
                result['GroupDOList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DepartmentId') is not None:
            self.department_id = m.get('DepartmentId')

        if m.get('DepartmentName') is not None:
            self.department_name = m.get('DepartmentName')

        self.group_dolist = []
        if m.get('GroupDOList') is not None:
            for k1 in m.get('GroupDOList'):
                temp_model = main_models.QueryHotlineNumberResponseBodyDataHotlineNumListCalloutRangeListGroupDOList()
                self.group_dolist.append(temp_model.from_map(k1))

        return self

class QueryHotlineNumberResponseBodyDataHotlineNumListCalloutRangeListGroupDOList(DaraModel):
    def __init__(
        self,
        group_id: int = None,
        group_name: str = None,
    ):
        self.group_id = group_id
        self.group_name = group_name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.group_id is not None:
            result['GroupId'] = self.group_id

        if self.group_name is not None:
            result['GroupName'] = self.group_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GroupId') is not None:
            self.group_id = m.get('GroupId')

        if m.get('GroupName') is not None:
            self.group_name = m.get('GroupName')

        return self


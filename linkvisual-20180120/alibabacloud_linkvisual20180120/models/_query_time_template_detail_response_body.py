# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_linkvisual20180120 import models as main_models
from darabonba.model import DaraModel

class QueryTimeTemplateDetailResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: main_models.QueryTimeTemplateDetailResponseBodyData = None,
        error_message: str = None,
        request_id: str = None,
        success: bool = None,
    ):
        # The response code:
        # 
        # - **200**: The call is successful.
        # - Other values: error codes. For more information, see [Error codes](https://help.aliyun.com/document_detail/145071.html).
        self.code = code
        # The time template information returned when the call was successful.
        self.data = data
        # The error message returned when the call failed.
        self.error_message = error_message
        # The ID of the request.
        self.request_id = request_id
        # Indicates whether the call was successful:
        # - **true**: The call was successful.
        # - **false**: The call failed.
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

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

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
            temp_model = main_models.QueryTimeTemplateDetailResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class QueryTimeTemplateDetailResponseBodyData(DaraModel):
    def __init__(
        self,
        all_day: int = None,
        default: int = None,
        name: str = None,
        template_id: str = None,
        time_section_list: List[main_models.QueryTimeTemplateDetailResponseBodyDataTimeSectionList] = None,
    ):
        # Indicates whether 24/7 recording is enabled:
        # 
        # - **1**: Yes.
        # - **0**: No. For detailed configuration, see the **TimeSectionList** parameter.
        self.all_day = all_day
        # Indicates whether the template is the default template:
        # 
        # - **1**: Default template.
        # - **0**: Custom template.
        self.default = default
        # The name of the time template.
        self.name = name
        # The ID of the time template.
        self.template_id = template_id
        # The list of time sections in the time template.
        self.time_section_list = time_section_list

    def validate(self):
        if self.time_section_list:
            for v1 in self.time_section_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.all_day is not None:
            result['AllDay'] = self.all_day

        if self.default is not None:
            result['Default'] = self.default

        if self.name is not None:
            result['Name'] = self.name

        if self.template_id is not None:
            result['TemplateId'] = self.template_id

        result['TimeSectionList'] = []
        if self.time_section_list is not None:
            for k1 in self.time_section_list:
                result['TimeSectionList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AllDay') is not None:
            self.all_day = m.get('AllDay')

        if m.get('Default') is not None:
            self.default = m.get('Default')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('TemplateId') is not None:
            self.template_id = m.get('TemplateId')

        self.time_section_list = []
        if m.get('TimeSectionList') is not None:
            for k1 in m.get('TimeSectionList'):
                temp_model = main_models.QueryTimeTemplateDetailResponseBodyDataTimeSectionList()
                self.time_section_list.append(temp_model.from_map(k1))

        return self

class QueryTimeTemplateDetailResponseBodyDataTimeSectionList(DaraModel):
    def __init__(
        self,
        begin: int = None,
        day_of_week: int = None,
        end: int = None,
    ):
        # The start time of each day, in seconds.
        self.begin = begin
        # The day of the week. Valid values: 0 to 6, where 0 indicates Sunday and 6 indicates Saturday.
        self.day_of_week = day_of_week
        # The end time of each day, in seconds.
        self.end = end

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.begin is not None:
            result['Begin'] = self.begin

        if self.day_of_week is not None:
            result['DayOfWeek'] = self.day_of_week

        if self.end is not None:
            result['End'] = self.end

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Begin') is not None:
            self.begin = m.get('Begin')

        if m.get('DayOfWeek') is not None:
            self.day_of_week = m.get('DayOfWeek')

        if m.get('End') is not None:
            self.end = m.get('End')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListSessionGroupResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        current_page: int = None,
        data: main_models.ListSessionGroupResponseBodyData = None,
        http_status_code: int = None,
        last_data_id: str = None,
        message: str = None,
        messages: main_models.ListSessionGroupResponseBodyMessages = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        result_count_id: str = None,
        success: bool = None,
    ):
        self.code = code
        self.count = count
        self.current_page = current_page
        self.data = data
        self.http_status_code = http_status_code
        self.last_data_id = last_data_id
        self.message = message
        self.messages = messages
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.result_count_id = result_count_id
        self.success = success

    def validate(self):
        if self.data:
            self.data.validate()
        if self.messages:
            self.messages.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.count is not None:
            result['Count'] = self.count

        if self.current_page is not None:
            result['CurrentPage'] = self.current_page

        if self.data is not None:
            result['Data'] = self.data.to_map()

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.last_data_id is not None:
            result['LastDataId'] = self.last_data_id

        if self.message is not None:
            result['Message'] = self.message

        if self.messages is not None:
            result['Messages'] = self.messages.to_map()

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.result_count_id is not None:
            result['ResultCountId'] = self.result_count_id

        if self.success is not None:
            result['Success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('Count') is not None:
            self.count = m.get('Count')

        if m.get('CurrentPage') is not None:
            self.current_page = m.get('CurrentPage')

        if m.get('Data') is not None:
            temp_model = main_models.ListSessionGroupResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('LastDataId') is not None:
            self.last_data_id = m.get('LastDataId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Messages') is not None:
            temp_model = main_models.ListSessionGroupResponseBodyMessages()
            self.messages = temp_model.from_map(m.get('Messages'))

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('ResultCountId') is not None:
            self.result_count_id = m.get('ResultCountId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        return self

class ListSessionGroupResponseBodyMessages(DaraModel):
    def __init__(
        self,
        message: List[str] = None,
    ):
        self.message = message

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.message is not None:
            result['Message'] = self.message

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Message') is not None:
            self.message = m.get('Message')

        return self

class ListSessionGroupResponseBodyData(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListSessionGroupResponseBodyDataData] = None,
    ):
        self.data = data

    def validate(self):
        if self.data:
            for v1 in self.data:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSessionGroupResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        return self

class ListSessionGroupResponseBodyDataData(DaraModel):
    def __init__(
        self,
        assign_status: int = None,
        call_start_time: str = None,
        caller_list: main_models.ListSessionGroupResponseBodyDataDataCallerList = None,
        customer_id_list: main_models.ListSessionGroupResponseBodyDataDataCustomerIdList = None,
        customer_name_list: main_models.ListSessionGroupResponseBodyDataDataCustomerNameList = None,
        customer_service_id_list: main_models.ListSessionGroupResponseBodyDataDataCustomerServiceIdList = None,
        customer_service_name_list: main_models.ListSessionGroupResponseBodyDataDataCustomerServiceNameList = None,
        hit_session_count: int = None,
        last_data_id: str = None,
        review_status: int = None,
        reviewer_list: main_models.ListSessionGroupResponseBodyDataDataReviewerList = None,
        scheme_task_config_id: int = None,
        scheme_task_config_name: str = None,
        score: int = None,
        session_count: int = None,
        session_group_id: str = None,
        session_group_reviewed_or_complained: bool = None,
        skill_group_name_list: main_models.ListSessionGroupResponseBodyDataDataSkillGroupNameList = None,
    ):
        self.assign_status = assign_status
        self.call_start_time = call_start_time
        self.caller_list = caller_list
        self.customer_id_list = customer_id_list
        self.customer_name_list = customer_name_list
        self.customer_service_id_list = customer_service_id_list
        self.customer_service_name_list = customer_service_name_list
        self.hit_session_count = hit_session_count
        self.last_data_id = last_data_id
        self.review_status = review_status
        self.reviewer_list = reviewer_list
        self.scheme_task_config_id = scheme_task_config_id
        self.scheme_task_config_name = scheme_task_config_name
        self.score = score
        self.session_count = session_count
        self.session_group_id = session_group_id
        self.session_group_reviewed_or_complained = session_group_reviewed_or_complained
        self.skill_group_name_list = skill_group_name_list

    def validate(self):
        if self.caller_list:
            self.caller_list.validate()
        if self.customer_id_list:
            self.customer_id_list.validate()
        if self.customer_name_list:
            self.customer_name_list.validate()
        if self.customer_service_id_list:
            self.customer_service_id_list.validate()
        if self.customer_service_name_list:
            self.customer_service_name_list.validate()
        if self.reviewer_list:
            self.reviewer_list.validate()
        if self.skill_group_name_list:
            self.skill_group_name_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assign_status is not None:
            result['AssignStatus'] = self.assign_status

        if self.call_start_time is not None:
            result['CallStartTime'] = self.call_start_time

        if self.caller_list is not None:
            result['CallerList'] = self.caller_list.to_map()

        if self.customer_id_list is not None:
            result['CustomerIdList'] = self.customer_id_list.to_map()

        if self.customer_name_list is not None:
            result['CustomerNameList'] = self.customer_name_list.to_map()

        if self.customer_service_id_list is not None:
            result['CustomerServiceIdList'] = self.customer_service_id_list.to_map()

        if self.customer_service_name_list is not None:
            result['CustomerServiceNameList'] = self.customer_service_name_list.to_map()

        if self.hit_session_count is not None:
            result['HitSessionCount'] = self.hit_session_count

        if self.last_data_id is not None:
            result['LastDataId'] = self.last_data_id

        if self.review_status is not None:
            result['ReviewStatus'] = self.review_status

        if self.reviewer_list is not None:
            result['ReviewerList'] = self.reviewer_list.to_map()

        if self.scheme_task_config_id is not None:
            result['SchemeTaskConfigId'] = self.scheme_task_config_id

        if self.scheme_task_config_name is not None:
            result['SchemeTaskConfigName'] = self.scheme_task_config_name

        if self.score is not None:
            result['Score'] = self.score

        if self.session_count is not None:
            result['SessionCount'] = self.session_count

        if self.session_group_id is not None:
            result['SessionGroupId'] = self.session_group_id

        if self.session_group_reviewed_or_complained is not None:
            result['SessionGroupReviewedOrComplained'] = self.session_group_reviewed_or_complained

        if self.skill_group_name_list is not None:
            result['SkillGroupNameList'] = self.skill_group_name_list.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignStatus') is not None:
            self.assign_status = m.get('AssignStatus')

        if m.get('CallStartTime') is not None:
            self.call_start_time = m.get('CallStartTime')

        if m.get('CallerList') is not None:
            temp_model = main_models.ListSessionGroupResponseBodyDataDataCallerList()
            self.caller_list = temp_model.from_map(m.get('CallerList'))

        if m.get('CustomerIdList') is not None:
            temp_model = main_models.ListSessionGroupResponseBodyDataDataCustomerIdList()
            self.customer_id_list = temp_model.from_map(m.get('CustomerIdList'))

        if m.get('CustomerNameList') is not None:
            temp_model = main_models.ListSessionGroupResponseBodyDataDataCustomerNameList()
            self.customer_name_list = temp_model.from_map(m.get('CustomerNameList'))

        if m.get('CustomerServiceIdList') is not None:
            temp_model = main_models.ListSessionGroupResponseBodyDataDataCustomerServiceIdList()
            self.customer_service_id_list = temp_model.from_map(m.get('CustomerServiceIdList'))

        if m.get('CustomerServiceNameList') is not None:
            temp_model = main_models.ListSessionGroupResponseBodyDataDataCustomerServiceNameList()
            self.customer_service_name_list = temp_model.from_map(m.get('CustomerServiceNameList'))

        if m.get('HitSessionCount') is not None:
            self.hit_session_count = m.get('HitSessionCount')

        if m.get('LastDataId') is not None:
            self.last_data_id = m.get('LastDataId')

        if m.get('ReviewStatus') is not None:
            self.review_status = m.get('ReviewStatus')

        if m.get('ReviewerList') is not None:
            temp_model = main_models.ListSessionGroupResponseBodyDataDataReviewerList()
            self.reviewer_list = temp_model.from_map(m.get('ReviewerList'))

        if m.get('SchemeTaskConfigId') is not None:
            self.scheme_task_config_id = m.get('SchemeTaskConfigId')

        if m.get('SchemeTaskConfigName') is not None:
            self.scheme_task_config_name = m.get('SchemeTaskConfigName')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SessionCount') is not None:
            self.session_count = m.get('SessionCount')

        if m.get('SessionGroupId') is not None:
            self.session_group_id = m.get('SessionGroupId')

        if m.get('SessionGroupReviewedOrComplained') is not None:
            self.session_group_reviewed_or_complained = m.get('SessionGroupReviewedOrComplained')

        if m.get('SkillGroupNameList') is not None:
            temp_model = main_models.ListSessionGroupResponseBodyDataDataSkillGroupNameList()
            self.skill_group_name_list = temp_model.from_map(m.get('SkillGroupNameList'))

        return self

class ListSessionGroupResponseBodyDataDataSkillGroupNameList(DaraModel):
    def __init__(
        self,
        skill_group_name_list: List[str] = None,
    ):
        self.skill_group_name_list = skill_group_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.skill_group_name_list is not None:
            result['SkillGroupNameList'] = self.skill_group_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SkillGroupNameList') is not None:
            self.skill_group_name_list = m.get('SkillGroupNameList')

        return self

class ListSessionGroupResponseBodyDataDataReviewerList(DaraModel):
    def __init__(
        self,
        reviewer_list: List[str] = None,
    ):
        self.reviewer_list = reviewer_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.reviewer_list is not None:
            result['ReviewerList'] = self.reviewer_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ReviewerList') is not None:
            self.reviewer_list = m.get('ReviewerList')

        return self

class ListSessionGroupResponseBodyDataDataCustomerServiceNameList(DaraModel):
    def __init__(
        self,
        customer_service_name_list: List[str] = None,
    ):
        self.customer_service_name_list = customer_service_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_service_name_list is not None:
            result['CustomerServiceNameList'] = self.customer_service_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerServiceNameList') is not None:
            self.customer_service_name_list = m.get('CustomerServiceNameList')

        return self

class ListSessionGroupResponseBodyDataDataCustomerServiceIdList(DaraModel):
    def __init__(
        self,
        customer_service_id_list: List[str] = None,
    ):
        self.customer_service_id_list = customer_service_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_service_id_list is not None:
            result['CustomerServiceIdList'] = self.customer_service_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerServiceIdList') is not None:
            self.customer_service_id_list = m.get('CustomerServiceIdList')

        return self

class ListSessionGroupResponseBodyDataDataCustomerNameList(DaraModel):
    def __init__(
        self,
        customer_name_list: List[str] = None,
    ):
        self.customer_name_list = customer_name_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_name_list is not None:
            result['CustomerNameList'] = self.customer_name_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerNameList') is not None:
            self.customer_name_list = m.get('CustomerNameList')

        return self

class ListSessionGroupResponseBodyDataDataCustomerIdList(DaraModel):
    def __init__(
        self,
        customer_id_list: List[str] = None,
    ):
        self.customer_id_list = customer_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.customer_id_list is not None:
            result['CustomerIdList'] = self.customer_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CustomerIdList') is not None:
            self.customer_id_list = m.get('CustomerIdList')

        return self

class ListSessionGroupResponseBodyDataDataCallerList(DaraModel):
    def __init__(
        self,
        caller_list: List[str] = None,
    ):
        self.caller_list = caller_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.caller_list is not None:
            result['CallerList'] = self.caller_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CallerList') is not None:
            self.caller_list = m.get('CallerList')

        return self


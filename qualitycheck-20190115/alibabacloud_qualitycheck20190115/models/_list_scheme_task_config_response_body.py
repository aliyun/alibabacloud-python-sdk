# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List, Any

from alibabacloud_qualitycheck20190115 import models as main_models
from darabonba.model import DaraModel

class ListSchemeTaskConfigResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        count: int = None,
        current_page: int = None,
        data: main_models.ListSchemeTaskConfigResponseBodyData = None,
        http_status_code: int = None,
        last_data_id: str = None,
        message: str = None,
        messages: main_models.ListSchemeTaskConfigResponseBodyMessages = None,
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
            temp_model = main_models.ListSchemeTaskConfigResponseBodyData()
            self.data = temp_model.from_map(m.get('Data'))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('LastDataId') is not None:
            self.last_data_id = m.get('LastDataId')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('Messages') is not None:
            temp_model = main_models.ListSchemeTaskConfigResponseBodyMessages()
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

class ListSchemeTaskConfigResponseBodyMessages(DaraModel):
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

class ListSchemeTaskConfigResponseBodyData(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListSchemeTaskConfigResponseBodyDataData] = None,
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
                temp_model = main_models.ListSchemeTaskConfigResponseBodyDataData()
                self.data.append(temp_model.from_map(k1))

        return self

class ListSchemeTaskConfigResponseBodyDataData(DaraModel):
    def __init__(
        self,
        asr_task_priority: int = None,
        asr_version: int = None,
        assign_type: int = None,
        create_time: str = None,
        create_user: int = None,
        data_config: main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfig = None,
        finish_rate: float = None,
        id: int = None,
        manual_review: int = None,
        mode_customization_id: str = None,
        model_name: str = None,
        name: str = None,
        number_executing: int = None,
        number_fail: int = None,
        number_success: int = None,
        number_sum: int = None,
        scheme_id_list: main_models.ListSchemeTaskConfigResponseBodyDataDataSchemeIdList = None,
        scheme_list: main_models.ListSchemeTaskConfigResponseBodyDataDataSchemeList = None,
        scheme_task_config_id: int = None,
        source_data_type: int = None,
        status: int = None,
        type: int = None,
        update_time: str = None,
        update_user: int = None,
        user_group: str = None,
        vocab_id: str = None,
        vocab_name: str = None,
    ):
        self.asr_task_priority = asr_task_priority
        self.asr_version = asr_version
        self.assign_type = assign_type
        self.create_time = create_time
        self.create_user = create_user
        self.data_config = data_config
        self.finish_rate = finish_rate
        self.id = id
        self.manual_review = manual_review
        self.mode_customization_id = mode_customization_id
        self.model_name = model_name
        self.name = name
        self.number_executing = number_executing
        self.number_fail = number_fail
        self.number_success = number_success
        self.number_sum = number_sum
        self.scheme_id_list = scheme_id_list
        self.scheme_list = scheme_list
        self.scheme_task_config_id = scheme_task_config_id
        self.source_data_type = source_data_type
        self.status = status
        self.type = type
        self.update_time = update_time
        self.update_user = update_user
        self.user_group = user_group
        self.vocab_id = vocab_id
        self.vocab_name = vocab_name

    def validate(self):
        if self.data_config:
            self.data_config.validate()
        if self.scheme_id_list:
            self.scheme_id_list.validate()
        if self.scheme_list:
            self.scheme_list.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.asr_task_priority is not None:
            result['AsrTaskPriority'] = self.asr_task_priority

        if self.asr_version is not None:
            result['AsrVersion'] = self.asr_version

        if self.assign_type is not None:
            result['AssignType'] = self.assign_type

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.create_user is not None:
            result['CreateUser'] = self.create_user

        if self.data_config is not None:
            result['DataConfig'] = self.data_config.to_map()

        if self.finish_rate is not None:
            result['FinishRate'] = self.finish_rate

        if self.id is not None:
            result['Id'] = self.id

        if self.manual_review is not None:
            result['ManualReview'] = self.manual_review

        if self.mode_customization_id is not None:
            result['ModeCustomizationId'] = self.mode_customization_id

        if self.model_name is not None:
            result['ModelName'] = self.model_name

        if self.name is not None:
            result['Name'] = self.name

        if self.number_executing is not None:
            result['NumberExecuting'] = self.number_executing

        if self.number_fail is not None:
            result['NumberFail'] = self.number_fail

        if self.number_success is not None:
            result['NumberSuccess'] = self.number_success

        if self.number_sum is not None:
            result['NumberSum'] = self.number_sum

        if self.scheme_id_list is not None:
            result['SchemeIdList'] = self.scheme_id_list.to_map()

        if self.scheme_list is not None:
            result['SchemeList'] = self.scheme_list.to_map()

        if self.scheme_task_config_id is not None:
            result['SchemeTaskConfigId'] = self.scheme_task_config_id

        if self.source_data_type is not None:
            result['SourceDataType'] = self.source_data_type

        if self.status is not None:
            result['Status'] = self.status

        if self.type is not None:
            result['Type'] = self.type

        if self.update_time is not None:
            result['UpdateTime'] = self.update_time

        if self.update_user is not None:
            result['UpdateUser'] = self.update_user

        if self.user_group is not None:
            result['UserGroup'] = self.user_group

        if self.vocab_id is not None:
            result['VocabId'] = self.vocab_id

        if self.vocab_name is not None:
            result['VocabName'] = self.vocab_name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AsrTaskPriority') is not None:
            self.asr_task_priority = m.get('AsrTaskPriority')

        if m.get('AsrVersion') is not None:
            self.asr_version = m.get('AsrVersion')

        if m.get('AssignType') is not None:
            self.assign_type = m.get('AssignType')

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('CreateUser') is not None:
            self.create_user = m.get('CreateUser')

        if m.get('DataConfig') is not None:
            temp_model = main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfig()
            self.data_config = temp_model.from_map(m.get('DataConfig'))

        if m.get('FinishRate') is not None:
            self.finish_rate = m.get('FinishRate')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('ManualReview') is not None:
            self.manual_review = m.get('ManualReview')

        if m.get('ModeCustomizationId') is not None:
            self.mode_customization_id = m.get('ModeCustomizationId')

        if m.get('ModelName') is not None:
            self.model_name = m.get('ModelName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('NumberExecuting') is not None:
            self.number_executing = m.get('NumberExecuting')

        if m.get('NumberFail') is not None:
            self.number_fail = m.get('NumberFail')

        if m.get('NumberSuccess') is not None:
            self.number_success = m.get('NumberSuccess')

        if m.get('NumberSum') is not None:
            self.number_sum = m.get('NumberSum')

        if m.get('SchemeIdList') is not None:
            temp_model = main_models.ListSchemeTaskConfigResponseBodyDataDataSchemeIdList()
            self.scheme_id_list = temp_model.from_map(m.get('SchemeIdList'))

        if m.get('SchemeList') is not None:
            temp_model = main_models.ListSchemeTaskConfigResponseBodyDataDataSchemeList()
            self.scheme_list = temp_model.from_map(m.get('SchemeList'))

        if m.get('SchemeTaskConfigId') is not None:
            self.scheme_task_config_id = m.get('SchemeTaskConfigId')

        if m.get('SourceDataType') is not None:
            self.source_data_type = m.get('SourceDataType')

        if m.get('Status') is not None:
            self.status = m.get('Status')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')

        if m.get('UpdateUser') is not None:
            self.update_user = m.get('UpdateUser')

        if m.get('UserGroup') is not None:
            self.user_group = m.get('UserGroup')

        if m.get('VocabId') is not None:
            self.vocab_id = m.get('VocabId')

        if m.get('VocabName') is not None:
            self.vocab_name = m.get('VocabName')

        return self

class ListSchemeTaskConfigResponseBodyDataDataSchemeList(DaraModel):
    def __init__(
        self,
        scheme_list: List[main_models.ListSchemeTaskConfigResponseBodyDataDataSchemeListSchemeList] = None,
    ):
        self.scheme_list = scheme_list

    def validate(self):
        if self.scheme_list:
            for v1 in self.scheme_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SchemeList'] = []
        if self.scheme_list is not None:
            for k1 in self.scheme_list:
                result['SchemeList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.scheme_list = []
        if m.get('SchemeList') is not None:
            for k1 in m.get('SchemeList'):
                temp_model = main_models.ListSchemeTaskConfigResponseBodyDataDataSchemeListSchemeList()
                self.scheme_list.append(temp_model.from_map(k1))

        return self

class ListSchemeTaskConfigResponseBodyDataDataSchemeListSchemeList(DaraModel):
    def __init__(
        self,
        name: str = None,
        scheme_id: int = None,
    ):
        self.name = name
        self.scheme_id = scheme_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.name is not None:
            result['Name'] = self.name

        if self.scheme_id is not None:
            result['SchemeId'] = self.scheme_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('SchemeId') is not None:
            self.scheme_id = m.get('SchemeId')

        return self

class ListSchemeTaskConfigResponseBodyDataDataSchemeIdList(DaraModel):
    def __init__(
        self,
        scheme_id_list: List[int] = None,
    ):
        self.scheme_id_list = scheme_id_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scheme_id_list is not None:
            result['SchemeIdList'] = self.scheme_id_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('SchemeIdList') is not None:
            self.scheme_id_list = m.get('SchemeIdList')

        return self

class ListSchemeTaskConfigResponseBodyDataDataDataConfig(DaraModel):
    def __init__(
        self,
        assign_configs: main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigs = None,
        data_sets: str = None,
        index: int = None,
        result_param: str = None,
    ):
        self.assign_configs = assign_configs
        self.data_sets = data_sets
        self.index = index
        self.result_param = result_param

    def validate(self):
        if self.assign_configs:
            self.assign_configs.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assign_configs is not None:
            result['AssignConfigs'] = self.assign_configs.to_map()

        if self.data_sets is not None:
            result['DataSets'] = self.data_sets

        if self.index is not None:
            result['Index'] = self.index

        if self.result_param is not None:
            result['ResultParam'] = self.result_param

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignConfigs') is not None:
            temp_model = main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigs()
            self.assign_configs = temp_model.from_map(m.get('AssignConfigs'))

        if m.get('DataSets') is not None:
            self.data_sets = m.get('DataSets')

        if m.get('Index') is not None:
            self.index = m.get('Index')

        if m.get('ResultParam') is not None:
            self.result_param = m.get('ResultParam')

        return self

class ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigs(DaraModel):
    def __init__(
        self,
        assign_config: List[main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfig] = None,
    ):
        self.assign_config = assign_config

    def validate(self):
        if self.assign_config:
            for v1 in self.assign_config:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssignConfig'] = []
        if self.assign_config is not None:
            for k1 in self.assign_config:
                result['AssignConfig'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assign_config = []
        if m.get('AssignConfig') is not None:
            for k1 in m.get('AssignConfig'):
                temp_model = main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfig()
                self.assign_config.append(temp_model.from_map(k1))

        return self

class ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfig(DaraModel):
    def __init__(
        self,
        assign_config_contests: main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContests = None,
    ):
        self.assign_config_contests = assign_config_contests

    def validate(self):
        if self.assign_config_contests:
            self.assign_config_contests.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.assign_config_contests is not None:
            result['AssignConfigContests'] = self.assign_config_contests.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AssignConfigContests') is not None:
            temp_model = main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContests()
            self.assign_config_contests = temp_model.from_map(m.get('AssignConfigContests'))

        return self

class ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContests(DaraModel):
    def __init__(
        self,
        assign_config_contest: List[main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContest] = None,
    ):
        self.assign_config_contest = assign_config_contest

    def validate(self):
        if self.assign_config_contest:
            for v1 in self.assign_config_contest:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['AssignConfigContest'] = []
        if self.assign_config_contest is not None:
            for k1 in self.assign_config_contest:
                result['AssignConfigContest'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.assign_config_contest = []
        if m.get('AssignConfigContest') is not None:
            for k1 in m.get('AssignConfigContest'):
                temp_model = main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContest()
                self.assign_config_contest.append(temp_model.from_map(k1))

        return self

class ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContest(DaraModel):
    def __init__(
        self,
        data_type: int = None,
        list_object: main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContestListObject = None,
        name: str = None,
        symbol: int = None,
        value: str = None,
    ):
        self.data_type = data_type
        self.list_object = list_object
        self.name = name
        self.symbol = symbol
        self.value = value

    def validate(self):
        if self.list_object:
            self.list_object.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.data_type is not None:
            result['DataType'] = self.data_type

        if self.list_object is not None:
            result['ListObject'] = self.list_object.to_map()

        if self.name is not None:
            result['Name'] = self.name

        if self.symbol is not None:
            result['Symbol'] = self.symbol

        if self.value is not None:
            result['Value'] = self.value

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DataType') is not None:
            self.data_type = m.get('DataType')

        if m.get('ListObject') is not None:
            temp_model = main_models.ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContestListObject()
            self.list_object = temp_model.from_map(m.get('ListObject'))

        if m.get('Name') is not None:
            self.name = m.get('Name')

        if m.get('Symbol') is not None:
            self.symbol = m.get('Symbol')

        if m.get('Value') is not None:
            self.value = m.get('Value')

        return self

class ListSchemeTaskConfigResponseBodyDataDataDataConfigAssignConfigsAssignConfigAssignConfigContestsAssignConfigContestListObject(DaraModel):
    def __init__(
        self,
        list_object: List[Any] = None,
    ):
        self.list_object = list_object

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.list_object is not None:
            result['ListObject'] = self.list_object

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ListObject') is not None:
            self.list_object = m.get('ListObject')

        return self


# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class ListSearchTaskDialoguesResponseBody(DaraModel):
    def __init__(
        self,
        code: str = None,
        data: List[main_models.ListSearchTaskDialoguesResponseBodyData] = None,
        http_status_code: int = None,
        message: str = None,
        page_number: int = None,
        page_size: int = None,
        request_id: str = None,
        success: bool = None,
        total_count: int = None,
    ):
        self.code = code
        self.data = data
        self.http_status_code = http_status_code
        self.message = message
        self.page_number = page_number
        self.page_size = page_size
        self.request_id = request_id
        self.success = success
        self.total_count = total_count

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
        if self.code is not None:
            result['Code'] = self.code

        result['Data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['Data'].append(k1.to_map() if k1 else None)

        if self.http_status_code is not None:
            result['HttpStatusCode'] = self.http_status_code

        if self.message is not None:
            result['Message'] = self.message

        if self.page_number is not None:
            result['PageNumber'] = self.page_number

        if self.page_size is not None:
            result['PageSize'] = self.page_size

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        if self.success is not None:
            result['Success'] = self.success

        if self.total_count is not None:
            result['TotalCount'] = self.total_count

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        self.data = []
        if m.get('Data') is not None:
            for k1 in m.get('Data'):
                temp_model = main_models.ListSearchTaskDialoguesResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('HttpStatusCode') is not None:
            self.http_status_code = m.get('HttpStatusCode')

        if m.get('Message') is not None:
            self.message = m.get('Message')

        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')

        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        if m.get('Success') is not None:
            self.success = m.get('Success')

        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')

        return self

class ListSearchTaskDialoguesResponseBodyData(DaraModel):
    def __init__(
        self,
        chat_config: main_models.ListSearchTaskDialoguesResponseBodyDataChatConfig = None,
        create_time: str = None,
        dialogue_type: int = None,
        good_text: str = None,
        origin_session_id: str = None,
        prompt: str = None,
        rating: str = None,
        response_body_str: str = None,
        session_id: str = None,
        tags: List[str] = None,
        task_id: str = None,
        text: str = None,
    ):
        self.chat_config = chat_config
        self.create_time = create_time
        self.dialogue_type = dialogue_type
        self.good_text = good_text
        self.origin_session_id = origin_session_id
        self.prompt = prompt
        self.rating = rating
        self.response_body_str = response_body_str
        self.session_id = session_id
        self.tags = tags
        self.task_id = task_id
        self.text = text

    def validate(self):
        if self.chat_config:
            self.chat_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chat_config is not None:
            result['ChatConfig'] = self.chat_config.to_map()

        if self.create_time is not None:
            result['CreateTime'] = self.create_time

        if self.dialogue_type is not None:
            result['DialogueType'] = self.dialogue_type

        if self.good_text is not None:
            result['GoodText'] = self.good_text

        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.rating is not None:
            result['Rating'] = self.rating

        if self.response_body_str is not None:
            result['ResponseBodyStr'] = self.response_body_str

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.tags is not None:
            result['Tags'] = self.tags

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.text is not None:
            result['Text'] = self.text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ChatConfig') is not None:
            temp_model = main_models.ListSearchTaskDialoguesResponseBodyDataChatConfig()
            self.chat_config = temp_model.from_map(m.get('ChatConfig'))

        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')

        if m.get('DialogueType') is not None:
            self.dialogue_type = m.get('DialogueType')

        if m.get('GoodText') is not None:
            self.good_text = m.get('GoodText')

        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('Rating') is not None:
            self.rating = m.get('Rating')

        if m.get('ResponseBodyStr') is not None:
            self.response_body_str = m.get('ResponseBodyStr')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('Tags') is not None:
            self.tags = m.get('Tags')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        return self

class ListSearchTaskDialoguesResponseBodyDataChatConfig(DaraModel):
    def __init__(
        self,
        dialogue_type: int = None,
        end_to_end: bool = None,
        generate_level: str = None,
        generate_technology: str = None,
        search_models: List[str] = None,
        search_param: main_models.ListSearchTaskDialoguesResponseBodyDataChatConfigSearchParam = None,
    ):
        self.dialogue_type = dialogue_type
        self.end_to_end = end_to_end
        self.generate_level = generate_level
        self.generate_technology = generate_technology
        self.search_models = search_models
        self.search_param = search_param

    def validate(self):
        if self.search_param:
            self.search_param.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.dialogue_type is not None:
            result['DialogueType'] = self.dialogue_type

        if self.end_to_end is not None:
            result['EndToEnd'] = self.end_to_end

        if self.generate_level is not None:
            result['GenerateLevel'] = self.generate_level

        if self.generate_technology is not None:
            result['GenerateTechnology'] = self.generate_technology

        if self.search_models is not None:
            result['SearchModels'] = self.search_models

        if self.search_param is not None:
            result['SearchParam'] = self.search_param.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DialogueType') is not None:
            self.dialogue_type = m.get('DialogueType')

        if m.get('EndToEnd') is not None:
            self.end_to_end = m.get('EndToEnd')

        if m.get('GenerateLevel') is not None:
            self.generate_level = m.get('GenerateLevel')

        if m.get('GenerateTechnology') is not None:
            self.generate_technology = m.get('GenerateTechnology')

        if m.get('SearchModels') is not None:
            self.search_models = m.get('SearchModels')

        if m.get('SearchParam') is not None:
            temp_model = main_models.ListSearchTaskDialoguesResponseBodyDataChatConfigSearchParam()
            self.search_param = temp_model.from_map(m.get('SearchParam'))

        return self

class ListSearchTaskDialoguesResponseBodyDataChatConfigSearchParam(DaraModel):
    def __init__(
        self,
        end_time: str = None,
        multimodal_search_types: List[str] = None,
        search_sources: List[main_models.ListSearchTaskDialoguesResponseBodyDataChatConfigSearchParamSearchSources] = None,
        start_time: str = None,
    ):
        self.end_time = end_time
        self.multimodal_search_types = multimodal_search_types
        self.search_sources = search_sources
        self.start_time = start_time

    def validate(self):
        if self.search_sources:
            for v1 in self.search_sources:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end_time is not None:
            result['EndTime'] = self.end_time

        if self.multimodal_search_types is not None:
            result['MultimodalSearchTypes'] = self.multimodal_search_types

        result['SearchSources'] = []
        if self.search_sources is not None:
            for k1 in self.search_sources:
                result['SearchSources'].append(k1.to_map() if k1 else None)

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MultimodalSearchTypes') is not None:
            self.multimodal_search_types = m.get('MultimodalSearchTypes')

        self.search_sources = []
        if m.get('SearchSources') is not None:
            for k1 in m.get('SearchSources'):
                temp_model = main_models.ListSearchTaskDialoguesResponseBodyDataChatConfigSearchParamSearchSources()
                self.search_sources.append(temp_model.from_map(k1))

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class ListSearchTaskDialoguesResponseBodyDataChatConfigSearchParamSearchSources(DaraModel):
    def __init__(
        self,
        code: str = None,
        dataset_name: str = None,
        name: str = None,
    ):
        self.code = code
        self.dataset_name = dataset_name
        self.name = name

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.code is not None:
            result['Code'] = self.code

        if self.dataset_name is not None:
            result['DatasetName'] = self.dataset_name

        if self.name is not None:
            result['Name'] = self.name

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        if m.get('Name') is not None:
            self.name = m.get('Name')

        return self


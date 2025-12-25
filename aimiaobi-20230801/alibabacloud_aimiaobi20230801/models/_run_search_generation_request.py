# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunSearchGenerationRequest(DaraModel):
    def __init__(
        self,
        agent_context: main_models.RunSearchGenerationRequestAgentContext = None,
        chat_config: main_models.RunSearchGenerationRequestChatConfig = None,
        file_url: str = None,
        model_id: str = None,
        original_session_id: str = None,
        prompt: str = None,
        task_id: str = None,
        workspace_id: str = None,
    ):
        self.agent_context = agent_context
        self.chat_config = chat_config
        self.file_url = file_url
        self.model_id = model_id
        self.original_session_id = original_session_id
        self.prompt = prompt
        self.task_id = task_id
        # This parameter is required.
        self.workspace_id = workspace_id

    def validate(self):
        if self.agent_context:
            self.agent_context.validate()
        if self.chat_config:
            self.chat_config.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_context is not None:
            result['AgentContext'] = self.agent_context.to_map()

        if self.chat_config is not None:
            result['ChatConfig'] = self.chat_config.to_map()

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.original_session_id is not None:
            result['OriginalSessionId'] = self.original_session_id

        if self.prompt is not None:
            result['Prompt'] = self.prompt

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.workspace_id is not None:
            result['WorkspaceId'] = self.workspace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentContext') is not None:
            temp_model = main_models.RunSearchGenerationRequestAgentContext()
            self.agent_context = temp_model.from_map(m.get('AgentContext'))

        if m.get('ChatConfig') is not None:
            temp_model = main_models.RunSearchGenerationRequestChatConfig()
            self.chat_config = temp_model.from_map(m.get('ChatConfig'))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('OriginalSessionId') is not None:
            self.original_session_id = m.get('OriginalSessionId')

        if m.get('Prompt') is not None:
            self.prompt = m.get('Prompt')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('WorkspaceId') is not None:
            self.workspace_id = m.get('WorkspaceId')

        return self

class RunSearchGenerationRequestChatConfig(DaraModel):
    def __init__(
        self,
        enable_thinking: bool = None,
        exclude_generate_options: List[str] = None,
        generate_level: str = None,
        generate_technology: str = None,
        model_custom_prompt_template: str = None,
        model_custom_vl_prompt_template: str = None,
        search_models: List[str] = None,
        search_param: main_models.RunSearchGenerationRequestChatConfigSearchParam = None,
    ):
        self.enable_thinking = enable_thinking
        self.exclude_generate_options = exclude_generate_options
        self.generate_level = generate_level
        self.generate_technology = generate_technology
        self.model_custom_prompt_template = model_custom_prompt_template
        self.model_custom_vl_prompt_template = model_custom_vl_prompt_template
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
        if self.enable_thinking is not None:
            result['EnableThinking'] = self.enable_thinking

        if self.exclude_generate_options is not None:
            result['ExcludeGenerateOptions'] = self.exclude_generate_options

        if self.generate_level is not None:
            result['GenerateLevel'] = self.generate_level

        if self.generate_technology is not None:
            result['GenerateTechnology'] = self.generate_technology

        if self.model_custom_prompt_template is not None:
            result['ModelCustomPromptTemplate'] = self.model_custom_prompt_template

        if self.model_custom_vl_prompt_template is not None:
            result['ModelCustomVlPromptTemplate'] = self.model_custom_vl_prompt_template

        if self.search_models is not None:
            result['SearchModels'] = self.search_models

        if self.search_param is not None:
            result['SearchParam'] = self.search_param.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EnableThinking') is not None:
            self.enable_thinking = m.get('EnableThinking')

        if m.get('ExcludeGenerateOptions') is not None:
            self.exclude_generate_options = m.get('ExcludeGenerateOptions')

        if m.get('GenerateLevel') is not None:
            self.generate_level = m.get('GenerateLevel')

        if m.get('GenerateTechnology') is not None:
            self.generate_technology = m.get('GenerateTechnology')

        if m.get('ModelCustomPromptTemplate') is not None:
            self.model_custom_prompt_template = m.get('ModelCustomPromptTemplate')

        if m.get('ModelCustomVlPromptTemplate') is not None:
            self.model_custom_vl_prompt_template = m.get('ModelCustomVlPromptTemplate')

        if m.get('SearchModels') is not None:
            self.search_models = m.get('SearchModels')

        if m.get('SearchParam') is not None:
            temp_model = main_models.RunSearchGenerationRequestChatConfigSearchParam()
            self.search_param = temp_model.from_map(m.get('SearchParam'))

        return self

class RunSearchGenerationRequestChatConfigSearchParam(DaraModel):
    def __init__(
        self,
        end_time: int = None,
        multimodal_search_types: List[str] = None,
        search_audio_min_score: float = None,
        search_image_min_score: float = None,
        search_sources: List[main_models.RunSearchGenerationRequestChatConfigSearchParamSearchSources] = None,
        search_text_min_score: float = None,
        search_video_min_score: float = None,
        start_time: int = None,
    ):
        self.end_time = end_time
        self.multimodal_search_types = multimodal_search_types
        self.search_audio_min_score = search_audio_min_score
        self.search_image_min_score = search_image_min_score
        self.search_sources = search_sources
        self.search_text_min_score = search_text_min_score
        self.search_video_min_score = search_video_min_score
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

        if self.search_audio_min_score is not None:
            result['SearchAudioMinScore'] = self.search_audio_min_score

        if self.search_image_min_score is not None:
            result['SearchImageMinScore'] = self.search_image_min_score

        result['SearchSources'] = []
        if self.search_sources is not None:
            for k1 in self.search_sources:
                result['SearchSources'].append(k1.to_map() if k1 else None)

        if self.search_text_min_score is not None:
            result['SearchTextMinScore'] = self.search_text_min_score

        if self.search_video_min_score is not None:
            result['SearchVideoMinScore'] = self.search_video_min_score

        if self.start_time is not None:
            result['StartTime'] = self.start_time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('EndTime') is not None:
            self.end_time = m.get('EndTime')

        if m.get('MultimodalSearchTypes') is not None:
            self.multimodal_search_types = m.get('MultimodalSearchTypes')

        if m.get('SearchAudioMinScore') is not None:
            self.search_audio_min_score = m.get('SearchAudioMinScore')

        if m.get('SearchImageMinScore') is not None:
            self.search_image_min_score = m.get('SearchImageMinScore')

        self.search_sources = []
        if m.get('SearchSources') is not None:
            for k1 in m.get('SearchSources'):
                temp_model = main_models.RunSearchGenerationRequestChatConfigSearchParamSearchSources()
                self.search_sources.append(temp_model.from_map(k1))

        if m.get('SearchTextMinScore') is not None:
            self.search_text_min_score = m.get('SearchTextMinScore')

        if m.get('SearchVideoMinScore') is not None:
            self.search_video_min_score = m.get('SearchVideoMinScore')

        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')

        return self

class RunSearchGenerationRequestChatConfigSearchParamSearchSources(DaraModel):
    def __init__(
        self,
        code: str = None,
        dataset_name: str = None,
    ):
        self.code = code
        self.dataset_name = dataset_name

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

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')

        if m.get('DatasetName') is not None:
            self.dataset_name = m.get('DatasetName')

        return self

class RunSearchGenerationRequestAgentContext(DaraModel):
    def __init__(
        self,
        biz_context: main_models.RunSearchGenerationRequestAgentContextBizContext = None,
    ):
        self.biz_context = biz_context

    def validate(self):
        if self.biz_context:
            self.biz_context.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.biz_context is not None:
            result['BizContext'] = self.biz_context.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('BizContext') is not None:
            temp_model = main_models.RunSearchGenerationRequestAgentContextBizContext()
            self.biz_context = temp_model.from_map(m.get('BizContext'))

        return self

class RunSearchGenerationRequestAgentContextBizContext(DaraModel):
    def __init__(
        self,
        ask_user: str = None,
        ask_user_keywords: List[str] = None,
        current_step: str = None,
        multimodal_media_selection: main_models.RunSearchGenerationRequestAgentContextBizContextMultimodalMediaSelection = None,
        next_step: str = None,
        skip_current_supplement: bool = None,
        supplement_data_type: str = None,
        supplement_enable: bool = None,
        user_back: str = None,
        user_back_keywords: List[str] = None,
    ):
        self.ask_user = ask_user
        self.ask_user_keywords = ask_user_keywords
        self.current_step = current_step
        self.multimodal_media_selection = multimodal_media_selection
        self.next_step = next_step
        self.skip_current_supplement = skip_current_supplement
        self.supplement_data_type = supplement_data_type
        self.supplement_enable = supplement_enable
        self.user_back = user_back
        self.user_back_keywords = user_back_keywords

    def validate(self):
        if self.multimodal_media_selection:
            self.multimodal_media_selection.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.ask_user is not None:
            result['AskUser'] = self.ask_user

        if self.ask_user_keywords is not None:
            result['AskUserKeywords'] = self.ask_user_keywords

        if self.current_step is not None:
            result['CurrentStep'] = self.current_step

        if self.multimodal_media_selection is not None:
            result['MultimodalMediaSelection'] = self.multimodal_media_selection.to_map()

        if self.next_step is not None:
            result['NextStep'] = self.next_step

        if self.skip_current_supplement is not None:
            result['SkipCurrentSupplement'] = self.skip_current_supplement

        if self.supplement_data_type is not None:
            result['SupplementDataType'] = self.supplement_data_type

        if self.supplement_enable is not None:
            result['SupplementEnable'] = self.supplement_enable

        if self.user_back is not None:
            result['UserBack'] = self.user_back

        if self.user_back_keywords is not None:
            result['UserBackKeywords'] = self.user_back_keywords

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AskUser') is not None:
            self.ask_user = m.get('AskUser')

        if m.get('AskUserKeywords') is not None:
            self.ask_user_keywords = m.get('AskUserKeywords')

        if m.get('CurrentStep') is not None:
            self.current_step = m.get('CurrentStep')

        if m.get('MultimodalMediaSelection') is not None:
            temp_model = main_models.RunSearchGenerationRequestAgentContextBizContextMultimodalMediaSelection()
            self.multimodal_media_selection = temp_model.from_map(m.get('MultimodalMediaSelection'))

        if m.get('NextStep') is not None:
            self.next_step = m.get('NextStep')

        if m.get('SkipCurrentSupplement') is not None:
            self.skip_current_supplement = m.get('SkipCurrentSupplement')

        if m.get('SupplementDataType') is not None:
            self.supplement_data_type = m.get('SupplementDataType')

        if m.get('SupplementEnable') is not None:
            self.supplement_enable = m.get('SupplementEnable')

        if m.get('UserBack') is not None:
            self.user_back = m.get('UserBack')

        if m.get('UserBackKeywords') is not None:
            self.user_back_keywords = m.get('UserBackKeywords')

        return self

class RunSearchGenerationRequestAgentContextBizContextMultimodalMediaSelection(DaraModel):
    def __init__(
        self,
        original_session_id: str = None,
        search_model: str = None,
        search_model_data_value: str = None,
        selection_type: str = None,
        session_id: str = None,
        text_search_result: main_models.RunSearchGenerationRequestAgentContextBizContextMultimodalMediaSelectionTextSearchResult = None,
    ):
        self.original_session_id = original_session_id
        self.search_model = search_model
        self.search_model_data_value = search_model_data_value
        self.selection_type = selection_type
        self.session_id = session_id
        self.text_search_result = text_search_result

    def validate(self):
        if self.text_search_result:
            self.text_search_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.original_session_id is not None:
            result['OriginalSessionId'] = self.original_session_id

        if self.search_model is not None:
            result['SearchModel'] = self.search_model

        if self.search_model_data_value is not None:
            result['SearchModelDataValue'] = self.search_model_data_value

        if self.selection_type is not None:
            result['SelectionType'] = self.selection_type

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.text_search_result is not None:
            result['TextSearchResult'] = self.text_search_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('OriginalSessionId') is not None:
            self.original_session_id = m.get('OriginalSessionId')

        if m.get('SearchModel') is not None:
            self.search_model = m.get('SearchModel')

        if m.get('SearchModelDataValue') is not None:
            self.search_model_data_value = m.get('SearchModelDataValue')

        if m.get('SelectionType') is not None:
            self.selection_type = m.get('SelectionType')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TextSearchResult') is not None:
            temp_model = main_models.RunSearchGenerationRequestAgentContextBizContextMultimodalMediaSelectionTextSearchResult()
            self.text_search_result = temp_model.from_map(m.get('TextSearchResult'))

        return self

class RunSearchGenerationRequestAgentContextBizContextMultimodalMediaSelectionTextSearchResult(DaraModel):
    def __init__(
        self,
        search_result: List[main_models.RunSearchGenerationRequestAgentContextBizContextMultimodalMediaSelectionTextSearchResultSearchResult] = None,
    ):
        self.search_result = search_result

    def validate(self):
        if self.search_result:
            for v1 in self.search_result:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['SearchResult'] = []
        if self.search_result is not None:
            for k1 in self.search_result:
                result['SearchResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_result = []
        if m.get('SearchResult') is not None:
            for k1 in m.get('SearchResult'):
                temp_model = main_models.RunSearchGenerationRequestAgentContextBizContextMultimodalMediaSelectionTextSearchResultSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        return self

class RunSearchGenerationRequestAgentContextBizContextMultimodalMediaSelectionTextSearchResultSearchResult(DaraModel):
    def __init__(
        self,
        chunks: List[str] = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        pub_time: str = None,
        score: float = None,
        search_source: str = None,
        search_source_name: str = None,
        search_source_type: str = None,
        source: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.chunks = chunks
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.pub_time = pub_time
        self.score = score
        self.search_source = search_source
        self.search_source_name = search_source_name
        self.search_source_type = search_source_type
        self.source = source
        self.summary = summary
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.chunks is not None:
            result['Chunks'] = self.chunks

        if self.content is not None:
            result['Content'] = self.content

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.score is not None:
            result['Score'] = self.score

        if self.search_source is not None:
            result['SearchSource'] = self.search_source

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.search_source_type is not None:
            result['SearchSourceType'] = self.search_source_type

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Chunks') is not None:
            self.chunks = m.get('Chunks')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('SearchSourceType') is not None:
            self.search_source_type = m.get('SearchSourceType')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self


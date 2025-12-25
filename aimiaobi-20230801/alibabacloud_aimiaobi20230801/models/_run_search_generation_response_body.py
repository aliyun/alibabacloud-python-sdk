# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aimiaobi20230801 import models as main_models
from darabonba.model import DaraModel

class RunSearchGenerationResponseBody(DaraModel):
    def __init__(
        self,
        header: main_models.RunSearchGenerationResponseBodyHeader = None,
        payload: main_models.RunSearchGenerationResponseBodyPayload = None,
        request_id: str = None,
    ):
        self.header = header
        self.payload = payload
        self.request_id = request_id

    def validate(self):
        if self.header:
            self.header.validate()
        if self.payload:
            self.payload.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.header is not None:
            result['Header'] = self.header.to_map()

        if self.payload is not None:
            result['Payload'] = self.payload.to_map()

        if self.request_id is not None:
            result['RequestId'] = self.request_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Header') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyHeader()
            self.header = temp_model.from_map(m.get('Header'))

        if m.get('Payload') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayload()
            self.payload = temp_model.from_map(m.get('Payload'))

        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')

        return self

class RunSearchGenerationResponseBodyPayload(DaraModel):
    def __init__(
        self,
        output: main_models.RunSearchGenerationResponseBodyPayloadOutput = None,
        usage: main_models.RunSearchGenerationResponseBodyPayloadUsage = None,
    ):
        self.output = output
        self.usage = usage

    def validate(self):
        if self.output:
            self.output.validate()
        if self.usage:
            self.usage.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.output is not None:
            result['Output'] = self.output.to_map()

        if self.usage is not None:
            result['Usage'] = self.usage.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Output') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutput()
            self.output = temp_model.from_map(m.get('Output'))

        if m.get('Usage') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadUsage()
            self.usage = temp_model.from_map(m.get('Usage'))

        return self

class RunSearchGenerationResponseBodyPayloadUsage(DaraModel):
    def __init__(
        self,
        input_tokens: int = None,
        output_tokens: int = None,
        total_tokens: int = None,
    ):
        self.input_tokens = input_tokens
        self.output_tokens = output_tokens
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.input_tokens is not None:
            result['InputTokens'] = self.input_tokens

        if self.output_tokens is not None:
            result['OutputTokens'] = self.output_tokens

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('InputTokens') is not None:
            self.input_tokens = m.get('InputTokens')

        if m.get('OutputTokens') is not None:
            self.output_tokens = m.get('OutputTokens')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class RunSearchGenerationResponseBodyPayloadOutput(DaraModel):
    def __init__(
        self,
        agent_context: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContext = None,
        messages: List[main_models.RunSearchGenerationResponseBodyPayloadOutputMessages] = None,
    ):
        self.agent_context = agent_context
        self.messages = messages

    def validate(self):
        if self.agent_context:
            self.agent_context.validate()
        if self.messages:
            for v1 in self.messages:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.agent_context is not None:
            result['AgentContext'] = self.agent_context.to_map()

        result['Messages'] = []
        if self.messages is not None:
            for k1 in self.messages:
                result['Messages'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AgentContext') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContext()
            self.agent_context = temp_model.from_map(m.get('AgentContext'))

        self.messages = []
        if m.get('Messages') is not None:
            for k1 in m.get('Messages'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputMessages()
                self.messages.append(temp_model.from_map(k1))

        return self

class RunSearchGenerationResponseBodyPayloadOutputMessages(DaraModel):
    def __init__(
        self,
        clarifications: bool = None,
        content: str = None,
        generate_finished: bool = None,
        id: str = None,
        node_code: str = None,
        search_queries: List[str] = None,
        search_query: str = None,
        search_result: List[main_models.RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResult] = None,
    ):
        self.clarifications = clarifications
        self.content = content
        self.generate_finished = generate_finished
        self.id = id
        self.node_code = node_code
        self.search_queries = search_queries
        self.search_query = search_query
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
        if self.clarifications is not None:
            result['Clarifications'] = self.clarifications

        if self.content is not None:
            result['Content'] = self.content

        if self.generate_finished is not None:
            result['GenerateFinished'] = self.generate_finished

        if self.id is not None:
            result['Id'] = self.id

        if self.node_code is not None:
            result['NodeCode'] = self.node_code

        if self.search_queries is not None:
            result['SearchQueries'] = self.search_queries

        if self.search_query is not None:
            result['SearchQuery'] = self.search_query

        result['SearchResult'] = []
        if self.search_result is not None:
            for k1 in self.search_result:
                result['SearchResult'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Clarifications') is not None:
            self.clarifications = m.get('Clarifications')

        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('GenerateFinished') is not None:
            self.generate_finished = m.get('GenerateFinished')

        if m.get('Id') is not None:
            self.id = m.get('Id')

        if m.get('NodeCode') is not None:
            self.node_code = m.get('NodeCode')

        if m.get('SearchQueries') is not None:
            self.search_queries = m.get('SearchQueries')

        if m.get('SearchQuery') is not None:
            self.search_query = m.get('SearchQuery')

        self.search_result = []
        if m.get('SearchResult') is not None:
            for k1 in m.get('SearchResult'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        return self

class RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResult(DaraModel):
    def __init__(
        self,
        audios: List[main_models.RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultAudios] = None,
        images: List[main_models.RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultImages] = None,
        multimodal_search_query: str = None,
        texts: List[main_models.RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultTexts] = None,
        videos: List[main_models.RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultVideos] = None,
    ):
        self.audios = audios
        self.images = images
        self.multimodal_search_query = multimodal_search_query
        self.texts = texts
        self.videos = videos

    def validate(self):
        if self.audios:
            for v1 in self.audios:
                 if v1:
                    v1.validate()
        if self.images:
            for v1 in self.images:
                 if v1:
                    v1.validate()
        if self.texts:
            for v1 in self.texts:
                 if v1:
                    v1.validate()
        if self.videos:
            for v1 in self.videos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Audios'] = []
        if self.audios is not None:
            for k1 in self.audios:
                result['Audios'].append(k1.to_map() if k1 else None)

        result['Images'] = []
        if self.images is not None:
            for k1 in self.images:
                result['Images'].append(k1.to_map() if k1 else None)

        if self.multimodal_search_query is not None:
            result['MultimodalSearchQuery'] = self.multimodal_search_query

        result['Texts'] = []
        if self.texts is not None:
            for k1 in self.texts:
                result['Texts'].append(k1.to_map() if k1 else None)

        result['Videos'] = []
        if self.videos is not None:
            for k1 in self.videos:
                result['Videos'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.audios = []
        if m.get('Audios') is not None:
            for k1 in m.get('Audios'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultAudios()
                self.audios.append(temp_model.from_map(k1))

        self.images = []
        if m.get('Images') is not None:
            for k1 in m.get('Images'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultImages()
                self.images.append(temp_model.from_map(k1))

        if m.get('MultimodalSearchQuery') is not None:
            self.multimodal_search_query = m.get('MultimodalSearchQuery')

        self.texts = []
        if m.get('Texts') is not None:
            for k1 in m.get('Texts'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultTexts()
                self.texts.append(temp_model.from_map(k1))

        self.videos = []
        if m.get('Videos') is not None:
            for k1 in m.get('Videos'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultVideos()
                self.videos.append(temp_model.from_map(k1))

        return self

class RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultVideos(DaraModel):
    def __init__(
        self,
        media_id: str = None,
    ):
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultTexts(DaraModel):
    def __init__(
        self,
        doc_uuid: str = None,
    ):
        self.doc_uuid = doc_uuid

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        return self

class RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultImages(DaraModel):
    def __init__(
        self,
        media_id: str = None,
    ):
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class RunSearchGenerationResponseBodyPayloadOutputMessagesSearchResultAudios(DaraModel):
    def __init__(
        self,
        media_id: str = None,
    ):
        self.media_id = media_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContext(DaraModel):
    def __init__(
        self,
        biz_context: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContext = None,
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
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContext()
            self.biz_context = temp_model.from_map(m.get('BizContext'))

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContext(DaraModel):
    def __init__(
        self,
        ask_user: str = None,
        ask_user_keywords: List[str] = None,
        current_step: str = None,
        generated_content: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContent = None,
        model_id: str = None,
        next_step: str = None,
        recommend_search_query_list: List[str] = None,
        search_keywords: List[str] = None,
        search_query_list: List[str] = None,
        supplement_data_type: str = None,
        supplement_enable: bool = None,
        token_calculate: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextTokenCalculate = None,
    ):
        self.ask_user = ask_user
        self.ask_user_keywords = ask_user_keywords
        self.current_step = current_step
        self.generated_content = generated_content
        self.model_id = model_id
        self.next_step = next_step
        self.recommend_search_query_list = recommend_search_query_list
        self.search_keywords = search_keywords
        self.search_query_list = search_query_list
        self.supplement_data_type = supplement_data_type
        self.supplement_enable = supplement_enable
        self.token_calculate = token_calculate

    def validate(self):
        if self.generated_content:
            self.generated_content.validate()
        if self.token_calculate:
            self.token_calculate.validate()

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

        if self.generated_content is not None:
            result['GeneratedContent'] = self.generated_content.to_map()

        if self.model_id is not None:
            result['ModelId'] = self.model_id

        if self.next_step is not None:
            result['NextStep'] = self.next_step

        if self.recommend_search_query_list is not None:
            result['RecommendSearchQueryList'] = self.recommend_search_query_list

        if self.search_keywords is not None:
            result['SearchKeywords'] = self.search_keywords

        if self.search_query_list is not None:
            result['SearchQueryList'] = self.search_query_list

        if self.supplement_data_type is not None:
            result['SupplementDataType'] = self.supplement_data_type

        if self.supplement_enable is not None:
            result['SupplementEnable'] = self.supplement_enable

        if self.token_calculate is not None:
            result['TokenCalculate'] = self.token_calculate.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AskUser') is not None:
            self.ask_user = m.get('AskUser')

        if m.get('AskUserKeywords') is not None:
            self.ask_user_keywords = m.get('AskUserKeywords')

        if m.get('CurrentStep') is not None:
            self.current_step = m.get('CurrentStep')

        if m.get('GeneratedContent') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContent()
            self.generated_content = temp_model.from_map(m.get('GeneratedContent'))

        if m.get('ModelId') is not None:
            self.model_id = m.get('ModelId')

        if m.get('NextStep') is not None:
            self.next_step = m.get('NextStep')

        if m.get('RecommendSearchQueryList') is not None:
            self.recommend_search_query_list = m.get('RecommendSearchQueryList')

        if m.get('SearchKeywords') is not None:
            self.search_keywords = m.get('SearchKeywords')

        if m.get('SearchQueryList') is not None:
            self.search_query_list = m.get('SearchQueryList')

        if m.get('SupplementDataType') is not None:
            self.supplement_data_type = m.get('SupplementDataType')

        if m.get('SupplementEnable') is not None:
            self.supplement_enable = m.get('SupplementEnable')

        if m.get('TokenCalculate') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextTokenCalculate()
            self.token_calculate = temp_model.from_map(m.get('TokenCalculate'))

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextTokenCalculate(DaraModel):
    def __init__(
        self,
        first_token_time: float = None,
        output_avg_time: float = None,
        search_time: float = None,
        time: float = None,
        total_tokens: int = None,
    ):
        self.first_token_time = first_token_time
        self.output_avg_time = output_avg_time
        self.search_time = search_time
        self.time = time
        self.total_tokens = total_tokens

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.first_token_time is not None:
            result['FirstTokenTime'] = self.first_token_time

        if self.output_avg_time is not None:
            result['OutputAvgTime'] = self.output_avg_time

        if self.search_time is not None:
            result['SearchTime'] = self.search_time

        if self.time is not None:
            result['Time'] = self.time

        if self.total_tokens is not None:
            result['TotalTokens'] = self.total_tokens

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FirstTokenTime') is not None:
            self.first_token_time = m.get('FirstTokenTime')

        if m.get('OutputAvgTime') is not None:
            self.output_avg_time = m.get('OutputAvgTime')

        if m.get('SearchTime') is not None:
            self.search_time = m.get('SearchTime')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        if m.get('TotalTokens') is not None:
            self.total_tokens = m.get('TotalTokens')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContent(DaraModel):
    def __init__(
        self,
        audio_search_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResult = None,
        cluster_topic_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResult = None,
        excerpt_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResult = None,
        image_search_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentImageSearchResult = None,
        news_element_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResult = None,
        text_generate_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResult = None,
        text_search_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextSearchResult = None,
        timeline_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResult = None,
        video_search_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResult = None,
    ):
        self.audio_search_result = audio_search_result
        self.cluster_topic_result = cluster_topic_result
        self.excerpt_result = excerpt_result
        self.image_search_result = image_search_result
        self.news_element_result = news_element_result
        self.text_generate_result = text_generate_result
        self.text_search_result = text_search_result
        self.timeline_result = timeline_result
        self.video_search_result = video_search_result

    def validate(self):
        if self.audio_search_result:
            self.audio_search_result.validate()
        if self.cluster_topic_result:
            self.cluster_topic_result.validate()
        if self.excerpt_result:
            self.excerpt_result.validate()
        if self.image_search_result:
            self.image_search_result.validate()
        if self.news_element_result:
            self.news_element_result.validate()
        if self.text_generate_result:
            self.text_generate_result.validate()
        if self.text_search_result:
            self.text_search_result.validate()
        if self.timeline_result:
            self.timeline_result.validate()
        if self.video_search_result:
            self.video_search_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_search_result is not None:
            result['AudioSearchResult'] = self.audio_search_result.to_map()

        if self.cluster_topic_result is not None:
            result['ClusterTopicResult'] = self.cluster_topic_result.to_map()

        if self.excerpt_result is not None:
            result['ExcerptResult'] = self.excerpt_result.to_map()

        if self.image_search_result is not None:
            result['ImageSearchResult'] = self.image_search_result.to_map()

        if self.news_element_result is not None:
            result['NewsElementResult'] = self.news_element_result.to_map()

        if self.text_generate_result is not None:
            result['TextGenerateResult'] = self.text_generate_result.to_map()

        if self.text_search_result is not None:
            result['TextSearchResult'] = self.text_search_result.to_map()

        if self.timeline_result is not None:
            result['TimelineResult'] = self.timeline_result.to_map()

        if self.video_search_result is not None:
            result['VideoSearchResult'] = self.video_search_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioSearchResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResult()
            self.audio_search_result = temp_model.from_map(m.get('AudioSearchResult'))

        if m.get('ClusterTopicResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResult()
            self.cluster_topic_result = temp_model.from_map(m.get('ClusterTopicResult'))

        if m.get('ExcerptResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResult()
            self.excerpt_result = temp_model.from_map(m.get('ExcerptResult'))

        if m.get('ImageSearchResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentImageSearchResult()
            self.image_search_result = temp_model.from_map(m.get('ImageSearchResult'))

        if m.get('NewsElementResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResult()
            self.news_element_result = temp_model.from_map(m.get('NewsElementResult'))

        if m.get('TextGenerateResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResult()
            self.text_generate_result = temp_model.from_map(m.get('TextGenerateResult'))

        if m.get('TextSearchResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextSearchResult()
            self.text_search_result = temp_model.from_map(m.get('TextSearchResult'))

        if m.get('TimelineResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResult()
            self.timeline_result = temp_model.from_map(m.get('TimelineResult'))

        if m.get('VideoSearchResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResult()
            self.video_search_result = temp_model.from_map(m.get('VideoSearchResult'))

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResult(DaraModel):
    def __init__(
        self,
        search_result: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResultSearchResult] = None,
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
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResultSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResultSearchResult(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResultSearchResultArticle = None,
        clip_infos: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResultSearchResultClipInfos] = None,
        file_url: str = None,
        media_id: str = None,
        traceability_id: str = None,
    ):
        self.article = article
        self.clip_infos = clip_infos
        self.file_url = file_url
        self.media_id = media_id
        self.traceability_id = traceability_id

    def validate(self):
        if self.article:
            self.article.validate()
        if self.clip_infos:
            for v1 in self.clip_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        result['ClipInfos'] = []
        if self.clip_infos is not None:
            for k1 in self.clip_infos:
                result['ClipInfos'].append(k1.to_map() if k1 else None)

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.traceability_id is not None:
            result['TraceabilityId'] = self.traceability_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResultSearchResultArticle()
            self.article = temp_model.from_map(m.get('Article'))

        self.clip_infos = []
        if m.get('ClipInfos') is not None:
            for k1 in m.get('ClipInfos'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResultSearchResultClipInfos()
                self.clip_infos.append(temp_model.from_map(k1))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('TraceabilityId') is not None:
            self.traceability_id = m.get('TraceabilityId')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResultSearchResultClipInfos(DaraModel):
    def __init__(
        self,
        from_: float = None,
        score: float = None,
        text: str = None,
        to: float = None,
        type: str = None,
    ):
        self.from_ = from_
        self.score = score
        self.text = text
        self.to = to
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.score is not None:
            result['Score'] = self.score

        if self.text is not None:
            result['Text'] = self.text

        if self.to is not None:
            result['To'] = self.to

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentVideoSearchResultSearchResultArticle(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        search_source_name: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.search_source_name = search_source_name
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
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResult(DaraModel):
    def __init__(
        self,
        generate_finished: bool = None,
        generate_traceability: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceability = None,
        multimodal_search_result_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultList] = None,
        reason_text_generate: str = None,
        reference_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultReferenceList] = None,
        text_generate: str = None,
        text_generate_multimodal_media_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultTextGenerateMultimodalMediaList] = None,
    ):
        self.generate_finished = generate_finished
        self.generate_traceability = generate_traceability
        self.multimodal_search_result_list = multimodal_search_result_list
        self.reason_text_generate = reason_text_generate
        self.reference_list = reference_list
        self.text_generate = text_generate
        self.text_generate_multimodal_media_list = text_generate_multimodal_media_list

    def validate(self):
        if self.generate_traceability:
            self.generate_traceability.validate()
        if self.multimodal_search_result_list:
            for v1 in self.multimodal_search_result_list:
                 if v1:
                    v1.validate()
        if self.reference_list:
            for v1 in self.reference_list:
                 if v1:
                    v1.validate()
        if self.text_generate_multimodal_media_list:
            for v1 in self.text_generate_multimodal_media_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_finished is not None:
            result['GenerateFinished'] = self.generate_finished

        if self.generate_traceability is not None:
            result['GenerateTraceability'] = self.generate_traceability.to_map()

        result['MultimodalSearchResultList'] = []
        if self.multimodal_search_result_list is not None:
            for k1 in self.multimodal_search_result_list:
                result['MultimodalSearchResultList'].append(k1.to_map() if k1 else None)

        if self.reason_text_generate is not None:
            result['ReasonTextGenerate'] = self.reason_text_generate

        result['ReferenceList'] = []
        if self.reference_list is not None:
            for k1 in self.reference_list:
                result['ReferenceList'].append(k1.to_map() if k1 else None)

        if self.text_generate is not None:
            result['TextGenerate'] = self.text_generate

        result['TextGenerateMultimodalMediaList'] = []
        if self.text_generate_multimodal_media_list is not None:
            for k1 in self.text_generate_multimodal_media_list:
                result['TextGenerateMultimodalMediaList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GenerateFinished') is not None:
            self.generate_finished = m.get('GenerateFinished')

        if m.get('GenerateTraceability') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceability()
            self.generate_traceability = temp_model.from_map(m.get('GenerateTraceability'))

        self.multimodal_search_result_list = []
        if m.get('MultimodalSearchResultList') is not None:
            for k1 in m.get('MultimodalSearchResultList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultList()
                self.multimodal_search_result_list.append(temp_model.from_map(k1))

        if m.get('ReasonTextGenerate') is not None:
            self.reason_text_generate = m.get('ReasonTextGenerate')

        self.reference_list = []
        if m.get('ReferenceList') is not None:
            for k1 in m.get('ReferenceList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultReferenceList()
                self.reference_list.append(temp_model.from_map(k1))

        if m.get('TextGenerate') is not None:
            self.text_generate = m.get('TextGenerate')

        self.text_generate_multimodal_media_list = []
        if m.get('TextGenerateMultimodalMediaList') is not None:
            for k1 in m.get('TextGenerateMultimodalMediaList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultTextGenerateMultimodalMediaList()
                self.text_generate_multimodal_media_list.append(temp_model.from_map(k1))

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultTextGenerateMultimodalMediaList(DaraModel):
    def __init__(
        self,
        end: int = None,
        multimodal_media_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultTextGenerateMultimodalMediaListMultimodalMediaList] = None,
        start: int = None,
    ):
        self.end = end
        self.multimodal_media_list = multimodal_media_list
        self.start = start

    def validate(self):
        if self.multimodal_media_list:
            for v1 in self.multimodal_media_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        result['MultimodalMediaList'] = []
        if self.multimodal_media_list is not None:
            for k1 in self.multimodal_media_list:
                result['MultimodalMediaList'].append(k1.to_map() if k1 else None)

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        self.multimodal_media_list = []
        if m.get('MultimodalMediaList') is not None:
            for k1 in m.get('MultimodalMediaList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultTextGenerateMultimodalMediaListMultimodalMediaList()
                self.multimodal_media_list.append(temp_model.from_map(k1))

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultTextGenerateMultimodalMediaListMultimodalMediaList(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultTextGenerateMultimodalMediaListMultimodalMediaListArticle = None,
        file_url: str = None,
        media_id: str = None,
        media_type: str = None,
    ):
        self.article = article
        self.file_url = file_url
        self.media_id = media_id
        self.media_type = media_type

    def validate(self):
        if self.article:
            self.article.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultTextGenerateMultimodalMediaListMultimodalMediaListArticle()
            self.article = temp_model.from_map(m.get('Article'))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultTextGenerateMultimodalMediaListMultimodalMediaListArticle(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        search_source_name: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.search_source_name = search_source_name
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
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultReferenceList(DaraModel):
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
        select: bool = None,
        source: str = None,
        summary: str = None,
        title: str = None,
        traceability_id: int = None,
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
        self.select = select
        self.source = source
        self.summary = summary
        self.title = title
        self.traceability_id = traceability_id
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

        if self.select is not None:
            result['Select'] = self.select

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.traceability_id is not None:
            result['TraceabilityId'] = self.traceability_id

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

        if m.get('Select') is not None:
            self.select = m.get('Select')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TraceabilityId') is not None:
            self.traceability_id = m.get('TraceabilityId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultList(DaraModel):
    def __init__(
        self,
        search_result: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultListSearchResult] = None,
        timeline_date_str: str = None,
    ):
        self.search_result = search_result
        self.timeline_date_str = timeline_date_str

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

        if self.timeline_date_str is not None:
            result['TimelineDateStr'] = self.timeline_date_str

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.search_result = []
        if m.get('SearchResult') is not None:
            for k1 in m.get('SearchResult'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultListSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        if m.get('TimelineDateStr') is not None:
            self.timeline_date_str = m.get('TimelineDateStr')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultListSearchResult(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultListSearchResultArticle = None,
        clip_infos: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultListSearchResultClipInfos] = None,
        file_url: str = None,
        media_id: str = None,
        media_type: str = None,
    ):
        self.article = article
        self.clip_infos = clip_infos
        self.file_url = file_url
        self.media_id = media_id
        self.media_type = media_type

    def validate(self):
        if self.article:
            self.article.validate()
        if self.clip_infos:
            for v1 in self.clip_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        result['ClipInfos'] = []
        if self.clip_infos is not None:
            for k1 in self.clip_infos:
                result['ClipInfos'].append(k1.to_map() if k1 else None)

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultListSearchResultArticle()
            self.article = temp_model.from_map(m.get('Article'))

        self.clip_infos = []
        if m.get('ClipInfos') is not None:
            for k1 in m.get('ClipInfos'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultListSearchResultClipInfos()
                self.clip_infos.append(temp_model.from_map(k1))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultListSearchResultClipInfos(DaraModel):
    def __init__(
        self,
        from_: float = None,
        score: float = None,
        text: str = None,
        to: float = None,
        type: str = None,
    ):
        self.from_ = from_
        self.score = score
        self.text = text
        self.to = to
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.score is not None:
            result['Score'] = self.score

        if self.text is not None:
            result['Text'] = self.text

        if self.to is not None:
            result['To'] = self.to

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultMultimodalSearchResultListSearchResultArticle(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        search_source_name: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.search_source_name = search_source_name
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
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceability(DaraModel):
    def __init__(
        self,
        coordinates: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceabilityCoordinates] = None,
        duplicate: float = None,
    ):
        self.coordinates = coordinates
        self.duplicate = duplicate

    def validate(self):
        if self.coordinates:
            for v1 in self.coordinates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Coordinates'] = []
        if self.coordinates is not None:
            for k1 in self.coordinates:
                result['Coordinates'].append(k1.to_map() if k1 else None)

        if self.duplicate is not None:
            result['Duplicate'] = self.duplicate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.coordinates = []
        if m.get('Coordinates') is not None:
            for k1 in m.get('Coordinates'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceabilityCoordinates()
                self.coordinates.append(temp_model.from_map(k1))

        if m.get('Duplicate') is not None:
            self.duplicate = m.get('Duplicate')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceabilityCoordinates(DaraModel):
    def __init__(
        self,
        generate_coordinate: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceabilityCoordinatesGenerateCoordinate = None,
        news_coordinate: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceabilityCoordinatesNewsCoordinate = None,
    ):
        self.generate_coordinate = generate_coordinate
        self.news_coordinate = news_coordinate

    def validate(self):
        if self.generate_coordinate:
            self.generate_coordinate.validate()
        if self.news_coordinate:
            self.news_coordinate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_coordinate is not None:
            result['GenerateCoordinate'] = self.generate_coordinate.to_map()

        if self.news_coordinate is not None:
            result['NewsCoordinate'] = self.news_coordinate.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GenerateCoordinate') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceabilityCoordinatesGenerateCoordinate()
            self.generate_coordinate = temp_model.from_map(m.get('GenerateCoordinate'))

        if m.get('NewsCoordinate') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceabilityCoordinatesNewsCoordinate()
            self.news_coordinate = temp_model.from_map(m.get('NewsCoordinate'))

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceabilityCoordinatesNewsCoordinate(DaraModel):
    def __init__(
        self,
        media_type: str = None,
        x: int = None,
        y: int = None,
        z: int = None,
    ):
        self.media_type = media_type
        self.x = x
        self.y = y
        self.z = z

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.z is not None:
            result['Z'] = self.z

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('Z') is not None:
            self.z = m.get('Z')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTimelineResultGenerateTraceabilityCoordinatesGenerateCoordinate(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
        z: int = None,
    ):
        self.x = x
        self.y = y
        self.z = z

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.z is not None:
            result['Z'] = self.z

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('Z') is not None:
            self.z = m.get('Z')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextSearchResult(DaraModel):
    def __init__(
        self,
        current: int = None,
        search_result: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextSearchResultSearchResult] = None,
        size: int = None,
        total: int = None,
    ):
        self.current = current
        self.search_result = search_result
        self.size = size
        self.total = total

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
        if self.current is not None:
            result['Current'] = self.current

        result['SearchResult'] = []
        if self.search_result is not None:
            for k1 in self.search_result:
                result['SearchResult'].append(k1.to_map() if k1 else None)

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        self.search_result = []
        if m.get('SearchResult') is not None:
            for k1 in m.get('SearchResult'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextSearchResultSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextSearchResultSearchResult(DaraModel):
    def __init__(
        self,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        pub_time: str = None,
        search_source: str = None,
        search_source_name: str = None,
        search_source_type: str = None,
        summary: str = None,
        title: str = None,
        traceability_id: str = None,
        url: str = None,
    ):
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.pub_time = pub_time
        self.search_source = search_source
        self.search_source_name = search_source_name
        self.search_source_type = search_source_type
        self.summary = summary
        self.title = title
        self.traceability_id = traceability_id
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.content is not None:
            result['Content'] = self.content

        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.search_source is not None:
            result['SearchSource'] = self.search_source

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.search_source_type is not None:
            result['SearchSourceType'] = self.search_source_type

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.traceability_id is not None:
            result['TraceabilityId'] = self.traceability_id

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Content') is not None:
            self.content = m.get('Content')

        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('SearchSourceType') is not None:
            self.search_source_type = m.get('SearchSourceType')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TraceabilityId') is not None:
            self.traceability_id = m.get('TraceabilityId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResult(DaraModel):
    def __init__(
        self,
        generate_finished: bool = None,
        generate_level: str = None,
        generate_traceability: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceability = None,
        multimodal_search_result_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultList] = None,
        reason_text_generate: str = None,
        reference_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultReferenceList] = None,
        text_generate: str = None,
        text_generate_multimodal_media_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultTextGenerateMultimodalMediaList] = None,
    ):
        self.generate_finished = generate_finished
        self.generate_level = generate_level
        self.generate_traceability = generate_traceability
        self.multimodal_search_result_list = multimodal_search_result_list
        self.reason_text_generate = reason_text_generate
        self.reference_list = reference_list
        self.text_generate = text_generate
        self.text_generate_multimodal_media_list = text_generate_multimodal_media_list

    def validate(self):
        if self.generate_traceability:
            self.generate_traceability.validate()
        if self.multimodal_search_result_list:
            for v1 in self.multimodal_search_result_list:
                 if v1:
                    v1.validate()
        if self.reference_list:
            for v1 in self.reference_list:
                 if v1:
                    v1.validate()
        if self.text_generate_multimodal_media_list:
            for v1 in self.text_generate_multimodal_media_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_finished is not None:
            result['GenerateFinished'] = self.generate_finished

        if self.generate_level is not None:
            result['GenerateLevel'] = self.generate_level

        if self.generate_traceability is not None:
            result['GenerateTraceability'] = self.generate_traceability.to_map()

        result['MultimodalSearchResultList'] = []
        if self.multimodal_search_result_list is not None:
            for k1 in self.multimodal_search_result_list:
                result['MultimodalSearchResultList'].append(k1.to_map() if k1 else None)

        if self.reason_text_generate is not None:
            result['ReasonTextGenerate'] = self.reason_text_generate

        result['ReferenceList'] = []
        if self.reference_list is not None:
            for k1 in self.reference_list:
                result['ReferenceList'].append(k1.to_map() if k1 else None)

        if self.text_generate is not None:
            result['TextGenerate'] = self.text_generate

        result['TextGenerateMultimodalMediaList'] = []
        if self.text_generate_multimodal_media_list is not None:
            for k1 in self.text_generate_multimodal_media_list:
                result['TextGenerateMultimodalMediaList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GenerateFinished') is not None:
            self.generate_finished = m.get('GenerateFinished')

        if m.get('GenerateLevel') is not None:
            self.generate_level = m.get('GenerateLevel')

        if m.get('GenerateTraceability') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceability()
            self.generate_traceability = temp_model.from_map(m.get('GenerateTraceability'))

        self.multimodal_search_result_list = []
        if m.get('MultimodalSearchResultList') is not None:
            for k1 in m.get('MultimodalSearchResultList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultList()
                self.multimodal_search_result_list.append(temp_model.from_map(k1))

        if m.get('ReasonTextGenerate') is not None:
            self.reason_text_generate = m.get('ReasonTextGenerate')

        self.reference_list = []
        if m.get('ReferenceList') is not None:
            for k1 in m.get('ReferenceList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultReferenceList()
                self.reference_list.append(temp_model.from_map(k1))

        if m.get('TextGenerate') is not None:
            self.text_generate = m.get('TextGenerate')

        self.text_generate_multimodal_media_list = []
        if m.get('TextGenerateMultimodalMediaList') is not None:
            for k1 in m.get('TextGenerateMultimodalMediaList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultTextGenerateMultimodalMediaList()
                self.text_generate_multimodal_media_list.append(temp_model.from_map(k1))

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultTextGenerateMultimodalMediaList(DaraModel):
    def __init__(
        self,
        end: int = None,
        multimodal_media_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultTextGenerateMultimodalMediaListMultimodalMediaList] = None,
        start: int = None,
    ):
        self.end = end
        self.multimodal_media_list = multimodal_media_list
        self.start = start

    def validate(self):
        if self.multimodal_media_list:
            for v1 in self.multimodal_media_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.end is not None:
            result['End'] = self.end

        result['MultimodalMediaList'] = []
        if self.multimodal_media_list is not None:
            for k1 in self.multimodal_media_list:
                result['MultimodalMediaList'].append(k1.to_map() if k1 else None)

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('End') is not None:
            self.end = m.get('End')

        self.multimodal_media_list = []
        if m.get('MultimodalMediaList') is not None:
            for k1 in m.get('MultimodalMediaList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultTextGenerateMultimodalMediaListMultimodalMediaList()
                self.multimodal_media_list.append(temp_model.from_map(k1))

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultTextGenerateMultimodalMediaListMultimodalMediaList(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultTextGenerateMultimodalMediaListMultimodalMediaListArticle = None,
        file_url: str = None,
        media_id: str = None,
        media_type: str = None,
    ):
        self.article = article
        self.file_url = file_url
        self.media_id = media_id
        self.media_type = media_type

    def validate(self):
        if self.article:
            self.article.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultTextGenerateMultimodalMediaListMultimodalMediaListArticle()
            self.article = temp_model.from_map(m.get('Article'))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultTextGenerateMultimodalMediaListMultimodalMediaListArticle(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        search_source_name: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.search_source_name = search_source_name
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
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultReferenceList(DaraModel):
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
        select: bool = None,
        source: str = None,
        summary: str = None,
        title: str = None,
        traceability_id: int = None,
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
        self.select = select
        self.source = source
        self.summary = summary
        self.title = title
        self.traceability_id = traceability_id
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

        if self.select is not None:
            result['Select'] = self.select

        if self.source is not None:
            result['Source'] = self.source

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.traceability_id is not None:
            result['TraceabilityId'] = self.traceability_id

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

        if m.get('Select') is not None:
            self.select = m.get('Select')

        if m.get('Source') is not None:
            self.source = m.get('Source')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TraceabilityId') is not None:
            self.traceability_id = m.get('TraceabilityId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultList(DaraModel):
    def __init__(
        self,
        current: int = None,
        search_query: str = None,
        search_result: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultListSearchResult] = None,
        search_type: str = None,
        size: int = None,
        timeline_date_str: str = None,
        total: int = None,
    ):
        self.current = current
        self.search_query = search_query
        self.search_result = search_result
        self.search_type = search_type
        self.size = size
        self.timeline_date_str = timeline_date_str
        self.total = total

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
        if self.current is not None:
            result['Current'] = self.current

        if self.search_query is not None:
            result['SearchQuery'] = self.search_query

        result['SearchResult'] = []
        if self.search_result is not None:
            for k1 in self.search_result:
                result['SearchResult'].append(k1.to_map() if k1 else None)

        if self.search_type is not None:
            result['SearchType'] = self.search_type

        if self.size is not None:
            result['Size'] = self.size

        if self.timeline_date_str is not None:
            result['TimelineDateStr'] = self.timeline_date_str

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('SearchQuery') is not None:
            self.search_query = m.get('SearchQuery')

        self.search_result = []
        if m.get('SearchResult') is not None:
            for k1 in m.get('SearchResult'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultListSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        if m.get('SearchType') is not None:
            self.search_type = m.get('SearchType')

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('TimelineDateStr') is not None:
            self.timeline_date_str = m.get('TimelineDateStr')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultListSearchResult(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultListSearchResultArticle = None,
        clip_infos: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultListSearchResultClipInfos] = None,
        file_url: str = None,
        media_id: str = None,
        media_type: str = None,
    ):
        self.article = article
        self.clip_infos = clip_infos
        self.file_url = file_url
        self.media_id = media_id
        self.media_type = media_type

    def validate(self):
        if self.article:
            self.article.validate()
        if self.clip_infos:
            for v1 in self.clip_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        result['ClipInfos'] = []
        if self.clip_infos is not None:
            for k1 in self.clip_infos:
                result['ClipInfos'].append(k1.to_map() if k1 else None)

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultListSearchResultArticle()
            self.article = temp_model.from_map(m.get('Article'))

        self.clip_infos = []
        if m.get('ClipInfos') is not None:
            for k1 in m.get('ClipInfos'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultListSearchResultClipInfos()
                self.clip_infos.append(temp_model.from_map(k1))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultListSearchResultClipInfos(DaraModel):
    def __init__(
        self,
        from_: float = None,
        score: float = None,
        text: str = None,
        to: float = None,
        type: str = None,
    ):
        self.from_ = from_
        self.score = score
        self.text = text
        self.to = to
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.score is not None:
            result['Score'] = self.score

        if self.text is not None:
            result['Text'] = self.text

        if self.to is not None:
            result['To'] = self.to

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultMultimodalSearchResultListSearchResultArticle(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        search_source_name: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.search_source_name = search_source_name
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
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceability(DaraModel):
    def __init__(
        self,
        coordinates: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceabilityCoordinates] = None,
        duplicate: float = None,
    ):
        self.coordinates = coordinates
        self.duplicate = duplicate

    def validate(self):
        if self.coordinates:
            for v1 in self.coordinates:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['Coordinates'] = []
        if self.coordinates is not None:
            for k1 in self.coordinates:
                result['Coordinates'].append(k1.to_map() if k1 else None)

        if self.duplicate is not None:
            result['Duplicate'] = self.duplicate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.coordinates = []
        if m.get('Coordinates') is not None:
            for k1 in m.get('Coordinates'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceabilityCoordinates()
                self.coordinates.append(temp_model.from_map(k1))

        if m.get('Duplicate') is not None:
            self.duplicate = m.get('Duplicate')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceabilityCoordinates(DaraModel):
    def __init__(
        self,
        generate_coordinate: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceabilityCoordinatesGenerateCoordinate = None,
        news_coordinate: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceabilityCoordinatesNewsCoordinate = None,
    ):
        self.generate_coordinate = generate_coordinate
        self.news_coordinate = news_coordinate

    def validate(self):
        if self.generate_coordinate:
            self.generate_coordinate.validate()
        if self.news_coordinate:
            self.news_coordinate.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_coordinate is not None:
            result['GenerateCoordinate'] = self.generate_coordinate.to_map()

        if self.news_coordinate is not None:
            result['NewsCoordinate'] = self.news_coordinate.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GenerateCoordinate') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceabilityCoordinatesGenerateCoordinate()
            self.generate_coordinate = temp_model.from_map(m.get('GenerateCoordinate'))

        if m.get('NewsCoordinate') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceabilityCoordinatesNewsCoordinate()
            self.news_coordinate = temp_model.from_map(m.get('NewsCoordinate'))

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceabilityCoordinatesNewsCoordinate(DaraModel):
    def __init__(
        self,
        media_type: str = None,
        x: int = None,
        y: int = None,
        z: int = None,
    ):
        self.media_type = media_type
        self.x = x
        self.y = y
        self.z = z

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.media_type is not None:
            result['MediaType'] = self.media_type

        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.z is not None:
            result['Z'] = self.z

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('Z') is not None:
            self.z = m.get('Z')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentTextGenerateResultGenerateTraceabilityCoordinatesGenerateCoordinate(DaraModel):
    def __init__(
        self,
        x: int = None,
        y: int = None,
        z: int = None,
    ):
        self.x = x
        self.y = y
        self.z = z

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.x is not None:
            result['X'] = self.x

        if self.y is not None:
            result['Y'] = self.y

        if self.z is not None:
            result['Z'] = self.z

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('X') is not None:
            self.x = m.get('X')

        if m.get('Y') is not None:
            self.y = m.get('Y')

        if m.get('Z') is not None:
            self.z = m.get('Z')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResult(DaraModel):
    def __init__(
        self,
        generate_finished: bool = None,
        news_element_article_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleList] = None,
        text_generate: str = None,
    ):
        self.generate_finished = generate_finished
        self.news_element_article_list = news_element_article_list
        self.text_generate = text_generate

    def validate(self):
        if self.news_element_article_list:
            for v1 in self.news_element_article_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.generate_finished is not None:
            result['GenerateFinished'] = self.generate_finished

        result['NewsElementArticleList'] = []
        if self.news_element_article_list is not None:
            for k1 in self.news_element_article_list:
                result['NewsElementArticleList'].append(k1.to_map() if k1 else None)

        if self.text_generate is not None:
            result['TextGenerate'] = self.text_generate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GenerateFinished') is not None:
            self.generate_finished = m.get('GenerateFinished')

        self.news_element_article_list = []
        if m.get('NewsElementArticleList') is not None:
            for k1 in m.get('NewsElementArticleList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleList()
                self.news_element_article_list.append(temp_model.from_map(k1))

        if m.get('TextGenerate') is not None:
            self.text_generate = m.get('TextGenerate')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleList(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleListArticle = None,
        news_element_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleListNewsElementList] = None,
        text_generate: str = None,
    ):
        self.article = article
        self.news_element_list = news_element_list
        self.text_generate = text_generate

    def validate(self):
        if self.article:
            self.article.validate()
        if self.news_element_list:
            for v1 in self.news_element_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        result['NewsElementList'] = []
        if self.news_element_list is not None:
            for k1 in self.news_element_list:
                result['NewsElementList'].append(k1.to_map() if k1 else None)

        if self.text_generate is not None:
            result['TextGenerate'] = self.text_generate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleListArticle()
            self.article = temp_model.from_map(m.get('Article'))

        self.news_element_list = []
        if m.get('NewsElementList') is not None:
            for k1 in m.get('NewsElementList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleListNewsElementList()
                self.news_element_list.append(temp_model.from_map(k1))

        if m.get('TextGenerate') is not None:
            self.text_generate = m.get('TextGenerate')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleListNewsElementList(DaraModel):
    def __init__(
        self,
        event: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleListNewsElementListEvent = None,
        location: str = None,
        people: str = None,
        time: str = None,
    ):
        self.event = event
        self.location = location
        self.people = people
        self.time = time

    def validate(self):
        if self.event:
            self.event.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.event is not None:
            result['Event'] = self.event.to_map()

        if self.location is not None:
            result['Location'] = self.location

        if self.people is not None:
            result['People'] = self.people

        if self.time is not None:
            result['Time'] = self.time

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Event') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleListNewsElementListEvent()
            self.event = temp_model.from_map(m.get('Event'))

        if m.get('Location') is not None:
            self.location = m.get('Location')

        if m.get('People') is not None:
            self.people = m.get('People')

        if m.get('Time') is not None:
            self.time = m.get('Time')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleListNewsElementListEvent(DaraModel):
    def __init__(
        self,
        cause_list: List[str] = None,
        process_list: List[str] = None,
        result_list: List[str] = None,
    ):
        self.cause_list = cause_list
        self.process_list = process_list
        self.result_list = result_list

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.cause_list is not None:
            result['CauseList'] = self.cause_list

        if self.process_list is not None:
            result['ProcessList'] = self.process_list

        if self.result_list is not None:
            result['ResultList'] = self.result_list

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('CauseList') is not None:
            self.cause_list = m.get('CauseList')

        if m.get('ProcessList') is not None:
            self.process_list = m.get('ProcessList')

        if m.get('ResultList') is not None:
            self.result_list = m.get('ResultList')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentNewsElementResultNewsElementArticleListArticle(DaraModel):
    def __init__(
        self,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        pub_time: str = None,
        score: float = None,
        search_source: str = None,
        search_source_name: str = None,
        search_source_type: str = None,
        select: bool = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.pub_time = pub_time
        self.score = score
        self.search_source = search_source
        self.search_source_name = search_source_name
        self.search_source_type = search_source_type
        self.select = select
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

        if self.select is not None:
            result['Select'] = self.select

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
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

        if m.get('Select') is not None:
            self.select = m.get('Select')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentImageSearchResult(DaraModel):
    def __init__(
        self,
        search_result: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentImageSearchResultSearchResult] = None,
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
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentImageSearchResultSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentImageSearchResultSearchResult(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentImageSearchResultSearchResultArticle = None,
        file_url: str = None,
        media_id: str = None,
        traceability_id: str = None,
    ):
        self.article = article
        self.file_url = file_url
        self.media_id = media_id
        self.traceability_id = traceability_id

    def validate(self):
        if self.article:
            self.article.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.traceability_id is not None:
            result['TraceabilityId'] = self.traceability_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentImageSearchResultSearchResultArticle()
            self.article = temp_model.from_map(m.get('Article'))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('TraceabilityId') is not None:
            self.traceability_id = m.get('TraceabilityId')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentImageSearchResultSearchResultArticle(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        search_source_name: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.search_source_name = search_source_name
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
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResult(DaraModel):
    def __init__(
        self,
        generate_finished: bool = None,
        generate_level: str = None,
        reason_text_generate: str = None,
        search_result: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResult] = None,
        text_generate: str = None,
    ):
        self.generate_finished = generate_finished
        self.generate_level = generate_level
        self.reason_text_generate = reason_text_generate
        self.search_result = search_result
        self.text_generate = text_generate

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
        if self.generate_finished is not None:
            result['GenerateFinished'] = self.generate_finished

        if self.generate_level is not None:
            result['GenerateLevel'] = self.generate_level

        if self.reason_text_generate is not None:
            result['ReasonTextGenerate'] = self.reason_text_generate

        result['SearchResult'] = []
        if self.search_result is not None:
            for k1 in self.search_result:
                result['SearchResult'].append(k1.to_map() if k1 else None)

        if self.text_generate is not None:
            result['TextGenerate'] = self.text_generate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('GenerateFinished') is not None:
            self.generate_finished = m.get('GenerateFinished')

        if m.get('GenerateLevel') is not None:
            self.generate_level = m.get('GenerateLevel')

        if m.get('ReasonTextGenerate') is not None:
            self.reason_text_generate = m.get('ReasonTextGenerate')

        self.search_result = []
        if m.get('SearchResult') is not None:
            for k1 in m.get('SearchResult'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        if m.get('TextGenerate') is not None:
            self.text_generate = m.get('TextGenerate')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResult(DaraModel):
    def __init__(
        self,
        chunks: List[str] = None,
        content: str = None,
        doc_id: str = None,
        doc_uuid: str = None,
        excerpt: str = None,
        multimodal_medias: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultMultimodalMedias] = None,
        pub_time: str = None,
        score: float = None,
        search_source: str = None,
        search_source_name: str = None,
        search_source_type: str = None,
        select: bool = None,
        summary: str = None,
        text_generate_multimodal_media_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultTextGenerateMultimodalMediaList] = None,
        title: str = None,
        traceability_id: int = None,
        url: str = None,
    ):
        self.chunks = chunks
        self.content = content
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.excerpt = excerpt
        self.multimodal_medias = multimodal_medias
        self.pub_time = pub_time
        self.score = score
        self.search_source = search_source
        self.search_source_name = search_source_name
        self.search_source_type = search_source_type
        self.select = select
        self.summary = summary
        self.text_generate_multimodal_media_list = text_generate_multimodal_media_list
        self.title = title
        self.traceability_id = traceability_id
        self.url = url

    def validate(self):
        if self.multimodal_medias:
            for v1 in self.multimodal_medias:
                 if v1:
                    v1.validate()
        if self.text_generate_multimodal_media_list:
            for v1 in self.text_generate_multimodal_media_list:
                 if v1:
                    v1.validate()

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

        if self.excerpt is not None:
            result['Excerpt'] = self.excerpt

        result['MultimodalMedias'] = []
        if self.multimodal_medias is not None:
            for k1 in self.multimodal_medias:
                result['MultimodalMedias'].append(k1.to_map() if k1 else None)

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

        if self.select is not None:
            result['Select'] = self.select

        if self.summary is not None:
            result['Summary'] = self.summary

        result['TextGenerateMultimodalMediaList'] = []
        if self.text_generate_multimodal_media_list is not None:
            for k1 in self.text_generate_multimodal_media_list:
                result['TextGenerateMultimodalMediaList'].append(k1.to_map() if k1 else None)

        if self.title is not None:
            result['Title'] = self.title

        if self.traceability_id is not None:
            result['TraceabilityId'] = self.traceability_id

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

        if m.get('Excerpt') is not None:
            self.excerpt = m.get('Excerpt')

        self.multimodal_medias = []
        if m.get('MultimodalMedias') is not None:
            for k1 in m.get('MultimodalMedias'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultMultimodalMedias()
                self.multimodal_medias.append(temp_model.from_map(k1))

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

        if m.get('Select') is not None:
            self.select = m.get('Select')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        self.text_generate_multimodal_media_list = []
        if m.get('TextGenerateMultimodalMediaList') is not None:
            for k1 in m.get('TextGenerateMultimodalMediaList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultTextGenerateMultimodalMediaList()
                self.text_generate_multimodal_media_list.append(temp_model.from_map(k1))

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('TraceabilityId') is not None:
            self.traceability_id = m.get('TraceabilityId')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultTextGenerateMultimodalMediaList(DaraModel):
    def __init__(
        self,
        doc_uuid: str = None,
        end: int = None,
        multimodal_media_list: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultTextGenerateMultimodalMediaListMultimodalMediaList] = None,
        start: int = None,
    ):
        self.doc_uuid = doc_uuid
        self.end = end
        self.multimodal_media_list = multimodal_media_list
        self.start = start

    def validate(self):
        if self.multimodal_media_list:
            for v1 in self.multimodal_media_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.end is not None:
            result['End'] = self.end

        result['MultimodalMediaList'] = []
        if self.multimodal_media_list is not None:
            for k1 in self.multimodal_media_list:
                result['MultimodalMediaList'].append(k1.to_map() if k1 else None)

        if self.start is not None:
            result['Start'] = self.start

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('End') is not None:
            self.end = m.get('End')

        self.multimodal_media_list = []
        if m.get('MultimodalMediaList') is not None:
            for k1 in m.get('MultimodalMediaList'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultTextGenerateMultimodalMediaListMultimodalMediaList()
                self.multimodal_media_list.append(temp_model.from_map(k1))

        if m.get('Start') is not None:
            self.start = m.get('Start')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultTextGenerateMultimodalMediaListMultimodalMediaList(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultTextGenerateMultimodalMediaListMultimodalMediaListArticle = None,
        file_url: str = None,
        media_id: str = None,
        media_type: str = None,
    ):
        self.article = article
        self.file_url = file_url
        self.media_id = media_id
        self.media_type = media_type

    def validate(self):
        if self.article:
            self.article.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultTextGenerateMultimodalMediaListMultimodalMediaListArticle()
            self.article = temp_model.from_map(m.get('Article'))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultTextGenerateMultimodalMediaListMultimodalMediaListArticle(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        search_source_name: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.search_source_name = search_source_name
        self.title = title
        self.url = url

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentExcerptResultSearchResultMultimodalMedias(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_id: str = None,
        media_type: str = None,
    ):
        self.file_url = file_url
        self.media_id = media_id
        self.media_type = media_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResult(DaraModel):
    def __init__(
        self,
        cluster_topics: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopics] = None,
        generate_finished: bool = None,
        text_generate: str = None,
    ):
        self.cluster_topics = cluster_topics
        self.generate_finished = generate_finished
        self.text_generate = text_generate

    def validate(self):
        if self.cluster_topics:
            for v1 in self.cluster_topics:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        result['ClusterTopics'] = []
        if self.cluster_topics is not None:
            for k1 in self.cluster_topics:
                result['ClusterTopics'].append(k1.to_map() if k1 else None)

        if self.generate_finished is not None:
            result['GenerateFinished'] = self.generate_finished

        if self.text_generate is not None:
            result['TextGenerate'] = self.text_generate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.cluster_topics = []
        if m.get('ClusterTopics') is not None:
            for k1 in m.get('ClusterTopics'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopics()
                self.cluster_topics.append(temp_model.from_map(k1))

        if m.get('GenerateFinished') is not None:
            self.generate_finished = m.get('GenerateFinished')

        if m.get('TextGenerate') is not None:
            self.text_generate = m.get('TextGenerate')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopics(DaraModel):
    def __init__(
        self,
        audio_search_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResult = None,
        image_search_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsImageSearchResult = None,
        text_search_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsTextSearchResult = None,
        topic: str = None,
        video_search_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResult = None,
    ):
        self.audio_search_result = audio_search_result
        self.image_search_result = image_search_result
        self.text_search_result = text_search_result
        self.topic = topic
        self.video_search_result = video_search_result

    def validate(self):
        if self.audio_search_result:
            self.audio_search_result.validate()
        if self.image_search_result:
            self.image_search_result.validate()
        if self.text_search_result:
            self.text_search_result.validate()
        if self.video_search_result:
            self.video_search_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.audio_search_result is not None:
            result['AudioSearchResult'] = self.audio_search_result.to_map()

        if self.image_search_result is not None:
            result['ImageSearchResult'] = self.image_search_result.to_map()

        if self.text_search_result is not None:
            result['TextSearchResult'] = self.text_search_result.to_map()

        if self.topic is not None:
            result['Topic'] = self.topic

        if self.video_search_result is not None:
            result['VideoSearchResult'] = self.video_search_result.to_map()

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('AudioSearchResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResult()
            self.audio_search_result = temp_model.from_map(m.get('AudioSearchResult'))

        if m.get('ImageSearchResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsImageSearchResult()
            self.image_search_result = temp_model.from_map(m.get('ImageSearchResult'))

        if m.get('TextSearchResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsTextSearchResult()
            self.text_search_result = temp_model.from_map(m.get('TextSearchResult'))

        if m.get('Topic') is not None:
            self.topic = m.get('Topic')

        if m.get('VideoSearchResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResult()
            self.video_search_result = temp_model.from_map(m.get('VideoSearchResult'))

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResult(DaraModel):
    def __init__(
        self,
        current: int = None,
        search_result: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResultSearchResult] = None,
        size: int = None,
        total: int = None,
    ):
        self.current = current
        self.search_result = search_result
        self.size = size
        self.total = total

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
        if self.current is not None:
            result['Current'] = self.current

        result['SearchResult'] = []
        if self.search_result is not None:
            for k1 in self.search_result:
                result['SearchResult'].append(k1.to_map() if k1 else None)

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        self.search_result = []
        if m.get('SearchResult') is not None:
            for k1 in m.get('SearchResult'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResultSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResultSearchResult(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResultSearchResultArticle = None,
        clip_infos: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResultSearchResultClipInfos] = None,
        file_url: str = None,
        media_id: str = None,
    ):
        self.article = article
        self.clip_infos = clip_infos
        self.file_url = file_url
        self.media_id = media_id

    def validate(self):
        if self.article:
            self.article.validate()
        if self.clip_infos:
            for v1 in self.clip_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        result['ClipInfos'] = []
        if self.clip_infos is not None:
            for k1 in self.clip_infos:
                result['ClipInfos'].append(k1.to_map() if k1 else None)

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResultSearchResultArticle()
            self.article = temp_model.from_map(m.get('Article'))

        self.clip_infos = []
        if m.get('ClipInfos') is not None:
            for k1 in m.get('ClipInfos'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResultSearchResultClipInfos()
                self.clip_infos.append(temp_model.from_map(k1))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResultSearchResultClipInfos(DaraModel):
    def __init__(
        self,
        from_: float = None,
        score: float = None,
        text: str = None,
        to: float = None,
        type: str = None,
    ):
        self.from_ = from_
        self.score = score
        self.text = text
        self.to = to
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.score is not None:
            result['Score'] = self.score

        if self.text is not None:
            result['Text'] = self.text

        if self.to is not None:
            result['To'] = self.to

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsVideoSearchResultSearchResultArticle(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        search_source_name: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.search_source_name = search_source_name
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
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsTextSearchResult(DaraModel):
    def __init__(
        self,
        current: int = None,
        search_result: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsTextSearchResultSearchResult] = None,
        size: int = None,
        total: int = None,
    ):
        self.current = current
        self.search_result = search_result
        self.size = size
        self.total = total

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
        if self.current is not None:
            result['Current'] = self.current

        result['SearchResult'] = []
        if self.search_result is not None:
            for k1 in self.search_result:
                result['SearchResult'].append(k1.to_map() if k1 else None)

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        self.search_result = []
        if m.get('SearchResult') is not None:
            for k1 in m.get('SearchResult'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsTextSearchResultSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsTextSearchResultSearchResult(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        multimodal_medias: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsTextSearchResultSearchResultMultimodalMedias] = None,
        pub_time: str = None,
        search_source: str = None,
        search_source_name: str = None,
        search_source_type: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.multimodal_medias = multimodal_medias
        self.pub_time = pub_time
        self.search_source = search_source
        self.search_source_name = search_source_name
        self.search_source_type = search_source_type
        self.summary = summary
        self.title = title
        self.url = url

    def validate(self):
        if self.multimodal_medias:
            for v1 in self.multimodal_medias:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        result['MultimodalMedias'] = []
        if self.multimodal_medias is not None:
            for k1 in self.multimodal_medias:
                result['MultimodalMedias'].append(k1.to_map() if k1 else None)

        if self.pub_time is not None:
            result['PubTime'] = self.pub_time

        if self.search_source is not None:
            result['SearchSource'] = self.search_source

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.search_source_type is not None:
            result['SearchSourceType'] = self.search_source_type

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        self.multimodal_medias = []
        if m.get('MultimodalMedias') is not None:
            for k1 in m.get('MultimodalMedias'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsTextSearchResultSearchResultMultimodalMedias()
                self.multimodal_medias.append(temp_model.from_map(k1))

        if m.get('PubTime') is not None:
            self.pub_time = m.get('PubTime')

        if m.get('SearchSource') is not None:
            self.search_source = m.get('SearchSource')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('SearchSourceType') is not None:
            self.search_source_type = m.get('SearchSourceType')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsTextSearchResultSearchResultMultimodalMedias(DaraModel):
    def __init__(
        self,
        file_url: str = None,
        media_id: str = None,
        media_type: str = None,
    ):
        self.file_url = file_url
        self.media_id = media_id
        self.media_type = media_type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.media_type is not None:
            result['MediaType'] = self.media_type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('MediaType') is not None:
            self.media_type = m.get('MediaType')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsImageSearchResult(DaraModel):
    def __init__(
        self,
        current: int = None,
        search_result: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsImageSearchResultSearchResult] = None,
        size: int = None,
        total: int = None,
    ):
        self.current = current
        self.search_result = search_result
        self.size = size
        self.total = total

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
        if self.current is not None:
            result['Current'] = self.current

        result['SearchResult'] = []
        if self.search_result is not None:
            for k1 in self.search_result:
                result['SearchResult'].append(k1.to_map() if k1 else None)

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        self.search_result = []
        if m.get('SearchResult') is not None:
            for k1 in m.get('SearchResult'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsImageSearchResultSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsImageSearchResultSearchResult(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsImageSearchResultSearchResultArticle = None,
        file_url: str = None,
        media_id: str = None,
    ):
        self.article = article
        self.file_url = file_url
        self.media_id = media_id

    def validate(self):
        if self.article:
            self.article.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsImageSearchResultSearchResultArticle()
            self.article = temp_model.from_map(m.get('Article'))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsImageSearchResultSearchResultArticle(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        search_source_name: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.search_source_name = search_source_name
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
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResult(DaraModel):
    def __init__(
        self,
        current: int = None,
        search_result: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResultSearchResult = None,
        size: int = None,
        total: int = None,
    ):
        self.current = current
        self.search_result = search_result
        self.size = size
        self.total = total

    def validate(self):
        if self.search_result:
            self.search_result.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.current is not None:
            result['Current'] = self.current

        if self.search_result is not None:
            result['SearchResult'] = self.search_result.to_map()

        if self.size is not None:
            result['Size'] = self.size

        if self.total is not None:
            result['Total'] = self.total

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Current') is not None:
            self.current = m.get('Current')

        if m.get('SearchResult') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResultSearchResult()
            self.search_result = temp_model.from_map(m.get('SearchResult'))

        if m.get('Size') is not None:
            self.size = m.get('Size')

        if m.get('Total') is not None:
            self.total = m.get('Total')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResultSearchResult(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResultSearchResultArticle = None,
        clip_infos: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResultSearchResultClipInfos] = None,
        file_url: str = None,
        media_id: str = None,
    ):
        self.article = article
        self.clip_infos = clip_infos
        self.file_url = file_url
        self.media_id = media_id

    def validate(self):
        if self.article:
            self.article.validate()
        if self.clip_infos:
            for v1 in self.clip_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        result['ClipInfos'] = []
        if self.clip_infos is not None:
            for k1 in self.clip_infos:
                result['ClipInfos'].append(k1.to_map() if k1 else None)

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResultSearchResultArticle()
            self.article = temp_model.from_map(m.get('Article'))

        self.clip_infos = []
        if m.get('ClipInfos') is not None:
            for k1 in m.get('ClipInfos'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResultSearchResultClipInfos()
                self.clip_infos.append(temp_model.from_map(k1))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResultSearchResultClipInfos(DaraModel):
    def __init__(
        self,
        from_: float = None,
        score: float = None,
        text: str = None,
        to: float = None,
        type: str = None,
    ):
        self.from_ = from_
        self.score = score
        self.text = text
        self.to = to
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.score is not None:
            result['Score'] = self.score

        if self.text is not None:
            result['Text'] = self.text

        if self.to is not None:
            result['To'] = self.to

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentClusterTopicResultClusterTopicsAudioSearchResultSearchResultArticle(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        search_source_name: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.search_source_name = search_source_name
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
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResult(DaraModel):
    def __init__(
        self,
        search_result: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResultSearchResult] = None,
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
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResultSearchResult()
                self.search_result.append(temp_model.from_map(k1))

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResultSearchResult(DaraModel):
    def __init__(
        self,
        article: main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResultSearchResultArticle = None,
        clip_infos: List[main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResultSearchResultClipInfos] = None,
        file_url: str = None,
        media_id: str = None,
        traceability_id: str = None,
    ):
        self.article = article
        self.clip_infos = clip_infos
        self.file_url = file_url
        self.media_id = media_id
        self.traceability_id = traceability_id

    def validate(self):
        if self.article:
            self.article.validate()
        if self.clip_infos:
            for v1 in self.clip_infos:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article is not None:
            result['Article'] = self.article.to_map()

        result['ClipInfos'] = []
        if self.clip_infos is not None:
            for k1 in self.clip_infos:
                result['ClipInfos'].append(k1.to_map() if k1 else None)

        if self.file_url is not None:
            result['FileUrl'] = self.file_url

        if self.media_id is not None:
            result['MediaId'] = self.media_id

        if self.traceability_id is not None:
            result['TraceabilityId'] = self.traceability_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('Article') is not None:
            temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResultSearchResultArticle()
            self.article = temp_model.from_map(m.get('Article'))

        self.clip_infos = []
        if m.get('ClipInfos') is not None:
            for k1 in m.get('ClipInfos'):
                temp_model = main_models.RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResultSearchResultClipInfos()
                self.clip_infos.append(temp_model.from_map(k1))

        if m.get('FileUrl') is not None:
            self.file_url = m.get('FileUrl')

        if m.get('MediaId') is not None:
            self.media_id = m.get('MediaId')

        if m.get('TraceabilityId') is not None:
            self.traceability_id = m.get('TraceabilityId')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResultSearchResultClipInfos(DaraModel):
    def __init__(
        self,
        from_: float = None,
        score: float = None,
        text: str = None,
        to: float = None,
        type: str = None,
    ):
        self.from_ = from_
        self.score = score
        self.text = text
        self.to = to
        self.type = type

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.from_ is not None:
            result['From'] = self.from_

        if self.score is not None:
            result['Score'] = self.score

        if self.text is not None:
            result['Text'] = self.text

        if self.to is not None:
            result['To'] = self.to

        if self.type is not None:
            result['Type'] = self.type

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('From') is not None:
            self.from_ = m.get('From')

        if m.get('Score') is not None:
            self.score = m.get('Score')

        if m.get('Text') is not None:
            self.text = m.get('Text')

        if m.get('To') is not None:
            self.to = m.get('To')

        if m.get('Type') is not None:
            self.type = m.get('Type')

        return self

class RunSearchGenerationResponseBodyPayloadOutputAgentContextBizContextGeneratedContentAudioSearchResultSearchResultArticle(DaraModel):
    def __init__(
        self,
        doc_id: str = None,
        doc_uuid: str = None,
        search_source_name: str = None,
        summary: str = None,
        title: str = None,
        url: str = None,
    ):
        self.doc_id = doc_id
        self.doc_uuid = doc_uuid
        self.search_source_name = search_source_name
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
        if self.doc_id is not None:
            result['DocId'] = self.doc_id

        if self.doc_uuid is not None:
            result['DocUuid'] = self.doc_uuid

        if self.search_source_name is not None:
            result['SearchSourceName'] = self.search_source_name

        if self.summary is not None:
            result['Summary'] = self.summary

        if self.title is not None:
            result['Title'] = self.title

        if self.url is not None:
            result['Url'] = self.url

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('DocId') is not None:
            self.doc_id = m.get('DocId')

        if m.get('DocUuid') is not None:
            self.doc_uuid = m.get('DocUuid')

        if m.get('SearchSourceName') is not None:
            self.search_source_name = m.get('SearchSourceName')

        if m.get('Summary') is not None:
            self.summary = m.get('Summary')

        if m.get('Title') is not None:
            self.title = m.get('Title')

        if m.get('Url') is not None:
            self.url = m.get('Url')

        return self

class RunSearchGenerationResponseBodyHeader(DaraModel):
    def __init__(
        self,
        error_code: str = None,
        error_message: str = None,
        event: str = None,
        event_info: str = None,
        origin_session_id: str = None,
        response_time: int = None,
        session_id: str = None,
        task_id: str = None,
        trace_id: str = None,
    ):
        self.error_code = error_code
        self.error_message = error_message
        self.event = event
        self.event_info = event_info
        self.origin_session_id = origin_session_id
        self.response_time = response_time
        self.session_id = session_id
        self.task_id = task_id
        self.trace_id = trace_id

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.error_code is not None:
            result['ErrorCode'] = self.error_code

        if self.error_message is not None:
            result['ErrorMessage'] = self.error_message

        if self.event is not None:
            result['Event'] = self.event

        if self.event_info is not None:
            result['EventInfo'] = self.event_info

        if self.origin_session_id is not None:
            result['OriginSessionId'] = self.origin_session_id

        if self.response_time is not None:
            result['ResponseTime'] = self.response_time

        if self.session_id is not None:
            result['SessionId'] = self.session_id

        if self.task_id is not None:
            result['TaskId'] = self.task_id

        if self.trace_id is not None:
            result['TraceId'] = self.trace_id

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('ErrorCode') is not None:
            self.error_code = m.get('ErrorCode')

        if m.get('ErrorMessage') is not None:
            self.error_message = m.get('ErrorMessage')

        if m.get('Event') is not None:
            self.event = m.get('Event')

        if m.get('EventInfo') is not None:
            self.event_info = m.get('EventInfo')

        if m.get('OriginSessionId') is not None:
            self.origin_session_id = m.get('OriginSessionId')

        if m.get('ResponseTime') is not None:
            self.response_time = m.get('ResponseTime')

        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')

        if m.get('TaskId') is not None:
            self.task_id = m.get('TaskId')

        if m.get('TraceId') is not None:
            self.trace_id = m.get('TraceId')

        return self


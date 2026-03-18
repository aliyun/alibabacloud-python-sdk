# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import annotations

from typing import List

from alibabacloud_aicontent20240611 import models as main_models
from darabonba.model import DaraModel

class ListTextbookAssistantArticleDetailsResponseBody(DaraModel):
    def __init__(
        self,
        data: List[main_models.ListTextbookAssistantArticleDetailsResponseBodyData] = None,
        err_code: str = None,
        err_message: str = None,
        http_status_code: int = None,
        request_id: str = None,
        success: bool = None,
    ):
        self.data = data
        self.err_code = err_code
        self.err_message = err_message
        self.http_status_code = http_status_code
        # Id of the request
        self.request_id = request_id
        self.success = success

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
        result['data'] = []
        if self.data is not None:
            for k1 in self.data:
                result['data'].append(k1.to_map() if k1 else None)

        if self.err_code is not None:
            result['errCode'] = self.err_code

        if self.err_message is not None:
            result['errMessage'] = self.err_message

        if self.http_status_code is not None:
            result['httpStatusCode'] = self.http_status_code

        if self.request_id is not None:
            result['requestId'] = self.request_id

        if self.success is not None:
            result['success'] = self.success

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        self.data = []
        if m.get('data') is not None:
            for k1 in m.get('data'):
                temp_model = main_models.ListTextbookAssistantArticleDetailsResponseBodyData()
                self.data.append(temp_model.from_map(k1))

        if m.get('errCode') is not None:
            self.err_code = m.get('errCode')

        if m.get('errMessage') is not None:
            self.err_message = m.get('errMessage')

        if m.get('httpStatusCode') is not None:
            self.http_status_code = m.get('httpStatusCode')

        if m.get('requestId') is not None:
            self.request_id = m.get('requestId')

        if m.get('success') is not None:
            self.success = m.get('success')

        return self

class ListTextbookAssistantArticleDetailsResponseBodyData(DaraModel):
    def __init__(
        self,
        article_id: str = None,
        question_list: List[main_models.ListTextbookAssistantArticleDetailsResponseBodyDataQuestionList] = None,
        scene_list: List[main_models.ListTextbookAssistantArticleDetailsResponseBodyDataSceneList] = None,
        sentence_list: List[main_models.ListTextbookAssistantArticleDetailsResponseBodyDataSentenceList] = None,
        target: str = None,
        theme: main_models.ListTextbookAssistantArticleDetailsResponseBodyDataTheme = None,
        topic: main_models.ListTextbookAssistantArticleDetailsResponseBodyDataTopic = None,
        word_list: List[main_models.ListTextbookAssistantArticleDetailsResponseBodyDataWordList] = None,
    ):
        self.article_id = article_id
        self.question_list = question_list
        self.scene_list = scene_list
        self.sentence_list = sentence_list
        self.target = target
        self.theme = theme
        self.topic = topic
        self.word_list = word_list

    def validate(self):
        if self.question_list:
            for v1 in self.question_list:
                 if v1:
                    v1.validate()
        if self.scene_list:
            for v1 in self.scene_list:
                 if v1:
                    v1.validate()
        if self.sentence_list:
            for v1 in self.sentence_list:
                 if v1:
                    v1.validate()
        if self.theme:
            self.theme.validate()
        if self.topic:
            self.topic.validate()
        if self.word_list:
            for v1 in self.word_list:
                 if v1:
                    v1.validate()

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.article_id is not None:
            result['articleId'] = self.article_id

        result['questionList'] = []
        if self.question_list is not None:
            for k1 in self.question_list:
                result['questionList'].append(k1.to_map() if k1 else None)

        result['sceneList'] = []
        if self.scene_list is not None:
            for k1 in self.scene_list:
                result['sceneList'].append(k1.to_map() if k1 else None)

        result['sentenceList'] = []
        if self.sentence_list is not None:
            for k1 in self.sentence_list:
                result['sentenceList'].append(k1.to_map() if k1 else None)

        if self.target is not None:
            result['target'] = self.target

        if self.theme is not None:
            result['theme'] = self.theme.to_map()

        if self.topic is not None:
            result['topic'] = self.topic.to_map()

        result['wordList'] = []
        if self.word_list is not None:
            for k1 in self.word_list:
                result['wordList'].append(k1.to_map() if k1 else None)

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('articleId') is not None:
            self.article_id = m.get('articleId')

        self.question_list = []
        if m.get('questionList') is not None:
            for k1 in m.get('questionList'):
                temp_model = main_models.ListTextbookAssistantArticleDetailsResponseBodyDataQuestionList()
                self.question_list.append(temp_model.from_map(k1))

        self.scene_list = []
        if m.get('sceneList') is not None:
            for k1 in m.get('sceneList'):
                temp_model = main_models.ListTextbookAssistantArticleDetailsResponseBodyDataSceneList()
                self.scene_list.append(temp_model.from_map(k1))

        self.sentence_list = []
        if m.get('sentenceList') is not None:
            for k1 in m.get('sentenceList'):
                temp_model = main_models.ListTextbookAssistantArticleDetailsResponseBodyDataSentenceList()
                self.sentence_list.append(temp_model.from_map(k1))

        if m.get('target') is not None:
            self.target = m.get('target')

        if m.get('theme') is not None:
            temp_model = main_models.ListTextbookAssistantArticleDetailsResponseBodyDataTheme()
            self.theme = temp_model.from_map(m.get('theme'))

        if m.get('topic') is not None:
            temp_model = main_models.ListTextbookAssistantArticleDetailsResponseBodyDataTopic()
            self.topic = temp_model.from_map(m.get('topic'))

        self.word_list = []
        if m.get('wordList') is not None:
            for k1 in m.get('wordList'):
                temp_model = main_models.ListTextbookAssistantArticleDetailsResponseBodyDataWordList()
                self.word_list.append(temp_model.from_map(k1))

        return self

class ListTextbookAssistantArticleDetailsResponseBodyDataWordList(DaraModel):
    def __init__(
        self,
        word_analysis: str = None,
        word_id: str = None,
        word_text: str = None,
    ):
        self.word_analysis = word_analysis
        self.word_id = word_id
        self.word_text = word_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.word_analysis is not None:
            result['wordAnalysis'] = self.word_analysis

        if self.word_id is not None:
            result['wordId'] = self.word_id

        if self.word_text is not None:
            result['wordText'] = self.word_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('wordAnalysis') is not None:
            self.word_analysis = m.get('wordAnalysis')

        if m.get('wordId') is not None:
            self.word_id = m.get('wordId')

        if m.get('wordText') is not None:
            self.word_text = m.get('wordText')

        return self

class ListTextbookAssistantArticleDetailsResponseBodyDataTopic(DaraModel):
    def __init__(
        self,
        topic_image_list: List[str] = None,
        topic_name: str = None,
        topic_translate: str = None,
    ):
        self.topic_image_list = topic_image_list
        self.topic_name = topic_name
        self.topic_translate = topic_translate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.topic_image_list is not None:
            result['topicImageList'] = self.topic_image_list

        if self.topic_name is not None:
            result['topicName'] = self.topic_name

        if self.topic_translate is not None:
            result['topicTranslate'] = self.topic_translate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('topicImageList') is not None:
            self.topic_image_list = m.get('topicImageList')

        if m.get('topicName') is not None:
            self.topic_name = m.get('topicName')

        if m.get('topicTranslate') is not None:
            self.topic_translate = m.get('topicTranslate')

        return self

class ListTextbookAssistantArticleDetailsResponseBodyDataTheme(DaraModel):
    def __init__(
        self,
        theme_image_list: List[str] = None,
        theme_name: str = None,
        theme_translate: str = None,
    ):
        self.theme_image_list = theme_image_list
        self.theme_name = theme_name
        self.theme_translate = theme_translate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.theme_image_list is not None:
            result['themeImageList'] = self.theme_image_list

        if self.theme_name is not None:
            result['themeName'] = self.theme_name

        if self.theme_translate is not None:
            result['themeTranslate'] = self.theme_translate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('themeImageList') is not None:
            self.theme_image_list = m.get('themeImageList')

        if m.get('themeName') is not None:
            self.theme_name = m.get('themeName')

        if m.get('themeTranslate') is not None:
            self.theme_translate = m.get('themeTranslate')

        return self

class ListTextbookAssistantArticleDetailsResponseBodyDataSentenceList(DaraModel):
    def __init__(
        self,
        sentence_analysis: str = None,
        sentence_id: str = None,
        sentence_text: str = None,
    ):
        self.sentence_analysis = sentence_analysis
        self.sentence_id = sentence_id
        self.sentence_text = sentence_text

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.sentence_analysis is not None:
            result['sentenceAnalysis'] = self.sentence_analysis

        if self.sentence_id is not None:
            result['sentenceId'] = self.sentence_id

        if self.sentence_text is not None:
            result['sentenceText'] = self.sentence_text

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('sentenceAnalysis') is not None:
            self.sentence_analysis = m.get('sentenceAnalysis')

        if m.get('sentenceId') is not None:
            self.sentence_id = m.get('sentenceId')

        if m.get('sentenceText') is not None:
            self.sentence_text = m.get('sentenceText')

        return self

class ListTextbookAssistantArticleDetailsResponseBodyDataSceneList(DaraModel):
    def __init__(
        self,
        scene: str = None,
        scene_id: str = None,
        scene_image_list: List[str] = None,
        scene_translate: str = None,
    ):
        self.scene = scene
        self.scene_id = scene_id
        self.scene_image_list = scene_image_list
        self.scene_translate = scene_translate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.scene is not None:
            result['scene'] = self.scene

        if self.scene_id is not None:
            result['sceneId'] = self.scene_id

        if self.scene_image_list is not None:
            result['sceneImageList'] = self.scene_image_list

        if self.scene_translate is not None:
            result['sceneTranslate'] = self.scene_translate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('scene') is not None:
            self.scene = m.get('scene')

        if m.get('sceneId') is not None:
            self.scene_id = m.get('sceneId')

        if m.get('sceneImageList') is not None:
            self.scene_image_list = m.get('sceneImageList')

        if m.get('sceneTranslate') is not None:
            self.scene_translate = m.get('sceneTranslate')

        return self

class ListTextbookAssistantArticleDetailsResponseBodyDataQuestionList(DaraModel):
    def __init__(
        self,
        answer: str = None,
        question: str = None,
        question_translate: str = None,
    ):
        self.answer = answer
        self.question = question
        self.question_translate = question_translate

    def validate(self):
        pass

    def to_map(self):
        result = dict()
        _map = super().to_map()
        if _map is not None:
            result = _map
        if self.answer is not None:
            result['answer'] = self.answer

        if self.question is not None:
            result['question'] = self.question

        if self.question_translate is not None:
            result['questionTranslate'] = self.question_translate

        return result

    def from_map(self, m: dict = None):
        m = m or dict()
        if m.get('answer') is not None:
            self.answer = m.get('answer')

        if m.get('question') is not None:
            self.question = m.get('question')

        if m.get('questionTranslate') is not None:
            self.question_translate = m.get('questionTranslate')

        return self

